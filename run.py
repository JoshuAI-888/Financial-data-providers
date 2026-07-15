#!/usr/bin/env python3
"""
Orchestrator: extract -> transform -> insights -> interactive HTML.

Usage:
  python run.py                 # DEMO mode (synthetic data, no network) — default
  python run.py --live          # LIVE mode: pulls real FMP data (needs FMP_API_KEY + open network)
  python run.py --live --probe-only   # just run the API performance harness
  python run.py --out outputs/report.html --limit-sectors 4

DEMO exists because some environments block egress to financialmodelingprep.com.
LIVE and DEMO share the entire downstream pipeline, so the report layout is identical.
"""

from __future__ import annotations
import argparse
import os
import sys
from datetime import datetime, timezone

from fmp_milford.config import SETTINGS, UNIVERSE, all_tickers
from fmp_milford import transform as T
from fmp_milford import insights as I
from fmp_milford import report as R


def _load_dotenv():
    path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def main():
    ap = argparse.ArgumentParser(description="Milford FMP free-tier intelligence builder")
    ap.add_argument("--live", action="store_true", help="pull real FMP data (needs FMP_API_KEY + network)")
    ap.add_argument("--probe-only", action="store_true", help="run the API performance harness and exit")
    ap.add_argument("--out", default=SETTINGS["output_html"], help="output HTML path")
    ap.add_argument("--limit-sectors", type=int, default=0, help="use only the first N sectors (call budget)")
    args = ap.parse_args()
    _load_dotenv()

    tickers = all_tickers()
    if args.limit_sectors:
        keep = list(UNIVERSE)[:args.limit_sectors]
        tickers = [t for s in keep for t in UNIVERSE[s]]

    perf = None

    if args.live or args.probe_only:
        from fmp_milford.client import FMPClient
        from fmp_milford import perf as PF
        from fmp_milford import extract as X
        try:
            client = FMPClient()
        except RuntimeError as e:
            print(f"[error] {e}"); sys.exit(1)
        print(f"[live] calls remaining today: {client.calls_remaining}/{SETTINGS['daily_call_budget']}")
        print("[live] running performance probe (AAPL)...")
        perf = PF.probe(client, symbol="AAPL")
        for r in perf:
            print(f"   {r['endpoint']:<34} http={r['status']} {r['latency_ms']:>7}ms  {r['bytes']:>8}B  {r['tier_note']}")
        print("  summary:", PF.summarise(perf, client.calls_remaining))
        if args.probe_only:
            return
        print(f"[live] extracting {len(tickers)} companies...")
        dataset = X.extract_live(client, tickers)
        print(f"[live] calls remaining after pull: {client.calls_remaining}")
    else:
        from fmp_milford import mockdata as M
        ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"[demo] building synthetic dataset for {len(tickers)} companies...")
        dataset = M.build_demo_dataset(ts)
        if args.limit_sectors:
            dataset["companies"] = {t: c for t, c in dataset["companies"].items() if t in tickers}

    print("[*] transforming metrics...")
    tr = T.transform_all(dataset)
    print("[*] building role insights...")
    ins = I.build_insights(dataset, tr)
    n = sum(len(v) for v in ins.values())
    print(f"[*] {n} insights across {len(ins)} roles")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    R.write_report(args.out, dataset, tr, ins, perf)
    size_kb = os.path.getsize(args.out) / 1024
    print(f"[done] wrote {args.out}  ({size_kb:.0f} KB, self-contained)  mode={dataset['mode']}")


if __name__ == "__main__":
    main()
