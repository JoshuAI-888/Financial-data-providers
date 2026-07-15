# Support & Operations

## Quick start
```bash
python run.py                      # DEMO (offline) → outputs/milford_fmp_report.html
open outputs/milford_fmp_report.html
```

## Live mode
```bash
echo "FMP_API_KEY=your_key" > .env       # git-ignored
python run.py --live                     # pull + latency
python run.py --live --probe-only        # speed test only
python run.py --live --limit-sectors 3   # budget-safe partial pull
python run.py --out outputs/custom.html  # choose output path
```

## Tests
```bash
python tests/test_transform.py           # metric-formula unit tests (stdlib only)
pip install playwright                    # optional, for the browser smoke test
python tests/verify_report.py            # clicks every tab, checks for JS/render errors
```

## Regenerate reference docs after changing metrics/universe
```bash
python docs/gen_reference.py             # rewrites docs/GLOSSARY.md + docs/DATA_DICTIONARY.md
```

## Common operations

| Task | How |
|---|---|
| Add/remove companies | Edit `UNIVERSE` in `fmp_milford/config.py` |
| Add ASX/NZX tickers (after upgrade) | Add to `UNIVERSE`; no other change needed |
| Add a metric | Add to `transform.company_metrics` (+ formula/steps) and to `glossary.METRIC_GLOSSARY` |
| Add a role insight | Append an `ins(...)` in `insights.build_insights`; add an `INSIGHT_EXPLAINERS` entry |
| Change daily budget / cache TTL | `SETTINGS` in `config.py` |
| Enable a gated endpoint (higher tier) | Set `free: True` and add to `PULL_ENDPOINTS`/`extract.py` |

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `No API key` | `FMP_API_KEY` unset | Put it in `.env` or the environment |
| `BudgetExceeded` | 250/day cap hit | Wait for reset, or use cache / `--limit-sectors` |
| `--live` HTTP 000/403 | Network blocks FMP host | Run on open network / allowlist the host |
| Blank widgets in LIVE | FMP field-name mismatch | Inspect a record in `data/raw/`, tighten mapping in `extract.py` |
| Report won't open | — | It's a plain local HTML; open in any modern browser |

## Data & cache locations
- `data/raw/*.json` — cached API responses (git-ignored).
- `data/call_budget.json` — daily call counter (git-ignored).
- `outputs/milford_fmp_report.html` — the deliverable.

## Security
- Key read from `FMP_API_KEY` (env/`.env`), **never** written to outputs, logs or commits.
- `.env` is git-ignored; URLs are sanitised (`apikey=***`) in all metadata.
- **Rotate** any key shared in plain text.

## Escalation / ownership
- Data-coverage or tier questions → see [FAQ.md](FAQ.md) and `datarequirementsandprovidercoverage.md`.
- Metric definitions → [GLOSSARY.md](GLOSSARY.md); data shapes → [DATA_DICTIONARY.md](DATA_DICTIONARY.md).
- Architecture / extension → [ARCHITECTURE.md](ARCHITECTURE.md).
- This is internal analytical tooling — not for client-facing use (FMA boundary).
