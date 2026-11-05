# NeoXam

## 1. Snapshot
- **Category:** Investment data management / xBOR platform (IBOR, ABOR, CBOR, PBOR) with adjacent performance, reporting, reconciliation and PMS modules.
- **Owner / parent:** Private, France-headquartered. Founded 2014 by BlackFin Capital Partners + CEO Serge Delpla from SunGard's GP3/Decalog assets; Cathay Capital/Bpifrance were later shareholders; Eurazeo agreed in Nov 2022 to invest up to €100m and become majority shareholder. Serial acquirer (SmartCo, Nexfi, EZOPS in 2024, and others). ~652 employees, ~$122m revenue reported for 2026, ~10,000 customers group-wide across NeoXam's full software estate (data mgmt, accounting, PMS) — not all institutional-AM IDP buyers specifically.
- **HQ / footprint:** Paris HQ; 20 offices worldwide, clients in 30+ countries. APAC: Sydney office since 2023, Melbourne office added subsequently; ~20 APAC clients including Platinum Asset Management (Australia) and Lion Global Investors (Singapore).
- **Initial fit:** Moderate–High
- **Positioning:** Broad, modular xBOR + data management suite with a genuine APAC (ANZ) delivery footprint and named references, but AI/agent story is explicitly early-adopter/preview, not production, and no public evidence of native Databricks/open-lakehouse integration.
- **Recent developments:** As of 3 Nov 2026 NeoXam Agents (launched 24 Jun 2026) remain preview: a Sept 2026 GA target was reported but no GA release was found, and production is still guided to early 2027; no MCP, Databricks, ownership change or new direct ANZ client.

## 2. Investment-domain mastering
DataHub is billed as a one-stop master reference/security-master store covering instrument master data (ISIN, CUSIP, SEDOL, tickers) with identifier concordance across vendor schemes. It builds a per-domain "golden copy" via a stated Silver-to-Gold lifecycle: field-level ranking, configurable survivorship rules and multi-golden-copy support, merging multi-vendor feeds and filling gaps automatically. Public+private and market/risk/private-asset data are described as unified within Investment Data Solution (IDS). Point-in-time/bitemporal history depth and business-user model extensibility are asserted in marketing copy (industry-standard model, modular MDM) but no independently documented technical spec of bitemporal depth or no-code extension mechanics was found — native/configurable balance not established beyond vendor claims.

## 3. Databricks & open architecture
DataHub is described as cloud-native (AWS, Azure, OpenShift) with "Snowflake-native integration," REST/SOAP APIs, direct DB connectors and custom adapters. No public evidence of a native Delta Sharing/OpenSharing integration, Unity Catalog compatibility, or a Databricks partner listing was found in this research — this is a **coverage gap**, not a confirmed capability or a confirmed absence. Egress/duplication posture (replicate-in vs share-in-place) is not established from public sources.

## 4. IBOR & investment modelling
NeoXam markets a dedicated IBOR engine within IDS providing "real-time data on positions, transactions and cash" for front-office/risk use, implying event-driven, intraday capability, alongside ABOR/CBOR/PBOR for accounting, consolidated and performance views. Trade-date vs settlement-date handling, projected-position mechanics and point-in-time reconstruction depth are not detailed in public material beyond the general IBOR framing.

## 5. Data quality & investment operations
DataHub applies "hundreds of automated controls" — presence/format validation, outlier detection, cross-source comparisons — feeding a golden-copy pipeline. A separate reconciliation product (Aro) offers no-code match-rule configuration (tolerances on account/ISIN/trade date/quantity/amount), exception logging with full context, and routing/escalation by asset, account or urgency. Four-eyes/override controls specific to DataHub's exception workflow are not independently confirmed. Managed-service option exists (NeoXam Managed Services) but SLA specifics (e.g., a 07:00 validated-portfolio commitment) are not established from public sources.

## 6. Public/private total portfolio
NeoXam has actively invested in private markets: "Private Market Data" proposition targeting the GP/LP data gap, and AI-powered Intelligent Document Processing (IDP) launched to automate ingestion/classification/extraction/validation/routing of unstructured private-markets documents (broker statements, trade confirms, PDFs) with figures passed to downstream systems. This is a genuine, differentiated capability set for the buyer's PE extension, though maturity/GA status of the document-extraction tool and named production references are not established from public sources.

## 7. AI & agent readiness — ROADMAP/PREVIEW
NeoXam Agents launched 24 June 2026 as three components: a platform to build/run/supervise agents, a family of specialised agents in **preview**, and an **early-adopter programme** opening to a select group of firms in Q3 2026, with test deployment/measurement through Q4 2026 and a stated **path to production only in early 2027**. Agent categories: answer questions, take action, help configure the software; a reporting agent and knowledge agents are cited as early examples. No public evidence of MCP support, per-agent identity/entitlements, provenance/citation mechanics, or write-approval controls — this entire domain is pre-GA by NeoXam's own announcement and must be scored at roadmap/preview ceiling.

