# LSEG / Refinitiv

## 1. Snapshot
- **Owner/parent:** London Stock Exchange Group plc (LSEG). Acquired Refinitiv (ex-Thomson Reuters Financial & Risk) in a ~US$27B deal completed 2021; Refinitiv products rebranded under LSEG. HQ: London, UK. LSEG group formed 2007 (LSE itself dates to 1801).
- **Scale signal:** ~27,700 employees; group revenue ~US$12–13B (TTM); Data & Analytics is roughly two-thirds of group revenue. Strategic cloud/data partnership with Microsoft (Microsoft holds ~4% equity stake).
- **Positioning:** The clear #2 to Bloomberg and its most credible cross-asset challenger — holds ~20% of the financial-data market. Sells on breadth + Reuters news + FX/FI + lower cost + open/cloud delivery.
- **Pricing (approx.):** Workspace commonly cited ~10% below comparable Bloomberg seats; tiered by role/data entitlements. Enterprise feeds (Tick History, DataScope, Real-Time) and World-Check are **negotiated — not publicly disclosed**. Academic/library seats materially cheaper.

## 2. Asset-class coverage
- **Public equity:** Deep global equities, fundamentals, I/B/E/S estimates (the classic consensus dataset), ownership, StarMine analytics. Strength: I/B/E/S + StarMine breadth. Weakness: some workflow depth still trails Bloomberg.
- **Private equity / VC:** Private-company and deals data (PE/VC, M&A via legacy Thomson deal data). Moderate — not a category leader vs. PitchBook/Preqin.
- **Fixed income & credit:** Broad FI reference, pricing, and evaluated data; strong governments/rates/FX-adjacent. Strength: solid; Weakness: Bloomberg still wins decisively on FI depth/evaluated pricing per practitioner consensus.
- **Other (indexes/ratings/ESG/macro/FX/commodities/alt data):** **FTSE Russell** indices (major moat), **WM/Refinitiv FX benchmarks** (the FX fixing standard), **World-Check** (KYC/AML/screening leader), ESG data/scores, deep macro (Datastream), strong FX and commodities. Reuters News integrated throughout. Strength: FX benchmarks + FTSE Russell + World-Check are franchise assets.

## 3. Datasets
- **Datastream:** ~120 years of history, 175 countries, 35M+ instruments/indicators incl. 8.5M active economic series — premier academic/macro time-series set (pricing back to 1960s/70s, indices to 1950s).
- **I/B/E/S** consensus estimates; **StarMine** quant models (SmartEstimate, Predicted Surprise, credit-risk, alpha models).
- **Tick History** — global tick/timestamped data back to 1996 across all asset classes.
- **World-Check** — proprietary structured risk-intelligence/PEP/sanctions screening database (20+ years).
- **FTSE Russell** index data + constituents; **WM/Refinitiv** FX rates; Reuters News archive; ESG dataset covering thousands of companies with long history.

## 4. APIs & technical integration
- **Desktop/analytics:** LSEG Workspace (web + desktop, formerly Eikon), Excel Add-in, **CodeBook** (hosted Python/Jupyter inside Workspace), Datastream Web Service (Python/R/MATLAB/EViews connectors + Datastream Data Loader).
- **Programmatic:** **LSEG Data Library for Python** (v2; evolution of Refinitiv Data Library / RDP Libraries — access, content, delivery layers), **Data Platform (RDP/LSEG Data Platform) REST + streaming APIs**, **Tick History REST API**, **DataScope Select (DSS)** REST & SOAP for bulk reference/pricing/corax/entity, **Real-Time (Elektron/RTDS)** streaming feeds, **World-Check One API** for screening.
- **Auth/delivery:** OAuth/token via the Data Platform; desktop, deployed streaming, or direct-to-cloud with the **same** Python code. Cloud delivery via Microsoft Azure (strategic), plus data on cloud marketplaces; formats REST/JSON, bulk files, streaming. Real-time and EOD both available.
- **Constraints:** Redistribution/entitlement licensing; real-time exchange fees; World-Check access gated by compliance vetting.

## 5. Enabling technology
- **Microsoft partnership** is the strategic backbone — Workspace + data re-platformed on Azure; joint AI product build.
- Permanent Identifiers (PermID) — open entity/symbology system for cross-referencing.
- AI/LLM: LSEG Digest / AI-generated summaries and alerts, GenAI features in Workspace, Microsoft-co-developed generative tools; CodeBook for quant/data-science.
- Data platform designed for desktop → deployed → cloud continuity via unified libraries.

## 6. Customer / user feedback
- **Triangulated ~3.3/5** average across G2, Trustpilot, and Gartner Peer Insights (~67 reviews aggregate in comparison sources). Gartner Peer Insights respondents praise product capability + support; Trustpilot skews lower on service.
- **Recurring PROS:** broad multi-asset data; Reuters News integration; strong FX + macro/Datastream; modern web-based Workspace UI; CodeBook/Python; ~10% cheaper than Bloomberg; excellent for academia/research.
- **Recurring CONS:** customer-service accessibility complaints; some analytics/workflow depth lags Bloomberg; no equivalent to Bloomberg's messaging network; migration churn from Eikon→Workspace; occasional performance/stability gripes.
- **Segments:** buy-side and sell-side research/trading, risk & compliance (World-Check), corporate KYC, and heavy academic/library adoption (Datastream is a research standard).

## 7. Edge & positioning
- **Leads:** FX (WM/Refinitiv fixing benchmark) and Reuters News; index franchise (FTSE Russell); risk/compliance screening (World-Check leadership); macro/academic time series (Datastream); I/B/E/S + StarMine estimates. Open symbology (PermID) and Azure-native cloud delivery are genuine differentiators vs. Bloomberg's closed model.
- **Why:** inherited Thomson Reuters' franchise datasets + Reuters newsroom, plus LSE's index/benchmark assets, re-platformed with Microsoft.
- **Lags:** fixed-income depth and evaluated pricing behind Bloomberg; no messaging network effect; brand/UX churn from the multi-year Eikon→Workspace transition; private-markets coverage behind specialists; support perception weaker than FactSet.

## 8. Provenance
- https://en.wikipedia.org/wiki/London_Stock_Exchange_Group — parent, scale, Refinitiv deal (2026-08-10)
- https://en.wikipedia.org/wiki/Refinitiv — Refinitiv lineage/products (2026-08-10)
- https://developers.lseg.com/en/article-catalog/article/essential-guide-to-the-data-libraries — RDP/RD/LSEG Data Libraries lineage (2026-08-10)
- https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api — Tick History REST API (2026-08-10)
- https://www.lseg.com/en/data-catalogue/risk/worldcheck-data/world-check — World-Check screening dataset (2026-08-10)
- https://www.lseg.com/en/data-analytics/products/datastream-macroeconomic-analysis — Datastream history/breadth (2026-08-10)
- https://www.fidelity.com/trading/research-firms/lseg-starmine — StarMine analytics/methodology (2026-08-10)
- https://ctacquisitions.com/refinitiv-vs-bloomberg-vs-factset-vs-capital-iq/ — competitive positioning, market share (2026-08-10)
- https://www.globaldatabase.com/bloomberg-vs-refinitiv-vs-sp-capital-iq-which-financial-terminal-is-worth-it — ratings triangulation + pros/cons (2026-08-10)
