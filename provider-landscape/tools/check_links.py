#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dead-link checker for the source register (and, optionally, any HTML/Markdown files).

Run it on an OPEN network — a laptop, or the "Link check" GitHub Actions workflow.
The Claude Code cloud sandbox blocks egress to vendor sites, so results from there are
meaningless.

    python3 provider-landscape/tools/check_links.py                 # every URL in source_register.csv
    python3 provider-landscape/tools/check_links.py page.html a.md  # URLs found in specific files

Writes provider-landscape/link_check.csv (url, link_status, http_status, final_url, checked_at)
and prints a summary. Then re-run build_register.py to merge the results into the register.

link_status:
    ok       2xx/3xx
    dead     404 / 410 / DNS failure — the page is gone; fix or replace the citation
    blocked  401 / 403 / 429 / 999 and similar bot walls — probably alive, confirm in a browser
    error    timeouts, TLS or connection errors, 5xx — retry later before treating as dead

    --baseline FILE  a previous link_check.csv; only dead links NOT already dead there fail the run
                     (the PR workflow uses the committed results, so known dead links are reported,
                     and listed in the audit log, but don't block unrelated PRs)

Exit code: 0 if no (new) dead links, 1 if any, 2 if nothing to check. Stdlib only.
Based on the checker first written on branch claude/financial-provider-analysis-9r9cqd.
"""
import csv, io, os, re, socket, ssl, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PL = os.path.dirname(HERE)
REGISTER = os.path.join(PL, "source_register.csv")
OUT = os.path.join(PL, "link_check.csv")
TIMEOUT = 20
WORKERS = 24
UA = "Mozilla/5.0 (compatible; provider-landscape-link-check/1.0)"
BLOCKED = {401, 403, 406, 429, 451, 999}
DEAD = {404, 410}


def urls_from_files(paths):
    urls = set()
    for p in paths:
        t = io.open(p, encoding="utf-8", errors="ignore").read()
        for m in re.findall(r'https?://[^\s"\'<>\\)\]]+', t):
            u = m.rstrip(".,;:)'\"]")
            if "json-schema.org" in u or "://www.w3.org" in u:
                continue
            urls.add(u)
    return sorted(urls)


def urls_from_register():
    with io.open(REGISTER, encoding="utf-8") as fh:
        return [r["url"] for r in csv.DictReader(fh)]


def classify(code):
    if isinstance(code, int):
        if code < 400:
            return "ok"
        if code in DEAD:
            return "dead"
        if code in BLOCKED:
            return "blocked"
        return "error" if code >= 500 else "dead"
    return "dead" if code == "ERR:DNS" else "error"


def check(url):
    ctx = ssl.create_default_context()
    last = "ERR"
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                return url, r.status, r.geturl()
        except urllib.error.HTTPError as e:
            last = e.code
            if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 500, 501, 503):
                continue  # many servers mishandle HEAD; confirm with GET
            return url, e.code, ""
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", None)
            last = "ERR:DNS" if isinstance(reason, socket.gaierror) else "ERR:" + type(reason).__name__
        except Exception as e:  # timeouts, TLS, resets
            last = "ERR:" + type(e).__name__
    return url, last, ""


def main():
    args = sys.argv[1:]
    known_dead = set()
    if "--baseline" in args:
        i = args.index("--baseline")
        base = args[i + 1]
        del args[i:i + 2]
        if os.path.exists(base):
            with io.open(base, encoding="utf-8") as fh:
                known_dead = {r["url"] for r in csv.DictReader(fh) if r.get("link_status") == "dead"}
    if args:
        paths = [p for p in args if os.path.exists(p)]
        urls = urls_from_files(paths)
    elif os.path.exists(REGISTER):
        urls = urls_from_register()
    else:
        urls = []
    if not urls:
        print("Nothing to check (no register and no input files)."); sys.exit(2)
    print("Checking %d unique URLs ..." % len(urls))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    results = []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for i, (url, status, final) in enumerate(ex.map(check, urls), 1):
            results.append((url, classify(status), str(status), final))
            if i % 100 == 0:
                print("  ...%d/%d" % (i, len(urls)), flush=True)
    with io.open(OUT, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["url", "link_status", "http_status", "final_url", "checked_at"])
        for r in sorted(results):
            w.writerow(list(r) + [now])
    counts = {}
    for _, s, _, _ in results:
        counts[s] = counts.get(s, 0) + 1
    print("\n==== RESULT (%s) ====" % now)
    print("  ".join("%s: %d" % (k, counts.get(k, 0)) for k in ("ok", "dead", "blocked", "error")))
    new_dead = 0
    for url, s, code, _ in sorted(results, key=lambda r: (r[1], r[0])):
        if s == "dead":
            known = url in known_dead
            new_dead += not known
            print("  [DEAD %s]%s %s" % (code, " (known)" if known else " (NEW)" if known_dead else "", url))
    if known_dead:
        print("%d dead link(s) not in the baseline." % new_dead)
    sys.exit(1 if new_dead else 0)


if __name__ == "__main__":
    main()
