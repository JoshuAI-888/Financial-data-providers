# MSCI

## 1. Snapshot
- **Owner/parent:** MSCI Inc. (NYSE: MSCI), independent public company; spun out of Morgan Stanley (2007–09). Origins in Capital International indices (1969); "Morgan Stanley Capital International."
- **HQ:** New York, NY (7 World Trade Center). **Founded:** 1969 (index lineage). **Employees:** ~6,100 (2024).
- **Scale signal:** ~US$2.86B revenue (FY2024); Index segment ~56% of revenue. ~US$18.3T AUM benchmarked to MSCI indexes; ~US$6.4T in ETF + non-ETF products linked to MSCI indexes (record ETF AUM). ~290,000+ indexes calculated daily.
- **Positioning one-liner:** The global standard-setter in equity indexes, factor/risk models (Barra) and ESG/climate data — the "picks-and-shovels" toll-taker on global asset allocation.
- **Pricing model & known ranges (approx.):**
  - Index licensing: asset-based fees ~**1–3.5 bps on AUM** for ETF/passive licensees (paid in arrears); plus recurring subscriptions for index data/analytics.
  - Barra/analytics (BarraOne, Barra models): enterprise recurring subscriptions, seat/module-based — **not publicly disclosed** (typically five- to six-figure annual).
  - ESG & Climate: subscription per issuer-coverage/data-point packages — **not publicly disclosed**.

## 2. Asset-class coverage
- **Public equity:** Deepest in market. Flagship GICS-based equity indexes (ACWI, World, EM, EAFE, USA, country/sector/factor/thematic families). Barra equity factor models — **70+ equity factor models** spanning **~90,000 securities, 49 industries, 85+ countries**.
- **Private equity / VC:** MSCI Private Capital Solutions via **Burgiss acquisition (closed Oct 2023)** — LP/GP fund performance, benchmarking, cash-flow/J-curve analytics, private-asset climate/transition risk; targets GPs, LPs, secondaries desks.
- **Fixed income & credit:** Multi-asset-class risk via Barra Integrated Model / BarraOne (fixed income factors, term-structure, spread/credit). Fixed-income *indexes* are a relative gap vs. ICE/Bloomberg; MSCI is not a primary evaluated-pricing vendor.
- **Other (ESG/climate, risk analytics, manager/allocator data, alt data):** MSCI ESG Ratings & Research (AAA–CCC), Climate (Implied Temperature Rise, scenario analysis, physical/transition risk — **250,000+ companies** in climate coverage), Sustainability screens/controversies; RiskMetrics (VaR/liquidity/stress); real-estate analytics (RCA/Real Capital Analytics).

## 3. Datasets
- **Equity indexes:** ~290,000+ live indexes; GICS classification (co-owned with S&P). Deep constituent-level history (multi-decade for flagship families).
- **Barra factor models:** long factor-return/exposure history; "next-gen" models add crowding, machine-learning, climate, sustainability factors.
- **ESG & Climate:** 4,000+ ESG data points per issuer; ratings on ~8,500+ companies (17,000+ issuers incl. subsidiaries); climate scenario data across 250,000+ companies; Scope 1/2/3 emissions, ITR.
- **Private Capital (Burgiss):** private-fund universe spanning tens of thousands of funds / trillions in committed capital, look-through to underlying portfolio companies; PE/VC/RE/private-debt/infra.
- **Real assets:** RCA transaction database for CRE.

## 4. APIs & technical integration
- **API types:** MSCI Developer Community (developer.msci.com) — REST APIs for Index Performance/Levels, ESG Data (4,000+ points), Indicative ESG Score, Climate; Barra model files; Excel add-ins; Python access.
- **Cloud/marketplace:** Barra risk models distributed via **Crux Deliver** (REST API, Python client, S/FTP, or push into AWS S3, GCP, Azure, **Snowflake**; formats Avro/CSV/Parquet; SQL/Excel/Tableau via Crux Query). **BarraOne** offers Snowflake-integrated data models.
- **Auth/delivery/formats:** API-key/OAuth; flat files, SFTP, cloud warehouse shares; CSV/JSON/Parquet.
- **Index licensing & redistribution:** tightly governed — separate license required to create ETFs/derivatives/structured products on MSCI indexes; redistribution of constituent data restricted and metered.

