# ICE Data Services

## 1. Snapshot
- **Owner/parent:** Intercontinental Exchange, Inc. (NYSE: ICE). ICE Data Services is the data & analytics arm; the pricing entity is ICE Data Pricing & Reference Data, LLC (SEC-registered). Built via acquisitions of Interactive Data Corp (IDC, 2015), NYSE (2013) and BofA Merrill Lynch Global Research index business (ICE BofA indices, 2017).
- **HQ:** Atlanta, GA (ICE); data operations across NY, Bedford MA, London, and globally.
- **Founded:** ICE 2000; ICE Data Services launched/branded 2016 consolidating IDC + NYSE + SuperDerivatives data.
- **Scale signal:** Independent daily evaluations for **~2.7 million** fixed-income & international-equity securities; reference data on **~13 million** instruments across 210+ markets; **6,000+** fixed-income indices tracking **~US$100T+** debt. Data & analytics is a large recurring-revenue pillar of ICE's Fixed Income & Data Services segment.
- **Positioning one-liner:** The fixed-income data utility — evaluated pricing, reference data, feeds/connectivity and bond indices (ICE BofA) that price and benchmark the credit markets.
- **Pricing model & known ranges (approx.):** Enterprise recurring subscriptions — evaluated-pricing packages by asset class/security count, reference-data licenses, consolidated feed connectivity, index licensing (bps-on-AUM for ETF licensees). **Not publicly disclosed**; negotiated enterprise contracts.

## 2. Asset-class coverage
- **Public equity:** International-equity evaluated prices; real-time equity data via ICE Consolidated Feed / exchange feeds (NYSE roots). Equity is secondary to fixed income in the data franchise.
- **Private equity / VC:** Minimal — not a private-markets data provider. Some private/illiquid instrument valuation via evaluated-pricing and fair-value services, but no fund/manager database.
- **Fixed income & credit:** **Core strength.** Continuous Evaluated Pricing (CEP) and EOD evaluated pricing across corporates (IG/HY), sovereigns/agencies, EM, munis, MBS/TBAs/pass-throughs, ABS/structured, convertibles, bank loans, money-market, preferreds. Best-execution and ICE Liquidity Indicators. ICE BofA / ICE fixed-income indices.
- **Other (ESG/climate, risk analytics, allocator data, alt data):** ICE Climate risk data (physical/transition, munis climate), ESG reference data, ICE Liquidity Indicators, MOVE Index (bond volatility), commodity indices, ICE ETF Hub, mortgage/loan-level data (via Ellie Mae/ICE Mortgage Technology).

## 3. Datasets
- **Evaluated pricing:** ~2.7M securities priced daily; CEP intraday continuous stream throughout trading hours.
- **Reference data:** ~13M instruments, 210+ markets — terms & conditions, corporate actions, identifiers, classifications.
- **Indices:** 6,000+ standard fixed-income indices (ICE BofA family — e.g. US Corporate, High Yield, Broad Market, Global indices), tracking ~US$100T+ debt; convertible coverage in 16 currencies; real-time/intraday index valuation via CEP; MOVE Index; commodity indices.
- **History depth:** ICE BofA index history extends multi-decade (legacy Merrill Lynch indices, some to the 1970s–80s).
- **Unique holdings:** deep muni + structured-products evaluations; loan/mortgage-level data via ICE Mortgage Technology.

## 4. APIs & technical integration
- **API types:** ICE Developer Portal (developer.ice.com) — REST/Data API for intraday pricing, on-demand analytics, reference data; CEP feed; Analytics API (cash-flow, risk, scenario analytics); bulk file delivery.
- **Feeds:** **ICE Consolidated Feed** (hundreds of sources, low latency), **ICE Global Index Feed (GIF)** for real-time index levels/constituents, real-time exchange feeds. Delivery over **SFTI** (Secure Financial Transaction Infrastructure) low-latency network.
- **Auth/delivery/formats:** API keys; feed handlers/multicast; SFTP bulk files; CSV/JSON/FIX; cloud delivery. Available via CME Group and other distribution partners; LSEG redistributes ICE pricing/reference data.
- **Index licensing & redistribution:** ETF/derivative licensing on ICE indices requires separate agreement; constituent redistribution governed and metered.

