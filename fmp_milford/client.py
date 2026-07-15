"""
FMP stable-API client (zero third-party deps — uses urllib).

Free-tier aware:
  - enforces a per-day call budget (default 250) persisted to disk,
  - polite pacing (calls/minute),
  - on-disk JSON cache so re-runs don't burn quota,
  - records latency + payload size for every call (feeds the perf harness),
  - NEVER logs or stores the API key (URLs are sanitised in all metadata).
"""

from __future__ import annotations
import json
import os
import time
import hashlib
import urllib.parse
import urllib.request
import urllib.error
from datetime import date

from .config import FMP_BASE, ENDPOINTS, SETTINGS


class BudgetExceeded(RuntimeError):
    pass


class FMPClient:
    def __init__(self, api_key=None, settings=None):
        self.settings = {**SETTINGS, **(settings or {})}
        self.api_key = api_key or os.environ.get(self.settings["api_key_env"])
        if not self.api_key:
            raise RuntimeError(f"No API key. Set {self.settings['api_key_env']} in the environment / .env")
        self.base = FMP_BASE
        self.cache_dir = self.settings["cache_dir"]
        os.makedirs(self.cache_dir, exist_ok=True)
        self._last_call = 0.0
        self._budget = self._load_budget()

    # ---- budget accounting (per calendar day) ----
    def _load_budget(self):
        path = self.settings["budget_file"]
        today = date.today().isoformat()
        try:
            with open(path) as f:
                b = json.load(f)
            if b.get("date") != today:
                b = {"date": today, "count": 0}
        except Exception:
            b = {"date": today, "count": 0}
        return b

    def _save_budget(self):
        os.makedirs(os.path.dirname(self.settings["budget_file"]), exist_ok=True)
        with open(self.settings["budget_file"], "w") as f:
            json.dump(self._budget, f)

    @property
    def calls_remaining(self):
        return self.settings["daily_call_budget"] - self._budget["count"]

    # ---- cache ----
    def _cache_path(self, endpoint_key, params):
        h = hashlib.md5((endpoint_key + json.dumps(params, sort_keys=True)).encode()).hexdigest()[:16]
        return os.path.join(self.cache_dir, f"{endpoint_key}_{h}.json")

    def _sanitise(self, url):
        return url.split("apikey=")[0] + "apikey=***"

    # ---- core GET ----
    def get(self, endpoint_key, symbol=None, extra=None, use_cache=True, count_budget=True):
        """Returns (data, meta). meta = {latency_ms, bytes, status, from_cache, url}."""
        spec = ENDPOINTS.get(endpoint_key, {"path": endpoint_key, "params": {}})
        params = dict(spec.get("params", {}))
        if symbol:
            params["symbol"] = symbol
        if extra:
            params.update(extra)
        cache_file = self._cache_path(endpoint_key, params)

        if use_cache and os.path.exists(cache_file):
            age_h = (time.time() - os.path.getmtime(cache_file)) / 3600.0
            if age_h < self.settings["cache_ttl_hours"]:
                with open(cache_file) as f:
                    data = json.load(f)
                return data, {"latency_ms": 0, "bytes": os.path.getsize(cache_file),
                              "status": 200, "from_cache": True, "url": self._sanitise(self._url(spec["path"], params))}

        if count_budget and self.calls_remaining <= 0:
            raise BudgetExceeded(f"Daily free-tier budget ({self.settings['daily_call_budget']}) exhausted. "
                                 f"Cached data still available; new calls resume tomorrow.")

        # pace
        gap = 60.0 / self.settings["calls_per_minute"]
        wait = gap - (time.time() - self._last_call)
        if wait > 0:
            time.sleep(wait)

        url = self._url(spec["path"], params)
        t0 = time.time()
        status, raw = self._fetch(url)
        latency_ms = round((time.time() - t0) * 1000, 1)
        self._last_call = time.time()
        if count_budget:
            self._budget["count"] += 1
            self._save_budget()

        data = None
        if status == 200 and raw:
            try:
                data = json.loads(raw)
                with open(cache_file, "w") as f:
                    json.dump(data, f)
            except json.JSONDecodeError:
                data = None
        return data, {"latency_ms": latency_ms, "bytes": len(raw or b""), "status": status,
                      "from_cache": False, "url": self._sanitise(url)}

    def _url(self, path, params):
        q = dict(params)
        q["apikey"] = self.api_key
        return f"{self.base}/{path}?{urllib.parse.urlencode(q)}"

    def _fetch(self, url):
        req = urllib.request.Request(url, headers={"User-Agent": "milford-fmp/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()
        except Exception:
            return 0, b""
