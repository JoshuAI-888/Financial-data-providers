# The Motley Fool

## 1. Snapshot
- **Owner/parent:** The Motley Fool, LLC — privately held media/investment-education company, co-founded 1993 by brothers David Gardner and Tom Gardner with Erik Rydholm. Independent (not a subsidiary of a larger financial-data conglomerate); primary business is subscription investing newsletters (Stock Advisor, Rule Breakers, etc.), not data/transcripts.
- **Coverage:** Broad US-listed public-company coverage; transcript archive spans roughly 2007–present, with roughly 1,000–1,500 new transcripts published per quarterly earnings season. Exact total company count not disclosed.
- **Free tier:** Yes — the earnings-call transcript library itself (fool.com/earnings-call-transcripts) is free and openly accessible, unlike Motley Fool's core Stock Advisor/paid-newsletter business.
- **Pricing model & ranges:** Transcripts: free. Motley Fool's broader paid products (Stock Advisor, Rule Breakers, Epic/premium bundles) run roughly $99–$499+/year depending on service, but these are stock-picking newsletters, not transcript-access paywalls — a distinct product line from the free transcript archive.

## 2. Coverage
US-listed companies only (consistent with Motley Fool's US retail-investor audience); no evidence of non-US exchange coverage for transcripts. History runs from approximately 2007 to present. Coverage is broad but reactive/event-driven — Motley Fool publishes a transcript whenever a covered company reports, at a volume of roughly 1,000–1,500 transcripts per quarter, implying coverage of several hundred to low-thousands of individual tickers per season rather than the full US market. No slide-deck or investor-presentation capture; transcripts are text-only (no audio hosted directly on the transcript pages, though calls typically link back to the company's own IR replay).

## 3. Datasets
- Full **earnings-call transcripts**, structured with prepared-remarks and a distinct **Q&A section**, speaker-attributed.
- Occasional companion articles (analysis/commentary) from Motley Fool's editorial team layered around select transcripts.
- No native audio hosting, no slides/decks, no structured KPI extraction, and no proprietary sentiment scoring on the free transcript product — this is a plain-text transcript library, not an analytics layer.

## 4. APIs & technical integration
No official public API for transcripts was found. Third-party scrapers exist (Apify's "Motley Fool Earnings Transcripts Scraper," open-source GitHub scrapers, and a Kaggle dataset of scraped transcripts), which confirms there is **no sanctioned programmatic access** — integration in practice means unofficial scraping of the public HTML pages, with attendant fragility/ToS risk.

## 5. Enabling technology
Transcription is credited to Motley Fool's own "Motley Fool Transcription"/"Motley Fool Transcribers" bylines rather than a named AI vendor in any source found — no independent confirmation of whether production is human-transcribed, AI-assisted, or licensed from a third party (e.g., AlphaStreet, which supplies transcripts to other outlets such as MarketBeat, was found to be an unrelated separate business, not confirmed as Motley Fool's supplier). Turnaround for a full formatted transcript is on the order of same-day to next-day; one transcript's own text states the raw conference-call replay becomes available "approximately 2 hours after completion of the call," with Motley Fool's edited transcript following afterward — this is a T+hours/T+1 profile, not real-time.

## 6. Customer / user feedback
No dedicated review-site presence (G2/Capterra/TrustRadius) exists for the transcript product specifically, since it's a free content feature rather than a purchased software product — feedback signal is indirect. Motley Fool's broader newsletter business claims 700,000+ premium subscribers, indicating a large, established retail user base and brand trust, but this reflects the stock-picking service, not transcript quality specifically. No independent complaints or praise about transcript accuracy/timeliness were found in the sources gathered; this is a genuine coverage gap.

## 7. Edge & positioning
- **Leads on:** Zero cost and open accessibility — the only provider in this set with a fully free, unpaywalled, searchable transcript archive at meaningful scale and history depth (2007–present).
- **Lags on:** Speed (no real-time or intraday availability — T+hours to T+1), no API, US-only coverage, no AI synthesis (summaries/sentiment/KPI extraction), no audio/slides, and no confirmed vendor/technology transparency behind transcript production.
- **Best-for:** Retail investors and researchers who want free, citable, full-text US earnings-call transcripts for manual reading/keyword search, and are not sensitive to same-day timing, structured data extraction, or non-US coverage.

## 8. Provenance
- https://www.fool.com/earnings-call-transcripts/ — Transcript library landing page (accessed 2026-08-14, indexed via search only — direct fetch egress-blocked)
- https://www.fool.com/earnings/call-transcripts/2026/08/13/insight-enterprises-nsit-q2-2026-earnings-call-transcript/ — Example transcript noting "~2 hours after completion" replay timing (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/The_Motley_Fool — Company founding, founders, history (accessed 2026-08-14, indexed via search only — direct fetch egress-blocked)
- https://www.fundinguniverse.com/company-histories/the-motley-fool-inc-history/ — Business-model evolution, subscriber base (accessed 2026-08-14)
- https://apify.com/jungle_synthesizer/motley-fool-earnings-transcripts-scraper — Confirms no official API, third-party scraping only (accessed 2026-08-14)
- https://www.kaggle.com/datasets/tpotterer/motley-fool-scraped-earnings-call-transcripts — Independent scraped dataset, corroborates archive scope (accessed 2026-08-14)
- https://github.com/hamid-vakilzadeh/motley-fool-scraper — Further confirmation of unofficial access pattern (accessed 2026-08-14)