## 5. Enabling technology
- **Risk-model engines:** Barra multi-factor equity & multi-asset (Barra Integrated Model / BIM, BarraOne); RiskMetrics for VaR, stress-testing, liquidity.
- **Methodology:** transparent published factor methodologies; GICS classification backbone; "next-generation" Barra integrates ML/crowding/climate factors.
- **Cloud strategy:** cloud-warehouse-native delivery (Snowflake, AWS/GCP/Azure) via Crux; API-first developer portal.
- **AI/ML:** ML-based factors, NLP for ESG controversies/news, GenAI research assistants; climate scenario modeling (NGFS-aligned).

## 6. Customer / user feedback
- **Ratings (triangulated):** Product-specific third-party review volume is thin (MSCI sells enterprise). Employer/brand proxies: **Glassdoor ~4.0/5** (2,000+ employee reviews, 82% recommend). Sell-side/analyst commentary consistently frames MSCI as premium-priced category leader.
- **Recurring PROS:**
  - Industry-standard benchmarks — being MSCI-benchmarked is table stakes for global/EM equity mandates.
  - Barra is the incumbent factor-risk lingua franca among quants and risk teams.
  - Breadth: index + factor + ESG + private + real assets under one roof.
- **Recurring CONS:**
  - **Expensive** — widely cited as costly, "the brand most used," pricing power resented by ETF issuers/asset managers.
  - **ESG-ratings credibility:** heavily criticized (IEEFA, Bloomberg Businessweek 2021, academics) — ratings measure financial materiality *to* the company, not impact *on* world; methodology-change-driven upgrades; low cross-vendor correlation.
  - Some products seen as **dated**; heavy vendor lock-in; z-scores/models opaque to non-specialists.
- **User segments:** asset managers, ETF issuers, pension funds/asset owners, hedge funds, banks, wealth managers, GPs/LPs.

## 7. Edge & positioning
- **Leads (and why):**
  - **Global/EM equity indexes** — network-effect moat: MSCI ACWI/EM/EAFE are default institutional benchmarks; switching cost is systemic (mandates, ETFs, derivatives all reference them). ~US$18.3T benchmarked.
  - **Factor/equity risk (Barra)** — decades-long incumbency; de facto standard in quant risk.
  - **ESG/climate breadth** — largest coverage footprint despite credibility debate; regulatory-driven demand tailwind.
  - **Private capital** — Burgiss vaulted MSCI into a top private-markets benchmarking position.
- **Lags / what keeps it off top:**
  - **Fixed-income indexes & evaluated pricing** — not a leader; ICE and Bloomberg own bond indices/pricing.
  - **ESG methodology trust** — reputational drag; regulatory scrutiny of ESG raters.
  - **Price/lock-in backlash** — opens door to lower-cost index challengers (FTSE Russell, Solactive, S&P) on cost-sensitive passive mandates.

## 8. Provenance
- https://www.msci.com/our-solutions/factor-investing/factor-models — Barra factor model counts, accessed 2026-08-10.
- https://www.msci.com/data-and-analytics/portfolio-management/barra-one — BarraOne Snowflake delivery, accessed 2026-08-10.
- https://quartr.com/insights/edge/msci-indexing-the-world — MSCI scale/AUM/positioning, accessed 2026-08-10.
- https://en.wikipedia.org/wiki/MSCI — HQ/founding/history, accessed 2026-08-10.
- https://ir.msci.com/news-releases/news-release-details/msci-reports-financial-results-fourth-quarter-and-full-year-2024 — FY2024 segment revenue/AUM, accessed 2026-08-10.
- https://www.institutionalassetmanager.co.uk/2020/07/29/288029/msci-expands-access-risk-models-cloud-crux — Crux cloud delivery, accessed 2026-08-10.
- https://developer.msci.com/apis/msci-indicative-esg-score-api-v1-0 — ESG/index REST APIs, accessed 2026-08-10.
- https://ieefa.org/resources/unregulated-esg-rating-system-reveals-its-flaws — ESG ratings criticism, accessed 2026-08-10.
- https://pomegra.io/learn/library/track-c-strategies/passive-investing/chapter-07-the-major-index-providers/index-licensing-fees — index licensing bps ranges, accessed 2026-08-10.
- https://www.glassdoor.com/Reviews/MSCI-Reviews-E14616.htm — employee/brand ratings, accessed 2026-08-10.
- Burgiss acquisition (Oct 2023) & Private Capital — MSCI blog/annual report, accessed 2026-08-10.
