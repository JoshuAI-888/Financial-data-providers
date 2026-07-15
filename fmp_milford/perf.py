"""
Extraction performance harness — answers "how fast can we get data from the API".

Times each free-tier endpoint (latency + payload + HTTP status) for a probe symbol,
bypassing the cache so numbers reflect the real network round-trip. Also reports how
many companies fit inside the remaining daily call budget at the measured cost.
"""

from __future__ import annotations
import statistics as st
from .config import PULL_ENDPOINTS, ENDPOINTS


def probe(client, symbol="AAPL", endpoints=None, repeats=1) -> list[dict]:
    endpoints = endpoints or PULL_ENDPOINTS
    results = []
    for ek in endpoints:
        lats, status, nbytes, ok = [], None, 0, False
        for _ in range(repeats):
            data, meta = client.get(ek, symbol=symbol, use_cache=False, count_budget=True)
            lats.append(meta["latency_ms"]); status = meta["status"]; nbytes = meta["bytes"]
            ok = meta["status"] == 200 and data not in (None, [], {})
        results.append({
            "endpoint": ENDPOINTS.get(ek, {}).get("path", ek),
            "key": ek,
            "status": status,
            "latency_ms": round(st.mean(lats), 1),
            "bytes": nbytes,
            "ok": ok,
            "tier_note": "free" if ENDPOINTS.get(ek, {}).get("free") else "verify/gated",
        })
    return results


def summarise(results, calls_remaining, endpoints_per_company=None) -> dict:
    per_co = endpoints_per_company or len(PULL_ENDPOINTS)
    ok = [r for r in results if r["ok"]]
    med_lat = round(st.median([r["latency_ms"] for r in ok]), 1) if ok else None
    total_ms = sum(r["latency_ms"] for r in results)
    return {
        "endpoints_probed": len(results),
        "ok": len(ok),
        "median_latency_ms": med_lat,
        "wall_time_one_company_s": round(total_ms / 1000.0, 2),
        "calls_per_company": per_co,
        "companies_left_in_budget": max(0, calls_remaining // per_co),
    }
