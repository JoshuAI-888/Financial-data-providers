# CLAUDE.md

Guidance for Claude Code (and future contributors) working in this repository.

## What this repo is
A role-based **investment-intelligence portal** built on **FMP free-tier** data for Milford
Asset Management. It turns raw FMP data into transparent, comparable financial models and
presents them as a **single self-contained interactive HTML** organised by the five investment
roles. Read [docs/PROBLEM_STATEMENT.md](docs/PROBLEM_STATEMENT.md) first, then
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## The one constraint that shapes everything
FMP **free tier = US-listed only, EOD, ~5y annual, 250 calls/day**. Milford's home exchanges
(NZX/ASX/LSE/HKEX/SGX/KRX/TWSE) are **not** reachable here. The universe is US comparables.
Do not imply otherwise in code, docs, or UI copy.

## Project layout
```
fmp_milford/   config, client, perf, extract, mockdata, transform, insights, glossary, report
run.py         orchestrator (demo default; --live; --probe-only; --limit-sectors)
outputs/       milford_fmp_report.html  (the deliverable)
docs/          problem/requirements/architecture/assumptions/FAQ/support + generated glossary & data dictionary
tests/         metric unit tests + browser smoke test
```

## How to run / test
```bash
python run.py                    # DEMO (offline, no deps) -> outputs/milford_fmp_report.html
python run.py --live             # real FMP data (needs FMP_API_KEY + open network)
python tests/test_transform.py   # metric unit tests
python tests/verify_report.py    # browser smoke test (needs: pip install playwright)
python docs/gen_reference.py     # regenerate GLOSSARY.md + DATA_DICTIONARY.md
```

## Conventions & invariants (please preserve)
- **Stdlib-only core.** No third-party imports in `fmp_milford/` except optional tooling.
  Keep it runnable with a bare Python.
- **Compute metrics, never ingest them.** Every metric in `transform.py` must carry
  `{value, formula, inputs, steps, unit, good}` so the UI can show its working.
- **Demo == Live shape.** `mockdata.py` and `extract.py` emit the *same* normalized record;
  never branch `transform/insights/report` on data source.
- **Provenance is mandatory.** Every widget shows source + last-updated + DEMO/LIVE badge.
- **Explainers are mandatory.** New metrics need a `glossary.METRIC_GLOSSARY` entry; new
  widgets need an `INSIGHT_EXPLAINERS` entry (meaning/good/target/alpha).
- **Self-contained HTML.** `report.py` inlines all CSS/JS/data/logos — no external requests
  (CSP/offline safe). Don't add CDN links.
- **Budget first.** All live calls go through `client.py` (rate-limit + 250/day budget + cache).

## Security (hard rules)
- API key only via `FMP_API_KEY` (env/`.env`). **Never** commit it or write it into any output.
- `.env` and `data/raw/` are git-ignored. Before committing, scan: `git grep -I "apikey\|FMP_API_KEY"`.
- URLs in metadata must be sanitised (`apikey=***`).

## Adding things
- **A company:** edit `UNIVERSE` in `config.py`.
- **A metric:** `transform.company_metrics` (+ formula/steps) **and** `glossary.METRIC_GLOSSARY`.
- **An insight:** an `ins(...)` in `insights.build_insights` **and** an `INSIGHT_EXPLAINERS` entry;
  add a renderer in `report.py` if it's a new widget type.
- Then run `python docs/gen_reference.py` and regenerate the report.

## Guardrails
- This is **analytical tooling, not investment advice**, and **not** for client-facing or
  decision-of-record use (**FMA boundary**).
- No book-of-record data (positions/NAV/performance) — that is IBOR/AlphaCert, out of scope.

## Gotchas
- This managed environment **blocks egress to financialmodelingprep.com** → `--live` fails here;
  run it elsewhere. The committed report is DEMO.
- Factor z-scores are **relative to the active universe** and change as you filter.
