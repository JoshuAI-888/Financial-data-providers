# Architecture

## Overview

A linear, source-agnostic pipeline. Demo and live differ only at the extraction stage;
everything downstream is identical, so the report layout is guaranteed to match.

```
                          ┌───────────────── DEMO ─────────────────┐
                          │  mockdata.py (seeded one-factor model)  │
                          └────────────────────┬────────────────────┘
                                               │  normalized records
 FMP stable API ──► client.py ──► extract.py ──┤
   (LIVE, needs        rate-limit,   FMP JSON → │
    open network)      budget,       normalized │
                       cache, timing  records   ▼
                                        transform.py ──► insights.py ──► report.py ──► outputs/*.html
                                        metric engine    role insights   self-contained
                                        (formula+steps)  (≥3/role) +      interactive HTML
                                        + factors + risk  PM commentary
   perf.py ──► latency/throughput harness (feeds Data & Performance tab)
   glossary.py ──► meaning/good/target/alpha (tooltips, modal, docs)
```

## Modules (`fmp_milford/`)

| Module | Responsibility | Key detail |
|---|---|---|
| `config.py` | Universe, FMP endpoint catalogue + tiers, settings | Single place to add ASX/NZX tickers on upgrade |
| `client.py` | FMP stable-API client | urllib only; 250/day budget persisted; 24h cache; key never logged |
| `perf.py` | Extraction performance harness | Per-endpoint latency/bytes/status; companies-per-budget |
| `extract.py` | Live pull → normalized records | Defensive field mapping (stable/legacy key fallbacks) |
| `mockdata.py` | Offline demo dataset | Seeded; one-factor price model → realistic beta/correlation |
| `transform.py` | Metric engine + factors + risk | Every metric = `{value, formula, inputs, steps, unit, good}` |
| `insights.py` | Role insight builders + PM commentary | References metric keys (no duplication); rule-based narrative |
| `glossary.py` | Plain-language knowledge base | meaning/good/target/alpha per metric + per widget |
| `report.py` | Single-file interactive HTML | Inline CSS/JS/data/logos; provenance, calc modal, explainers |

`run.py` orchestrates; `tests/` holds metric unit tests + a browser smoke test;
`docs/gen_reference.py` regenerates GLOSSARY.md + DATA_DICTIONARY.md from code.

## Canonical data model (star-schema-in-a-dict)

The normalized company record is the join backbone (see [DATA_DICTIONARY.md](DATA_DICTIONARY.md)).
Conceptually:

- **Dimensions:** security (ticker/name/sector/industry/currency), fiscal year, benchmark.
- **Facts (per year):** income, balance, cash-flow line items.
- **Point-in-time facts:** price series (weekly), market cap, dividends.
- **Derived:** metrics, factor z-scores, risk statistics, correlation matrix.

Demo and live both emit this shape, so `transform → insights → report` never branch on source.

## Presentation architecture (in-browser)

- **State:** selected tickers (Set) + market-cap slider + composite-z slider + active tab.
  Every render reads `activeTickers()` so controls filter *all* widgets consistently.
- **Widget renderers** keyed by `insight.widget`: `metric_table`, `scatter`, `bar`,
  `sector_heatmap`, `flag_table`, `dupont`, `lines`, `heatmap_matrix`, `commentary`,
  `perf_table`. Each wrapped by `card()` → adds notes, explainer box, provenance line.
- **Transparency:** table cells call `openCalc()` → modal with formula/inputs/steps +
  glossary (meaning/good/target/alpha). Column headers carry hover tooltips.
- **Self-contained:** data injected as one JSON blob; logos are inline SVG monograms
  (or real FMP logos embedded when live). No external requests → strict-CSP / offline safe.

## Data flow for one number (traceability)

`FMP income-statement.revenue` → `extract.py` maps to `income[y].revenue` →
`transform.company_metrics` computes e.g. `net_margin = net_income / revenue` with
`formula/inputs/steps` attached → `insights.pa_comps` references key `net_margin` →
`report.metricTable` renders the cell → click → `openCalc` shows the working + glossary.

## Why these choices
- **Stdlib-only core** → runs anywhere, no supply-chain surface, trivial for analysts.
- **Compute, don't ingest, metrics** → one consistent definition, fully auditable.
- **Source-agnostic normalized shape** → demo == live layout; safe to develop offline.
- **Single HTML file** → distributable, offline, no server, survives email/attachment.
- **Budget + cache in client** → the 250/day cap is a first-class constraint, not an afterthought.

## Upgrade path (unchanged code)
Add non-US tickers to `config.UNIVERSE` and move to FMP **Premium** (LSE, 30y, intraday) or
**Ultimate** (ASX/NZX/HKEX/SGX/KRX/TWSE + transcripts + 13F + bulk). The pipeline is identical;
only the tier gate and universe change.
