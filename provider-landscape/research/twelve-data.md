# Twelve Data

## 1. Snapshot
- **Owner/parent:** Twelve Data Inc. (independent, privately held). **HQ:** commonly listed as Singapore (US Delaware entity; distributed team). **Founded:** 2018. Positioning: single, well-documented REST + WebSocket API unifying stocks, forex, crypto, ETFs, indices, funds and fundamentals across global markets — "generous free plan" developer onboarding.
- **Regions/markets covered:** Broadly global — marketed as 250+ / 90+ international exchanges. **ASX explicitly covered** (dedicated exchange page; 20-min delayed + EOD, ASX-compliant, 99.95% SLA). **NZX explicitly covered** (dedicated XNZE exchange page + support article). Deep US coverage plus Europe (LSE, XETRA, Euronext) and Asia (HKEX, TSE, SGX, KRX etc.).
- **Free tier:** Yes (Basic) — 800 API credits/day, ~8 credits/min; US equities, forex, crypto; most technical indicators and international/fundamental data gated to paid.
- **Pricing model & known ranges (published):** Credit-based subscriptions. After a March-2026 revision, individual plans: Basic (free), **Grow ~$79/mo**, **Pro ~$229/mo**, **Ultra ~$999/mo** (earlier tiers were $29/$99/$329). Business plans (Venture/Enterprise) are higher/custom. Higher tiers add international markets, level B/C assets, deeper fundamentals, more credits/min.

## 2. Data-domain coverage
- **Public equity:** strong — global stocks/ETFs/indices/funds via one API.
- **Fundamentals:** yes — statements, ratios, earnings, dividends/splits (depth scales with tier).
- **Forex:** strong — broad currency-pair coverage, real-time.
- **Crypto:** strong — 180+ crypto exchanges referenced.
- **News:** yes — news endpoints on paid tiers.
- **Macro:** partial — economic/reference data.
- **Options / fixed income / ESG / alt-data:** limited or not a focus.

## 3. Datasets
- Real-time (WebSocket), delayed, and EOD across US + 90-250 global exchanges; time-series (1min → monthly), technical indicators (50+ built in), fundamentals, dividends/splits, earnings, forex, crypto, indices, mutual funds. History depth varies by asset/exchange (multi-year). Differentiator: unusually generous free tier and one consistent schema across asset classes and geographies (incl. ASX + NZX).

## 4. APIs & technical integration
- **API type:** REST (JSON/CSV) + real-time **WebSocket** (wss://ws.twelvedata.com); official SDKs (Python, etc.); Google Sheets add-on; Excel support.
- **Auth:** API key. **Rate limits:** credit-based (per-minute + per-day) rather than raw request caps.
- **Delivery:** API + WebSocket + spreadsheet add-ons; batch endpoints. No prominent first-party Snowflake/Databricks marketplace listing surfaced.
- **MCP:** no widely-documented official Twelve Data MCP server as of research date (community wrappers may exist); primary integration is REST/WebSocket/SDK.

## 5. Enabling technology
- Aggregates multiple licensed venue/vendor feeds into a normalized multi-asset API; advertises 99.95% SLA uptime and low-latency streaming. AI/analytics: built-in technical indicators computed server-side. Reliability signals: strong docs, stable WebSocket, SLA guarantees on paid tiers.

## 6. Customer / user feedback
- **G2 (Twelve Data):** ~4.7/5 (small sample, ~3 reviews). **Trustpilot / SourceForge / Slashdot:** additional listings, generally positive.
- **Recurring pros:** best-in-class free tier, clean docs, reliable data, responsive support, competitive price, genuine global (ASX/NZX) coverage. **Cons:** low-tier rate/credit limits feel restrictive; some indicators/international/fundamental data locked behind paid; review sample sizes small.
- **Who uses it:** indie developers, fintech apps, trading-bot builders, dashboards needing multi-asset global coverage cheaply.

## 7. Edge & positioning
- **Leads:** breadth of global exchanges (explicit ASX + NZX), unified multi-asset schema, most generous free plan, solid WebSocket. **Lags:** thin options/fixed-income/ESG; credit model can surprise heavy users; smaller independent-review footprint than incumbents. **Best-for:** developers wanting one API for worldwide equities+forex+crypto (including ANZ markets) with a usable free tier.

## 8. Provenance
- https://twelvedata.com/pricing — official individual pricing/credits (accessed 2026-08-11)
- https://twelvedata.com/exchanges/XASX — ASX coverage page (accessed 2026-08-11)
- https://support.twelvedata.com/en/articles/5749835-new-zealand-s-exchange-nzx — NZX support article (accessed 2026-08-11)
- https://twelvedata.com/exchanges/xnze — NZX exchange page (accessed 2026-08-11)
- https://datarade.ai/data-providers/twelve-data/profile — profile, coverage, founding (accessed 2026-08-11)
- https://www.g2.com/products/twelve-data/pricing — G2 pricing/rating (accessed 2026-08-11)
- https://www.trustpilot.com/review/twelvedata.com — user reviews (accessed 2026-08-11)
- https://twelvedata.com/ — product overview & WebSocket (accessed 2026-08-11)
