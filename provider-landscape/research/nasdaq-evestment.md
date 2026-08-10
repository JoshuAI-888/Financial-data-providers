# Nasdaq / eVestment

## 1. Snapshot
- **Owner/parent:** Nasdaq, Inc. (NASDAQ: NDAQ). eVestment acquired by Nasdaq for **US$705M (closed Oct 23, 2017)**; now branded **Nasdaq eVestment**, part of Nasdaq's Financial Technology / investment-intelligence portfolio. Nasdaq Data Link is the former **Quandl** platform (acquired 2018).
- **HQ:** eVestment — Atlanta, GA (founded 2000 by Jim Minnick, Karen Minnick, Matt Crisp); offices London, Sydney, Dubai, Canada. Nasdaq HQ — New York, NY.
- **Founded:** eVestment 2000 (25 years in 2025); Quandl 2011.
- **Scale signal:** **30,000–31,000+** institutional strategies (traditional + alternative); **28,000+** corporate/public asset owners covered; **700+** granular peer universes; the only suite of **OCIO indices**; supports ~6,000 institutional firms worldwide.
- **Positioning one-liner:** The institutional manager-and-allocator intelligence network — the standard database where asset managers report performance and consultants/asset owners screen and select managers.
- **Pricing model & known ranges (approx.):** Enterprise SaaS subscriptions by module (Analytics, Omni for DDQ/RFP, Market Intelligence, TopQ private-markets, Asset Flows) and seats. **Not publicly disclosed** (five-/six-figure annual typical). Nasdaq Data Link/Quandl: mix of free and premium per-dataset subscriptions; daily refresh (~8:00 AM ET).

## 2. Asset-class coverage
- **Public equity:** Deep — long-only equity strategy/composite performance, holdings, attribution, characteristics across global manager universes.
- **Private equity / VC:** Alternatives coverage via eVestment private-markets & **TopQ** (PE/VC/private-debt/RE fund performance, cash-flow analytics, PME); alternative funds included in the 30,000+ strategy count. Narrower than dedicated private-markets vendors (Preqin/PitchBook/Burgiss).
- **Fixed income & credit:** Fixed-income manager strategies, composites and peer universes; not a pricing/index vendor — coverage is manager-reported product data, not security-level.
- **Other (ESG/climate, allocator data, alt data):** Asset-owner/allocator intelligence (28,000+ investors, mandate/search activity, asset flows), consultant data, DDQ/RFP workflow (**Nasdaq eVestment Omni**), ESG strategy attributes; **Nasdaq Data Link (Quandl)** — alternative & financial datasets (core financials, alt data, sentiment) via marketplace.

## 3. Datasets
- **Manager universe:** 30,000–31,000+ institutional strategies, manager-reported (performance, holdings, fees, AUM/flows, vehicle terms); 700+ pre-built peer universes; multi-decade composite history for many managers.
- **Asset-owner/allocator data:** 28,000+ corporate & public investors; search/mandate activity, manager hiring/firing, asset flows, OCIO indices.
- **Private markets (TopQ):** fund-level PE/VC/RE/debt performance, PME, cash-flow modeling.
- **Nasdaq Data Link / Quandl:** large marketplace of premium & free datasets — equity fundamentals, alternative data, economic/commodity series; API-delivered, daily refresh.
- **Unique holdings:** manager self-reported composite dataset is the network-effect asset — managers must populate eVestment to be discoverable by consultants/asset owners.

## 4. APIs & technical integration
- **API types:** Nasdaq eVestment offers a suite of APIs (incl. "Next Best Action" participant factor model) for programmatic access to database analytics; primary UX is the web Analytics platform (screening, charting, peer analysis). **Nasdaq Data Link** — REST API with **Python, R, Excel** client libraries and bulk download; daily table refresh delivered ~8:00 AM ET.
- **Auth/delivery/formats:** API key auth (Data Link); CSV/JSON; web exports; SaaS dashboards. eVestment Omni = digital DDQ/RFP exchange between managers and allocators.
- **Latency:** not real-time — manager data updates monthly/quarterly on reporting cycles; Data Link refreshes daily.
- **Redistribution:** database access is licensed/seat-based; redistribution of manager-reported data restricted by subscription terms.

