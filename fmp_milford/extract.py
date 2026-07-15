"""
Live extraction: pull free-tier FMP endpoints for the universe and map them into the
SAME normalized record shape that mockdata.build_demo_dataset produces, so transform/
insights/report are identical for demo and live.

Field mapping is defensive (multiple candidate keys) because FMP field names differ
slightly across stable/legacy responses. On the first live run, eyeball one record in
data/raw/ and tighten any mapping that came through empty.
"""

from __future__ import annotations
from datetime import datetime, timezone

from .config import UNIVERSE, all_tickers, COMPANY_NAMES, ticker_to_sector, BENCHMARK


def _g(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and d.get(k) not in (None, ""):
            return d[k]
    return default


def _year(row):
    return int(_g(row, "calendarYear", "fiscalYear", default=str(_g(row, "date", default="0"))[:4]) or 0)


def _weekly(prices):
    """Downsample daily EOD (newest-first from FMP) to weekly close, oldest-first."""
    rows = prices if isinstance(prices, list) else prices.get("historical", [])
    rows = sorted(rows, key=lambda r: _g(r, "date", default=""))
    closes = [float(_g(r, "adjClose", "close", default=0) or 0) for r in rows]
    weekly = closes[::5] if len(closes) > 60 else closes
    start = _g(rows[0], "date", default="2020-01-01") if rows else "2020-01-01"
    return {"start": start, "freq": "W", "closes": [round(c, 2) for c in weekly if c]}


def extract_company(client, ticker):
    prof, _ = client.get("profile", symbol=ticker)
    inc, _ = client.get("income_statement", symbol=ticker)
    bal, _ = client.get("balance_sheet", symbol=ticker)
    cff, _ = client.get("cash_flow", symbol=ticker)
    div, _ = client.get("dividends", symbol=ticker)
    prc, _ = client.get("prices_eod", symbol=ticker)
    scr, _ = client.get("financial_scores", symbol=ticker)

    p = (prof or [{}])[0] if isinstance(prof, list) else (prof or {})
    inc = inc or []; bal = bal or []; cff = cff or []
    # align by year, newest first -> keep up to 5, then order ascending
    by_year_i = {_year(r): r for r in inc}
    by_year_b = {_year(r): r for r in bal}
    by_year_c = {_year(r): r for r in cff}
    years = sorted(set(by_year_i) & set(by_year_b) & set(by_year_c))[-5:]
    if not years:
        years = sorted(by_year_i)[-5:] or [datetime.now().year]

    income, balance, cash_flow = {}, {}, {}
    for y in years:
        I = by_year_i.get(y, {}); B = by_year_b.get(y, {}); C = by_year_c.get(y, {})
        income[y] = dict(
            revenue=float(_g(I, "revenue", default=0) or 0),
            gross_profit=float(_g(I, "grossProfit", default=0) or 0),
            operating_income=float(_g(I, "operatingIncome", default=0) or 0),
            ebitda=float(_g(I, "ebitda", "EBITDA", default=0) or 0),
            dep_amort=float(_g(I, "depreciationAndAmortization", default=0) or 0),
            interest_expense=abs(float(_g(I, "interestExpense", default=0) or 0)),
            net_income=float(_g(I, "netIncome", default=0) or 0),
            shares=float(_g(I, "weightedAverageShsOutDil", "weightedAverageShsOut", default=0) or 0),
            eps=float(_g(I, "epsdiluted", "eps", default=0) or 0),
        )
        balance[y] = dict(
            total_assets=float(_g(B, "totalAssets", default=0) or 0),
            current_assets=float(_g(B, "totalCurrentAssets", default=0) or 0),
            cash=float(_g(B, "cashAndCashEquivalents", "cashAndShortTermInvestments", default=0) or 0),
            inventory=float(_g(B, "inventory", default=0) or 0),
            receivables=float(_g(B, "netReceivables", default=0) or 0),
            total_liabilities=float(_g(B, "totalLiabilities", default=0) or 0),
            current_liabilities=float(_g(B, "totalCurrentLiabilities", default=0) or 0),
            total_debt=float(_g(B, "totalDebt", default=0) or 0),
            total_equity=float(_g(B, "totalStockholdersEquity", "totalEquity", default=0) or 0),
            retained_earnings=float(_g(B, "retainedEarnings", default=0) or 0),
            payables=float(_g(B, "accountPayables", default=0) or 0),
        )
        cash_flow[y] = dict(
            operating_cf=float(_g(C, "operatingCashFlow", "netCashProvidedByOperatingActivities", default=0) or 0),
            capex=abs(float(_g(C, "capitalExpenditure", default=0) or 0)),
            free_cash_flow=float(_g(C, "freeCashFlow", default=0) or 0),
            dividends_paid=float(_g(C, "dividendsPaid", "commonDividendsPaid", default=0) or 0),
            buybacks=float(_g(C, "commonStockRepurchased", default=0) or 0),
        )

    # dividends -> ttm dps and yield
    dps = 0.0
    dlist = div.get("historical", div) if isinstance(div, dict) else (div or [])
    if isinstance(dlist, list) and dlist:
        recent = sorted(dlist, key=lambda r: _g(r, "date", default=""))[-4:]
        dps = sum(float(_g(r, "adjDividend", "dividend", default=0) or 0) for r in recent)
    price = float(_g(p, "price", default=0) or 0)
    dyield = (dps / price * 100) if price else 0.0

    sc = (scr or [{}])[0] if isinstance(scr, list) else (scr or {})
    return dict(
        ticker=ticker, name=_g(p, "companyName", default=COMPANY_NAMES.get(ticker, ticker)),
        sector=ticker_to_sector().get(ticker, _g(p, "sector", default="")),
        industry=_g(p, "industry", default=""), currency=_g(p, "currency", default="USD"),
        price=price, shares_out=float(_g(p, "sharesOutstanding", default=0) or 0),
        market_cap=float(_g(p, "marketCap", "mktCap", default=0) or 0), beta=float(_g(p, "beta", default=1) or 1),
        logo=_g(p, "image"),
        years=years, income=income, balance=balance, cash_flow=cash_flow,
        dividend_per_share=round(dps, 3), dividend_yield=round(dyield, 2),
        prices=_weekly(prc or []),
        fmp_scores=dict(altman_z=_g(sc, "altmanZScore"), piotroski=_g(sc, "piotroskiScore")),
        source="FMP /stable/", retrieved=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )


def extract_live(client, tickers=None) -> dict:
    tickers = tickers or all_tickers()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    companies = {}
    for t in tickers:
        try:
            companies[t] = extract_company(client, t)
        except Exception as e:
            print(f"  ! {t}: extraction error ({e})")
    # benchmark prices
    bpr, _ = client.get("prices_eod", symbol=BENCHMARK)
    benchmark = dict(ticker=BENCHMARK, name="SPDR S&P 500 ETF", prices=_weekly(bpr or []),
                     source="FMP /stable/", retrieved=ts)
    return {"companies": companies, "benchmark": benchmark, "mode": "LIVE", "retrieved": ts}
