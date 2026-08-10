# Bloomberg

## 1. Snapshot
- **Owner/parent:** Bloomberg L.P. — privately held; Michael Bloomberg owns ~88% (Merrill Lynch legacy stake bought back). HQ: Midtown Manhattan, New York City. Founded 1981 (Michael Bloomberg + Thomas Secunda, Duncan MacMillan, Charles Zegar).
- **Scale signal:** ~26,000 employees; ~US$15B revenue (2024); ~325,000+ Terminal subscribers. The de facto incumbent / category-defining "market-data terminal."
- **Positioning:** Premium, closed, all-in-one cross-asset terminal + news + messaging + trading + enterprise data. The benchmark everyone else is measured against.
- **Pricing (approx., publicly reported):**
  - Terminal single seat ~US$31,980/yr (~$2,665/mo); ~$28,320/seat for multiple seats; volume tiers down to ~$22,660/seat at 50+. ~6.5% list increase effective Jan 2025. Typically 2-year non-cancelable contracts.
  - Enterprise products (B-PIPE, Data License / Enterprise Access Point, DL+, Bloomberg Anywhere) are **negotiated enterprise contracts — not publicly disclosed**; B-PIPE feeds commonly cited in the ~$50k–$200k+/yr range depending on volume.

## 2. Asset-class coverage
- **Public equity:** Deep global equities, fundamentals, estimates (BEST), corporate actions, ownership, intraday + historical. Strength: breadth + consistency. Weakness: expensive per-seat model, data hard to extract at scale outside enterprise licensing.
- **Private equity / VC:** Present but not a core strength — private company data thinner than dedicated players (PitchBook/Preqin/Capital IQ). Weakness: private markets are a gap vs. specialists.
- **Fixed income & credit:** Category leader. Deep bond reference/pricing, evaluated pricing via **BVAL** (evaluated prices for ~2.5–3M+ securities incl. thinly traded), muni/credit/govvies, Bloomberg Fixed Income Indices (ex-Barclays/AGG). Strength: the decisive FI moat. Weakness: none material.
- **Other (indexes/ratings/ESG/macro/FX/commodities/alt data):** Bloomberg Indices (fixed income + equity), ESG data + scores, strong FX (FXGO) and commodities/energy (BNEF), macro/ECO. Growing alternative-data marketplace. Strength: cross-asset breadth under one roof.

## 3. Datasets
- Proprietary security/entity master + symbology (BBGID / FIGI — open-sourced identifier), corporate actions, fundamentals + BEST estimates.
- **BVAL** evaluated pricing (100M+ data points/day) — differentiated for illiquid FI.
- Bloomberg Fixed Income & Equity Indices, ESG scores, supply-chain, ownership/holdings.
- Bloomberg News + First Word; Bloomberg Intelligence (research), Bloomberg Government/Law, BNEF (New Energy Finance).
- Deep intraday tick and historical archives; alternative-data catalog (Enterprise Access Point).

## 4. APIs & technical integration
- **Terminal-side:** `BLPAPI` (Desktop/Server API), Excel Add-in (BDP/BDH/BDS formulas), **BQL** (Bloomberg Query Language — server-side computed data), **BQNT** (BQuant, hosted Python/Jupyter research environment), **EMSX** (execution management API), **PORT** (portfolio & risk analytics).
- **Enterprise/off-terminal:** **Data License** (bulk reference/pricing/history), **Enterprise Access Point** (self-serve data marketplace), **DL+** (cloud data-management), **B-PIPE** (real-time consolidated managed feed / low-latency streaming), SAPI.
- **Auth/delivery:** Terminal APIs tied to authenticated Terminal login (B-Unit / biometric). Enterprise: S3 object stores + native S3 APIs; cloud-native via **AWS** and **Snowflake** (Data License on cloud, Snowflake Native App, PORT-to-Snowflake via DL+). Formats bulk/flat + programmatic.
- **Constraints:** Strong redistribution/licensing controls; Terminal data is per-user and largely not permitted to leave the Terminal without enterprise Data License. "Data leaving the terminal" is the central commercial control point. Contracts non-cancelable.

