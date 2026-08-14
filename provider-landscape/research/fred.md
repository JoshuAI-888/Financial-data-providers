# FRED (Federal Reserve Economic Data)

## 1. Snapshot
- **Owner/parent:** Federal Reserve Bank of St. Louis (Research Division); a US public-sector institution, not a commercial vendor.
- **Coverage:** 800,000+ economic time series from 100+ source agencies; primarily US national/state/regional macro, financial, and demographic data, with some international series (e.g., OECD, World Bank, IMF series republished within FRED).
- **Free tier:** yes — the entire service is free; a free API key is required and raises the rate limit from 30 to 120 requests/minute (40 req/min for the series-observations endpoint specifically). No paid tier exists.
- **Pricing model & ranges:** None. 100% free, no premium upgrade path, no seat licensing.

## 2. Coverage
US-centric: national accounts, employment (BLS), prices (CPI/PCE), interest rates and Treasury yields, money/banking aggregates, housing, regional/state/metro series (via FRED's companion GeoFRED), and international benchmark series sourced from the OECD, BIS, World Bank, and other national statistical agencies. ALFRED (Archival FRED) preserves historical "vintages" of each series so users can reconstruct exactly what data was known/published as of any past date — valuable for real-time forecasting and policy research replication. Update frequency ranges from daily (market/rates series) to annual, following each source agency's own release calendar.

## 3. Datasets
Key series families: GDP/GNP and national accounts, CPI/PCE inflation, unemployment/labor force (U-3/U-6, JOLTS), Fed funds rate and full Treasury yield curve, M1/M2 money supply, industrial production, housing starts/Case-Shiller, consumer/producer sentiment indices, corporate bond spreads, and state/MSA-level series via GeoFRED. FRED also republishes select international indicators (exchange rates, foreign GDP/CPI) but this is not its core strength. ALFRED provides point-in-time vintages of the same series for reproducible historical analysis.

## 4. APIs & technical integration
REST API (fred/…) returning XML, JSON, XLSX, or CSV; endpoints cover series metadata, observations, releases, categories, tags, and search (search capped at 1,000 results). Supports `realtime_start`/`realtime_end` parameters for ALFRED vintage queries. Free API key via self-service signup (no approval wait). Widely wrapped by third-party client libraries — `fredapi` and `pyfredapi` (Python), `alfred`/`fredr` (R), and numerous MCP servers/community connectors — plus native integration inside Excel, Trading Economics, TradingView, Bloomberg-adjacent tools and BI platforms.

## 5. Enabling technology
Purpose-built government statistical-data warehouse maintained by the St. Louis Fed's Research Division; not AI/ML-driven — value comes from curation, standardization, and the ALFRED vintage-archiving architecture that timestamps every revision. A data committee of Fed economists, librarians, and information professionals vets each source before inclusion and enforces ongoing quality control. No proprietary modeling; FRED is a distribution and archival layer over official source-agency data.

## 6. Customer / user feedback
Consistently cited as the default free reference source for US macro data among academics, students, journalists, and quant/fintech developers; usage grew from ~620 users at launch (1991) to 5.9 million users worldwide by 2018. Praised for reliability, breadth, free/no-friction access, and the ALFRED vintage feature that supports reproducible research. Commonly used as a benchmark or free substitute/complement to paid terminals (Bloomberg, Haver, Macrobond) for US series specifically; the main limitation raised by users is its US-centric scope, which pushes international-macro use cases toward DBnomics, Trading Economics, or Haver.

## 7. Edge & positioning
- **Leads on:** Free, unrestricted access to deep, long-history, revision-tracked (ALFRED) US macro/financial data; enormous developer ecosystem and near-zero integration cost.
- **Lags on:** International/non-US coverage is thin and secondary; no proprietary forecasts, nowcasts, or analytics layer — it's a data warehouse, not an analytics platform; consumer-grade tooling (basic charting, no advanced BI).
- **Best-for:** Free, citable, revision-aware US macro time series for research, screening, dashboards, and as an input feed to other analytics/report layers (fits the Financial-data-providers "MACRO" free-tier category well).

## 8. Provenance
- https://fred.stlouisfed.org/docs/api/fred/series_observations.html — official series/observations endpoint docs (accessed 2026-08-14)
- https://dev.to/0012303/fred-has-a-free-api-800000-us-economic-time-series-at-your-fingertips-46e9 — free API, 800k+ series overview (accessed 2026-08-14)
- https://apispine.com/fred/pricing — confirms no paid tier, rate limits (accessed 2026-08-14)
- https://www.stlouisfed.org/publications/page-one-economics/2025/jun/data-releases-with-fred — St. Louis Fed on FRED/ALFRED usage (accessed 2026-08-14)
- https://www.stlouisfed.org/news-releases/2019/04/16/st-louis-fed-2018-annual-report-go-figure-with-fred — user growth 1991→2018 stats (accessed 2026-08-14)
- https://github.com/mortada/fredapi — Python client for FRED/ALFRED, vintage data (accessed 2026-08-14)
- https://www.findmymoat.com/vs/fred-federal-reserve-economic-data-vs-trading-economics — FRED vs Trading Economics comparison (accessed 2026-08-14)
- https://fredhelp.stlouisfed.org/fred/data/understanding-the-data/how-does-fred-add-new-data/ — data committee/curation process (accessed 2026-08-14)