## 5. Enabling technology
- **Evaluated-pricing methodology:** hybrid **system + human analyst** approach — continuous ingestion of market inputs (trades, quotes, spreads) blended with evaluator judgment rather than a pure "black-box" model; documented, defensible for audit/NAV use.
- **Continuous Evaluated Pricing (CEP):** intraday continuous valuations enabling real-time index and ETF iNAV calculation.
- **Analytics:** ICE cash-flow/analytics engines, best-execution, liquidity scoring (ICE Liquidity Indicators), climate risk analytics.
- **Cloud/infra:** SFTI network backbone; cloud-based data distribution; API-first developer portal.
- **AI/ML:** increasing use of ML in pricing inputs, anomaly detection, and climate/liquidity analytics.

## 6. Customer / user feedback
- **Ratings (triangulated):** Dedicated review-site coverage (G2/TrustRadius) for ICE Data Services is sparse — enterprise/institutional buyer base, sold via contract. Sentiment triangulated from industry press, regulatory filings, and buy-side commentary.
- **Recurring PROS:**
  - Trusted, audit-defensible evaluated prices widely used for **fund NAV/valuation** and regulatory reporting.
  - Unmatched breadth in muni + structured-products + illiquid bond pricing.
  - ICE BofA indices are default HY/credit benchmarks; strong ETF-linkage.
  - Robust low-latency feed/connectivity (SFTI, Consolidated Feed).
- **Recurring CONS:**
  - **Cost/complexity** of enterprise licensing; opaque negotiated pricing.
  - **Governance risk:** SEC charged ICE Data Pricing & Reference Data **US$8M (2020)** for delivering single-broker-quote-based prices (2015–2020) without adequate controls — a cited concern on evaluation transparency for thinly traded names.
  - Evaluated prices for illiquid instruments inherently model/judgment-dependent (staleness debate).
- **User segments:** asset managers, fund administrators, banks, insurers, ETF issuers, custodians, trading platforms.

## 7. Edge & positioning
- **Leads (and why):**
  - **Fixed-income evaluated pricing** — deepest breadth (~2.7M securities, munis/structured/loans) + hybrid methodology trusted for NAV; entrenched in fund-admin/back-office workflows (high switching cost).
  - **Credit indices (ICE BofA)** — the benchmark franchise for HY/credit, with intraday CEP-valued indices for ETFs.
  - **Feeds/connectivity** — SFTI + Consolidated Feed give an infrastructure moat spanning exchange to bond markets.
- **Lags / what keeps it off top:**
  - **Equity indexes / factor & ESG franchises** — far behind MSCI/S&P/FTSE; not an equity-benchmark leader.
  - **Private markets / manager-allocator data** — essentially absent.
  - **Transparency perception** — post-SEC-settlement scrutiny on evaluated-price sourcing for illiquid securities.

## 8. Provenance
- https://www.ice.com/fixed-income-data-services/data-and-analytics/pricing/cep — CEP coverage/methodology, accessed 2026-08-10.
- https://www.ice.com/market-data/pricing-and-analytics — ~2.7M securities priced daily, accessed 2026-08-10.
- https://www.ice.com/fixed-income-data-services/index-solutions/fixed-income-indices — 6,000+ indices, ~$100T debt, accessed 2026-08-10.
- https://developer.ice.com/fixed-income-data-services/catalog/ice-data-indices — index/API catalog (GIF, constituents), accessed 2026-08-10.
- https://www.sec.gov/newsroom/press-releases/2020-310 — $8M SEC settlement (single-broker quotes), accessed 2026-08-10.
- https://developer.ice.com/fixed-income-data-services/catalog/ice-reference-data — ~13M instruments reference data, accessed 2026-08-10.
- https://www.ice.com/fixed-income-data-services/access-and-delivery/connectivity-and-feeds — SFTI/Consolidated Feed, accessed 2026-08-10.
- https://ir.theice.com/press/news-details/2016/Intercontinental-Exchange-Launches-Expanded-ICE-Data-Services/default.aspx — ICE Data Services launch/history, accessed 2026-08-10.
- https://www.cmegroup.com/solutions/market-tech-and-data-services/technology-vendor-services/ice-data-services.html — distribution/partners, accessed 2026-08-10.