**Nov 2026 update:** no GA release of NeoXam Agents was found as of 3 Nov 2026. A-Team Insight and FTF News (Jun–Jul 2026) reported a September 2026 GA target for the specialised agents, while NeoXam's launch page and Asset Servicing Times cite only a path to production in early 2027. NeoXam says firms can choose and later switch the underlying AI model (vendor claim on a preview product). No MCP reference found. The private-markets document-processing module was announced as available from Dec 2025 with no named customer.

## 8. Time-to-value, implementation, managed services & APAC support
Modular, "non-intrusive" approach claimed for front-to-back deployment; Bloomberg and other major vendor connectivity implied via DataHub's ingestion layer but a dedicated pre-built-connector count is not established from public sources. APAC support is a genuine differentiator: Sydney (2023) and Melbourne offices, ~20 APAC clients, named Australian reference (Platinum Asset Management, data management + Impress reporting) and Singapore reference (Lion Global Investors). 30–60 day PoV and 3–6 month foundation feasibility are not documented publicly for this buyer's scope.

**Nov 2026 update:** UniSuper (A$149bn) uses BNP Paribas' Data PRISM360, built on NeoXam IDS (Jun 2025) — an indirect, service-provider-delivered ANZ deployment. No new direct ANZ client beyond Platinum Asset Management.

**5 Nov 2026 update:** the public NeoXam–Apex Group relationship found is a renewed partnership following Apex's acquisition of Maitland (South Africa, May 2024); no public evidence of a live Apex integration in Australia or New Zealand, or of Charles River IMS production experience, was found. An external consultant's Sep 2026 shortlisting reports a demo of an Apex Australia integration; treat as demo evidence pending a named reference. Hosting for Asian clients is AWS Singapore and reconciliation managed services run from Chennai (vendor pages).

## 9. Commercials, TCO, exit & vendor viability
No public pricing, platform-vs-content separation, egress/API charge schedule, or exit/data-portability terms were found — normal for enterprise software but a genuine information gap requiring RFP disclosure. Vendor viability: well-capitalised via Eurazeo's up-to-€100m majority investment (agreed Nov 2022), strong APAC investment trajectory, but has changed PE ownership multiple times since 2014 (BlackFin → Cathay/Bpifrance → Eurazeo), and continues an active roll-up strategy (SmartCo, Nexfi) that adds integration/roadmap-coherence risk.

## 10. Evidence, maturity & provisional scores

**Hard-gate read (G01–G22):**
- G01 (native equities/ETF/govvies/credit/FX/PE): PARTIAL — broad asset coverage claimed, PE via separate private-markets line
- G02 (security+entity+price mastering): PASS — documented golden-copy/survivorship pipeline
- G03 (intraday position/price, near-real-time txns): PARTIAL — IBOR "real-time" claimed, depth undocumented
- G04 (5yr history + point-in-time): UNKNOWN — not established from public sources
- G05 (IDP-as-master, Databricks consumes): UNKNOWN — no Databricks evidence found
- G06 (open/native Databricks integration): FAIL — only Snowflake-native cited, no Databricks evidence
- G07 (bidirectional API): PARTIAL — REST/SOAP APIs cited, write-back specifics undocumented
- G08 (business users extend model, no vendor code): UNKNOWN — asserted, not evidenced
- G09 (buyer can use own LLMs): UNKNOWN — Agents platform model-independence undocumented
- G10 (permission-aware agent/MCP interface): FAIL — preview-stage, no MCP evidence, path to production 2027
- G11 (field-level provenance/lineage/override/audit): PARTIAL — cross-source/exception logging documented, audit depth unclear
- G12 (full export on exit): UNKNOWN — not established from public sources
- G13 (governable AI/LLM data-use rights): UNKNOWN — not established from public sources
- G14 (credible APAC + ANZ support): PASS — Sydney/Melbourne offices, named ANZ reference
- G15 (30–60 day PoV): UNKNOWN — not established from public sources
- G16 (3–6 month production foundation): UNKNOWN — not established from public sources
- G17 (07:00 validated-portfolio SLA): UNKNOWN — not established from public sources
- G18 (internal ops retains exception/override control): PARTIAL — Aro exception workflow documented
- G19 (institutional security architecture): UNKNOWN — not established from public sources
- G20 (5-yr TCO transparency): UNKNOWN — no public pricing
- G21 (critical function not roadmap-dependent): PASS — core mastering/xBOR is shipping, not roadmap
- G22 (controlled write-back to downstream): PARTIAL — API-based extraction/update cited, controls undocumented


