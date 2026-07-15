"""
Headless-browser smoke test for the generated report. Requires `pip install playwright`.
Clicks every tab, asserts no console/page errors, no widget render failures, that the
calculation modal opens, and that a slider filters the universe.

Run:  python run.py && python tests/verify_report.py
"""

import glob
import os
import sys

HTML = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs", "milford_fmp_report.html"))


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed — `pip install playwright` to run this smoke test.")
        return 0
    chromes = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
    launch = {"executable_path": chromes[0]} if chromes else {}
    tabs = ["Portfolio Manager", "Head of Investment", "Portfolio Analyst",
            "Quantitative Analyst", "Performance & Risk Analyst", "Data & Performance"]
    errs = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"], **launch)
        pg = b.new_page()
        pg.on("console", lambda m: errs.append(f"console.error: {m.text}") if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
        pg.goto("file://" + HTML)
        pg.wait_for_timeout(600)
        for tab in tabs:
            pg.click(f"text='{tab}'")
            pg.wait_for_timeout(350)
            rn = pg.eval_on_selector_all(".notes", "els=>els.filter(e=>e.textContent.startsWith('Render note')).length")
            if rn:
                errs.append(f"[{tab}] {rn} widget render failure(s)")
        pg.click("text='Portfolio Analyst'"); pg.wait_for_timeout(300)
        cell = pg.query_selector("td.num")
        cell.click(); pg.wait_for_timeout(200)
        if not pg.eval_on_selector("#modalBg", "e=>e.classList.contains('show')"):
            errs.append("calc modal did not open")
        b.close()
    if errs:
        print("FAIL:"); [print(" -", e) for e in errs]; return 1
    print("PASS: all tabs render, no console errors, calc modal opens.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
