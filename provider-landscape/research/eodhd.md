# EODHD (EOD Historical Data)

## 1. Snapshot
- **Owner/parent:** Unicorn Data Services SAS (trades as EODHD / EODHistoricalData). **HQ:** Lyon, France. **Founded:** ~2018; bootstrapped, no outside VC. Positioning: affordable, developer-first "all-world" historical + real-time financial-data API for retail quants, fintechs and researchers.
- **Regions/markets covered:** Genuinely global — 60+ exchanges, 150K+ tickers across US, Europe, Asia-Pacific, LATAM. **ASX explicitly covered** (EODHD is a licensed ASX redistributor with a dedicated ASX product page: EOD, fundamentals, live/delayed, corporate actions). European (LSE, XETRA, Euronext) and major Asian markets (HKEX, TSE, SGX, KRX) covered. **NZX:** not clearly listed as a supported exchange in EODHD's coverage lists — treat NZX as unconfirmed/likely absent.
- **Free tier:** Yes — free API key gives ~20 API calls/day and a ~1-year EOD history window, limited US-centric fundamentals. Adequate for testing only.
- **Pricing model & known ranges (published):** EOD Historical Data (All World) ~$19.99/mo ($199/yr); EOD+Intraday (All World Extended) ~$29.99/mo; Fundamentals Data Feed ~$59.99/mo; "All-In-One" bundle ~€99.99/mo (historical + fundamentals + real-time + intraday + news). Annual billing discounts ~2 months.

## 2. Data-domain coverage
- **Public equity:** strong — 60+ exchanges, 30+ yrs EOD history, splits/dividends.
- **Fundamentals:** strong — standardized financial statements, ratios, ~30 yrs depth for many names; global (not US-only).
- **Fixed income:** partial — government bond yields / some bond data.
- **Forex:** yes — ~1,100 pairs, EOD + intraday + real-time.
- **Crypto:** yes — major coins/exchanges.
- **Options:** yes — US options (EOD chains, IV/greeks).
- **News:** yes — financial news + sentiment feed.
- **Macro:** yes — macro-economic indicators, US Treasury rates, economic calendar.
- **ESG:** yes — ESG scores endpoint.

## 3. Datasets
- 150K+ tickers / 60+ exchanges; 30+ years EOD price history; splits & dividends; global fundamentals (income/balance/cash-flow, ratios, analyst estimates, insider transactions); intraday (1m/5m/1h) with limited history; real-time (US) and 15-20-min delayed feeds for many international venues; US options chains; ESG, macro, calendars, index constituents, stock logos; a "Marketplace" of add-on premium datasets. Bulk API downloads a whole exchange's EOD/splits/dividends for one day in a single call.
- Differentiated: licensed ASX redistribution; breadth-per-dollar (all-world EOD for ~$20/mo) is the standout.

## 4. APIs & technical integration
- **API type:** REST (JSON/CSV) primary; **WebSocket** for real-time streaming (sub-second, US + major EU/Asia + forex/crypto); Python/other community SDKs; official downloader tools (Windows/Linux); Excel/Google-Sheets guides.
- **Auth:** API token in query string; OAuth 2.1 supported on the v2 API path.
- **Rate limits:** per-plan daily API-call quotas (free = 20/day; paid tiers scale to tens of thousands+/day); some endpoints cost multiple "calls".
- **Delivery:** REST + WebSocket + bulk endpoints + downloadable files. No first-party Snowflake/Databricks listing surfaced (bulk flat downloads instead).
- **MCP:** Yes — official **EODHD MCP Server** (GitHub: EodHistoricalData/EODHD-MCP-Server), 70+ tools across 15 categories (prices, fundamentals, news/sentiment, technicals, options, treasury, ESG, macro, calendars, marketplace), OAuth 2.1, works with Claude and other LLM clients.

## 5. Enabling technology
- Aggregates/normalizes third-party and exchange-licensed feeds into a uniform schema; official redistribution licenses for regulated venues (e.g. ASX). Emphasis on standardized fundamentals so cross-market comparison works. AI features: MCP server + news-sentiment scoring. Reliability: bootstrapped to six-figure MRR with a long-standing retail/quant user base; documented SLAs on paid real-time.

## 6. Customer / user feedback
- **Trustpilot (eodhd.com):** ~4/5 stars across ~130-140 reviews. **G2:** listed (EODHD Financial Data APIs) with a smaller review count.
- **Recurring pros:** exceptional price-to-breadth, responsive/helpful support, clear docs, reliable EOD. **Cons:** free tier very tight (20 calls/day, 1-yr history); some fundamentals gaps/lag on smaller international names; real-time depth narrower than pure market-data vendors.
- **Who uses it:** indie quants, fintech startups, academic researchers, portfolio tools needing cheap global EOD + fundamentals.

## 7. Edge & positioning
- **Leads:** best value for all-world EOD + global fundamentals at retail price; licensed ASX access; strong MCP/LLM story. **Lags:** not a low-latency/tick microstructure vendor; NZX and some frontier venues absent; intraday history shallow vs specialists. **Best-for:** budget-conscious builders needing broad global EOD + fundamentals (incl. ASX) through one cheap API.

## 8. Provenance
- https://eodhd.com/pricing — official pricing tiers (accessed 2026-08-11)
- https://eodhd.com/asx-data — ASX coverage & license (accessed 2026-08-11)
- https://eodhd.com/financial-apis/mcp-server-for-financial-data-by-eodhd — official MCP server docs (accessed 2026-08-11)
- https://github.com/EodHistoricalData/eodhd-mcp-server — MCP server repo (accessed 2026-08-11)
- https://eodhd.com/financial-apis/bulk-api-eod-splits-dividends — bulk download API (accessed 2026-08-11)
- https://www.trustpilot.com/review/eodhd.com — user ratings/reviews (accessed 2026-08-11)
- https://www.g2.com/products/eodhd-financial-data-apis/pricing — G2 listing/pricing (accessed 2026-08-11)
- https://hackernoon.com/how-eodhd-apis-quietly-built-a-six-figure-business-by-fixing-financial-data — company background (accessed 2026-08-11)
