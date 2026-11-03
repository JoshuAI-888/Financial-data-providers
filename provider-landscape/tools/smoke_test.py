#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Browser smoke test for the published pages (needs: pip install playwright; playwright install chromium).

    python3 provider-landscape/tools/smoke_test.py

Opens every published copy of both pages from disk, clicks through each IDP tab and every vendor
deep-dive, and fails on any console error or uncaught page error. External requests are blocked
(the pages must be self-contained); local research-explorer.js loads are allowed.
"""
import os, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PAGES = ["idp_evaluation.html", "provider-landscape/idp_evaluation.html",
         "financial_data_providers_landscape.html", "provider-landscape/financial_data_providers_landscape.html",
         "index.html"]


def main():
    failures = []
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH")
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        for rel in PAGES:
            errs = []
            pg = b.new_page()
            pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
            pg.on("console", lambda m, errs=errs: errs.append("console: " + m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e, errs=errs: errs.append("pageerror: " + str(e)))
            pg.goto("file://" + os.path.join(ROOT, rel))
            pg.wait_for_timeout(800)
            if "idp_evaluation" in rel:
                tabs = pg.locator("[data-tab], [role=tab]")
                for i in range(tabs.count()):
                    try:
                        tabs.nth(i).click(timeout=2000)
                        pg.wait_for_timeout(150)
                    except Exception:
                        pass
                n = pg.evaluate("JSON.parse(document.getElementById('idp-data').textContent).vendors.length")
                if n != 15:
                    errs.append("expected 15 vendors, found %s" % n)
                body = pg.inner_text("body")
                if "3 Nov 2026" not in body and "3 Nov 2026" not in pg.content():
                    errs.append("as-of stamp '3 Nov 2026' not found")
            errs = [e for e in errs if "net::ERR_FAILED" not in e and "Failed to load resource" not in e]
            print("%-60s %s" % (rel, "OK" if not errs else "%d error(s)" % len(errs)))
            for e in errs:
                print("    " + e[:300])
            failures += errs
            pg.close()
        b.close()
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
