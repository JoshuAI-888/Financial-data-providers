# Ortex

## 1. Snapshot
- **Owner/parent:** Ortex Technologies Ltd — independent, privately held UK company (registered with UK Companies House, company no. 11033216). No disclosed parent or public acquisition found.
- **Coverage:** Short interest and securities-lending analytics on 70,000+ securities globally, modeled from data aggregated across 700K+ pools of liquidity (agent lenders, prime brokers, broker-dealers) rather than sourced from a single feed.
- **Free tier:** Yes, but limited — Ortex offers a free/lowest tier, though user reviews report that core features (short interest, trading signals) are gated behind paid plans even after free signup; treat as a limited "preview" tier rather than a fully functional free product.
- **Pricing model & ranges:** Consumer/prosumer subscription tiers, reported (with some inconsistency across sources) as roughly Basic ~$39-49/month (or ~$39/year in one annual-plan citation) and Advanced ~$99-149/month, i.e., a self-serve, individually-priced product — notably more accessible than institutional peers like S3 Partners. Ortex has also publicly announced pricing-structure changes ("A New Pricing Structure for ORTEX"), so current published rates should be reconfirmed.

## 2. Coverage
Global equities (70,000+ securities) with real-time and historical short-interest metrics: shares on loan, utilization rate, days-to-cover, cost-to-borrow, and free-float-on-loan. Data is modeled/estimated from securities-lending desks (agent lenders, prime brokers, broker-dealers) rather than pulled directly from a single exchange feed — Ortex explicitly states its own figures are *estimates* sampled from a portion of the lending market and can diverge from FINRA's official (lagged, twice-monthly) short-interest reports. Ortex reports a ~97% accuracy rate against eventually-published exchange-reported short interest.

## 3. Datasets
- Short interest (real-time/intraday estimate) and short-interest history/charting.
- Securities-lending analytics: shares on loan, utilization rate, days-to-cover, cost-to-borrow, free-float-on-loan.
- Ortex Stock Score: a proprietary 0-100 daily ranking per stock combining short-interest composites, quality/momentum/value ML-derived signals, and rule-based technical factors (EPS, RSI, MACD among cited inputs); backtested to 2010; supports custom factor-weighting via API.
- Short Squeeze signal/finder.
- Options analytics (cited as part of the API's institutional-grade dataset alongside short interest and stock scores).

## 4. APIs & technical integration
- **API type:** REST-style JSON/CSV API (docs.ortex.com) for programmatic access to short interest, options analytics, and stock scores; explicit endpoints for pulling custom-weighted stock scores (e.g., `stock_stock_scores_create`).
- **SDK:** Python SDK cited for programmatic access; also supports direct feeds into Excel.
- **Delivery:** Pull single-ticker or full-universe queries; scalable JSON/CSV designed for integration into trading and risk models.
- **MCP availability:** No official MCP server identified in research.
- **Auth:** Subscriber-based API access tied to paid plan tier (exact auth mechanism — API key vs. OAuth — not confirmed in available sources).

## 5. Enabling technology
A modeling/estimation engine that infers short-interest and lending-market metrics from an aggregated pool of 700K+ liquidity sources (agent lenders, prime brokers, broker-dealers) to approximate real-time short positioning between official (twice-monthly, lagged) exchange disclosures — Ortex reports ~97% back-tested accuracy against eventual official figures. Layered on top is a machine-learning/AI-weighted daily Stock Score model (backtested to 2010) blending proprietary short-interest composites with quality/momentum/value cross-sectional ML signals and standard technical indicators.

## 6. Customer / user feedback
79 reviews on Trustpilot with mixed sentiment: some praise data quality and support; others raise accuracy and billing-practice concerns, and one recurring theme is that certain features marketed as "free" (short interest, trading signals) are effectively inaccessible without a paid plan. Third-party comparison pieces (e.g., Ortex vs. S3 Partners) frame Ortex favorably for accessibility ("wins for accessible, timely short positioning at an individual budget") while conceding S3 wins on institutional depth and authority for large desks. No G2/Capterra enterprise-review volume found — consistent with Ortex's retail/prosumer rather than institutional customer base.

## 7. Edge & positioning
- **Leads on:** Accessibility and price — the only one of the three short-interest peers (Ortex, S3 Partners, Fintel) priced for individual/retail and semi-professional traders rather than institutional desks, with a genuine self-serve API and near-real-time (intraday) short-interest estimates versus the exchange's twice-monthly official cadence.
- **Lags on:** Institutional authority and depth versus S3 Partners (the standard for Bloomberg terminals, prime brokers, and large hedge-fund desks, drawing on aggregated buy-side/sell-side/regulatory data) and breadth of ownership/insider-activity context versus Fintel (which layers short data with ownership and insider activity); Ortex's own numbers are estimates, explicitly caveated as capable of diverging from official FINRA figures.
- **Best-for:** Retail and semi-professional traders and smaller funds wanting near-real-time, affordable short-squeeze and securities-lending signals via a self-serve API/Excel feed — not the default choice for large institutional desks that need S3-grade authoritative daily short-interest data or Fintel-style ownership/insider fusion.

## 8. Provenance
- https://docs.ortex.com/ — official API documentation: endpoints, stock score custom-weighting (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://public.ortex.com/help-stock-short-interest-data-row/ — short interest/securities-lending data methodology (accessed 2026-08-14)
- https://public.ortex.com/articles/ortex-stock-score-backtest — Stock Score methodology, ~97% accuracy claim (accessed 2026-08-14)
- https://public.ortex.com/ortex-pricing/ — pricing tiers (accessed 2026-08-14)
- https://www.trustpilot.com/review/ortex.com — customer reviews, 79 reviews, mixed sentiment (accessed 2026-08-14)
- https://www.alphanume.com/blog/ortex-vs-s3-partners — third-party peer comparison vs. S3 Partners (accessed 2026-08-14)
- https://www.s3partners.com/ — S3 Partners peer positioning (institutional short data) (accessed 2026-08-14)
- https://find-and-update.company-information.service.gov.uk/company/11033216 — UK company registration, Ortex Technologies Ltd (accessed 2026-08-14)

**Note:** WebFetch to ortex.com and docs.ortex.com was egress-blocked in this environment; findings rely on the WebSearch index and third-party secondary sources rather than direct page retrieval. Pricing figures showed minor inconsistencies across sources ($39-49/mo vs. $99-149/mo tier boundaries, and an "annual $39" citation) — Ortex has publicly changed its pricing structure at least once, so current rates should be reconfirmed directly.
