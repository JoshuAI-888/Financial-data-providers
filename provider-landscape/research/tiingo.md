# Tiingo

## 1. Snapshot
- **Owner/parent:** Tiingo, Inc. — privately owned, **unfunded/bootstrapped**. **HQ:** commonly listed as Seekonk, MA / New York City, USA. **Founded:** 2014 by Rishi Singh (ex-Citigroup exotic-derivatives trader; first employee at quant fund AlphaParity). Positioning: high-quality, low-cost financial-data platform + API with a genuinely usable free tier and deep clean price history; founder-run with hands-on support.
- **Regions/markets covered:** **US-centric.** Core is US equities, ETFs and mutual funds, plus **Chinese A-shares**. Global crypto (150+ exchanges) and FX (140+ pairs). **ASX and NZX: not covered** — Tiingo is not a broad multi-exchange international equities vendor.
- **Free tier:** Yes and genuinely usable — free key gives access to ~500 unique symbols/month and 30+ years of EOD history, with generous personal-use limits (rate caps apply).
- **Pricing model & known ranges (published):** Flat-rate, low-cost. Paid plans start around **$30/mo** (Power/commercial), with individual "starter" tiers cheaper; separate commercial licensing. Fundamentals are an add-on (via a third-party provider; contact sales). Much cheaper than institutional vendors.

## 2. Data-domain coverage
- **Public equity:** strong (US) — 80,000+ assets incl. delisted; EOD back to 1962.
- **Fundamentals:** yes (add-on) — US financial statements/metrics via partner.
- **Forex:** yes — 140+ pairs.
- **Crypto:** yes — 150+ exchanges.
- **News:** strong — 70M+ curated news articles spanning 20+ years, tagged to tickers.
- **Macro / options / fixed income / ESG / alt-data:** minimal/none.

## 3. Datasets
- 80,000+ US equities/ETFs/mutual funds (survivorship-bias-aware, incl. delisted); EOD price history back to 1962; **real-time via IEX**; real-time overnight/extended via **Blue Ocean ATS**; Chinese A-shares; crypto (150+ exchanges) and FX (140+ pairs); fundamentals add-on; large curated news corpus (70M+ articles, 20+ yrs). Differentiators: exceptionally deep, clean, cheap US EOD history; long news archive; founder-vetted data quality.

## 4. APIs & technical integration
- **API type:** REST (JSON/CSV); **WebSocket** streaming (IEX real-time, news, crypto/FX); Python SDK; pandas-datareader integration.
- **Auth:** API token.
- **Rate limits:** per-plan hourly/daily + monthly unique-symbol caps on free.
- **Delivery:** REST + WebSocket. No first-party Snowflake/Databricks marketplace or bulk flat-file program surfaced.
- **MCP:** no widely-documented official Tiingo MCP server (community wrappers possible); integration is REST/WebSocket/SDK.

## 5. Enabling technology
- Aggregates and cross-validates multiple licensed sources ("multiple trusted sources") with a focus on data-cleaning and point-in-time integrity; IEX + Blue Ocean ATS partnerships supply real-time and overnight US pricing. Reliability signal: profitable/bootstrapped, founder answers support calls/emails; used by pension/hedge funds and RIAs alongside retail.

## 6. Customer / user feedback
- No large single-source star rating surfaced; sentiment triangulated across reviews (Find My Moat, Capital Spectator, InvestingBrokers, day-trade review blogs) is consistently positive.
- **Recurring pros:** outstanding price-to-value, deep/clean US history, usable free tier, responsive founder-led support, reliable EOD, great news archive. **Cons:** US-only equity focus (plus China A-shares) — no ASX/NZX/broad international; fundamentals only via add-on; smaller support org than incumbents.
- **Who uses it:** independent RIAs, quant researchers, backtesters, fintech apps, and some institutional (pension/hedge) desks wanting cheap clean US history.

## 7. Edge & positioning
- **Leads:** best value for deep, clean US EOD history + long news corpus; trustworthy founder-run support. **Lags:** no meaningful international/ANZ equities, thinner fundamentals, no marketplace/bulk enterprise delivery. **Best-for:** US-focused research, backtesting and news analytics on a tight budget.

## 8. Provenance
- https://www.tiingo.com/pricing — official pricing/plans (accessed 2026-08-11)
- https://www.tiingo.com/about/pricing — pricing detail (accessed 2026-08-11)
- https://www.tiingo.com/products/end-of-day-stock-price-data — EOD dataset/history depth (accessed 2026-08-11)
- https://www.crunchbase.com/organization/tiingo — founding, HQ, funding status (accessed 2026-08-11)
- https://www.capitalspectator.com/tiingo-com-my-go-to-database-for-historical-market-prices/ — independent user review (accessed 2026-08-11)
- https://www.findmymoat.com/tools/tiingo — review, coverage, pricing (accessed 2026-08-11)
- https://investingbrokers.com/tiingo-review/ — independent review (accessed 2026-08-11)
