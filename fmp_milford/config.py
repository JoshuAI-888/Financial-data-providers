"""
Central configuration: the analysis universe, FMP endpoint catalogue (free tier),
and runtime settings.

FREE-TIER REALITY (verified 2026-07):
  - FMP Free/Basic = US-listed securities ONLY, EOD prices, ~5yr annual statements,
    250 API calls/day, 500MB/30d bandwidth.
  - No NZX/ASX/LSE/HKEX/KRX/TWSE coverage at this tier. NZ/AU tickers return nothing.
    To cover Milford's actual book you need Premium (LSE) or Ultimate (ASX/NZX/APAC).
  - The UNIVERSE below is therefore US-listed comparables grouped into the four
    themes requested. Add ASX/NZX tickers to any list once you upgrade — the code
    path is identical; only the tier gate changes.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Analysis universe: 4 themes x 8 US-listed names = 32
# (NZ/AU unavailable on FMP free tier -> US comparables used, per user's rule.)
# ---------------------------------------------------------------------------
UNIVERSE: dict[str, list[str]] = {
    "Utilities & AI Power": ["NEE", "SO", "DUK", "D", "AEP", "EXC", "CEG", "VST"],
    "Healthcare": ["JNJ", "UNH", "LLY", "ABBV", "MRK", "PFE", "TMO", "ABT"],
    "AI & Semiconductor Supply Chain": ["NVDA", "AVGO", "TSM", "ASML", "AMD", "MU", "MRVL", "SMCI"],
    "Robotics & Physical AI": ["TSLA", "ISRG", "ABB", "ROK", "TER", "SYM", "PATH", "ZBRA"],
}

# Human-readable names (used when the profile endpoint isn't populated, e.g. demo mode)
COMPANY_NAMES: dict[str, str] = {
    "NEE": "NextEra Energy", "SO": "Southern Company", "DUK": "Duke Energy",
    "D": "Dominion Energy", "AEP": "American Electric Power", "EXC": "Exelon",
    "CEG": "Constellation Energy", "VST": "Vistra",
    "JNJ": "Johnson & Johnson", "UNH": "UnitedHealth Group", "LLY": "Eli Lilly",
    "ABBV": "AbbVie", "MRK": "Merck & Co", "PFE": "Pfizer",
    "TMO": "Thermo Fisher Scientific", "ABT": "Abbott Laboratories",
    "NVDA": "NVIDIA", "AVGO": "Broadcom", "TSM": "Taiwan Semiconductor (ADR)",
    "ASML": "ASML Holding (ADR)", "AMD": "Advanced Micro Devices", "MU": "Micron Technology",
    "MRVL": "Marvell Technology", "SMCI": "Super Micro Computer",
    "TSLA": "Tesla", "ISRG": "Intuitive Surgical", "ABB": "ABB Ltd (ADR)",
    "ROK": "Rockwell Automation", "TER": "Teradyne", "SYM": "Symbotic",
    "PATH": "UiPath", "ZBRA": "Zebra Technologies",
}

BENCHMARK = "SPY"  # risk analytics reference

def ticker_to_sector() -> dict[str, str]:
    out = {}
    for sector, tickers in UNIVERSE.items():
        for t in tickers:
            out[t] = sector
    return out

def all_tickers() -> list[str]:
    return [t for tickers in UNIVERSE.values() for t in tickers]

# ---------------------------------------------------------------------------
# FMP stable-API endpoint catalogue (free-tier relevant).
# `calls` = number of API calls this endpoint costs per company.
# `free` = expected availability on the Free/Basic plan (verify live via perf probe).
# ---------------------------------------------------------------------------
FMP_BASE = "https://financialmodelingprep.com/stable"

# Per-company endpoints (symbol-scoped)
ENDPOINTS: dict[str, dict] = {
    "profile":            {"path": "profile",                    "params": {},                                   "free": True,  "feeds": "reference, logo, price, mktcap, beta, sector"},
    "income_statement":   {"path": "income-statement",           "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "revenue, margins, EPS, EBITDA"},
    "balance_sheet":      {"path": "balance-sheet-statement",    "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "assets, equity, debt, working capital"},
    "cash_flow":          {"path": "cash-flow-statement",        "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "OCF, capex, FCF, dividends paid, buybacks"},
    "ratios":             {"path": "ratios",                     "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "cross-check ratios"},
    "key_metrics":        {"path": "key-metrics",                "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "ROIC, per-share, EV metrics"},
    "financial_growth":   {"path": "financial-growth",           "params": {"period": "annual", "limit": 5},     "free": True,  "feeds": "growth rates"},
    "financial_scores":   {"path": "financial-scores",           "params": {},                                   "free": True,  "feeds": "Altman Z, Piotroski (cross-check)"},
    "dividends":          {"path": "dividends",                  "params": {},                                   "free": True,  "feeds": "dividend history / yield"},
    "prices_eod":         {"path": "historical-price-eod/full",  "params": {},                                   "free": True,  "feeds": "EOD OHLCV -> returns/vol/beta/drawdown"},
    # Verify-at-runtime (often gated above free):
    "analyst_estimates":  {"path": "analyst-estimates",          "params": {"period": "annual", "limit": 5},     "free": False, "feeds": "forward estimates (likely Premium+)"},
    "price_target":       {"path": "price-target-summary",       "params": {},                                   "free": False, "feeds": "price targets (likely Premium+)"},
    "grades":             {"path": "grades",                     "params": {},                                   "free": False, "feeds": "analyst ratings (likely Premium+)"},
}

# Endpoints used for the per-company data pull (order matters for budget accounting)
PULL_ENDPOINTS = [
    "profile", "income_statement", "balance_sheet", "cash_flow",
    "key_metrics", "financial_growth", "financial_scores", "dividends", "prices_eod",
]

# ---------------------------------------------------------------------------
# Runtime settings
# ---------------------------------------------------------------------------
SETTINGS = {
    "daily_call_budget": 250,        # Free tier hard cap
    "calls_per_minute": 60,          # be polite; free tier throttles
    "cache_ttl_hours": 24,           # served-from-cache within this window
    "cache_dir": "data/raw",
    "budget_file": "data/call_budget.json",
    "output_html": "outputs/milford_fmp_report.html",
    "price_years": 5,                # history depth on free tier
    "api_key_env": "FMP_API_KEY",
}

# Theme colours for logos / charts (accessible, works light+dark)
SECTOR_COLORS = {
    "Utilities & AI Power": "#2E86AB",
    "Healthcare": "#1B998B",
    "AI & Semiconductor Supply Chain": "#8E5EA2",
    "Robotics & Physical AI": "#E8871E",
}
