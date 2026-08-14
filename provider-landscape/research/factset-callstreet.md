# FactSet CallStreet

## 1. Snapshot
- **Owner/parent:** **FactSet Research Systems Inc.** (NYSE: FDS). CallStreet LLC was an independent NY-based transcript/event-calendar provider founded **2001**; **FactSet acquired it on 7 May 2004 for ~US$6.5M cash** and fully integrated it into the FactSet Workstation/data platform — it now operates as a FactSet-owned brand ("FactSet's CallStreet") rather than a separate company.
- **Coverage:** FactSet's Events & Transcripts feed tracks **40,000+ companies' events per year**, with full **transcripts produced for ~10,000 of them** (earnings calls, conference presentations, special situations, sales calls, analyst/investor meetings, guidance calls). History: **events from 2000, transcripts from 2003** onward in the structured datafeed.
- **Free tier:** **No.** Enterprise/quote-only, bundled into a FactSet Workstation subscription or licensed as a standalone Events & Transcripts / Documents Distributor data feed and API; no public self-serve signup found.
- **Pricing model & ranges:** **Not publicly disclosed** — sold as a Workstation content module or a negotiated enterprise datafeed/API license (OAuth2/API-key gated, FactSet account required). For reference, FactSet Workstation seats are commonly cited around **US$12–15k+/seat/year** (vs. Bloomberg ~$28–32k); CallStreet-specific/transcript-feed pricing is a separate, undisclosed line item.

