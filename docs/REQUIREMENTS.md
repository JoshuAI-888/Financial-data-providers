# Requirements

## Functional requirements

### FR1 — Free-tier data extraction
- FR1.1 Pull US-listed company reference, statements (IS/BS/CF, ~5y annual), prices (EOD),
  dividends and financial scores from FMP's stable API.
- FR1.2 Respect the **250 calls/day** cap: persistent daily budget counter, refuse calls
  past the cap with a clear message, and serve from cache within a 24h TTL.
- FR1.3 Never log or persist the API key in any output or committed file.

### FR2 — Performance measurement
- FR2.1 Measure and report per-endpoint **latency, payload size, HTTP status** ("how fast
  can we get data").
- FR2.2 Report how many companies fit inside the remaining daily budget at measured cost.

### FR3 — Metric / financial-modelling engine
- FR3.1 Compute (not ingest) all derived metrics so logic is transparent and consistent:
  profitability (incl. ROIC/ROCE), growth, liquidity, leverage, efficiency, cash conversion,
  valuation, per-share, DuPont, quality scores (Altman Z, Piotroski F), and price-based risk
  (vol, beta, drawdown, Sharpe, correlations).
- FR3.2 Every computed figure must carry its **formula, inputs, and step-by-step working**.
- FR3.3 Compute cross-sectional **factor z-scores** (value/quality/growth/momentum + composite).

### FR4 — Role-based insights (≥3 per role)
- FR4.1 Deliver ≥3 decision-useful insights for each of the five roles.
- FR4.2 Provide **auto-generated PM commentary** derived deterministically from the metrics.

### FR5 — Presentation (interactive HTML)
- FR5.1 A **single self-contained** HTML file (all CSS/JS/data/logos inline; opens offline).
- FR5.2 Clickable **role tabs / pages**; company **multi-select** and **sliders** to compare.
- FR5.3 Company **logos**; theme-aware (light/dark); responsive (no horizontal page scroll).
- FR5.4 **Provenance** on every widget: source field(s) + last-updated + DEMO/LIVE badge.
- FR5.5 **Expandable calculation** panel on every computed number (formula/inputs/steps).
- FR5.6 **Plain-language explainer** on every widget and metric: intent, what good looks
  like, what we're targeting, and the alpha / what it trades (tooltip + expandable box).

### FR6 — Comparability
- FR6.1 Metrics comparable across names via percentile shading and universe medians.
- FR6.2 Universe grouped into themes; extensible to ASX/NZX tickers on tier upgrade.

## Non-functional requirements
- NFR1 **Zero third-party deps** for the core pipeline (stdlib only) → trivial to run.
- NFR2 **Reproducible**: seeded demo data; deterministic (rule-based) commentary.
- NFR3 **Portable**: demo runs with no network; live path identical downstream.
- NFR4 **Auditable**: every number traceable to inputs and a named source endpoint.
- NFR5 **Secure**: key via env/`.env` (git-ignored); nothing sensitive in outputs.
- NFR6 **Testable**: metric unit tests + headless-browser smoke test.

## Constraints
- FMP **free tier**: US-only, EOD, ~5y, 250 calls/day, 500MB/30d.
- **This environment blocks egress to financialmodelingprep.com** → live pull runs
  elsewhere; committed report uses demo data.
- **FMA boundary**: not for client-facing or decision-of-record use.

## Acceptance criteria
- [x] `python run.py` produces a self-contained HTML with 5 role tabs × ≥3 insights.
- [x] Every figure opens a calculation panel; every widget shows provenance + explainer.
- [x] Company multi-select + sliders filter all widgets.
- [x] `python run.py --live` pulls real data + records latency (on an open network).
- [x] Daily budget enforced; key never committed.
- [x] Metric unit tests and browser smoke test pass.
