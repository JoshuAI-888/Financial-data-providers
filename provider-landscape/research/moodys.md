# Moody's

## 1. Snapshot
- **Owner/parent:** Moody's Corporation (NYSE: MCO). **HQ:** New York, NY. Founded 1909 (John Moody's ratings); Analytics unit built out 2000s; Bureau van Dijk acquired 2017 (~$3.3B), RMS 2021.
- **Scale signal:** Corporation revenue ~$7B (2024); two segments — **Moody's Investors Service / Moody's Ratings** and **Moody's Analytics (MA)** ~$3.6B. Orbis covers 630M+ entities.
- **Positioning one-liner:** The credit-risk powerhouse — ratings franchise (a "toll booth" duopolist with S&P) plus the deepest private-company (Orbis/BvD) and quantitative-credit (EDF/RiskCalc) analytics stack.
- **Pricing model:** Enterprise, negotiated, not publicly disclosed. Orbis/CreditView/CreditEdge sold as subscriptions by seats, modules, coverage scope; ratings feeds and API compute priced separately.

## 2. Asset-class coverage
- **Public equity:** Indirect — equity-market inputs feed CreditEdge/EDF (structural credit models on ~40k listed firms), not an equity-research product. Orbis carries listed-company financials.
- **Private equity / VC:** Strong on private-company reference & financials via **Orbis/BvD** (630M+ entities, ownership structures, beneficial ownership); RiskCalc for private-firm PD. Not a deal-sourcing/VC-fund product.
- **Fixed income & credit:** Core strength. Moody's Ratings on issuers/issues across corporates, financials, sovereigns, structured/muni; CreditView research; credit-risk models (EDF, RiskCalc, LGD); structured-finance cash-flow/pricing analytics; CreditLens origination.
- **Other:** Moody's Economics (macro forecasts, scenarios via former Economy.com); ESG (Orbis ESG scores on 300M+ entities); KYC/entity/beneficial-ownership; insurance/cat risk via RMS; commercial real estate (CRE) analytics.

## 3. Datasets
- **Orbis (ex-Bureau van Dijk)** — flagship global company database; 630M+ entities blended from 170+ sources; ownership/corporate-structure trees, financials, ESG scores (300M+), beneficial ownership — the widest private-company graph available.
- **Moody's Ratings history** — decades of issuer/issue ratings, rating actions, rationales; default & recovery data (DRD).
- **CreditEdge / EDF** — Expected Default Frequency, forward-looking PD (0.01%–50%), 1–10yr term structure, produced daily on ~40k public firms; 60k+ entities covered.
- **RiskCalc** — private-firm PD/LGD/EL models built on a large proprietary private-company default dataset.
- **Structured finance** — deal models, cash-flow, collateral; Data Alliance consortia (C&I, CRE, project/asset finance, agriculture) for portfolio benchmarking.

## 4. APIs & technical integration
- **Moody's DataHub** — cloud-based data-delivery platform; billions of data assets; cloud-to-cloud endpoints, **direct import into customer's Snowflake**, SFTP, direct download; model in Python/R/RStudio/Anaconda.
- **Structured Finance API** — RESTful (and local) APIs for cloud-hosted cash-flow, pricing, credit models across asset classes.
- **EDF-X** — API/web platform for early-warning, PD, and portfolio monitoring on public + private names.
- **CreditView / RatingsDelivery** — web + data feeds for ratings and research; ratings data feeds.
- **CreditLens** — cloud SaaS for commercial lending/credit workflow.
- **Auth/format:** enterprise API keys/OAuth; JSON/CSV/relational; EDF daily, ratings event-driven, structured-finance on-demand compute. Redistribution licensed per contract; regulatory separation between ratings and analytics.

## 5. Enabling technology
- **Cloud strategy:** DataHub as data-ops backbone; warehouse-native (Snowflake) delivery; open-source modeling tooling (Python/R).
- **Entity/company master:** Orbis BvD ID as global entity spine + ownership graph — a key symbology asset for KYC/credit.
- **AI/LLM:** Moody's Research Assistant / CoPilot (GenAI over ratings research + Orbis, built with Microsoft Azure OpenAI); AI-powered early-warning features added to CreditEdge/RiskCalc; NLP for financial-statement spreading in CreditLens.

## 6. Customer / user feedback
- **G2:** Moody's CreditView reviewed positively (speed, creditworthiness assessment); relatively few reviews (niche, enterprise). Page egress-blocked; triangulated via search snippets + Risk.net awards.
- **Risk.net:** repeatedly awarded Credit Data Provider / Credit Risk Management Solution of the Year — strong analyst/industry recognition.
- **PROS:** authoritative ratings + research; unmatched private-company/ownership coverage (Orbis); rigorous, well-documented credit models (EDF/RiskCalc); good for KYC, credit surveillance, benchmarking.
- **CONS:** expensive; complex/fragmented product portfolio (many acquired brands); Orbis data freshness/consistency varies by country; steep onboarding; models can be "black-box" to non-quants.
- **Segments:** banks (credit risk, lending), insurers, asset managers, corporates (KYC/compliance), regulators, academics.

## 7. Edge & positioning
- **Leads:** credit risk & ratings — the franchise. Private-company + ownership breadth via Orbis; quantitative PD models (EDF/RiskCalc) are industry benchmarks; structured-finance analytics. Why: 115-yr ratings brand + BvD acquisition + decades of default data.
- **Lags:** not an equity/markets or trading terminal; weaker in real-time market data, equity research, and general buy-side workflow vs Bloomberg/FactSet/S&P CIQ; ESG ratings trail MSCI/Sustainalytics; portfolio fragmentation from many acquisitions.

## 8. Provenance
- https://www.moodys.com/web/en/us/capabilities/company-reference-data/orbis.html — Orbis 630M+ entities (2026-08-10)
- https://en.wikipedia.org/wiki/Moody%27s_Analytics — MA revenue/history (2026-08-10)
- https://www.businesswire.com/news/home/20200824005363/en/ — CreditEdge/RiskCalc AI + EDF detail (2026-08-10)
- https://www.moodys.com/web/en/us/datahub.html — DataHub delivery/Snowflake (2026-08-10)
- https://www.moodys.com/web/en/us/site-assets/sf-api-brochure.pdf — Structured Finance REST API (2026-08-10)
- https://www.moodys.com/sites/products/productattachments/ma_riskcalc_factsheet.pdf — RiskCalc private-firm model (2026-08-10)
- https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/edfx-early-warning-system.pdf — EDF-X methodology (2026-08-10)
- https://www.risk.net/awards/7952216/credit-data-provider-moodys-analytics — industry award/recognition (2026-08-10)
- https://www.g2.com/products/moody-s-creditview/reviews — CreditView reviews (2026-08-10)
