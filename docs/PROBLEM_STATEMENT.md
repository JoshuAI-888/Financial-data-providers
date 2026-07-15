# Background & Problem Statement

## Who this is for
Milford Asset Management's investment team — **Portfolio Managers, Head of Investment,
Portfolio Analysts, Quantitative Analysts, and Performance & Risk Analysts** — across a
book whose home exchanges are NZX, ASX, LSE, SGX, KRX, HKEX and TWSE.

## The background
The team repeatedly performs the same manual work: pulling company data from vendors,
re-keying it into spreadsheets, and rebuilding the *same* financial models (valuation
multiples, ROIC, cash conversion, DuPont, quality scores, risk statistics) for every new
name and every review. This is slow, error-prone, inconsistent between analysts, and it
buries scarce judgement time under data-collation grunt work.

A prior review (`datarequirementsandprovidercoverage.md`) catalogued every data point a
Milford-type manager needs and scored six non-institutional providers. **Financial
Modeling Prep (FMP)** stood out for breadth of fundamental/estimate/ownership/transcript
data on one platform — but US-deep and ex-US thin.

## The problem this repo addresses
> Build a repeatable, transparent, role-aware platform that turns raw FMP data into the
> calculations and comparisons the investment team asks for again and again — so they
> stop re-collating data and re-deriving models, and spend time on judgement and alpha.

## The binding constraint
The user is on the **FMP free (Basic) / lowest tier**:
- **US-listed securities only** (none of Milford's home exchanges are reachable),
- **EOD** prices, **~5 years** of annual statements,
- **250 API calls/day**, 500 MB/30-day bandwidth.

This reframes the deliverable. On the free tier FMP cannot support core NZX/ASX decisions.
Its genuine value at this tier is as a:
1. **US-listed comparables / read-across** engine for NZ·AU·APAC names,
2. **fundamental-modelling & financial-calculation sandbox** (kill repeat modelling),
3. **dev/prototyping sandbox** for AskMilford-style agents on non-entitled data.

## What "done" looks like
- A **self-contained interactive portal** organised by the five roles, each with ≥3
  decision-useful insights, every figure computed transparently (click to see the maths),
  every widget carrying provenance (source + timestamp) and a plain-language explainer of
  intent, what "good" looks like, and the alpha/trade angle.
- A **live-ready extraction + performance-measurement** pipeline that respects the 250/day
  cap, plus an honest **upgrade path** showing what Premium (LSE) / Ultimate (full APAC
  book + transcripts + 13F) would unlock.

## Explicitly out of scope
- Book-of-record data (positions, NAV, performance, compliance) — that is IBOR/AlphaCert.
- Anything client-facing or decision-of-record — an **FMA regulatory boundary** applies.
- Milford's actual APAC holdings on the free tier — not available until Ultimate.
- Investment advice. This is analytical tooling, not a recommendation engine.