## 2. Coverage
- **Breadth:** 40,000+ companies covered for events annually; **~10,000 receive full transcripts** — a meaningful subset, implying FactSet prioritizes transcript production for larger/more liquid/more actively-followed names rather than transcribing every event it tracks.
- **Event types:** Six distinct categories — earnings calls (most prominent), conference presentations, special situations, sales calls, analyst/investor meetings, guidance calls.
- **History depth:** Structured datafeed coverage from **2000 (events) / 2003 (transcripts)** — roughly comparable to, slightly shallower than, LSEG StreetEvents' early-2000s archive, but still one of the deepest in the market and far ahead of newer AI-native entrants.
- **Audio / slides / Q&A:** **Events Audio** is a distinct dataset — historical and current audio recordings from earnings calls, conferences and investor days, delivered with timestamps and file IDs alongside the text. Transcripts explicitly separate prepared remarks from Q&A. No evidence found of native slide-deck capture (unlike Quartr).
- **US vs global:** Global events coverage, but as the classic "Wall Street" sell-side product (CallStreet's own branding — "1-877-FACTSET, www.callstreet.com" appears as the transcript-cover-page boilerplate on thousands of US corporate-IR-site PDFs), the depth and speed advantage is clearly strongest for US-listed large/mid-caps.

## 3. Datasets
- **Events & Transcripts XML Datafeed** ("Document Distributor") — bulk, machine-readable feed of company events + full transcripts, explicitly marketed for NLP use (launched as a distinct product in 2017 "to facilitate Natural Language Processing").
- **Documents Distributor – Near Real-Time Transcripts API** — a **CallStreet-branded, low-latency** transcript feed for time-sensitive users; includes **speaker metadata with confidence scores**, purpose-built for ML/sentiment pipelines that need the call text before the fully-edited version is ready.
- **Events Audio dataset** — recordings tied to the same event calendar, separately licensable from text.
- **Transcript Intelligence** — FactSet's **AI-generated, human-approved** earnings-call summary product, designed to let a user track "dozens of companies during busy earnings season" without reading full transcripts — the clearest value-add-synthesis layer in the FactSet stack.
- **Corrected/edited "verbatim" transcript** — the classic CallStreet deliverable seen as a PDF cover-paged "Corrected Transcript, 1-877-FACTSET, www.callstreet.com" attached to thousands of public company IR pages; produced after human editorial correction of the raw/real-time pass.

## 4. APIs & technical integration
- **Events and Transcripts API** (developer.factset.com) — REST API with an official multi-language SDK family (`fds.sdk.EventsandTranscripts`, also published to NuGet as `factset.sdk.eventsandtranscripts`, and a separate `fds.sdk.DocumentsDistributorCallStreetEvents` package on PyPI). Confirmed via NuGet: **API v2.2.2 / SDK v3.0.0**, **.NET Standard 2.0+**, **Apache 2.0** license, **OAuth 2.0 or API-key** auth — auto-generated via OpenAPI Generator with full docs.
- **Speed tiers, explicitly two-track:** (1) **Near Real-Time Transcripts** (CallStreet-sourced, machine-transcribed-first-pass with speaker confidence scores, for time-sensitive/algo consumers) vs. (2) the standard **Transcripts Service** full/edited transcript delivered after human correction — i.e., FactSet explicitly sells "fast-and-rough" and "slower-and-verbatim" as two distinct API products, unusual transparency about the speed/accuracy tradeoff versus peers.
- **Bulk delivery:** XML/Zip via **Standard DataFeeds (SDF)**, plus cloud-native access via **Snowflake** and **Databricks Marketplace** shares (consistent with FactSet's broader open-data-platform strategy documented in this repo's `factset.md`).
- **Desktop:** Surfaced natively inside **FactSet Workstation** with calendar-filtering "consistent with the Workstation experience," plus Excel/Office integration typical of the FactSet suite.
- **AI/LLM tooling:** Transcript Intelligence AI summaries; broader FactSet **Mercury** GenAI copilot can query/summarize transcript content within Workstation.

## 5. Enabling technology
- Hybrid **machine-transcription-then-human-correction** pipeline: a fast ASR/near-real-time pass (CallStreet Events, with per-speaker confidence scoring for downstream ML) followed by professional editorial correction to produce the "Corrected Transcript" verbatim record.
- **Speaker diarization with confidence scores** exposed directly in the API — a differentiator for teams building their own NLP/sentiment models on top of raw output rather than relying only on FactSet's own AI summaries.
- **Transcript Intelligence**: AI-generated summaries with a human-approval/QA step (not fully autonomous), reflecting FactSet's general "AI-assisted, human-checked" content philosophy also seen in Cobalt's AI Doc Ingest (per `factset.md`).
- Delivered on FactSet's broader open-architecture cloud stack (Snowflake, Databricks, OpenAPI-generated SDKs), the same infrastructure backing its other data feeds — i.e., CallStreet is not a bolted-on legacy silo but a first-class citizen of FactSet's modern API platform.

## 6. Customer / user feedback
- No reviews specific to "CallStreet" as a standalone brand were found (expected — it has been fully absorbed into FactSet's Workstation/data-feed catalog since 2004 and has no independent G2/Capterra listing).
- Triangulating from the parent: **FactSet Workstation ~4.3/5 on G2** (35 reviews; sub-scores: Quality of Support 9.3/10, Ease of Use 8.6/10, Ease of Setup 8.6/10, Data Visualization 8.1/10) and TrustRadius reviewers rate FactSet's **ongoing customer support above Bloomberg's** — support quality is FactSet's most consistently-cited edge across independent review sites (also reflected in this repo's `factset.md`).
- Indirect evidence of transcript-specific reliability: thousands of public-company investor-relations sites (Q4-hosted IR pages, e.g., Stanley Black & Decker, Palo Alto Networks, Verisk) attach FactSet/CallStreet "Corrected Transcript" PDFs as the official record of their earnings calls — implying broad de facto trust/adoption as the standard corporate-transcript vendor among US public companies, independent of any star rating.
- **Segments (inferred):** sell-side and buy-side equity research (core Workstation user base), quant/NLP teams consuming the near-real-time API feed, and corporate IR teams who use CallStreet-produced transcripts as their own official published record.

## 7. Edge & positioning
- **Leads on:** Explicit **two-speed delivery** (near-real-time machine transcript with confidence scores vs. fully corrected verbatim) is a genuine, documented differentiator — FactSet is the only one of the three profiled here that productizes both a fast and a verbatim tier as separate API offerings. Deep integration into a broader open, developer-friendly API/SDK ecosystem (OpenAPI-generated SDKs, Snowflake/Databricks) makes programmatic access more turnkey than LSEG's bulk-FTP-oriented delivery.
- **Lags on:** Like LSEG, **no free tier or public pricing** — enterprise/quote-only, requiring a FactSet account; smaller total transcript output than events tracked (only ~10,000 of 40,000+ companies get full transcripts, vs. LSEG's ~40,000 transcripts/year across ~10,400 companies, i.e., LSEG appears to transcribe a higher share of its universe, though the two vendors count differently and this is not a clean apples-to-apples comparison).
- **Best-for:** Quant/NLP teams and equity researchers who are already FactSet clients and want a developer-grade, speed-tiered transcript API (fast confidence-scored draft + verbatim corrected version) wired into the same platform as fundamentals/estimates/ownership — and for any team that wants the "industry-standard" transcript format that public companies themselves already treat as their canonical record.

## 8. Provenance
- https://www.crunchbase.com/acquisition/factset-acquires-callstreet--15f27d67 — acquisition date/price (accessed 2026-08-14)
- https://insight.factset.com/resources/at-a-glance-document-distributor-xml-company-events-transcript-datafeed — coverage figures, event types (accessed 2026-08-14; search-index only, WebFetch egress-blocked)
- https://www.factset.com/marketplace/catalog/product/documents-distributor-near-real-time-transcripts-api — near-real-time CallStreet API product (accessed 2026-08-14; search-index only, WebFetch egress-blocked)
- https://www.factset.com/marketplace/catalog/product/transcript-intelligence — AI summary product (accessed 2026-08-14; search-index only, WebFetch egress-blocked)
- https://www.nuget.org/packages/factset.sdk.eventsandtranscripts — SDK version, auth method, license (accessed 2026-08-14, fetched directly)
- https://www.globenewswire.com/en/news-release/2017/06/22/1027695/7768/en/FactSet-Releases-Events-and-Transcripts-Data-Feed-to-Facilitate-Natural-Language-Processing.html — 2017 datafeed launch for NLP (accessed 2026-08-14)
- https://www.g2.com/products/factset-workstation/reviews — parent-product review scores (accessed 2026-08-14)
- https://s29.q4cdn.com/767340216/files/doc_financials/2026/q1/CORRECTED-TRANSCRIPT-Verisk-Analytics-Inc-VRSK-US-Q1-2026-Earnings-Call-29-April-2026-8-30-AM-ET.pdf — real corporate-IR CallStreet transcript artifact, de facto adoption evidence (accessed 2026-08-14)

**Provenance note:** Direct WebFetch to factset.com, developer.factset.com, insight.factset.com and callstreet.factset.com was blocked by this environment's egress policy on every attempt (org-level 403); the NuGet package page loaded directly and is the one first-party primary source used. All other FactSet-domain facts above are triangulated from WebSearch index snippets rather than full-page fetches — verify exact latency/SLA figures against a live FactSet source before quoting externally.
