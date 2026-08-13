# Quartr

## 1. Snapshot
- **Owner/parent:** Quartr AB — independent, privately held. Founded **2020** by Oscar Küntzel, Sami Osman and David Dag (who met via the Swedish fintech community). HQ: **Stockholm, Sweden** (Sveavägen 52). Positioning one-liner: **first-party investor-relations data infrastructure** — live and historical earnings calls, transcripts, filings and slides — delivered both as a research app (Quartr Pro) and as an AI-ready data API.
- **M&A:** None; venture-funded. Raised roughly **$40M** total across several rounds; investors include **Altos Ventures, Yanno Capital, Öhman, Philian Invest** and fintech angels (Michael Batnick, Josh Brown). Reported ~$7.9M revenue in 2025 with ~72 staff.
- **Regions/markets covered:** **Global** — 65+ markets. Coverage of live public-company events is a stated global leadership claim; strong non-US/foreign-company coverage (structured first-party data from 15,000+ companies across 65 markets via the API).
- **Free tier:** **Yes (partial)** — the Quartr **mobile app is free** (live calls, transcripts, slides for retail/pro users). Quartr Pro, API datasets, exports, MCP and webhooks are paid/contract-gated.
- **Pricing model & known ranges:** Free mobile app; **Quartr Pro** subscription for professionals; **Quartr API** is enterprise/custom-priced (unlimited calls for paying customers). Exact figures **not publicly disclosed**.

## 2. Data-domain coverage
- **fundamentals:** Light/structured event-linked figures (KPIs surfaced from reports); not a full normalized-financials vendor.
- **filings:** **Yes** — filings and reports are one of the datasets (IR-sourced documents alongside events).
- **transcripts/expert calls:** **Core** — live and historical earnings-call transcripts, speaker-identified; conferences, capital-markets days, fireside chats. No expert-network component.
- **qualitative research:** **Core** — IR events, slide decks, event/segment summaries; positioned as a "qualitative market research platform."
- **private-company data:** Minimal — focus is public-company IR events.
- **entity/knowledge graph:** Not a knowledge-graph vendor; data is structured/tagged by company and event but not exposed as an entity graph.

## 3. Datasets
- **Corpus:** **50M+ first-party documents**; structured first-party IR data from **15,000+ companies across 65 markets** (API), with the broader library covering many more via the app.
- **Eight datasets** extracted from IR events (earnings calls, conferences, capital-markets days, investor updates, fireside chats, M&A announcements): (1) live audio, (2) live/real-time transcripts, (3) historical audio, (4) historical transcripts, (5) filings and reports, (6) slide presentations, (7) event/AI summaries, (8) segments.
- **Transcript depth:** Raw transcripts published shortly after an event (paragraph breaks); **edited transcripts** follow with speaker names, roles and company affiliations. Optimized for AI/search.
- **Sourcing method:** First-party collection direct from company IR (audio capture + speech-to-text + editorial cleanup), not third-party licensing — the proprietary holding is the first-party event/transcript corpus and its speaker-identification layer.

## 4. APIs & technical integration
- **Quartr API:** Enterprise IR-data API with three integration modes — (1) direct **query endpoints** (fetch/filter/paginate), (2) **webhooks** for real-time change notifications (no polling), (3) **Snowflake** native access via SQL in your own environment.
- **Auth/formats:** API-key auth; JSON REST; audio/transcript/document assets. Docs at docs.quartr.com.
- **Delivery:** REST API, webhooks, and **Snowflake** data share; live audio/transcript streaming.
- **Excel/model plugins:** Integrations page lists workflow connectors; no flagship Excel add-in emphasized (API-first).
- **MCP availability:** **Yes** — official **Quartr MCP server** (mcp.quartr.com/docs), installable via the Anthropic marketplace; positioned for individual research workflows (builders use the Public API). Native Claude/Snowflake integrations; embeds across 1,000+ AI tools.
- **AI/LLM features:** Data explicitly "structured for AI"; automated event summaries, speaker-identified transcripts, and MCP access for LLM agents.

## 5. Enabling technology
- **Capture + ASR pipeline:** first-party audio capture of live events, automatic speech recognition producing real-time raw transcripts, then an editorial/AI pass for **speaker identification** (names/roles/affiliations) and paragraph structuring.
- **AI summarization** and segmentation of events; tagging to companies and event types (entity/event resolution).
- **Human editorial QA** on edited transcripts; data-ops built for low-latency live delivery (webhooks, live streaming) across 65 markets.

## 6. Customer / user feedback
- **G2:** rated **5.0** across a small number of reviews (~**2** verified) — very limited sample.
- **Third-party tool reviews** (Find My Moat) describe it favorably as a modern, AI-ready IR-data source; developer interest reflected in community MCP projects on GitHub.
- **Pros:** Broad global/market coverage (65 markets), fast live transcripts, clean first-party sourcing, modern API + webhooks + Snowflake + MCP, free mobile app for lightweight use.
- **Cons:** Thin public review base (hard to triangulate at scale); enterprise API pricing opaque; not a source of normalized fundamentals or private-company data; younger vendor than incumbents.
- **User segments:** Hedge funds, asset managers, equity-research desks, IR professionals, fintech/media platforms building on the API, and retail investors via the free app.

## 7. Edge & positioning
- **Leads:** Real-time, speaker-identified earnings-call transcripts with genuinely global (65-market) first-party coverage and a modern, AI-native delivery stack (API + webhooks + Snowflake + MCP). Free mobile app lowers the on-ramp.
- **Lags:** Not a fundamentals/estimates or private-company provider; small independent-review footprint; enterprise pricing undisclosed.
- **Best for:** Teams and builders that need timely, structured, global earnings-call/IR content piped into research tools or LLM workflows — as a transcript/events layer rather than a full fundamentals database.

## 8. Provenance
- https://quartr.com/ — official site, positioning (accessed 2026-08-11)
- https://quartr.com/products/quartr-api — Quartr API product & coverage (accessed 2026-08-11)
- https://quartr.com/docs/datasets/earnings-call-transcripts — transcript dataset detail (accessed 2026-08-11)
- https://docs.quartr.com/v1/guide/webhooks — API webhooks documentation (accessed 2026-08-11)
- https://quartr.com/mcp — official MCP offering (accessed 2026-08-11)
- https://mcp.quartr.com/docs — Quartr MCP server documentation (accessed 2026-08-11)
- https://quartr.com/products/mobile-app — free mobile app (accessed 2026-08-11)
- https://www.cbinsights.com/company/quartr — company/funding profile (accessed 2026-08-11)
- https://siliconcanals.com/stockholm-quartr-raises-8-7m/ — funding & HQ (independent) (accessed 2026-08-11)
- https://www.g2.com/sellers/quartr — G2 reviews/rating (accessed 2026-08-11)
