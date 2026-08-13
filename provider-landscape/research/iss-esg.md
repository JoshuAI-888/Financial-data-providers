# ISS ESG

## 1. Snapshot
- **Owner/parent:** ISS ESG is the responsible-investment arm of Institutional Shareholder Services (ISS), now operating under the **ISS STOXX** brand. Majority-owned by **Deutsche Börse Group** (acquired ~80% for ~€1.5bn, closed 2021; consolidated further into ISS STOXX in 2023–24).
- **HQ:** Rockville, Maryland, USA (ISS parent); ISS ESG research rooted in **Munich, Germany** via the former Oekom Research. **Founded:** ISS 1985; the ESG Corporate Rating methodology traces to Oekom (1993, 25+ years). ISS STOXX employs ~4,000 people across ~34 offices in 20 countries.
- **Positioning one-liner:** A full-stack ESG/stewardship house pairing proxy-voting heritage with a deep, impact-and-materiality Corporate Rating, climate data and regulatory (SFDR/EU Taxonomy) reporting.
- **Regions covered:** Global — 7,300+ rated corporate issuers and 25,000–37,500 issuers for climate/emissions data across developed and emerging markets; strong European regulatory orientation.
- **Free tier:** No. Enterprise/subscription licensing only.
- **Pricing:** Not publicly disclosed. Datasets licensed individually (ESG Ratings, Climate, Fund Ratings, Regulatory) or as enterprise-wide access; typically five- to six-figure annual contracts.

## 2. Data-domain coverage
- **ESG ratings:** ISS ESG Corporate Rating (A+ to D–) across E/S/G plus SDG-based impact component; 30+ universal topics plus sector-specific criteria.
- **Climate/carbon:** ISS ESG Climate Solutions — Scope 1/2/3 emissions, carbon intensity, physical & transition risk, scenario alignment / Implied Temperature Rise, TCFD reporting.
- **Controversies/adverse-media:** Norm-Based Research (UN Global Compact / OECD / UNGP breaches) and controversy screening across corporate and 800+ sovereign issuers.
- **Biodiversity/nature:** Emerging biodiversity-impact assessment (e.g. bank biodiversity-controversy analysis); tied to EU Taxonomy biodiversity objective.
- **Regulatory (SFDR/EU taxonomy):** Extensive — PAI indicators, SFDR reporting, EU Taxonomy alignment (reported + modelled data), automated portfolio reporting.
- **Governance:** Deep heritage — Governance QualityScore, proxy research/voting policies, executive-comp and board analytics.

## 3. Datasets
- **Corporate Rating:** 7,300+ distinct corporate issuers; 130+ raw ESG metrics with coverage factors; A+/D– performance scores; forward-looking, value-chain and SDG impact lens.
- **Climate:** emissions/carbon data on 25,000+ companies with history back to ~2012; broader emissions coverage cited up to ~37,500 issuers.
- **Controversies:** Norm-Based Research plus sovereign controversy assessment (~800 sovereign issuers).
- **Fund/regulatory:** SFDR PAI, EU Taxonomy modelled + reported alignment, fund-level ESG data.
- **Methodology:** 25+ years of continuity from Oekom; analyst-verified with issuer engagement (companies can verify newly collected data during the annual rating survey).
- **Proprietary scores:** ESG Corporate Rating, Governance QualityScore, ESG Fund Rating, ITR/climate scores.

## 4. APIs & technical integration
- **API/feed:** ISS ESG Gateway platform plus raw-data feeds; clients license individual datasets or enterprise API integration.
- **Auth/formats:** Enterprise API keys / secured feeds; flat files (CSV), data feeds, and platform access.
- **Delivery:** Direct feed / SFTP, ISS ESG Gateway UI, and distribution through third-party platforms (FactSet, Deutsche Börse market data, Datarade). Snowflake/Databricks native marketplace listing is limited relative to MSCI/S&P; distribution leans on partner platforms and direct feeds.
- **MCP availability:** None known (no official Model Context Protocol server).

