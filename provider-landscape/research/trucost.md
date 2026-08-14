# Trucost

## 1. Snapshot
- **Owner/parent:** S&P Global — acquired by S&P Dow Jones Indices (a controlling stake, effective October 1, 2016); Trucost was originally founded in London in 2000 and now operates as part of S&P Global Sustainable1, S&P Global's dedicated sustainability business line.
- **Coverage:** Environmental data for 20,000+ companies, with the "Core Plus" universe (~11,500 large/mid/small/micro-cap companies via the S&P Broad Market Index, plus S&P 500, S&P Global 1200, S&P China A SmallCap 300, and ~1,500 additional large listed companies); historical records back to 2005 for large caps, from 2016 for small/mid-caps.
- **Free tier:** no — institutional data-licensing product distributed via S&P Global Marketplace/Workbench, WRDS (academic), and S&P ESG platforms; no free public tier.
- **Pricing model & ranges:** Enterprise data-license/subscription via S&P Global Marketplace; no public price list (quote-based); academic access available at discounted/institutional rates through WRDS (Wharton Research Data Services).
- **Owner note:** S&P Global's broader "Global ESG Scores and Trucost" product bundle is also distributed through WRDS for academic research use.

## 2. Coverage
Environmental-impact data on 20,000+ public companies globally, with deepest, most reliable coverage on the ~11,500-company Core Plus universe (S&P Broad Market Index plus major large/mid-cap indices) and roughly 1,500 additional large listed names. Historical depth reaches back to 2005 for large-cap companies and 2016 for small/mid-caps — among the longer environmental-data histories in the market, useful for trend/TCFD-style scenario analysis. Coverage is global but skews toward larger, more liquid, index-constituent companies where reported or modeled environmental data is most complete.

## 3. Datasets
**Trucost Environmental** dataset: greenhouse gas emissions (Scope 1/2/3 breakout), pollutants to air/land/water, waste generation, natural resource and water use, revenue by sector, and fossil-fuel reserves/power-generation capacity. **Carbon Earnings at Risk (CEaR)**: stress-tests a company's ability to absorb future carbon prices, quantifying "unpriced carbon cost" and earnings sensitivity under different carbon-price scenarios/time horizons (TCFD-aligned), using a Carbon Price Risk Premium multiplied against company Scope 1/2 emissions. **EU Taxonomy revenue-alignment dataset**: assesses revenue exposure to EU Taxonomy-eligible/aligned activities. Underlying all of these is Trucost's proprietary **Environmentally-Extended Input-Output (EEIO) model**, which combines industry-specific environmental-impact data with macroeconomic input-output tables (based on a customized NAICS classification) to estimate environmental impacts across a company's own operations and its full global supply chain from revenue-by-sector data — this is how Trucost fills gaps for companies that don't directly disclose granular environmental metrics.

## 4. APIs & technical integration
Distributed primarily through the **S&P Global Marketplace** (including the "Marketplace Workbench" delivery/analytics interface) as licensed datasets/feeds, and via **WRDS** for academic/research institutional access. Documented methodology guides (Trucost Environmental Data Methodology Guide, CEaR Methodology, Environmental Register Methodology FAQs) are published as detailed PDFs, reflecting an enterprise data-license delivery model (bulk files/feeds/workbench) rather than a lightweight public REST API aimed at individual developers.

## 5. Enabling technology
Proprietary Environmentally-Extended Input-Output (EEIO) economic model — not primarily AI/ML-based — that statistically estimates environmental impacts (including full supply-chain/Scope 3-type exposure) even where a company does not directly disclose them, by combining sector-level environmental-intensity data with input-output economic flow tables. This modeled/estimated approach (rather than disclosure-only) is Trucost's core methodological differentiator, similar in spirit to Clarity AI's AI-based gap-filling but built on economic input-output modeling rather than machine learning.

## 6. Customer / user feedback
Long-established, closely tied to institutional/index use cases (e.g., S&P Trucost-based indices, TCFD-aligned climate risk reporting used by asset owners such as Japan's GPIF for portfolio climate-risk assessment). Positioned within the broader ESG-ratings landscape where independent commentary notes that different providers (MSCI, Sustainalytics, ISS ESG, Trucost/S&P) "measure different things, on different scales, in different directions" and correlate only moderately (~0.54 average) with each other — a general industry caveat rather than a Trucost-specific criticism. No detailed user-review platform feedback (G2/Gartner) was found specific to Trucost as a standalone brand, likely reflecting its status as an embedded S&P Global Sustainable1 dataset rather than a self-service SaaS product with its own review presence.

## 7. Edge & positioning
- **Leads on:** Longest environmental-data history among major vendors (back to 2005 for large caps); proprietary EEIO supply-chain modeling that estimates full-chain environmental impact even without direct disclosure; deep integration with S&P Global's index business (Trucost-linked indices) and TCFD/carbon-pricing scenario tools (CEaR).
- **Lags on:** No free/self-serve tier or lightweight developer API; company-level breadth (20,000) is smaller than RepRisk's controversy database or Clarity AI's fund/company universe; distribution is enterprise-license/Marketplace-centric, adding integration friction versus REST-API-first competitors.
- **Best-for:** Institutional investors and index providers needing TCFD-aligned carbon/environmental risk analytics (esp. Scope 1-3 modeling and carbon-price scenario stress-testing) embedded in S&P Global's broader index and data ecosystem.

## 8. Provenance
- https://press.spglobal.com/2016-10-03-S-P-Dow-Jones-Indices-Acquires-Trucost — official 2016 acquisition press release (accessed 2026-08-14)
- https://www.support.marketplace.spglobal.com/content/dam/spglobal/mi/en/documents/marketplace/datasets/alternative/trucost_environmental/trucost_environmental_data_methodology_guide.pdf — official Trucost Environmental Data Methodology Guide (accessed 2026-08-14)
- https://portal.s1.spglobal.com/survey/documents/SPG_S1_Carbon_Earnings_at_Risk_Methodology.pdf — official Carbon Earnings at Risk methodology (accessed 2026-08-14)
- https://marketplace.spglobal.com/en/datasets/trucost-environmental-(46) — S&P Global Marketplace dataset listing (search-indexed; accessed 2026-08-14)
- https://wrds-www.wharton.upenn.edu/pages/data-announcements/new-sp-esg-data/ — WRDS academic access to S&P ESG/Trucost data (accessed 2026-08-14)
- https://www.gpif.go.jp/en/investment/20190906_trucost.html — GPIF TCFD climate-risk case study using Trucost (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/Trucost — founding history, 2000 London origin (accessed 2026-08-14)
- https://www.jpx.co.jp/corporate/sustainability/esgknowledgehub/esg-rating/nlsgeu0000053wxn-att/Trucost_Environmental_Register_Methodology_FAQs.pdf — Environmental Register methodology FAQ (accessed 2026-08-14)
