# DBnomics

## 1. Snapshot
- **Owner/parent:** Non-profit/public-good project run by CEPREMAP (Centre pour la Recherche Économique et ses Applications), launched with partners France Stratégie and Banque de France; funded via France's Investments for the Future Programme plus ongoing partner/community support.
- **Coverage:** Aggregates from 90+ national and international statistical providers (IMF, ECB, Eurostat, World Bank, OECD, US BLS, US BEA, and more) into millions of standardized economic time series covering essentially all major economies.
- **Free tier:** yes — entirely free, no authentication/API key required for API access; the whole service is open and free (no paid tier exists).
- **Pricing model & ranges:** None; free open-source public good, operating on a reported budget of under €200,000/year funded by partner institutions and community contributions.

## 2. Coverage
Global, cross-country macro coverage by virtue of harvesting rather than originating data: exchange rates, inflation, GDP, unemployment, population, central bank policy rates, trade, and thousands of other indicators sourced from >90 providers including IMF, ECB, Eurostat, World Bank, OECD, BLS, and BEA. Because it mirrors upstream sources' own geographic scope, coverage is as broad as the union of its providers — effectively near-global for headline macro series, deepest for economies tracked by IMF/OECD/Eurostat/ECB.

## 3. Datasets
Millions of time series spanning national accounts, prices/inflation, labour markets, population and living conditions, environment and energy, agriculture, finance, and trade. DBnomics preserves each original provider's own dataset structure, codes, and category tree "as-is" rather than remapping to a house taxonomy — it is intentionally non-opinionated, never modifies numerical values, and retains NA/missing-value flags exactly as published upstream.

## 4. APIs & technical integration
Unified free Web API (REST, JSON) plus a public website for browsing; no authentication required. Official/community client libraries exist for R (`rdbnomics`), Python, Julia (`DBnomics.jl`), and Stata (`dbnomics` Stata package), plus a documented "DBnomics Providers API" for enumerating source providers/datasets. Designed for reproducible, scriptable pulls (daily update pipeline) suitable for research and quant workflows; lower barrier to entry than querying each source's native SDMX/REST API individually.

## 5. Enabling technology
An open-source aggregation/normalization pipeline (not AI/ML-driven) that harvests from providers' native formats (often SDMX) and republishes through one standardized API and data model, while explicitly preserving each source's original codes/values (no black-box transformation). Publicly documented at docs.db.nomics.world; codebase and pipeline are open source, reflecting its "digital public good" positioning.

## 6. Customer / user feedback
Positioned and used by academics, journalists, and quant researchers as a free one-stop alternative to querying dozens of national/international statistical APIs individually, and as a free substitute for parts of what paid aggregators (Trading Economics, CEIC, Haver, Macrobond) charge for. Introduced favorably in economics blogs (Econbrowser, Bond Economics) as a genuinely useful free public good; noted strength is breadth (90+ providers, millions of series) and fidelity (no value-altering), with the tradeoff that lacking a house taxonomy across providers means less "curated"/normalized comparability than paid aggregators offer, and its small budget/team implies less commercial support/SLA than for-profit vendors.

## 7. Edge & positioning
- **Leads on:** Free, broad, multi-provider aggregation (90+ sources, millions of series) in one standardized API with zero authentication friction; strong fidelity to original source data (no silent edits).
- **Lags on:** No proprietary curation/cross-provider normalization (each provider's own codes/structure retained, unlike commercial aggregators), no forecasts/analytics layer, small non-profit team/budget means less commercial SLA/support than Trading Economics/CEIC/Macrobond.
- **Best-for:** Free, reproducible, script-friendly access to a very wide swath of official global macro data in one API — a strong complement to FRED (US-deep) and OECD/IMF/World Bank (authoritative but siloed).

## 8. Provenance
- https://db.nomics.world/ — DBnomics homepage, "world's economic database" (accessed 2026-08-14)
- https://docs.db.nomics.world/ — official documentation, "What is DBnomics?" (accessed 2026-08-14)
- https://db.nomics.world/about — about page, founding partners and mission (accessed 2026-08-14)
- https://econbrowser.com/archives/2018/11/introducing-dbnomics — independent economics-blog introduction (accessed 2026-08-14)
- http://www.bondeconomics.com/2018/12/new-data-resource-dbnomics.html — independent review, "New Data Resource: DB.nomics" (accessed 2026-08-14)
- https://apis.io/apis/dbnomics/dbnomics-providers-api/ — DBnomics Providers API documentation (accessed 2026-08-14)
- https://www.rdocumentation.org/packages/rdbnomics/versions/0.6.1 — R client package, confirms free/no-auth API (accessed 2026-08-14)
