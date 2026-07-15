"""
Realistic synthetic dataset for DEMO mode.

Why this exists: this session's environment blocks egress to financialmodelingprep.com,
so live extraction cannot run here. To make the interactive report fully demonstrable,
we generate a *plausible* dataset (seeded, reproducible) with sector-appropriate
magnitudes and cross-sectional variation (cheap vs dear, quality vs junk, profitable
vs loss-making, capital-heavy vs asset-light).

EVERYTHING here is clearly labelled `source="DEMO (synthetic)"` and every widget in the
report shows that provenance. Run `python run.py --live` on a network-open machine with
FMP_API_KEY set to replace this with real FMP data (identical downstream code path).
"""

from __future__ import annotations
import math
import random
from datetime import date, timedelta

from .config import UNIVERSE, COMPANY_NAMES, ticker_to_sector, BENCHMARK

# Per-ticker anchors (approximate, order-of-magnitude realistic — DEMO only):
#  rev   = latest FY revenue ($M)
#  nm    = net margin (%)
#  g     = revenue growth (% p.a.)
#  px    = share price ($)
#  beta  = equity beta
#  dy    = dividend yield (%)
#  roic  = target ROIC (%) (shapes capital base)
#  mult  = P/E if profitable else P/S (valuation multiple)
#  capx  = capex / revenue (%)   (capital intensity -> FCF conversion)
#  lev   = total debt / total assets (%)
ANCHORS = {
    # Utilities & AI Power
    "NEE":  dict(rev=28000, nm=22, g=8,  px=75,  beta=0.55, dy=2.8, roic=6,  mult=21, capx=34, lev=42),
    "SO":   dict(rev=26000, nm=15, g=4,  px=82,  beta=0.50, dy=3.6, roic=5,  mult=20, capx=30, lev=45),
    "DUK":  dict(rev=29000, nm=14, g=3,  px=105, beta=0.50, dy=4.0, roic=5,  mult=18, capx=32, lev=46),
    "D":    dict(rev=14000, nm=12, g=2,  px=52,  beta=0.55, dy=4.8, roic=4,  mult=17, capx=36, lev=48),
    "AEP":  dict(rev=19000, nm=13, g=4,  px=92,  beta=0.50, dy=3.8, roic=5,  mult=18, capx=33, lev=45),
    "EXC":  dict(rev=22000, nm=10, g=5,  px=38,  beta=0.55, dy=3.7, roic=4,  mult=17, capx=31, lev=44),
    "CEG":  dict(rev=24000, nm=8,  g=12, px=175, beta=0.80, dy=1.0, roic=9,  mult=28, capx=18, lev=30),
    "VST":  dict(rev=18000, nm=7,  g=20, px=95,  beta=0.95, dy=0.7, roic=11, mult=22, capx=14, lev=38),
    # Healthcare
    "JNJ":  dict(rev=88000, nm=20, g=4,  px=155, beta=0.55, dy=3.1, roic=14, mult=15, capx=5,  lev=20),
    "UNH":  dict(rev=372000,nm=6,  g=12, px=500, beta=0.60, dy=1.5, roic=13, mult=19, capx=2,  lev=25),
    "LLY":  dict(rev=40000, nm=22, g=25, px=780, beta=0.40, dy=0.7, roic=22, mult=45, capx=9,  lev=28),
    "ABBV": dict(rev=55000, nm=12, g=3,  px=165, beta=0.60, dy=3.5, roic=15, mult=16, capx=4,  lev=55),
    "MRK":  dict(rev=60000, nm=25, g=6,  px=105, beta=0.40, dy=2.9, roic=18, mult=14, capx=8,  lev=30),
    "PFE":  dict(rev=58000, nm=10, g=-8, px=28,  beta=0.60, dy=6.0, roic=7,  mult=12, capx=6,  lev=40),
    "TMO":  dict(rev=43000, nm=15, g=7,  px=560, beta=0.80, dy=0.3, roic=10, mult=25, capx=5,  lev=35),
    "ABT":  dict(rev=40000, nm=14, g=5,  px=110, beta=0.70, dy=2.0, roic=11, mult=22, capx=6,  lev=28),
    # AI & Semiconductor Supply Chain
    "NVDA": dict(rev=60000, nm=49, g=90, px=120, beta=1.70, dy=0.03,roic=55, mult=45, capx=3,  lev=10),
    "AVGO": dict(rev=50000, nm=20, g=30, px=165, beta=1.10, dy=1.6, roic=14, mult=30, capx=2,  lev=40),
    "TSM":  dict(rev=70000, nm=38, g=20, px=175, beta=1.20, dy=1.2, roic=25, mult=24, capx=40, lev=22),
    "ASML": dict(rev=28000, nm=27, g=15, px=950, beta=1.30, dy=0.9, roic=30, mult=35, capx=6,  lev=18),
    "AMD":  dict(rev=23000, nm=6,  g=20, px=160, beta=1.70, dy=0.0, roic=5,  mult=40, capx=3,  lev=8),
    "MU":   dict(rev=25000, nm=12, g=60, px=105, beta=1.40, dy=0.4, roic=8,  mult=18, capx=32, lev=20),
    "MRVL": dict(rev=5500,  nm=5,  g=15, px=70,  beta=1.50, dy=0.3, roic=4,  mult=9,  capx=4,  lev=22),  # mult=P/S (thin margin)
    "SMCI": dict(rev=15000, nm=8,  g=100,px=45,  beta=1.90, dy=0.0, roic=20, mult=22, capx=3,  lev=15),
    # Robotics & Physical AI
    "TSLA": dict(rev=97000, nm=12, g=15, px=250, beta=2.00, dy=0.0, roic=12, mult=60, capx=9,  lev=10),
    "ISRG": dict(rev=8000,  nm=27, g=15, px=480, beta=1.40, dy=0.0, roic=16, mult=55, capx=8,  lev=3),
    "ABB":  dict(rev=32000, nm=12, g=6,  px=52,  beta=1.10, dy=2.0, roic=13, mult=22, capx=3,  lev=28),
    "ROK":  dict(rev=9000,  nm=14, g=8,  px=270, beta=1.20, dy=1.9, roic=18, mult=24, capx=3,  lev=35),
    "TER":  dict(rev=2700,  nm=18, g=5,  px=130, beta=1.50, dy=0.4, roic=15, mult=28, capx=4,  lev=10),
    "SYM":  dict(rev=1800,  nm=-3, g=55, px=30,  beta=2.20, dy=0.0, roic=-5, mult=6,  capx=5,  lev=12),  # mult=P/S (loss-making)
    "PATH": dict(rev=1400,  nm=-8, g=20, px=13,  beta=1.60, dy=0.0, roic=-10,mult=5,  capx=2,  lev=5),   # mult=P/S (loss-making)
    "ZBRA": dict(rev=4600,  nm=10, g=3,  px=320, beta=1.40, dy=0.0, roic=11, mult=20, capx=3,  lev=30),
}

