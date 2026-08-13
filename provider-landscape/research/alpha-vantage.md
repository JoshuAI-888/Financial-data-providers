# Alpha Vantage

## 1. Snapshot
- **Owner/parent:** Alpha Vantage Inc. (independent; Y Combinator-affiliated). **HQ:** Boston, MA, USA. **Founded:** 2017 by Olivier Porte and Steve Zheng (started as a grad-school project; scaled fast when Yahoo Finance killed its API). Positioning: free-to-start, developer-friendly REST API for equities, forex, crypto and 50+ technical indicators — the classic "first API a hobbyist reaches for."
- **Regions/markets covered:** Primarily **US-centric** but with global equity reach — markets itself as 200,000+ tickers across 20+ exchanges. Non-US (Europe, Asia) equities exist but are a secondary, thinner catalog. **ASX and NZX:** some global-equity symbols may resolve, but ANZ markets are not a stated/first-class coverage area — treat as unreliable/unsupported for production ANZ use.
- **Free tier:** Yes — 25 API requests/day, 5 requests/min, free key by email. Notably, real-time and even 15-min-delayed US market data are excluded from free (require a paid plan + entitlement step).
- **Pricing model & known ranges (published):** Five premium tiers by requests/minute (no daily cap): $49.99/mo (75 rpm, 15-min delayed + EOD options), $99.99/mo (150 rpm, real-time US eligible), $149.99/mo (300 rpm), $199.99/mo (600 rpm), $249.99/mo (1,200 rpm); custom above. Annual ≈ 10× monthly.

## 2. Data-domain coverage
- **Public equity:** yes — global tickers, but US is the strong core.
- **Fundamentals:** yes — income/balance/cash-flow, overview, earnings, dividends/splits (US strongest).
- **Forex:** yes — real-time & historical FX.
- **Crypto:** yes — digital-currency endpoints.
- **News:** yes — news & sentiment API.
- **Macro:** yes — US macro indicators (GDP, CPI, treasury yields, etc.).
- **Options:** partial — EOD (and some real-time) US options on paid tiers.
- **Technical indicators:** strong — 50+ built-in.
- **ESG / fixed income / alt-data:** minimal/none.

## 3. Datasets
- 20+ years history on core equities; global equity symbol set (200K+ tickers claimed, US-weighted); intraday (1/5/15/30/60min), daily/weekly/monthly adjusted; 50+ technical indicators computed server-side; FX and crypto time-series; fundamentals; news-sentiment; US macro. Delivery is mostly EOD/delayed; real-time US requires higher paid tiers/entitlement. Differentiator: ready-made technical indicators + simplest possible onboarding.

## 4. APIs & technical integration
- **API type:** REST (JSON/CSV); official Python/other libraries; Excel & Google Sheets add-ons. No native streaming/WebSocket (polling only).
- **Auth:** single API key in query string.
- **Rate limits:** free 25/day + 5/min; paid tiers defined by requests/minute.
- **Delivery:** REST only; no first-party bulk flat-file or Snowflake/Databricks marketplace presence.
- **MCP:** no widely-known official Alpha Vantage MCP server (community/third-party wrappers exist); integration is REST + spreadsheet add-ons.

## 5. Enabling technology
- Cloud REST service aggregating market/fundamental feeds with server-side indicator computation; free-tier virality is the growth engine. AI features: news-sentiment scoring. Reliability: long-lived, widely embedded in tutorials/courses; but rate limits and delayed-by-default data cap production reliability.

## 6. Customer / user feedback
- **Trustpilot (alphavantage.co):** low — ~2.4/5 (small sample ~11 reviews). Software directories (SourceForge/Slashdot/G2) and review blogs are more mixed-to-positive on ease of use.
- **Recurring pros:** dead-simple to start, free key, great for learning/prototyping, built-in indicators, good docs. **Cons:** very tight free limits (25/day), no real-time on free, occasional data-quality/gaps complaints, no streaming, thin non-US depth, support responsiveness criticized.
- **Who uses it:** students, hobbyist algo-traders, tutorial/course authors, early prototypes.

## 7. Edge & positioning
- **Leads:** frictionless onboarding, indicator library, brand ubiquity in dev education. **Lags:** production scale (rate caps, delayed default data), no streaming, weak international/ANZ coverage, low trust score. **Best-for:** learning, prototyping and low-volume US-centric projects — not institutional or ANZ market data.

## 8. Provenance
- https://www.alphavantage.co/ — official product/overview (accessed 2026-08-11)
- https://www.alphavantage.co/documentation/ — official API docs/endpoints (accessed 2026-08-11)
- https://www.ycombinator.com/companies/alpha-vantage — company profile/founding (accessed 2026-08-11)
- https://apis.io/plans/alpha-vantage/alpha-vantage-plans-pricing/ — pricing tiers summary (accessed 2026-08-11)
- https://tradingtoolshub.com/review/alpha-vantage/ — independent review, free limits (accessed 2026-08-11)
- https://tradersunion.com/reviews/alphavantage-co/ — independent review/rating (accessed 2026-08-11)
- https://blocksentient.com/review/alpha-vantage/ — 2026 review, coverage notes (accessed 2026-08-11)
