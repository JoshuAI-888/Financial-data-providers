#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dead-link checker for the provider-landscape pages.

Run this in ANY environment with open outbound internet. (Claude Code's managed
sandbox blocks egress, so external URLs cannot be verified there — run it locally
or in CI instead.)

    # from the provider-landscape/ directory:
    python3 tools/check_links.py

    # or point it at specific file(s) anywhere:
    python3 tools/check_links.py path/to/page.html [more.html ...]

Stdlib only — no pip installs. It extracts every external http(s) URL from the
HTML, requests each (HEAD, falling back to GET), follows redirects, and reports
anything that is NOT reachable (DNS failure, connection error, timeout, or a
4xx/5xx status). Well-formed but dead links are exactly what this catches.

Exit code 0 = all links reachable; 1 = one or more dead/unreachable; 2 = no
input files found.
"""
import sys, re, io, os, ssl, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

# The two published pages live one directory up from this tools/ folder.
_HERE = os.path.dirname(os.path.abspath(__file__))
_PAGES_DIR = os.path.dirname(_HERE)
DEFAULT = [
    os.path.join(_PAGES_DIR, "idp_evaluation.html"),
    os.path.join(_PAGES_DIR, "financial_data_providers_landscape.html"),
]
TIMEOUT = 20
WORKERS = 24
UA = "Mozilla/5.0 (link-checker; provider-landscape QA) Python-urllib"

def extract(paths):
    urls = set()
    for p in paths:
        t = io.open(p, encoding="utf-8", errors="ignore").read()
        for m in re.findall(r'https?://[^\s"\'<>\\)]+', t):
            u = m.rstrip(".,;)'\"]")
            if "json-schema.org" in u or "://www.w3.org" in u:
                continue
            urls.add(u)
    return sorted(urls)

def check(url):
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                return (url, r.status, r.geturl())
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 501) and method == "HEAD":
                continue  # some servers reject HEAD; retry with GET
            return (url, e.code, "")
        except Exception as e:
            if method == "HEAD":
                continue
            return (url, "ERR:" + type(e).__name__, "")
    return (url, "ERR", "")

def main():
    args = sys.argv[1:]
    paths = args or DEFAULT
    paths = [p for p in paths if os.path.exists(p)]
    if not paths:
        print("No HTML files found. Pass paths, or run from provider-landscape/."); sys.exit(2)
    urls = extract(paths)
    print("Checking %d unique external URLs from: %s\n"
          % (len(urls), ", ".join(os.path.basename(p) for p in paths)))
    dead = []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for i, (url, status, final) in enumerate(ex.map(check, urls), 1):
            ok = isinstance(status, int) and status < 400
            if not ok:
                dead.append((url, status))
            if i % 50 == 0:
                print("  ...%d/%d checked" % (i, len(urls)))
    print("\n==== RESULT ====")
    print("OK: %d   DEAD/UNREACHABLE: %d" % (len(urls) - len(dead), len(dead)))
    for url, status in sorted(dead, key=lambda x: str(x[1])):
        print("  [%s] %s" % (status, url))
    sys.exit(1 if dead else 0)

if __name__ == "__main__":
    main()
