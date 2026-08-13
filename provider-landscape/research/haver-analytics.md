# Haver Analytics

## 1. Snapshot
- **Owner/parent:** Privately held (independent). Founded **1978**, HQ **New York City**, with offices in London, Singapore and Tokyo.
- **Positioning one-liner:** The long-standing "librarian" of global macro time series — 290+ curated databases from official/private sources, delivered through its DLX platform, favoured by professional economists and strategists for reliability and lineage.
- **Regions/coverage:** Global and **developed-market deep**, with strong detail for US, UK, Canada, Europe, Japan, Australia, New Zealand and China, plus 130+ emerging markets. Notable **US Economic Detail** depth; AU/NZ and Asia are well covered. EM breadth is real but CEIC is deeper on granular local EM sources.
- **Free tier:** No — subscription only. (Some Haver-sourced series surface publicly via FRED, but Haver's own product is paid.)
- **Pricing model & known ranges:** Enterprise subscription by database modules and seats; **not publicly disclosed** (quote-based). Independent competitor profiles imply low-mid six-figure institutional revenue per large client; individual footprints are mid five-figure and up.

## 2. Data-domain coverage
- **Macro indicators:** Yes — national accounts, prices, housing/construction, industrial production, employment, productivity, population; a core strength.
- **Central-bank/rates:** Yes — interest rates, money supply, public finance.
- **Trade:** Yes — international trade, wholesale/retail trade, shipments/inventories/orders.
- **Commodities:** Partial — commodity and market data databases via "Market Data" product, less a commodities specialist.
- **Forecasts:** Limited — Haver is a data-and-detail provider; forecasts come from third-party/consensus databases it hosts rather than proprietary models.
- **Country risk:** No dedicated rating product; supplies the underlying indicators.
- **High-frequency/alt-macro:** Yes — daily/weekly market and high-frequency series, business-cycle indicators, and archived vintages via HaverView.

## 3. Datasets
- **290+ time-series databases** (200+ from 1,350+ government and private sources; marketed as data from 2,500+ sources), spanning economic, financial, industry and market data.
- History depth: long official histories plus **archive/vintage databases** (point-in-time as-first-released data) for revision analysis.
- Update frequency: real-time to source cadence; databases refreshed continuously as releases arrive.
- Value-add: seasonally adjusted, nominal/real, USD-converted and other **calculated/derived series** on top of raw official data.

## 4. APIs & technical integration
- **API type:** Windows **DLX** desktop app; **DLX API** (COM/programmatic); platform-independent **HaverView** web access with a **RESTful API**; deep **Microsoft Office (Excel)** integration and connectors for **MATLAB, SAS, EViews, Stata, R/Python**.
- **Auth:** Subscription credentials / API keys via HaverView.
- **Formats:** Excel/CSV, and JSON/XML via the REST/HaverView API.
- **Rate limits:** Governed by subscription; not publicly published.
- **Delivery:** Desktop DLX, HaverView web/REST, Excel, statistical-package plugins, and bulk/archive database feeds; no publicly advertised native Snowflake/Databricks share or MCP server.

## 5. Enabling technology
- Emphasis on **curation and consistency**: standardised frequencies/units, derived aggregates, and careful source documentation ("data librarian" reputation).
- **Vintage/revision handling is a hallmark** — archive databases (ALFRED-like as-first-reported data) support real-time analysis and backtesting.
- DLX optimised for fast charting/analysis of very large series sets; HaverView modernises delivery.
- Growing REST/API and statistical-package integration; less marketed AI/LLM tooling than Macrobond.

## 6. Customer / user feedback
- Sentiment (industry profiles, research citations, practitioner commentary): trusted for **accuracy, breadth of detail and vintage archives**; a staple in central-bank, academic and sell-side macro workflows.
- Cons: legacy **Windows/DLX-centric UX** feels dated versus Macrobond's modern platform; enterprise pricing and setup; less slick charting/publishing. Public review volume is thin (gated, institutional).
- User segments: professional and academic economists, macro strategists, quants/modelers who need clean vintages, and research libraries.

## 7. Edge & positioning
- **Leads on:** data quality/curation, US and DM detail, and vintage/archive databases for revision-aware analysis.
- **Lags on:** modern UX, native cloud/Snowflake distribution, proprietary forecasts, and the deepest granular EM local-source data (where CEIC leads).
- **Best for:** economists/quants who prize reliable, well-documented, revision-tracked macro series and heavy Excel/stats-package integration.
- **Free pick?** No — premium institutional data.

## 8. Provenance
- https://www.haver.com/our-data — official coverage (290+ databases, sources) (accessed 2026-08-11)
- https://www.haver.com/about-us — official company background & offices (accessed 2026-08-11)
- https://haverproducts.com/products/ — official product line (US detail, market data, EM) (accessed 2026-08-11)
- https://www.mathworks.com/products/connections/product_detail/haver-time-series-databases.html — third-party integration (MATLAB, DLX API) (accessed 2026-08-11)
- https://www.owler.com/company/haver/competitors — independent competitor/positioning profile (accessed 2026-08-11)
- https://fred.stlouisfed.org/tags/series?t=haver — independent evidence of Haver-sourced series (accessed 2026-08-11)
