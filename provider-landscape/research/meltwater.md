# Meltwater

## 1. Snapshot
- **Owner/parent:** Publicly traded — Meltwater N.V. (previously Meltwater B.V.), listed on Oslo Børs (Euronext Growth Oslo initially, admitted 3 Dec 2020 under ticker MWTR; transferred to the main Oslo Børs 20 Dec 2021). Founded 2001 in Oslo, Norway; the world's first online media-monitoring company per its own history. Not a subsidiary — Meltwater is the parent/public entity itself.
- **Coverage:** Enterprise media, social, and consumer-intelligence monitoring: 270,000+ news, podcast, and broadcast sources plus a built-in journalist database, combined with social listening across major platforms; claims to process 500M+ documents and 12 trillion+ searches per day (algorithmic scale claim from company materials).
- **Free tier:** No published self-serve free tier or trial. Custom-quoted enterprise plans only.
- **Pricing model & ranges:** Fully custom/sales-quoted (no published rate card, no monthly billing option per third-party buyer commentary). Entry-level plans estimated around $6,000–$10,000/year by third-party pricing-intelligence sites; contracts typically annual with auto-renewal (60-day written cancellation notice window cited repeatedly in reviews).

## 2. Coverage
Same enterprise "social + media listening" category as Brandwatch and Talkwalker — all three are quote-only, no self-serve tier, positioned for large PR/marketing/comms teams rather than individual developers or quants. Meltwater differentiates on breadth of traditional media/news/broadcast/podcast sources and its journalist/press-contact database (PR-relations strength); social-listening depth is described by third-party comparisons as lagging Brandwatch (deep consumer intelligence) and Talkwalker (150M+ websites, 30+ social channels, 187 languages, strong visual-AI/image recognition). Note on X/Twitter specifically: due to X's API terms, Meltwater's API can only return tweet IDs (not full text) to API customers, who must separately call the X API to "rehydrate" tweet content.

## 3. Datasets
- Editorial/news, podcast, and broadcast monitoring (270,000+ sources) with full-text/quote-level content where licensing allows.
- Social listening across major platforms (subject to platform API restrictions, e.g., X ID-only limitation above).
- Journalist/media-contact database for PR targeting and outreach.
- Influencer data with demographics breakdowns (cited as a specific reviewer-praised strength).
- Media/social analytics and reporting (sentiment, reach, share-of-voice style metrics implied by "media intelligence" positioning).

## 4. APIs & technical integration
- **API type:** REST-style Meltwater API (developer.meltwater.com), covering data export/content access and analytics requests over the platform's dataset.
- **Delivery model:** Two primary access patterns — scheduled exports and real-time data streams — both delivering Meltwater's earned-media and social dataset in structured/machine-readable formats.
- **Auth:** Enterprise-contract based API access (part of paid platform subscription; no public self-serve key signup identified).
- **MCP availability:** No official MCP server identified in research.
- **Known limitation:** X/Twitter content delivered as tweet IDs only via API (not full text), due to X's terms of service — a documented platform-imposed constraint, not a Meltwater choice.

## 5. Enabling technology
Long-established (2001-founded) media-monitoring and NLP stack for large-scale content ingestion, entity/sentiment tagging, and search across hundreds of millions of documents daily; company claims real-time processing at "12 trillion searches" per day scale. No recent generative-AI/LLM architecture specifics surfaced in this research beyond general "AI-driven insights" marketing language common to the category.

## 6. Customer / user feedback
Large installed base: ~27,000 global customers, 50 offices across six continents, ~2,300 employees; repeatedly ranked #1 in G2's media-monitoring category and named to G2's 2026 Best Software Awards. G2 review average sits around 4.0–4.1/5 (~2,900 reviews). Praised for ease of use, customer-success responsiveness, influencer-demographics depth, and its journalist/media-contact database. Recurring, consistent criticism across G2/Trustpilot/TrustRadius: pricing opacity (no published rates, no free trial, no monthly billing — cost only obtainable via sales), aggressive sales/renewal practices (auto-renewal with a 60-day cancellation-notice window, multi-year contract pressure to avoid price increases), occasional article-tracking delays, and gaps in publication coverage ("blind spots").

## 7. Edge & positioning
- **Leads on:** Breadth of traditional news/broadcast/podcast source coverage (270K+ sources) and PR/journalist-relations tooling — the strongest of the three peers (Meltwater/Brandwatch/Talkwalker) for earned-media and comms-team workflows.
- **Lags on:** Social-listening depth and analytics sophistication versus Brandwatch (consumer intelligence) and visual/multilingual coverage versus Talkwalker (187 languages, image AI); also lags on pricing transparency and contract-friendliness (a recurring reviewer complaint across all review sites).
- **Best-for:** Corporate PR, comms, and brand-marketing teams needing broad earned-media + social monitoring with journalist outreach tools — not built for quant/systematic finance use cases (no finance-tuned sentiment score, no self-serve API tier, enterprise-only pricing).

## 8. Provenance
- https://developer.meltwater.com/docs/ — Meltwater API developer portal overview (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://developer.meltwater.com/docs/meltwater-api/social-analytics/overview/ — social analytics API scope (accessed 2026-08-14)
- https://live.euronext.com/en/ipo-showcase/meltwater — IPO/listing details, Oslo Børs ticker MWTR (accessed 2026-08-14)
- https://www.g2.com/products/meltwater/reviews — G2 rating (~4.0-4.1/5), review themes (accessed 2026-08-14)
- https://syncly.app/blog/brandwatch-vs-meltwater-vs-talkwalker — third-party peer comparison vs. Brandwatch/Talkwalker (accessed 2026-08-14)
- https://www.vendr.com/marketplace/meltwater — third-party pricing estimate ($6K-$10K/yr entry) (accessed 2026-08-14)
- https://www.meltwater.com/en/about/press-releases/g2-names-meltwater-the-top-media-monitoring-software — G2 #1 media-monitoring ranking (accessed 2026-08-14)
- https://community.meltwater.com/meltwater-api-140/accessing-exporting-your-data-with-the-meltwater-api-7924 — API export/data-access model (accessed 2026-08-14)

**Note:** WebFetch to meltwater.com and developer.meltwater.com was egress-blocked in this environment; findings rely on the WebSearch index and third-party review/comparison sites rather than direct page retrieval.