INDUSTRY = {
    "Utilities & AI Power": "Regulated & Merchant Electric Utilities",
    "Healthcare": "Pharma, Managed Care & Life Sciences",
    "AI & Semiconductor Supply Chain": "Semiconductors & Semi Equipment",
    "Robotics & Physical AI": "Automation, Robotics & Industrial Tech",
}


def _asset_turnover(sector: str) -> float:
    return {"Utilities & AI Power": 0.32, "Healthcare": 0.62,
            "AI & Semiconductor Supply Chain": 0.70, "Robotics & Physical AI": 0.85}.get(sector, 0.6)


def _gen_company(ticker: str, retrieved: str, market_rets) -> dict:
    a = ANCHORS[ticker]
    sector = ticker_to_sector()[ticker]
    rng = random.Random(hash(ticker) & 0xFFFFFFFF)
    years = [2020, 2021, 2022, 2023, 2024]
    g = a["g"] / 100.0
    nm = a["nm"] / 100.0

    rev_latest = a["rev"]
    # Revenue history: grow backwards from latest with mild noise
    revenue = {}
    r = rev_latest
    for y in reversed(years):
        revenue[y] = round(r, 1)
        r = r / (1 + g) * (1 + rng.uniform(-0.03, 0.03))

    at = _asset_turnover(sector)
    income, balance, cash_flow = {}, {}, {}
    profitable = nm > 0
    shares = None

    for y in years:
        rev = revenue[y]
        ni = rev * nm * (1 + rng.uniform(-0.05, 0.05))
        da = rev * (0.11 if sector == "Utilities & AI Power" else 0.06 if sector == "AI & Semiconductor Supply Chain" else 0.05)
        op_income = ni / 0.72 if profitable else rev * (nm * 1.2)  # approx pretax->op
        ebitda = op_income + da
        gross_profit = rev * (0.55 if sector == "Healthcare" else 0.45 if sector == "AI & Semiconductor Supply Chain" else 0.35)
        interest = rev * (a["lev"] / 100.0) * at * 0.05
        income[y] = dict(revenue=round(rev, 1), gross_profit=round(gross_profit, 1),
                         operating_income=round(op_income, 1), ebitda=round(ebitda, 1),
                         dep_amort=round(da, 1), interest_expense=round(interest, 1),
                         net_income=round(ni, 1))
        assets = rev / at
        equity = assets * (1 - a["lev"] / 100.0 - 0.15)
        debt = assets * (a["lev"] / 100.0)
        cash = assets * 0.08
        curr_assets = assets * 0.28
        curr_liab = assets * 0.20
        inventory = assets * (0.10 if sector in ("AI & Semiconductor Supply Chain", "Robotics & Physical AI") else 0.04)
        receivables = assets * 0.10
        payables = assets * 0.07
        balance[y] = dict(total_assets=round(assets, 1), current_assets=round(curr_assets, 1),
                          cash=round(cash, 1), inventory=round(inventory, 1), receivables=round(receivables, 1),
                          total_liabilities=round(assets - equity, 1), current_liabilities=round(curr_liab, 1),
                          total_debt=round(debt, 1), total_equity=round(equity, 1),
                          retained_earnings=round(equity * 0.6, 1), payables=round(payables, 1))
        ocf = ni + da + rng.uniform(-0.03, 0.03) * rev
        capex = rev * a["capx"] / 100.0
        fcf = ocf - capex
        cash_flow[y] = dict(operating_cf=round(ocf, 1), capex=round(capex, 1),
                            free_cash_flow=round(fcf, 1),
                            dividends_paid=round(-rev * a["dy"] / 100.0 * 0.5, 1),
                            buybacks=round(-rev * 0.02, 1) if profitable else 0.0)

    # Market cap & shares from valuation multiple
    ni_latest = income[years[-1]]["net_income"]
    if profitable and a["mult"] > 0 and ticker not in ("MRVL", "SYM", "PATH"):
        market_cap = ni_latest * a["mult"]
    else:  # loss-making or thin-margin: multiple is P/S
        market_cap = rev_latest * a["mult"]
    shares = market_cap / a["px"]
    for y in years:
        income[y]["shares"] = round(shares, 1)
        income[y]["eps"] = round(income[y]["net_income"] / shares, 3)

    dps = a["dy"] / 100.0 * a["px"]

    prices = _gen_prices(a, rng, market_rets)

    return dict(
        ticker=ticker, name=COMPANY_NAMES.get(ticker, ticker), sector=sector,
        industry=INDUSTRY[sector], currency="USD",
        price=a["px"], shares_out=round(shares, 1), market_cap=round(market_cap, 1), beta=a["beta"],
        years=years, income=income, balance=balance, cash_flow=cash_flow,
        dividend_per_share=round(dps, 3), dividend_yield=a["dy"],
        prices=prices,
        fmp_scores=dict(altman_z=None, piotroski=None),
        source="DEMO (synthetic)", retrieved=retrieved,
    )