## 5. Enabling technology
- **Methodology:** Analyst-led, materiality- and impact-oriented Corporate Rating with sector frameworks; modelled data (e.g. EU Taxonomy) fills reported-data gaps with a deliberately conservative "underestimate if in doubt" approach.
- **AI/ML/NLP:** NLP-assisted controversy/adverse-media monitoring and news screening; modelled estimation for emissions and taxonomy alignment where disclosure is absent.
- **Data sourcing:** Company disclosures, CSR reports, CDP, regulatory filings, NGO/media sources; direct issuer engagement for verification.
- **Data-ops:** Annual rating survey cycle, coverage-factor tagging, analyst QA and event-driven re-assessment on new controversies/corporate actions.

## 6. Customer / user feedback
- **Sentiment (triangulated):** Regarded as a credible, research-heavy incumbent especially strong in governance/stewardship and European regulatory reporting. As with all raters, ESG-score **divergence** is the central critique — academic work (MIT "Aggregate Confusion," Berg/Kölbel/Rigobon) shows low correlation between ISS, MSCI, Sustainalytics et al., driven by differing scope, measurement and weighting.
- **Pros:** breadth (ratings + climate + controversies + governance + regulatory in one house); proxy/stewardship heritage; strong SFDR/EU Taxonomy tooling; long methodological continuity; analyst verification with issuer engagement.
- **Cons:** opacity and cost of enterprise licensing; ratings-divergence and comparability concerns; European data-sovereignty debate around non-EU ownership of ESG data; biodiversity/nature coverage still maturing; less cloud-marketplace-native than peers.
- **User segments:** asset managers, asset owners/pension funds, banks, corporates (for their own rating), and regulatory-reporting teams.

## 7. Edge & positioning
- **Leads:** governance & proxy/stewardship integration; SFDR/EU Taxonomy regulatory reporting; impact/SDG-oriented Corporate Rating; Norm-Based controversy research including sovereigns.
- **Lags:** cloud-marketplace/API-native delivery vs MSCI and S&P; biodiversity/nature data depth; pricing transparency; caught in the general ESG-ratings comparability critique.
- **Best-for:** European-regulated investors needing SFDR/Taxonomy compliance plus integrated stewardship/proxy and impact-lens ESG ratings.

## 8. Provenance
- https://www.iss-stoxx.com/research-advisory/sustainability-ratings/ — ISS STOXX sustainability ratings overview (accessed 2026-08-11)
- https://www.issgovernance.com/esg/ratings/corporate-rating/ — Corporate Rating scale/coverage (accessed 2026-08-11)
- https://insight.factset.com/resources/at-a-glance-iss-esg-corporate-rating — 7,300+ issuers, 130 raw metrics (accessed 2026-08-11)
- https://insight.factset.com/resources/at-a-glance-iss-esg-carbon-and-climate-impact — climate/carbon coverage counts (accessed 2026-08-11)
- https://www.iss-stoxx.com/data-analytics/regulatory-data/ — SFDR/EU Taxonomy regulatory data (accessed 2026-08-11)
- https://www.esgtoday.com/iss-esg-launches-automated-portfolio-reporting-solutions-for-eu-taxonomy-sfdr-compliance/ — SFDR/Taxonomy reporting launch (accessed 2026-08-11)
- https://en.wikipedia.org/wiki/Institutional_Shareholder_Services — ownership, HQ, history (accessed 2026-08-11)
- https://gsh.cib.natixis.com/our-center-of-expertise/articles/iss-acquisition-by-deutsche-borse-in-a-context-of-mounting-esg-data-sourcing-quality-sovereignty-concerns-in-europe — Deutsche Börse acquisition, data-sovereignty (accessed 2026-08-11)
- https://datarade.ai/data-products/country-controversy-assessment-iss-esg — sovereign controversy assessment (accessed 2026-08-11)
- https://carbon-pulse.com/220683/ — biodiversity controversy research example (accessed 2026-08-11)
- https://www.issgovernance.com/esg/ratings/esg-scorecard/ — ESG scorecard/data structure (accessed 2026-08-11)