## 5. Enabling technology
- Closed, vertically integrated stack: private network, dedicated hardware/keyboard historically, B-Unit authentication.
- Cloud strategy maturing: Data License on AWS, Snowflake Native App + DL+ data management, PORT analytics delivered to Snowflake.
- Entity/security master + **FIGI** open symbology (widely adopted cross-industry standard).
- AI/LLM: **BloombergGPT** (domain LLM, research), AI-powered document/earnings summarization and search features rolling into Terminal; BQuant for quant/data-science workflows.

## 6. Customer / user feedback
- **G2:** Bloomberg Terminal ~4.4/5 (financial-data/terminal category leader by review volume).
- **TrustRadius:** strong ratings; positioned as the reference incumbent ("325,000 desks").
- **Analyst/practitioner commentary** (Wall Street Oasis, WallStreetPrep, comparison sites): consistently rated #1 for fixed income, news, and the Bloomberg messaging network (IB/MSG) as a social-network moat.
- **Recurring PROS:** unmatched breadth + data reliability; best-in-class fixed income; Bloomberg chat/IB network effect; real-time news; responsive support; deep functions (PORT, ECO, FXGO).
- **Recurring CONS:** very expensive; steep learning curve / dated command-line UX; per-seat lock-in and rigid non-cancelable contracts; hard/costly to extract data at enterprise scale; weaker private-markets coverage.
- **Segments:** dominant on sell-side (trading, IB, research) and buy-side (PM/trading/risk); also corporate treasury, gov/policy, academia (labs).

## 7. Edge & positioning
- **Leads:** Fixed income & credit (BVAL, indices, reference) — deepest in market; real-time cross-asset breadth; Bloomberg News + the Bloomberg messaging/IB network (a genuine social moat competitors can't replicate); trading (EMSX/AIM) integrated with data.
- **Why:** decades of proprietary pricing/evaluated data, closed integrated ecosystem, and the network effect of every counterparty being reachable on-terminal.
- **Lags:** price sensitivity opens the door to LSEG/FactSet/Capital IQ and low-cost challengers (Koyfin, YCharts); private-markets/VC coverage trails PitchBook/Preqin; open/programmatic data access and cloud-native delivery historically less flexible than API-first challengers; enterprise data extraction is expensive and license-heavy.

## 8. Provenance
- https://en.wikipedia.org/wiki/Bloomberg_L.P. — company scale/ownership/founding (2026-08-10)
- https://costbench.com/software/financial-data-terminals/bloomberg-terminal/ — Terminal seat pricing (2026-08-10)
- https://www.neugroup.com/bloomberg-terminals-how-much-more-youll-pay-next-year/ — 2025 price increase, volume tiers (2026-08-10)
- https://www.prnewswire.com/news-releases/bloomberg-announces-port-enterprise-data-delivery-to-snowflake-with-data-license-plus-dl-302321571.html — DL+/PORT/Snowflake delivery (2026-08-10)
- https://www.bloomberg.com/company/press/bloomberg-makes-data-license-content-available-on-the-cloud — Data License on AWS / EAP (2026-08-10)
- https://www.bloomberg.com/professional/insights/press-announcement/bloombergs-evaluated-pricing-service-bval-wins-best-pricing-and-valuations-data-provider/ — BVAL evaluated pricing (2026-08-10)
- https://www.g2.com/products/bloomberg-terminal/reviews — G2 rating + pros/cons (2026-08-10)
- https://www.trustradius.com/products/bloomberg-terminal/reviews — TrustRadius sentiment (2026-08-10)
- https://www.wallstreetprep.com/knowledge/bloomberg-vs-capital-iq-vs-factset-vs-thomson-reuters-eikon/ — competitive positioning (2026-08-10)
