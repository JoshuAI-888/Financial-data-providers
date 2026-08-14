# OECD / IMF / World Bank Open Data APIs

## 1. Snapshot
- **Owner/parent:** Three separate intergovernmental organizations — Organisation for Economic Co-operation and Development (38 member countries), International Monetary Fund (190 member countries), World Bank Group — each publishing its own free statistical API.
- **Coverage:** OECD: 38 member + accession/key-partner countries, 1,500+ datasets. IMF: near-global (190 countries), World Economic Outlook + ~10 major statistical databases (IFS, BOP, GFS, FM, MFS). World Bank: 200+ countries/economies, 29,000+ development indicators back to 1960.
- **Free tier:** yes for all three — no cost, and for OECD and World Bank no API key/registration is required either; IMF's SDMX API layer is also free, though some of IMF's premium analytical products/portals sit behind subscription.
- **Pricing model & ranges:** Free/open data (World Bank data is CC BY 4.0). No commercial pricing tier for the core statistical APIs; IMF's top-tier subscription products (e.g., certain WEO/IFS premium interfaces) are the exception, not the base API.

## 2. Coverage
**OECD**: 38 member countries plus G20/accession/key partner economies; ~1,500+ datasets spanning national accounts, prices, labour, trade, health, education, environment, and the Better Life Index; most series run 1980–present with near-term estimates for aggregates. **IMF**: near-universal country coverage (190 members) via World Economic Outlook (40+ indicators — GDP, inflation, unemployment, government debt, current account), International Financial Statistics, Balance of Payments, Government Finance Statistics, Monetary and Financial Statistics, and the Fiscal Monitor. **World Bank**: broadest country coverage (200+ economies/aggregates) and longest history (from 1960) across development indicators — GDP, population, poverty, health, education, trade, FDI — plus specialized sub-portals (World Bank Data360, African Development Indicators, Joint External Debt Hub, Global Economic Monitor).

## 3. Datasets
OECD: Quarterly National Accounts, Economic Outlook, Main Economic Indicators, PPPs, trade, employment/unemployment, government finance, environment/energy. IMF: WEO (flagship twice-yearly projections dataset), IFS (exchange rates, money & banking, prices), BOP, GFS, MFS, FM, and CPI/PPI databases. World Bank: World Development Indicators (flagship), Doing Business (discontinued but archived), Global Economic Monitor (high-frequency), Health Nutrition & Population Statistics, Gender Statistics, Education Statistics, Quarterly External Debt Statistics, and the newer World Bank Data360 cross-source portal.

## 4. APIs & technical integration
All three are built on the SDMX (Statistical Data and Metadata eXchange) standard, the common protocol also used by the ECB and BIS, which eases cross-source aggregation (this is exactly what DBnomics harvests from). **OECD**: RESTful SDMX API, JSON/XML/CSV via the OECD Data Explorer's "Developer API" button, no key required. **IMF**: SDMX 3.0 API at api.imf.org/external/sdmx/3.0, dataflow-based queries (e.g., WEO editions as dataflow versions); widely accessed via the `sdmx1` Python library or the community `imf-reader`/`imfweo` packages. **World Bank**: simple REST v2 Indicators API (JSON/XML, URL- or argument-based queries), no key, effectively no rate limit for normal use; also `world-bank-data` Python package and the newer Data360 API. All three support bulk/programmatic access suitable for ETL pipelines.

## 5. Enabling technology
Standard government/IGO statistical-warehouse architecture (SDMX data model + REST/XML gateways) rather than AI/ML-driven platforms. Data quality rests on each organization's own national-accounts and statistical-collection methodology and member-country reporting obligations (particularly binding for IMF Article IV / SDDS-subscribing countries). No proprietary estimation layer beyond each org's own official nowcasts/projections (e.g., IMF WEO forecasts).

## 6. Customer / user feedback
Treated as the authoritative, citable "ground truth" source for official macro/development statistics by academics, journalists, central banks, and other data aggregators (FRED, DBnomics, Trading Economics, CEIC all ingest and republish OECD/IMF/World Bank series). Common complaints: SDMX's steep learning curve versus simpler REST norms, inconsistent update lags across national contributors, occasional revision/break-in-series issues, and IMF's split between its fully-open SDMX layer and its higher-friction/subscription analytical portals. World Bank's API is broadly praised as the easiest of the three for developers (no key, simple JSON).

## 7. Edge & positioning
- **Leads on:** Unimpeachable official provenance, near-total country coverage (esp. World Bank/IMF), zero cost, standardized SDMX interoperability that other aggregators build on top of.
- **Lags on:** No proprietary company-level, ESG, or high-frequency market data; SDMX complexity vs. modern REST/JSON-first APIs; inconsistent release timeliness across member countries; limited built-in analytics/visualization beyond each org's own portal.
- **Best-for:** Ground-truth official macro/development benchmarks, cross-country comparisons, and as upstream feed sources for aggregator/report layers (complements FRED's US depth and DBnomics' aggregation).

## 8. Provenance
- https://data-explorer.oecd.org/ — OECD Data Explorer, SDMX API entry point (accessed 2026-08-14)
- https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html — official OECD API explainer (accessed 2026-08-14)
- https://www.oecd.org/en/data/insights/data-explainers/2024/09/OECD-DE-FAQ.html — OECD Data Explorer FAQ (accessed 2026-08-14)
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf — official IMF SDMX Central web-services guide (accessed 2026-08-14)
- https://bd-econ.com/imfapi1.html — practitioner IMF SDMX API walkthrough (accessed 2026-08-14)
- https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation — official World Bank Indicators API docs (accessed 2026-08-14)
- https://datahelpdesk.worldbank.org/knowledgebase/articles/1886674-new-features-and-enhancements-in-the-v2-api — World Bank API v2 features (accessed 2026-08-14)
- https://data.worldbank.org/ — World Bank Open Data portal, CC BY 4.0 licensing (accessed 2026-08-14)
