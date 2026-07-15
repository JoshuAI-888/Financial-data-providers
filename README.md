# Milford · FMP Free-Tier Investment Intelligence

A self-contained, interactive HTML intelligence portal built on **Financial Modeling Prep (FMP)**
data, scoped honestly to what the **free / lowest tier** can actually deliver, and organised around
the five Milford investment roles.

It answers three questions the team asked:

1. **What data can we actually get on the FMP free tier?** (spoiler: US-listed only, EOD, ~5y, 250 calls/day)
2. **How fast can we get it?** (a latency/throughput harness)
3. **What is that data worth to each role, and how should it be presented?** (≥3 insights per role)

---

## The free-tier reality (why the universe is US names)

| | Free (Basic) | Starter | Premium | Ultimate |
|---|---|---|---|---|
| Markets | **US only** | US only | + UK/Canada | **+ ASX/NZX/HKEX/SGX/KRX/TWSE (global)** |
| Prices | EOD | EOD + real-time US | + intraday | + 1-min |
| History | ~5y | ~5y | 30y | 30y |
| Calls/day | **250** | higher | higher | highest |
| Transcripts / 13F / bulk | – | – | – | ✓ |

**None of Milford's home exchanges are reachable on Free/Starter.** So this tool uses FMP as a
**US-listed comparables + fundamental-modelling + dev sandbox** — exactly the use-case FMP is strong at
for a NZ/AU manager. The universe is 32 US names across four requested themes (add ASX/NZX tickers to
`fmp_milford/config.py::UNIVERSE` the day you move to Ultimate — the code path is identical).

## What's in the box

```
fmp_milford/
  config.py     universe (4 themes x 8) + FMP endpoint catalogue + tiers + settings
  client.py     FMP stable-API client: rate-limit, 250/day budget, on-disk cache, key never logged
  perf.py       latency/throughput harness ("how fast can we get data")
  extract.py    live pull -> normalized records (same shape as demo)
  mockdata.py   realistic synthetic dataset (one-factor price model) for offline DEMO
  transform.py  metric engine: every figure carries formula + inputs + steps
  insights.py   role insight builders (>=3 per role) + rule-based PM commentary
  report.py     single-file interactive HTML (tabs, sliders, logos, provenance, calc panels)
run.py          orchestrator (demo | live | probe-only)
outputs/        milford_fmp_report.html   <- the deliverable
tests/          metric-formula unit tests
```

## Run it

```bash
# DEMO (default) — synthetic data, no network, fully interactive
python run.py
open outputs/milford_fmp_report.html

# LIVE — real FMP data (needs a key + open network to financialmodelingprep.com)
echo "FMP_API_KEY=your_key_here" > .env
python run.py --live               # pulls the universe, records real latency
python run.py --live --probe-only  # just the API performance harness

# Budget-safe partial pull (first N sectors only)
python run.py --live --limit-sectors 3
```

> **Note on this cloud environment:** egress to `financialmodelingprep.com` is blocked by the
> session network policy, so `--live` cannot run here. It runs on any network-open machine. DEMO
> and LIVE share the entire downstream pipeline, so the report layout is identical either way.

## The report

- **Tabs:** Overview · Portfolio Manager · Head of Investment · Portfolio Analyst · Quantitative
  Analyst · Performance & Risk Analyst · Data & Performance · Methodology.
- **Global controls:** multi-select company chips (grouped by theme) + market-cap and composite-z
  sliders that filter every table and chart. Compare any subset side by side.
- **Provenance everywhere:** each widget shows its FMP source endpoints, a DEMO/LIVE badge, and a
  last-updated timestamp.
- **Show-your-working:** click any computed number to open its formula, inputs, and step-by-step calc.
- **Offline & theme-aware:** one file, no external requests, light/dark.

### Insights per role (all computed from free-tier data)

| Role | Insights |
|---|---|
| **Portfolio Manager** | Peer valuation snapshot · Quality-vs-valuation scatter · Auto PM commentary · Capital-return |
| **Head of Investment** | Sector aggregates heatmap · Cheap-and-quality screen · Risk-flag register |
| **Portfolio Analyst** | Quality-scored comps grid · DuPont ROE bridge · 5y FCF-conversion trend |
| **Quantitative Analyst** | Multi-factor composite (V/Q/G/M) · Correlation matrix · API performance |
| **Performance & Risk** | Return/vol/beta/drawdown/Sharpe · Drawdown & cumulative-return · Diversification matrix |

## Metric methodology

Every metric is **computed by us from the raw statements** (never ingested pre-baked), so the logic is
transparent and identical across names. Families: profitability (ROIC/ROE/margins), cash quality
(FCF conversion, OCF/EBITDA), growth (CAGRs), leverage/liquidity, valuation (P/E, EV/EBITDA, FCF yield),
per-share, DuPont, quality scores (Altman Z, Piotroski F), and price-based risk (vol, beta, drawdown,
Sharpe, correlations). See the in-app **Methodology** tab and click any figure for its derivation.

## Documentation

| Doc | What's in it |
|---|---|
| [docs/PROBLEM_STATEMENT.md](docs/PROBLEM_STATEMENT.md) | Background, the problem, scope, what "done" means |
| [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) | Functional + non-functional requirements, acceptance criteria |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Pipeline, modules, data model, presentation, design rationale |
| [docs/ASSUMPTIONS.md](docs/ASSUMPTIONS.md) | Every assumption (data, demo, methodology, scope) |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | Every metric: meaning / what good looks like / target / alpha *(generated)* |
| [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) | FMP endpoints, canonical record, metric outputs *(generated)* |
| [docs/FAQ.md](docs/FAQ.md) | Common questions answered |
| [docs/SUPPORT.md](docs/SUPPORT.md) | Run/test/extend, troubleshooting, operations |
| [docs/SYSTEM_PROMPT.md](docs/SYSTEM_PROMPT.md) | Comprehensive system prompt for an AskMilford-style analyst copilot |
| [CLAUDE.md](CLAUDE.md) | Repo guidance & invariants for Claude Code / contributors |

Regenerate the generated docs after changing metrics/universe: `python docs/gen_reference.py`.

## Security

The API key is read from `FMP_API_KEY` (env or `.env`) and is **never** written into the HTML, logs,
or committed files. `.env` is git-ignored. Rotate any key that has been shared in plain text.
