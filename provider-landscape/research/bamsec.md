# BamSEC

## 1. Snapshot
- **Owner/parent:** Founded 2013 (San Francisco). Acquired by **Tegus** on October 26, 2021 (Tegus rolled BamSEC out to all Tegus customers). Tegus was in turn acquired by **AlphaSense** in July 2024 (~$930M deal, part of a $650M AlphaSense raise), so BamSEC is now ultimately owned by AlphaSense, sold alongside Tegus and Canalyst as part of the combined suite.
- **Coverage:** Full SEC EDGAR universe — all US public-company filings (10-K/10-Q/8-K/proxy/S-1 etc.), insider Forms 3/4/5, 13F institutional-holdings data, and earnings-call transcripts; US-listed only (consistent with EDGAR scope), no meaningful non-US filing regime coverage.
- **Free tier:** Yes — free access lets anyone browse all EDGAR filings in original form; enriched metadata/table tools and premium search are blurred/gated for non-subscribers.
- **Pricing model & ranges:** Self-serve subscription: **BamSEC Pro ≈ $69/month** (billed annually) for an individual, unlocking full-text document search, table tools, ownership/insider analytics, transcripts, alerts and all-company screening. Team/enterprise tier available with custom pricing, now sold/bundled via Tegus/AlphaSense channels for institutional accounts.
- 

## 2. Coverage
US-only by design — mirrors SEC EDGAR's scope, so no NZX/ASX/LSE/HKEX/SGX/KRX/TWSE filings (same US-listed constraint noted in this repo's CLAUDE.md for FMP). Historical depth follows EDGAR (full-text search back to 2001 for most form types, older filings available as scanned/archived documents). Coverage is document-level (every US filer that submits to EDGAR), not curated to a subset of large caps — a strength for long-tail/small-cap and micro-cap filing research.

## 3. Datasets
- Full-text-searchable SEC filings (all form types) with phrase, boolean, proximity, form-type, industry, market-cap and document-type filters.
- Earnings-call and investor-conference transcripts.
- Insider transactions (Forms 3, 4, 5) and institutional ownership/13F holdings analysis.
- Filing "redlines" — browser-based version-compare that highlights text/table changes between two filings (e.g., quarter-over-quarter 10-Q language changes).
- Table Tools: one-click extraction of any table from any filing into clean, Excel-ready format (preserves $ and % formatting, strips logos/styling).
- Watchlists and filing alerts by company, filer, form type, or EDGAR-wide new-filing sweep.

## 4. APIs & technical integration
**No public API access.** BamSEC is explicitly a document-display and human-workflow tool, not a data-feed/API product — it does not offer programmatic access, bulk data export, or AI-agent integration. Its only "integration" surface is one-click Excel table export (copy/paste-grade CSV-to-Excel table download, not a live Excel add-in/refreshable link) and browser-based redlining/search. This is a meaningful contrast to FMP-style REST APIs: BamSEC is consumed manually via its web UI, so it cannot be wired into an automated pipeline like `fmp_milford/client.py`.

## 5. Enabling technology
Full-text search/indexing engine over the EDGAR corpus with filing-diff (redline) computation and structured table parsing (turns HTML/XBRL filing tables into clean exportable tables). No disclosed use of generative AI/NLP summarization (unlike Sentieo/AlphaSense) — positioning is "fast, accurate document retrieval and table extraction," not AI-driven synthesis.

## 6. Customer / user feedback
Positioned as the practitioner-favorite alternative to raw EDGAR.gov for search speed and Excel table export — a Wall Street Oasis forum thread and multiple review sites frame it as a lower-cost "must-have" for equity research analysts and IR/legal teams doing heavy filing review, especially compared to enterprise terminals. A widely-shared LinkedIn post summarizes the community trade-off succinctly: "BamSEC is expensive, EDGAR is free but annoying to use" — i.e., the value proposition is UX/speed, not unique data (since underlying content is public EDGAR data). No major complaint themes surfaced beyond price-for-individuals and lack of API/data-analytics depth (explicitly not a financial-data or insider-analytics platform per some comparison sites).

## 7. Edge & positioning
- **Leads on:** speed and usability of full-text EDGAR search, one-click clean table-to-Excel export, and filing-version redlining — best-in-class for the specific job of "find and extract text/tables from SEC filings fast."
- **Lags on:** no API/programmatic access, US-only (EDGAR-bound) coverage, no structured fundamentals/estimates, no AI summarization.
- **Best-for:** individual equity analysts, IR/legal/compliance teams and students who need fast, reliable manual search and table extraction from US SEC filings at a fraction of a full terminal's cost; not suitable for automated/pipeline use cases needing an API.

## 8. Provenance
- https://www.prnewswire.com/news-releases/tegus-completes-bamsec-acquisition-announces-bamsec-rollout-to-all-tegus-customers-301444736.html — 2021 Tegus/BamSEC acquisition (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/alphasense-completes-acquisition-of-tegus-302190934.html — 2024 AlphaSense/Tegus deal (accessed 2026-08-14)
- https://www.bamsec.com/pricing — pricing page (accessed 2026-08-14, fetch blocked, via search snippet)
- https://www.bamsec.com/features/table-tools — Table Tools feature description (accessed 2026-08-14, via search snippet)
- https://www.saasworthy.com/product/bamsec/pricing — $69/mo Pro plan confirmation (accessed 2026-08-14)
- https://www.edgar.tools/vs/bamsec — competitor comparison, no-API confirmation (accessed 2026-08-14)
- https://www.wallstreetoasis.com/forum/investing/buying-a-bamsec-individual-account-or-other-platform-worth-it-recommendations — practitioner discussion/value framing (accessed 2026-08-14)
- https://www.linkedin.com/posts/alexbarr23_bamsec-is-expensive-edgar-is-free-but-annoying-activity-7280608713382494208-qPVS — user cost/value commentary (accessed 2026-08-14)

Note: WebFetch to bamsec.com, saasworthy.com and other primary/review domains was egress-blocked in this environment; facts above are triangulated from WebSearch result snippets across ≥2 independent sources, not direct page fetches.
