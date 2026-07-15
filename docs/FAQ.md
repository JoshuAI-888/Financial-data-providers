# FAQ

### Why are there no NZX / ASX companies?
FMP's **free and Starter tiers are US-listed only**. Milford's home exchanges (NZX, ASX,
LSE, HKEX, SGX, KRX, TWSE) are not reachable until **Premium** (adds LSE) or **Ultimate**
(adds the APAC exchanges). The universe is therefore US comparables — genuinely useful for
read-across to your NZ/AU names. Add non-US tickers to `config.UNIVERSE` the day you upgrade.

### Why does the report say "DEMO DATA"?
This build environment blocks outbound access to `financialmodelingprep.com`, so live data
could not be pulled here. The report uses a realistic **synthetic** dataset (labelled on every
widget). Run `python run.py --live` with your key on a network-open machine to populate real data.

### The numbers look plausible — can I trust them?
Only in **LIVE** mode. Demo figures are synthetic and for demonstrating the *mechanics* and
*layout*. Every widget shows a DEMO/LIVE badge so there is no ambiguity.

### How do I run it with real data?
```bash
echo "FMP_API_KEY=your_key" > .env      # .env is git-ignored
python run.py --live                    # full pull + real API latency
python run.py --live --probe-only       # just the speed test
python run.py --live --limit-sectors 3  # stay well under 250 calls/day
```

### How many companies can I refresh per day?
Free tier = **250 calls/day**; a full company pull is ~9 calls, so **~28–30 companies/day**.
The client tracks the budget, caches responses (24h), and refuses calls past the cap with a
clear message. Larger universes simply span multiple days from cache.

### Where do the metrics come from — are they FMP's ratios?
No. We **compute every metric ourselves** from the raw statements so definitions are consistent
across names and fully auditable. Click any number to see its formula, inputs and steps. FMP's
own `ratios`/`financial-scores` are used only as an optional cross-check.

### What does each metric mean / how does it earn alpha?
Every metric has a plain-language **meaning / what good looks like / target / alpha** entry —
hover a column header, click any figure, see [GLOSSARY.md](GLOSSARY.md), or open the
"What this means & how it earns alpha" box on any widget.

### Can I compare a custom set of companies?
Yes — use the company chips (grouped by theme; click a theme header to toggle the group) and
the market-cap / composite-z sliders. Every table and chart re-filters to your selection.

### Is the PM commentary written by an AI at runtime?
No — it is **rule-based** (deterministic thresholds on the computed metrics), so it is
reproducible and every sentence is traceable to a number. An LLM variant could be added later.

### Is this investment advice?
No. It is analytical tooling. It is **not** for client-facing or decision-of-record use
(FMA boundary), and does not source book-of-record data (positions/NAV) — that is IBOR/AlphaCert.

### Why weekly prices and a 21% tax rate?
Documented assumptions for consistency (see [ASSUMPTIONS.md](ASSUMPTIONS.md)). Weekly returns
give stable 5y risk stats within the free-tier history; a flat 21% NOPAT tax is a reasonable
default refined per-jurisdiction when precision matters.

### Nothing renders / the page is blank.
Open `outputs/milford_fmp_report.html` in a modern browser (Chrome/Edge/Firefox/Safari). It is
fully self-contained and offline — no server needed. If you regenerated it, re-run
`python run.py` and reopen.

### `--live` times out or 403s.
Your network is blocking `financialmodelingprep.com` (this managed environment does).
Run it from a machine with open egress, or enable the host in the environment's network policy.