## 5. Enabling technology
- **Analytics engine:** peer-universe construction, screening, attribution, market-sizing and competitive-intelligence tooling across the manager database.
- **Workflow tech:** Nasdaq eVestment Omni digitizes DDQ/RFP workflows (centralized, structured responses between managers and asset owners).
- **Cloud strategy:** cloud-based SaaS; Nasdaq Data Link is a cloud data-marketplace/delivery platform (ex-Quandl).
- **AI/ML:** marketed as "AI-ready insights"; "Next Best Action" participant factor model; Nasdaq-wide GenAI/analytics investment; sentiment/alt-data via Data Link.
- **Data-ops:** manager-self-reporting pipeline with data-quality validation; Nasdaq index/analytics infrastructure.

## 6. Customer / user feedback
- **Ratings (triangulated):** **G2 ~4.3/5** (~20+ reviews) for Nasdaq eVestment; corroborated by Nasdaq product-sheet testimonials and industry commentary. TrustRadius/Gartner Peer Insights coverage is thin (enterprise, contract-sold).
- **Recurring PROS:**
  - **Most comprehensive** institutional manager database — "opportunities that can't be found elsewhere"; de facto standard for peer analysis and competitive intelligence.
  - Strong for **market sizing, sales/flow trends, positioning** vs. competing strategies.
  - Omni streamlines DDQ/RFP — reduces friction between managers and asset owners.
  - User-friendly interface, ease of data retrieval.
- **Recurring CONS:**
  - **Data timeliness** — reliance on manager self-reporting causes lag (e.g., stale asset-flow data cited mid-2025); coverage only as current/complete as managers submit.
  - **Weak Asia coverage** — limited Asia-based asset-owner and RFP data; module cost hard to justify for Asia-focused firms.
  - Expensive; module-based pricing adds up; alternatives coverage narrower than specialist private-markets vendors.
- **User segments:** asset managers (sales/marketing/product/competitive intel), investment consultants, asset owners (pensions, endowments, OCIOs), fund-of-funds.

## 7. Edge & positioning
- **Leads (and why):**
  - **Institutional manager/allocator intelligence** — network-effect moat: managers self-report to be seen by consultants/asset owners who screen there; the two-sided network is very hard to replicate. Category standard for peer universes and competitive intelligence.
  - **Manager sales & marketing intelligence** — unmatched for flows/mandate/search activity.
  - **DDQ/RFP workflow (Omni)** entrenches the platform in day-to-day manager-allocator interaction.
- **Lags / what keeps it off top:**
  - **Not a market-data/pricing/index provider** — no security-level pricing, no evaluated pricing, no benchmark franchise (unlike MSCI/ICE within this cluster).
  - **Private markets** coverage trails Preqin/PitchBook/MSCI-Burgiss.
  - **Geographic gaps (Asia)** and **self-reporting latency** limit timeliness and completeness.
  - Nasdaq Data Link/Quandl is a secondary, marketplace-style asset — not a differentiated proprietary dataset at eVestment's level.

## 8. Provenance
- https://www.nasdaq.com/solutions/evestment — positioning, AI-ready framing, accessed 2026-08-10.
- https://www.nasdaq.com/solutions/evestment/global-database/datasets — 30,000+ strategies, 28,000+ investors, 700+ universes, OCIO indices, accessed 2026-08-10.
- https://www.g2.com/products/nasdaq-evestment/reviews — G2 ~4.3/5 rating, pros/cons, accessed 2026-08-10.
- https://venturebeat.com/business/nasdaq-to-acquire-investment-analytics-company-evestment-for-705-million/ — $705M acquisition, accessed 2026-08-10.
- https://www.nasdaq.com/newsroom/nasdaq-evestment-celebrates-25-years-shaping-institutional-landscape — founding 2000 / 25 years, accessed 2026-08-10.
- https://data.nasdaq.com/publishers — Nasdaq Data Link / Quandl marketplace, accessed 2026-08-10.
- https://data.nasdaq.com/databases/EVNBA — Data Link daily refresh (~8:00 AM ET), accessed 2026-08-10.
- https://www.nasdaq.com/solutions/evestment/data-coverage — coverage scope incl. Asia gap context, accessed 2026-08-10.
- https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-acquire-evestment — acquisition close Oct 2017, accessed 2026-08-10.
