# Dow Jones Factiva

## 1. Snapshot
- **Owner/parent:** Dow Jones & Company (owned by News Corp). Factiva is Dow Jones's flagship global news database/archive product; DNA (Data, News and Analytics) is the underlying enterprise API/cloud platform that also powers Factiva and licenses content to third parties (e.g., generative-AI vendors).
- **Coverage:** Premium international news and business-information database — 30,000+ sources historically (recent GenAI-licensing push reports 8,000+ *licensed* premium sources specifically cleared for AI use), spanning 200 countries and 33 languages; ~1 million incoming news articles/day processed through DNA.
- **Free tier:** No. Factiva/DNA is a paid enterprise/institutional product with no self-serve free tier; typically accessed via library/university seat licenses or corporate subscriptions.
- **Pricing model & ranges:** Enterprise licensing, quote-based (not published self-serve). Third-party cost trackers estimate roughly **~$1,500/month for a small-team DNA feed**, with broader Dow Jones product/contract bundles ranging **~$10,000 to $500,000+/year** for mid-market to enterprise buyers depending on user count, modules (Factiva search vs. DNA API/streams vs. GenAI licensing), and data volume. API/feed access and custom integration typically carry separate or higher-tier fees.

## 2. Coverage
Broad, deep general and business-news archive: newspapers, newswires, trade press, broadcast transcripts, and company/industry reports across 200 countries and 33 languages, including premium proprietary content (The Wall Street Journal, Barron's, Dow Jones Newswires, Investor's Business Daily, Financial News, MarketWatch, Private Equity News, The Washington Post). Strong on company profiles for small/mid-cap and niche-industry names not well covered elsewhere. Historical depth is a key differentiator — archives extend back decades, positioned as one of the largest licensed news archives available for enterprise/AI use.

## 3. Datasets
- **Factiva** (search/research interface): full-text news articles, company profiles/financials snapshots, industry reports, executive/people data, with taxonomy-based subject/industry/region coding for filtering.
- **DNA (Data, News and Analytics) platform**: three access modes — **DNA Snapshots** (bulk historical archive extracts), **DNA Streams** (real-time streaming content feed), and **DNA APIs** (look-up/search/transact functions). Content is normalized, entity-extracted and taxonomy-tagged using Dow Jones's proprietary classification system, then loaded to both the DNA archive and BigQuery tables for enterprise consumption.
- Recently expanded: GenAI-specific licensing surfaced 8,000+ sources cleared for use in conversational AI, summarization, and "deep research" tools — a distinct commercial track from standard Factiva/DNA licensing.

## 4. APIs & technical integration
- **API type:** REST-based DNA APIs plus bulk Snapshot extracts and real-time Streams; developer portal at developer.dowjones.com.
- **Auth:** Enterprise credential/OAuth-style access issued under contract (not self-serve signup).
- **Formats:** Structured JSON/XML with proprietary taxonomy codes for entity, subject, industry, and region tagging; BigQuery table delivery for enterprise data-warehouse integration.
- **Delivery:** Snapshot (batch/bulk), Streams (real-time push), and on-demand API query — a genuinely three-tier delivery architecture uncommon among lower-cost providers.
- **MCP availability:** No official MCP server identified; integration is via enterprise API/SDK (Dow Jones maintains a GitHub org with client tooling).

## 5. Enabling technology
Large-scale content ingestion and normalization pipeline (~1M articles/day) feeding a proprietary taxonomy/entity-extraction engine built over two decades of editorial classification. Recent investment in GenAI-grounding infrastructure — licensing content specifically for use as retrieval-augmented context in third-party LLM/AI products, positioning DNA as a "trusted content" layer for AI vendors rather than only a human-research tool.

## 6. Customer / user feedback
Triangulated from G2 (~4/5 average, 29 reviews) and TrustRadius. **Pros:** very broad international coverage including small/mid-cap and niche-industry names; strong company-profile depth leveraging Dow Jones's editorial strength; near-real-time updates; trusted/reliable premium sourcing. **Cons:** dated, unintuitive search UI described as "archaic" and query-heavy; the report/data-builder tool is confusing and takes real effort to extract needed data; inconsistent filter behavior; some subject/industry coding is unclear; no easy link-sharing feature. User base is heavily institutional/library — corporate research desks, librarians, compliance/reputational-risk teams, and (increasingly) AI vendors licensing content for grounding.

## 7. Edge & positioning
- **Leads on:** breadth and depth of licensed premium news archive (30,000+ historical sources, 200 countries, 33 languages, decades of history), trusted/vetted content suitable for compliance and GenAI-grounding use cases, and a three-tier (Snapshot/Streams/API) enterprise delivery architecture.
- **Lags on:** self-serve accessibility (no free tier, no transparent pricing, enterprise-sales-only), modern developer experience (dated UI, steep learning curve for the query/report tools), and price relative to API-first entity/sentiment vendors (RavenPack, Marketaux).
- **Best-for:** large enterprises, compliance/KYC and reputational-risk teams, corporate research libraries, and AI vendors needing licensed, copyright-compliant news content at scale — not a fit for budget-constrained or self-serve developer use cases.

## 8. Provenance
- https://www.businesswire.com/news/home/20260120489743/en/Dow-Jones-Factiva-Surpasses-8000-Licensed-Sources-for-GenAI-Use — official press release on GenAI source licensing (accessed 2026-08-14)
- https://medium.com/dowjones/where-does-dow-jones-dna-content-come-from-666fff5ec145 — official Dow Jones Tech blog on DNA content sourcing (accessed 2026-08-14)
- https://www.globenewswire.com/news-release/2017/04/10/958275/0/en/Dow-Jones-launches-Data-News-and-Analytics-DNA-Platform.html — official DNA platform launch announcement (accessed 2026-08-14)
- https://www.itqlick.com/factiva/pricing — independent pricing/cost estimate breakdown (accessed 2026-08-14)
- https://www.g2.com/products/factiva/reviews?qs=pros-and-cons — independent user reviews, pros/cons (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/Factiva — background/history summary (accessed 2026-08-14)
- https://datarade.ai/data-providers/dow-jones-factiva/profile — independent provider profile/data marketplace listing (accessed 2026-08-14)

**Note:** WebFetch to dowjones.com/datarade.ai domains was egress-blocked in this environment; findings rely on the WebSearch index and third-party review/comparison sites rather than direct page retrieval.