def _market_returns(weeks, rng):
    mu_w, sig_w = 0.09 / 52.0, 0.15 / math.sqrt(52.0)
    return [rng.gauss(mu_w, sig_w) for _ in range(weeks)]


def _series_from_returns(returns, end_price):
    level, closes = 1.0, []
    for r in returns:
        level *= (1 + r)
        closes.append(level)
    scale = end_price / closes[-1]
    return [round(c * scale, 2) for c in closes]


def _gen_prices(a: dict, rng: random.Random, market_rets):
    """Weekly closes via a one-factor model: r = alpha + beta*market + idiosyncratic.
    Makes realised beta vs the benchmark ~ the anchor beta and gives structured
    cross-correlations (high-beta names co-move; utilities diversify)."""
    beta = a["beta"]
    alpha_w = (0.02 + a["g"] / 100.0 * 0.15) / 52.0
    idio_sig = (0.10 + a["beta"] * 0.06) / math.sqrt(52.0)
    rets = [alpha_w + beta * mr + rng.gauss(0.0, idio_sig) for mr in market_rets]
    closes = _series_from_returns(rets, a["px"])
    return {"start": date(2020, 1, 3).isoformat(), "freq": "W", "closes": closes}


def build_demo_dataset(retrieved: str) -> dict:
    weeks = 5 * 52
    mkt = _market_returns(weeks, random.Random(42))
    companies = {t: _gen_company(t, retrieved, mkt) for t in ANCHORS}
    bench_closes = _series_from_returns(mkt, 540.0)
    benchmark = dict(ticker=BENCHMARK, name="SPDR S&P 500 ETF",
                     prices={"start": date(2020, 1, 3).isoformat(), "freq": "W", "closes": bench_closes},
                     source="DEMO (synthetic)", retrieved=retrieved)
    return {"companies": companies, "benchmark": benchmark, "mode": "DEMO", "retrieved": retrieved}
