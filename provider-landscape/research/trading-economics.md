# Trading Economics

## 1. Snapshot
- **Owner/parent:** Privately held (founder-owned); co-founders Andre Fernandes Sousa (CEO) and Anna Fedec retain ownership. HQ in New York City, with operations in Lisbon (Portugal), Jakarta and Belem. Founded 2007/2008.
- **Positioning one-liner:** Broad, low-cost, self-service macro + markets data covering "20 million indicators for 196 countries," known for its widely-embedded web charts, economic calendar and proprietary country forecasts/credit scores.
- **Regions/coverage:** Global. Strong on breadth over depth — it re-publishes official series for 196 countries including less-developed Africa/Latin America/Asia markets. Asia/Europe coverage is broad; NZ/AU present at the headline-indicator level (GDP, CPI, rates, calendar) but not deep local-source detail like CEIC/Haver.
- **Free tier:** Partial. The web site is free to browse; the legacy `guest:guest` sample key was discontinued for the REST API (July 2026). A free/trial developer account exists but is capped (widely reported ~100 requests / 100,000 data points), so it is a trial rather than a durable free tier. Free web-chart embeds remain available with attribution.
- **Pricing model & known ranges:** Subscription, scaled by features, request volume and redistribution rights. Not fully published on-site (requires account), but independent 2026 comparisons cite roughly **USD $149/month (Standard)** and **$299/month (Professional)**, billed yearly, with Enterprise custom. Analytics/terminal seats priced separately.

## 2. Data-domain coverage
- **Macro indicators:** Yes — GDP, inflation, labour, housing, tax/population etc. for 196 countries; the core product.
- **Central-bank/rates:** Yes — policy rates, government bond yields, money supply.
- **Trade:** Yes — balance of trade, current account, external-sector series.
- **Commodities:** Yes — commodity prices (energy, metals, agriculture) as market quotes.
- **Forecasts:** Yes — proprietary forward-looking forecasts for most indicators (1–2yr) plus consensus figures; a signature feature.
- **Country risk:** Yes — a proprietary numeric "TE credit rating" (0–100) from a forward-looking macro model, alongside agency ratings.
- **High-frequency/alt-macro:** Limited — real-time market quotes and a live economic calendar, but not a deep nowcasting/alt-data suite.

## 3. Datasets
- Marketed as **20 million indicators / 196 countries**; a curated National Statistical Database of 15,000+ series drawn directly from central banks and statistical agencies, plus markets (FX, indices, bonds, commodities) and company financials.
- History depth varies by series (typically to source availability, often decades); markets are real-time/EOD.
- Proprietary content: **country forecasts, consensus estimates and the numeric credit-rating index** are Trading Economics' own model output, not ingested.
- Update frequency: real-time for markets and the calendar; official series updated on release.

## 4. APIs & technical integration
- **API type:** REST (JSON/XML/CSV), plus an **Excel Add-In**, a Python package (`tradingeconomics` on PyPI), R examples, and a WebSocket **streaming** feed for markets.
- **Auth:** API key from developer.tradingeconomics.com (key or client:secret). Guest sample access largely retired in 2026.
- **Formats:** JSON, XML, CSV.
- **Rate limits:** Tied to plan; trial accounts limited (~100 requests / 100k data points). Higher tiers raise volume and grant redistribution.
- **Delivery:** API/Excel/streaming; no first-party Snowflake/Databricks share advertised. No MCP server known.

## 5. Enabling technology
- Ingests official releases and normalises them into a single indicator schema keyed by country/indicator, which powers the calendar and comparable cross-country charts.
- Revisions: actual values update on release; the calendar carries previous/consensus/actual, but it is not a formal point-in-time vintage archive like ALFRED/Macrobond.
- Proprietary econometric forecasting models and the model-driven credit score are the main "value-add" layer.
- Widely embedded web widgets/charts are a distinctive distribution technology.

## 6. Customer / user feedback
- Sentiment (independent reviews, developer forums): valued for **breadth, ease of embedding, and low cost** relative to Bloomberg/Refinitiv; the free web charts and calendar are ubiquitous in fintech and media.
- Cons: data is **re-published from official sources** (so accuracy/latency depends on TE's refresh), documentation and support are considered lighter than premium vendors, and forecasts are proprietary "black-box" model output. Media Bias/Fact Check rates its factual reporting as generally reliable/data-driven.
- User segments: fintech developers, retail/independent traders, journalists, students, and smaller research shops that need cheap wide coverage rather than deep local-source EM detail.

## 7. Edge & positioning
- **Leads on:** affordability, global breadth, easy API/Excel/web-embed access, and ready-made forecasts + a simple numeric country-risk score.
- **Lags on:** depth and provenance versus CEIC/Haver (fewer granular local-source series), vintage/revision rigour, and enterprise-grade support.
- **Best for:** cost-conscious teams, developers and media needing wide, quick, embeddable macro + markets coverage with forecasts.
- **Free pick?** Not a true free data source for programmatic use (trial-capped), but the **free web charts/calendar** make it the cheapest broad option; FRED/World Bank/DBnomics are the genuinely-free picks.

## 8. Provenance
- https://tradingeconomics.com/api/ — official API product page (accessed 2026-08-11)
- https://docs.tradingeconomics.com/get_started/ — official API docs & getting started (accessed 2026-08-11)
- https://docs.tradingeconomics.com/indicators/indicators-countries/ — indicators & country coverage list (accessed 2026-08-11)
- https://docs.tradingeconomics.com/markets/streaming/ — streaming/WebSocket & guest-key notes (accessed 2026-08-11)
- https://tradingeconomics.com/forecast/credit-rating — proprietary credit-rating methodology (accessed 2026-08-11)
- https://www.findmymoat.com/tools/trading-economics — independent review & pricing figures (accessed 2026-08-11)
- https://mediabiasfactcheck.com/trading-economics-bias/ — independent reliability assessment (accessed 2026-08-11)
- https://www.crunchbase.com/organization/trading-economics — company/founder background (accessed 2026-08-11)
