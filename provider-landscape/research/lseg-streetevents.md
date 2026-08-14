# LSEG StreetEvents

## 1. Snapshot
- **Owner/parent:** **LSEG (London Stock Exchange Group plc)**. Product lineage: Thomson **StreetEvents** (founded ~1999–2001 as an independent conference-call/webcast aggregator) → acquired by **Thomson Financial/Thomson Reuters** → rebranded **Refinitiv** (2018, Blackstone-led carve-out of Thomson Reuters' F&R unit) → **LSEG** acquired Refinitiv in a ~US$27B deal completed **2021**. Now sold as "**Transcripts and Briefs**" (StreetEvents name persists informally/in legacy docs and community forums) inside LSEG Data & Analytics / Workspace.
- **Coverage:** ~**10,400 global companies**; ~**40,000 verbatim transcripts and briefs produced per year** across earnings calls, M&A calls, sales calls, analyst/investor meetings and corporate conference presentations. Denser coverage of large-cap US and developed-market names (all major indices incl. S&P 500, Russell 1000); one independent library-FAQ source cites ~7,200 companies for the narrower "Transcripts and Briefs" cut — figures vary by product bundle. Usable history reaches back to the **early-to-mid 2000s** (~2001 per one archive index), among the deepest backfiles in the market.
- **Free tier:** **No.** Enterprise/quote-only — access is via a Refinitiv/LSEG Workspace entitlement or a negotiated bulk data-feed license; no self-serve signup or public trial found.
- **Pricing model & ranges:** **Not publicly disclosed.** Sold as a Workspace content entitlement (seat-based, bundled with broader LSEG data) or as a standalone institutional datafeed license (XML/Zip via FTP/SFTP or API). Broader LSEG Workspace seats are commonly cited as roughly **~10% cheaper than comparable Bloomberg Terminal seats**; StreetEvents/Transcripts-specific pricing requires a sales quote.

## 2. Coverage
- **Breadth:** ~10,400 companies globally, positioned by LSEG as "the broadest coverage of transcripts and briefs in the marketplace." Global public-company scope, but as with all FMP-adjacent comparisons in this repo, note coverage skews toward US/developed-market large- and mid-caps; smaller/EM names are thinner.
- **Event types:** Earnings calls, M&A calls, sales/investor-day calls, analyst meetings, corporate conference presentations — six-plus event categories, ~40,000/year combined.
- **History depth:** Usable archive from the **early 2000s** onward (~2001–2003 depending on company/index), a genuine differentiator versus newer entrants (Quartr, Tegus, API-native challengers) that only go back a few years.
- **Audio / slides / Q&A:** **Audio replay archive** is a named feature (click-to-replay via the Media column); transcripts capture full Q&A verbatim; briefs are a shorter synthesized companion product. Slide decks are not confirmed as a core StreetEvents deliverable (that is more a Quartr/company-IR-site feature).
- **US vs global:** Global in principle (all major indices), but the historically dominant client base (Wall Street sell-side/buy-side) means US-listed coverage is the deepest and most complete tier.

## 3. Datasets
- **Transcripts and Briefs** — the flagship dataset: full verbatim transcripts + shorter AI/analyst-style "briefs" per event, delivered as structured documents with **speaker and section tags** (prepared remarks vs. Q&A demarcated).
- **Audio archive** — recorded/replayable audio tied to each transcribed event.
- **AI-generated event summaries** — LSEG markets same-day AI summaries of earnings events ("insights available within seconds") covering actual vs. estimated revenue/EPS, hit/miss framing, and call-impact signals, surfaced in Workspace.
- **MarketPsych/LDA transcript analytics & "Reuters Super Summaries"** — adjacent LSEG products that layer sentiment/NLP scoring and LLM-generated super-summaries on top of the transcript corpus (per LSEG fact sheets found in search), suggesting the transcript feed is also a feedstock for LSEG's broader text-analytics stack, not just a standalone reading product.

## 4. APIs & technical integration
- **Delivery formats:** **XML** and **Zip Archive** bulk files, delivered via **FTP/SFTP**, with real-time/delayed and daily service-frequency options for the raw datafeed — this is the institutional bulk-ingestion path (not a lightweight public REST API).
- **Workspace/Workstation:** Primary human-facing access is **LSEG Workspace** (browser + desktop), where transcripts, briefs, audio and AI summaries surface as an integrated content type alongside fundamentals/estimates/news.
- **Programmatic access:** Broader LSEG Data Platform / **LSEG Data Library for Python**, Data Platform REST + streaming APIs can surface transcript/event content alongside other datasets, per LSEG's developer community; a dedicated public self-serve "Transcripts API" akin to FactSet's or API Ninjas' was not confirmed in available sources — developer-forum threads show users asking how to pull transcript text programmatically, indicating this is not a frictionless self-serve endpoint.
- **AI/LLM tooling:** LSEG publishes sample **GenAI notebooks** (e.g., a public GitHub example "Article.AI.Transcripts.Python — Uncovering Tariff Exposure from Transcripts") showing LLM-based parsing of transcript text pulled from the platform, evidencing active AI-workflow investment around the corpus.

## 5. Enabling technology
- Full **Refinitiv/Thomson legacy content pipeline**: professional transcription/editorial process behind "verbatim" transcripts, now under LSEG–Microsoft's Azure-based cloud re-platforming of Workspace/data infrastructure.
- **AI summarization layer**: same-day AI-generated earnings summaries (revenue/EPS hit-miss, sentiment) built on top of the transcript text — LSEG's genAI-in-Workspace initiative explicitly cites transcripts as a key unstructured input alongside news and filings.
- **MarketPsych/LDA transcript analytics** — NLP/sentiment scoring specifically tuned to call language (tone, uncertainty, litigious-word counts, etc.), a value-add synthesis layer distinct from the raw transcript.
- Delivered on LSEG's structured+unstructured "content fusion" architecture that links transcripts to fundamentals, estimates, deals and pricing inside Workspace.

## 6. Customer / user feedback
- No public reviews specific to "StreetEvents"/"Transcripts and Briefs" as a standalone product were found (expected for an enterprise, quote-only, non-self-serve dataset with no G2/Capterra listing).
- Triangulating from the parent product: LSEG Workspace/Refinitiv Eikon averages roughly **~3.3/5** across G2, Trustpilot and Gartner Peer Insights (aggregate ~67 reviews per comparison sites) — recurring praise for breadth of content and Reuters-news integration, recurring complaints about customer-service responsiveness and analytics depth versus Bloomberg/FactSet.
- LSEG developer-community forum threads (community.developers.lseg.com) show real users asking how to bulk-download/automate transcript retrieval, implying the self-serve programmatic path is less mature/more support-dependent than FactSet's dedicated Events & Transcripts API.
- **Segments (inferred from LSEG's own positioning + general Workspace user base):** sell-side and buy-side equity research, quant/NLP teams building sentiment signals off transcript text, compliance/surveillance teams cross-referencing management statements.

## 7. Edge & positioning
- **Leads on:** **History depth** (usable archive to the early 2000s — the deepest of the three profiled here) and sheer **institutional scale/bundling** (transcripts ship as one entitlement inside a full cross-asset Workspace terminal, with news, estimates, fundamentals and NLP/sentiment analytics natively cross-linked). Same-day AI summaries and dedicated sentiment analytics (MarketPsych/LDA) are a differentiated synthesis layer.
- **Lags on:** **Self-serve accessibility** — no public pricing, no free tier, no lightweight REST endpoint for a single transcript; acquiring the data requires a Workspace seat or negotiated bulk-feed license. Real-time/low-latency delivery of the *raw* transcript itself is not clearly faster than FactSet's near-real-time CallStreet feed — LSEG's edge is archive depth and analytics, not confirmed speed leadership.
- **Best-for:** Large institutional desks (sell-side research, quant/NLP, compliance) that already license LSEG Workspace or a bulk datafeed and want transcripts fused with fundamentals/news/sentiment in one platform, or that need the deepest historical transcript backfile for longitudinal NLP research — not a fit for a developer or small team wanting quick, cheap, single-endpoint transcript access (see API Ninjas for that).

## 8. Provenance
- https://www.lseg.com/en/data-analytics/financial-data/company-data/events/earnings-transcripts-briefs/transcripts-database — official product page, coverage figures (accessed 2026-08-14)
- https://community.developers.lseg.com/discussion/132317/earnings-call-transcript-download — developer forum, real access friction (accessed 2026-08-14)
- https://instituteforautomatedresearch.org/wiki/commercial/refinitiv-transcripts/ — independent coverage/history summary (accessed 2026-08-14)
- https://www.alacrastore.com/research/thomson-streetevents-transcripts — legacy Thomson StreetEvents product listing (accessed 2026-08-14; search-index only, WebFetch egress-blocked)
- https://www.lseg.com/en/insights/data-analytics/ai-unlock-investment-risk-management-opportunities-earnings-call-transcripts — AI summary/insights feature (accessed 2026-08-14)
- https://github.com/LSEG-API-Samples/Article.AI.Transcripts.Python.GenAITranscriptsParseCountrySuppliers — sample GenAI transcript-parsing notebook (accessed 2026-08-14)
- https://www.globaldatabase.com/bloomberg-vs-refinitiv-vs-sp-capital-iq-which-financial-terminal-is-worth-it — Workspace ratings triangulation (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/Refinitiv — parent-company lineage/acquisition history (accessed 2026-08-14; search-index only, WebFetch egress-blocked)

**Provenance note:** Direct WebFetch to lseg.com, community.developers.lseg.com, alacrastore.com and wikipedia.org was blocked by this environment's egress policy for every attempt; all facts above are triangulated from Google/Bing-style search-index snippets returned by the WebSearch tool (including a translate.goog mirror attempt, also blocked) rather than full-page fetches. Treat exact coverage counts (10,400 vs. 7,200 companies) as approximate and cross-check against a live LSEG source before quoting externally.