**Overall read:** NeoXam leads on APAC/ANZ physical presence and named regional references, and on private-markets document automation — a genuine differentiator for this buyer's PE extension. It lags badly on open-architecture/Databricks evidence (Snowflake is the only named lakehouse integration) and on AI/agent readiness, where NeoXam's own roadmap places production availability in 2027, not now. Biggest risk: buying into an early-adopter AI programme and repeated PE ownership churn while the Databricks-fit story remains unproven.

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- https://www.neoxam.com/neoxam-australia-office-expansion/ — NeoXam Australia office expansion [vendor · Vendor marketing · 2026-08-14 · search-only]
- https://www.neoxam.com/datahub/investment-data-solution/ — DataHub IDS product overview (accessed 2026-08-14)
- https://www.neoxam.com/neoxam-agents-investment-operations/ — NeoXam Agents launch, early-adopter programme (accessed 2026-08-14)
- https://www.neoxam.com/datahub/ibor-vs-abor-vs-pbor-data-integration/ — xBOR framework explainer (accessed 2026-08-14)
- https://www.neoxam.com/datahub/ibor/ — IBOR product page (accessed 2026-08-14)
- https://www.neoxam.com/datahub/golden-copy-management-for-trusted-financial-data/ — golden-copy/survivorship mechanics (accessed 2026-08-14)
- https://www.neoxam.com/mdm/ — master data management, cloud/API stack claims (accessed 2026-08-14)
- https://www.neoxam.com/aro/automated-reconciliation-exception-management-financial-data/ — Aro reconciliation/exception product (accessed 2026-08-14)
- https://www.neoxam.com/neoxam-ai-intelligent-document-processing-private-markets/ — private-markets document AI (IDP) launch (accessed 2026-08-14)
- https://www.neoxam.com/neoxam-private-market-data/ — private market data proposition (accessed 2026-08-14)
- https://www.neoxam.com/neoxam-australia-office-expansion/ — Melbourne office expansion (accessed 2026-08-14)
- https://www.neoxam.com/platinum-asset-management-bolsters-data-management-and-reporting-capabilities-with-neoxam/ — named ANZ reference, Platinum AM (accessed 2026-08-14)
- https://a-teaminsight.com/blog/neoxam-adds-lion-global-investors-to-growing-list-of-apac-clients/ — APAC client count, Lion Global reference (accessed 2026-08-14)
- https://ibsintelligence.com/ibsi-news/neoxam-launches-ai-agent-platform-for-investment-operations/ — Agents launch, early-adopter/path-to-production timeline (accessed 2026-08-14)
- https://www.ftfnews.com/neoxam-embraces-agentic-a-i/ — independent coverage of Agents preview status (accessed 2026-08-14)
- https://www.eurazeo.com/en/newsroom/press-releases/eurazeo-signs-agreement-invest-neoxam — Eurazeo majority investment (accessed 2026-08-14)
- https://www.blackfincp.com/news/neoxam-a-leading-provider-of-asset-management-software-solutions-backed-by-blackfin-capital-partners-acquires-smartco — ownership/M&A history (accessed 2026-08-14)
- https://pitchbook.com/profiles/company/61537-15 — employee/revenue/customer scale figures (accessed 2026-08-14)
- https://a-teaminsight.com/briefs/neoxam-agent-attaches-automative-functionality-to-platform/?brand=dmi — NeoXam Agent attaches automation functionality to platform (A-Team Insight; accessed 2026-11-03) [independent · News · 2026-06-24 · opened]
- https://www.assetservicingtimes.com/assetservicesnews/technologyarticle.php?article_id=18081 — NeoXam Agents unveiled (Asset Servicing Times; accessed 2026-11-03) [independent · News · 2026-06-24 · opened]
- https://www.neoxam.com/aro/ — NeoXam Aro reconciliation (NeoXam; accessed 2026-11-03) [vendor · Vendor marketing · 2026-03 · opened]
- https://www.neoxam.com/aro/agentic-ai-reconciliation — Agentic AI reconciliation (Aro) (NeoXam; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://www.neoxam.com/eurazeo-invests-e100m-in-neoxam/ — Eurazeo invests EUR100m in NeoXam (NeoXam; accessed 2026-11-03) [vendor · Vendor marketing · 2022-11-23 · opened]
- https://www.neoxam.com/clients — NeoXam clients (NeoXam; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://ffnews.com/newsarticle/tradetech/bnp-paribas-enhances-unisupers-post-trade-data-management-through-its-data-prism360-solution-supported-by-neoxam — BNP Paribas enhances UniSuper's post-trade data management ... supported by NeoXam (FF News; accessed 2026-11-03) [independent · News · 2025-06-11 · opened]
- https://www.finextra.com/pressarticle/97490/neoxam-names-daniel-joseph-as-country-head-for-australia — NeoXam names Daniel Joseph as country head for Australia (Finextra (press release); accessed 2026-11-03) [vendor · News · undated · search-only]
- https://www.neoxam.com/apex-group-renews-partnership-with-neoxam-following-maitland-acquisition/ — Apex Group renews partnership with NeoXam following Maitland acquisition (NeoXam; accessed 2026-11-05) [vendor · Vendor marketing · 2024-05 · search-only]
- https://www.neoxam.com/managed-services/ — NeoXam managed services (AWS Singapore hosting for Asia) (NeoXam; accessed 2026-11-05) [vendor · Vendor marketing · undated · search-only]
