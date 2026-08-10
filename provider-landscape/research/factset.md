# FactSet

## 1. Snapshot
- **Owner/parent:** FactSet Research Systems Inc. — publicly traded (NYSE: FDS). HQ: Norwalk, Connecticut, USA. Founded 1978.
- **Scale signal:** ~12,700 employees; ~US$2.3B revenue (FY2025). Positioned as the analyst-and-workflow-centric #3 cross-asset platform, strong on buy-side portfolio analytics and connectivity/openness.
- **Positioning:** "Open data + integrated workflow" challenger — sells on best-in-class support, portfolio analytics, flexible APIs/symbology concordance, and materially lower cost than Bloomberg.
- **Pricing (approx.):** Workstation commonly cited ~US$12k–$15k+/seat/yr (vs. Bloomberg ~$28–32k) — publicly, "not officially disclosed"; enterprise data feeds and API volumes negotiated. Modular/role-based pricing.

## 2. Asset-class coverage
- **Public equity:** Core strength — deep fundamentals, estimates, ownership, corporate actions, filings; strong equity-research and screening workflow. Weakness: none material for equities.
- **Private equity / VC:** Increasingly strong — **Cobalt** (acquired 2022) portfolio monitoring for private capital + AI Doc Ingest; private-markets data via partnerships/acquisitions. A deliberate growth area, now a differentiator vs. peers.
- **Fixed income & credit:** Solid FI reference, analytics, and fixed-income portfolio analytics; evaluated/pricing via partners. Weakness: FI depth trails Bloomberg.
- **Other (indexes/ratings/ESG/macro/FX/commodities/alt data):** **Truvalue Labs** ESG (AI-driven daily ESG signals, acquired 2020); benchmark/index datafeeds; macro; alternative data via Open:FactSet Marketplace. Strength: ESG signals + open data marketplace.

## 3. Datasets
- Proprietary **FactSet fundamentals, estimates, ownership, symbology/concordance** — mapping FactSet IDs to CUSIP, SEDOL, ISIN, FIGI (the Concordance Service is a differentiated cross-referencing asset).
- **Truvalue ESG** — AI-derived, time-series ESG/behavioral signals from unstructured sources.
- **Cobalt** — private-capital fund/portfolio-company performance, KPIs, portfolio monitoring.
- **Open:FactSet Marketplace** — curated third-party + proprietary + alternative datasets.
- Benchmark DataFeed, deep filings/documents, supply-chain (RBICS proprietary revenue-based industry classification), geographic revenue exposure.

## 4. APIs & technical integration
- **Desktop:** FactSet Workstation, Excel Add-in / FactSet functions, PowerPoint/Office integration.
- **Programmatic:** Broad catalog of **RESTful APIs** (developer.factset.com) — Fundamentals, Estimates, Prices, Ownership, Global Filings, Trading API; **Programmatic Environment API** (batch + interactive file/job management), **OnDemand** document/data services, **Open:FactSet Marketplace API**; official **Python SDKs** (`fds.sdk.*` on PyPI); Standard DataFeeds (SDF) for bulk.
- **Auth/delivery:** OAuth 2.0 / API keys; delivery via REST/JSON, bulk Standard DataFeeds, and cloud-native **Snowflake** (direct share + Snowflake Marketplace: Fundamentals, Benchmark, Concordance, Open Access) and **Databricks Marketplace**. Real-time and EOD.
- **Constraints:** Entitlement/redistribution licensing; some users report integrating *outside* data into FactSet jobs is difficult; enterprise data licensed by dataset/volume.

## 5. Enabling technology
- API-first, open-architecture positioning — designed to plug into client stacks rather than lock data in a terminal.
- **Concordance Service** (symbology mapping) is core enabling tech for entity/security mastering across vendors.
- Cloud-native delivery via Snowflake + Databricks marketplaces; standard datafeeds instantly delivered via Snowflake.
- AI/LLM: **FactSet Mercury** (GenAI conversational assistant / copilot), AI Doc Ingest for Cobalt (automated private-capital data extraction), LLM-powered search and document workflows.
- RBICS proprietary industry taxonomy underpins classification/analytics.

## 6. Customer / user feedback
- **G2:** FactSet Workstation ~4.3/5 (vs. Bloomberg ~4.4). **TrustRadius:** strong verified reviews; reviewers rate FactSet **higher than Bloomberg on quality of ongoing product/customer support**.
- **Recurring PROS:** excellent, responsive support (repeatedly cited edge over Bloomberg); clean, easy-to-navigate UI; superb equity-research + portfolio analytics; flexible APIs + Excel; lower cost than Bloomberg; strong client-service/onboarding.
- **Recurring CONS:** still expensive / "not appropriate for smaller managers"; integrating external/third-party data into FactSet jobs can be difficult; lacks some Bloomberg strengths (messaging network, certain search/contact-info functions, FI depth); real-time depth trails Bloomberg.
- **Segments:** strong on **buy-side** (asset managers, PMs, portfolio analytics, wealth), sell-side research/IB (pitchbooks, comps), increasingly private-capital GPs/LPs (Cobalt), and corporate.

## 7. Edge & positioning
- **Leads:** buy-side **portfolio analytics** and equity research workflow; **client support** (its standout, consistently review-validated moat); **open/flexible APIs + symbology concordance** (easiest to embed into client systems); private-markets monitoring (Cobalt) and ESG signals (Truvalue) as growth differentiators; cost advantage vs. Bloomberg.
- **Why:** analyst-workflow DNA, an open-architecture philosophy, and a support culture that wins on total experience rather than raw data monopoly.
- **Lags:** fixed-income depth and real-time/trading breadth behind Bloomberg; no messaging-network effect; smaller scale/brand gravity than Bloomberg and LSEG; some proprietary datasets rely on partners; still priced out of the small-manager segment.

## 8. Provenance
- https://en.wikipedia.org/wiki/FactSet — HQ, founding, employees, revenue (2026-08-10)
- https://developer.factset.com/api-catalog/factset-programmatic-environment-api — Programmatic Environment API (2026-08-10)
- https://go.factset.com/hubfs/Resources%20Section/Brochures/factset-apis-brochure.pdf — REST API catalog overview (2026-08-10)
- https://app.snowflake.com/marketplace/providers/GZT0Z28ANYN/FactSet — Snowflake Marketplace datasets (2026-08-10)
- https://marketplace.databricks.com/provider/48d55bd7-064c-4665-844d-dff8a6def12c/FactSet — Databricks Marketplace presence (2026-08-10)
- https://www.factset.com/marketplace/catalog/product/portfolio-monitoring-platform — Cobalt private-markets monitoring (2026-08-10)
- https://finance.yahoo.com/news/factset-launches-ai-doc-ingest-130000815.html — Cobalt AI Doc Ingest (2026-08-10)
- https://financefeeds.com/factset-acquires-portfolio-monitoring-solutions-private-markets/ — Cobalt acquisition (2026-08-10)
- https://www.trustradius.com/compare-products/bloomberg-terminal-vs-factset — ratings + support edge (2026-08-10)
- https://www.g2.com/compare/bloomberg-terminal-vs-factset-workstation — G2 comparative ratings (2026-08-10)
