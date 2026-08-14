# Wind Information

## 1. Snapshot
- **Owner/parent:** Wind Information Co., Ltd. (万得) — Shanghai-headquartered, independent Chinese company (not a subsidiary of an exchange or bank); often described as "the Bloomberg of China."
- **Coverage:** Dominant in mainland China (all listed companies, 170,000+ public/private Chinese bonds, 28,000+ ABS products); extends to overseas markets (US, UK, Germany, Singapore, Japan and others) for IPO/financial/corporate data; serves 70%+ of Qualified Foreign Institutional Investors (QFII) accessing China.
- **Free tier:** No free tier; the Wind Financial Terminal (WFT) is a paid professional terminal (occasionally miscast as "free" — search results reference explainer content specifically debunking this).
- **Pricing model & ranges:** Terminal subscriptions reportedly ranging roughly US$199–US$999/month depending on access tier/data package (individual vs institutional), though pricing is not formally published and is negotiated/quoted directly — comparable in structure to Bloomberg/Reuters terminal licensing but at a materially lower price point.
- Note: also distributed regionally — e.g., listed as an available data product via Japan Exchange Group's (JPX) client portal, indicating cross-border distribution partnerships.

## 2. Coverage
Wind's core strength is exhaustive mainland China market coverage: all listed China A-share companies, extensive fixed income (170,000+ domestic bonds, 1.1 million+ overseas bonds referenced, 28,000+ ABS products), funds, FX, insurance, futures/derivatives, spot commodities, and macroeconomic data, plus financial news. It extends internationally with IPO, financial-statement, corporate-action and operational data for listed and pre-IPO companies in the US, UK, Germany, Singapore, Japan and other major markets — giving it a "China-first, global-adjacent" coverage shape rather than true global parity.

## 3. Datasets
Differentiated holdings center on the depth and timeliness of onshore Chinese data unmatched by most Western vendors: comprehensive China equity/bond/fund/derivatives reference and pricing data, an ABS database, macroeconomic time series (Economic Database/EDB product), and China-specific corporate/ownership/private-company data. This onshore depth — sourced with local regulatory/market access that foreign vendors often cannot replicate — is Wind's primary edge, reinforced by its use by the majority of QFII investors as their gateway into China.

## 4. APIs & technical integration
Wind offers the Wind Financial Terminal (WFT) as its flagship desktop product, plus a "Wind Client API" enabling programmatic, secure access to the underlying database for building data-rich models and integrating with internal or third-party applications (analogous to Bloomberg's BLPAPI / Refinitiv Eikon API model). Mobile apps (WFT Mobile) are also available. No public evidence of REST/JSON self-serve APIs comparable to modern fintech data APIs, nor of an MCP server; integration appears oriented toward terminal-tethered institutional client API access rather than open developer self-service.

## 5. Enabling technology
Public materials do not disclose specific architecture, entity-resolution, or AI/LLM feature details. Wind's technology narrative in available sources is centered on breadth/timeliness of onshore data aggregation and terminal/API delivery rather than published data-science or AI capabilities — differing from the AI-forward marketing common among newer Western data platforms.

## 6. Customer / user feedback
Direct customer-review sources are scarce in English-language indexes (expected for a China-domestic-market product with limited Western retail review presence). University library guides (e.g., HKUST-Guangzhou, Xi'an Jiaotong-Liverpool, SMU) describe WFT as a standard academic/institutional research tool, implying broad adoption in finance education and research in Greater China. The "is it really free?" explainer content appearing in search results suggests recurring user confusion/misconception about WFT's cost model — a mild UX/marketing friction point rather than a substantive quality complaint. No structured pros/cons review base (G2/Capterra-style) was found.

## 7. Edge & positioning
- **Leads on:** Unmatched depth, breadth and timeliness of onshore mainland China market data (equities, bonds, ABS, macro) — the default gateway for QFII and China-focused institutional investors; strong academic/research adoption in Greater China; materially lower price point than Bloomberg/Refinitiv for China-specific coverage.
- **Lags on:** Coverage outside China/Asia is comparatively shallow versus true global vendors; API is terminal-centric/institutional rather than open developer self-serve; almost no public technology/AI feature disclosure; geopolitical/data-access risk for non-Chinese institutions given China's data-security and cross-border data-export regulatory environment (an emerging risk theme in US-China financial-data relations, though no specific Wind-targeted sanction was found in this research).
- **Best-for:** Institutional investors, QFII participants, sell-side research desks and academic researchers who need authoritative, timely onshore China market, macro and fixed-income data as a lower-cost complement or alternative to Bloomberg/Refinitiv for the China market specifically.

## 8. Provenance
- https://www.wind.com.cn/portal/en/Home/index.html — Wind Information corporate homepage (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/Wind_Information — Wind Information company background (Wikipedia, via search index; accessed 2026-08-14)
- https://hkust-gz.libguides.com/c.php?g=962735&p=6992564 — HKUST-GZ library guide describing WFT data coverage (accessed 2026-08-14)
- https://libguides.lib.xjtlu.edu.cn/c.php?g=960084&p=6969491 — XJTLU library guide on Wind Financial Terminal (accessed 2026-08-14)
- https://www.wind.com.cn/mobile/ClientApi/en.html — Wind Client API product page (accessed 2026-08-14)
- https://clientportal.jpx.co.jp/jpxjoinEN/s/product/Wind-WFT — JPX client portal listing for Wind WFT (cross-border distribution) (accessed 2026-08-14)
- https://www.bloomberg.com/profile/company/0564588D:CH — Bloomberg company profile of Wind Information (accessed 2026-08-14)
- Note: WebFetch to wind.com.cn and en.wikipedia.org was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches. Pricing figures (US$199-999/month) and free-tier claims are sourced from secondary explainer articles, not Wind's own published price list, and should be treated as indicative only.
