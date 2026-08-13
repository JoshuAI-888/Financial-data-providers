# Third Bridge

## 1. Snapshot
- **Owner/parent:** Third Bridge Group Limited — independent, privately held. Founded **2007** in London (originally as Cognolink; the two merged/rebranded under the Third Bridge name by 2016). HQ: **London, UK**, with ~12+ offices (New York, Los Angeles, Shanghai, Beijing, Hong Kong, Mumbai, Dubai, etc.) and 1,500+ employees. Positioning one-liner: a **human-led expert network + research library** that turns primary-research interviews into on-demand, analyst-produced intelligence for private equity, hedge funds and consultants.
- **M&A:** No major acquisitions of note; grew organically. Distributes its Forum/Library content through partners (e.g., Bloomberg) rather than through acquisitions.
- **Regions/markets covered:** **Global.** Company coverage spans every major sector and geography (65,000+ companies in the transcript library; 75,000+ public and private companies with primary intelligence). Strong non-US/foreign-company coverage — a differentiator versus US-centric filings tools.
- **Free tier:** **No.** Subscription/credit-based; enterprise sales only. No self-serve free plan.
- **Pricing model & known ranges:** Subscription (Forum/Library) plus credit packages for expert calls (Connections). Institutional pricing is **not publicly disclosed**; commonly cited annual subscriptions run into the tens of thousands USD. Expert-call economics (what experts are paid, indicative of call cost) run roughly **$110–$350** for manager-level experts and **$350–$1,000+** for C-level experts per consultation.

## 2. Data-domain coverage
- **fundamentals:** Not a structured-financials vendor; qualitative context around company/sector fundamentals rather than normalized statements.
- **filings:** Not a filings repository; references filings within analyst commentary but does not host SEC/EDGAR datasets.
- **transcripts/expert calls:** **Core.** Analyst-led interview transcripts (Forum/Library) and 1:1 expert consultations (Connections) — the primary product.
- **qualitative research:** **Core.** Sector- and company-specific primary research, value-chain "Maps," ESG and competitive-dynamics interviews produced by in-house analysts.
- **private-company data:** **Strong.** Intelligence on 75,000+ private and public companies; a differentiator for PE due-diligence.
- **entity/knowledge graph:** Partial — "Maps" provide value-chain/relationship intelligence on 100,000+ companies, but not a machine-queryable entity graph.

## 3. Datasets
- **Forum / Library:** Analyst-led interview transcripts covering **65,000+ companies**, published to subscribers and via distribution partners (Bloomberg first). Content is produced by Third Bridge sector analysts interviewing former executives, competitors and customers — proprietary primary research, not aggregated third-party feeds.
- **Connections:** On-demand access to a network of **1.5M+ vetted industry experts** via one-on-one calls, surveys and custom project recruiting.
- **Maps:** Visual value-chain intelligence covering **100,000+ companies**, mapping suppliers, customers and competitors.
- **Private Company Intelligence:** Real-time intelligence on **75,000+ private and public companies** across sectors/geographies.
- **Sourcing method:** Human expert network + in-house analyst interviews; AI search layered on top of the proprietary transcript corpus. Proprietary holding = the interview transcript library and expert relationships.
- **History/depth:** Transcript library built continuously since the late 2000s; deep in TMT, consumer, healthcare, industrials.

## 4. APIs & technical integration
- **API/export:** No broadly advertised public developer API for programmatic transcript retrieval; access is via the Forum/Library web platform and via **distribution partners** (Bloomberg terminal and other data platforms) that redistribute the content.
- **Auth/formats:** Platform login (SSO for enterprise); transcripts consumed as web documents / PDF exports within entitlement rules.
- **Delivery:** Web app + partner-platform embedding (Bloomberg). No advertised Snowflake/Databricks share.
- **Excel/model plugins:** None material — the product is qualitative, not model-feed.
- **MCP availability:** None advertised.
- **AI/LLM features:** AI search across the Library (natural-language querying of the transcript corpus) and AI-assisted summaries; the "three-part" Library combines company databases, transcript search and AI.

## 5. Enabling technology
- Primary stack is **human**: a global bench of sector analysts and a compliance-screened expert network. Analysts frame, conduct and edit interviews.
- Layered technology: NLP/AI search over the proprietary transcript corpus, AI summarization, and value-chain mapping tools ("Maps").
- **Human QA / compliance:** Heavy compliance and vetting workflows (expert screening, conflict checks) are central given the regulated expert-network space; content is analyst-edited rather than machine-generated.
- Data-ops centered on transcript production, tagging to companies/sectors, and distribution-partner feeds.

## 6. Customer / user feedback
- **Trustpilot (thirdbridge.com):** ~**4.5/5**, "Excellent," across ~**239** reviews — though much of this feedback is from **experts** (interviewees) describing recruiting/payment experience rather than institutional research buyers.
- **Glassdoor:** ~**1,396** employee reviews (employer sentiment, not product).
- **Independent expert-network directories** (Inex One, ExpertNetworks.net, Integrity Research) rank it among the top-tier "big three/four" expert networks alongside GLG, AlphaSights and Guidepoint.
- **Pros:** Deep, analyst-produced primary research; strong private-company and non-US coverage; content reusable via the Library (not just one-off calls); reputable compliance.
- **Cons:** Expensive, enterprise-only; no self-serve/free tier; no structured financials or developer API; product is qualitative and not built for quantitative model feeds.
- **User segments:** Private equity, hedge funds, long-only asset managers, management consultancies, corporates.

## 7. Edge & positioning
- **Leads:** Analyst-led primary research at scale (Forum/Library) — a reusable transcript library differentiates it from pure "connect-me-to-an-expert" networks; strong private-company and international coverage; distribution reach via Bloomberg.
- **Lags:** No structured fundamentals/filings data, no public API, no free tier, opaque pricing; not suitable for programmatic/quant workflows.
- **Best for:** PE and fundamental hedge-fund analysts who need qualitative, human primary research and expert access on specific companies/sectors — especially private and non-US names — rather than normalized financial data.

## 8. Provenance
- https://www.thirdbridge.com/en-us — official site, positioning & services (accessed 2026-08-11)
- https://thirdbridge.com/service/community/ — Library (formerly Forum) product page (accessed 2026-08-11)
- https://www.thirdbridge.com/en-us/services/expert-calls — Expert Calls / Connections service (accessed 2026-08-11)
- https://inex.one/expert-network-directory/third-bridge — independent expert-network directory profile (accessed 2026-08-11)
- https://expertnetworks.net/networks/third-bridge/ — independent review: pricing, compliance, coverage (accessed 2026-08-11)
- https://www.integrity-research.com/alphasense-merges-with-sentieo/ — industry analyst context on expert networks (accessed 2026-08-11)
- https://www.trustpilot.com/review/thirdbridge.com — Trustpilot rating and reviews (accessed 2026-08-11)
- https://www.zoominfo.com/c/third-bridge-group/358495803 — company overview / scale (accessed 2026-08-11)
