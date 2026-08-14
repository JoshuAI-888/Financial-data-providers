# Requirement scores — Cluster C: AI, Integration & Governance

**Buyer context:** institutional multi-asset manager; strategic platform is **Databricks**; wants to expose governed investment context to **its own AI models** (not just a vendor chatbot). AI-02 (buyer-own-LLM / model independence) is weighted as strategically important — vendor-locked LLMs are scored materially lower than open model-independence.

**Method:** grounded in the 10 existing fact-sheets + `_v2_updates.md` (2025-26 refresh), then targeted WebSearch to verify AI/MCP 2025-26 status. WebFetch not relied on (egress-blocked); URLs are **format-valid, search-sourced, not machine-fetched**. Paper screen → most cells capped at docs (≤3.0); roadmap/preview items capped ≤1.0. Evidence caps applied: roadmap≤1.0, sales≤2.0, docs≤3.0, demo≤3.5, named-customer≤4.0, sla≤4.5, pov≤5.0.

---

## AI-01 — MCP / tool-protocol interface for agents
- **Leaders (3.0):** FactSet (production-grade MCP server, "first sans intermediary"), FINBOURNE (named MCP+Claude, every LUSID entity exposed), Arcesium (Aquata MCP + Databricks MCP Marketplace launch partner). All docs-capped; recent, mostly unreferenced.
- **GoldenSource 2.5:** Scout has an explicit MCP-based agent-building tool, but two months old (Jun 2026), Bedrock-hosted, no named reference.
- **MSCI 2.0:** Private Assets AI Connector is an AI-connector, not a general MCP, and scoped to private assets.
- **Aladdin / SimCorp 1.5:** embedded/curated agents (Copilot GA; Agent Launchpad rolling GA), not an open tool-protocol for the buyer's external agents.
- **Rimes 1.5:** no native MCP; agent reach only via Databricks Agent Bricks/Delta Sharing.
- **NeoXam 1.0 / Gresham 0.5:** preview/roadmap only (NeoXam's own path-to-production is 2027; Gresham AI is a 2026 commitment).

## AI-02 — Buyer-own-LLM / model independence (weighted)
- **FactSet 3.0 / Arcesium 3.0:** explicit model independence — FactSet plug-and-play across Claude/ChatGPT/Gemini/Copilot/Databricks/Cursor/Perplexity with delivery into the client's *private LLM environment*; Arcesium MCP connects "any enterprise AI tool."
- **MSCI 2.5 / FINBOURNE 2.5:** MSCI connector queryable via Claude/ChatGPT/Copilot (scoped to private assets); FINBOURNE open MCP standard but announced with Claude, broader coverage unconfirmed.
- **Vendor-locked penalised:** GoldenSource 1.5 (Bedrock-hosted, choice unconfirmed), Rimes 1.5 (choice is Databricks-side), NeoXam 1.0 (undocumented), SimCorp 1.0 (Azure OpenAI-centric), **Aladdin 0.5** (GPT-4-based, BlackRock-controlled stack — the clearest vendor-lock), Gresham 0.5 (roadmap).

## AI-03 — Permission-aware / entitlement-aware AI access
- **FactSet 3.0 / FINBOURNE 3.0:** FactSet MCP has scope-based (tool/resource/parameter) entitlements; FINBOURNE markets "secure, permission-aware AI agents."
- **Arcesium 2.5:** Databricks managed MCP servers auto-enforce Unity Catalog permissions; per-agent granularity not itemised.
- **Aladdin 2.0:** Copilot filters tools to user permissions (vendor-controlled scope). GoldenSource 2.0 / MSCI 2.0: access-controls claimed, scoped/unreferenced.
- **SimCorp 1.5, Rimes 1.5, NeoXam 1.0, Gresham 0.5:** governed/roadmap but AI-specific entitlement mechanics thin or absent.

## AI-04 — Source provenance & audit trail for AI answers
- **FactSet 2.5 / FINBOURNE 2.5:** FactSet anchors answers to governed outputs via semantic/metadata layer + audit-friendly workflows; FINBOURNE bi-temporal trail + MCP compliance/auditability.
- **Arcesium 2.0, GoldenSource 2.0, MSCI 2.0:** governed/traceable framing (MSCI's PADP has document-level traceability but for extraction, not agent answers).
- **Aladdin 1.5** (output guardrails, no answer-citation), **Gresham/NeoXam 1.0** (strong non-AI lineage but no AI-answer provenance shipped), **Rimes/SimCorp 1.0** (none native).

## INT-01 — REST / streaming APIs
- Broadly well-served. **FactSet 3.0** (rich APIs + Event Hub streaming), **FINBOURNE 3.0** (unified API layer), **Gresham 3.0** (REST + Control Cloud API). NeoXam/MSCI/SimCorp/Aladdin/Arcesium 2.5 (solid REST, streaming/write-back specifics vary). Rimes 2.0 (Delta Sharing primary, REST not detailed), GoldenSource 2.0 (APIs general).

## INT-02 — Python / SDK access
- **FINBOURNE 3.0** (explicit Python/Java/C# SDKs), **Gresham 3.0** (R/Python/Spark delivery), **FactSet 3.0** (developer platform + Python). MSCI 2.5 (Python client via Crux). Aladdin 2.0 / Arcesium 2.0 (Studio/self-service, SDK not fully itemised). Rimes/NeoXam/GoldenSource/SimCorp 1.5 (Python not natively documented).

## INT-03 — Direct BI / notebook query (no spreadsheet extracts)
- **Databricks share-in-place leaders (3.0):** Rimes (Delta Sharing, no replication), FactSet (FactSet-via-Databricks Marketplace, Delta Sharing), FINBOURNE (Luminesce SQL virtualisation).
- **Proxy/adjacent (2.0-2.5):** Gresham (Spark-native delivery), Arcesium (self-service query), NeoXam & GoldenSource (Snowflake/warehouse), MSCI (Snowflake-native, not Databricks).
- **Weak (1.5):** SimCorp (integration-via-extraction), Aladdin (largely closed).

## INT-04 — Business-user model extension without vendor coding
- **Gresham 2.5** (Prime EDM configurable reusable template / flexible schema / hierarchies) is best-evidenced. NeoXam 2.0 (configurable survivorship + Aro no-code rules), FINBOURNE 2.0 / Arcesium 2.0 (configurable/self-service, depth not itemised). SimCorp/Aladdin 1.5 (developer-oriented config). GoldenSource 1.5 (asserted). **FactSet 1.0 / MSCI 1.0 / Rimes 1.0** — licensed-content or managed-service models; self-extension not established.

## GOV-01 — Field-level lineage
- **Gresham 3.0** (explicit lineage/change-history in normalised model — core EDM strength). NeoXam 2.5 (field-level ranking/survivorship), GoldenSource 2.5 (lineage/metadata extraction), FINBOURNE 2.5 (bi-temporal inherent). FactSet/SimCorp/Aladdin/Arcesium 2.0. MSCI 1.5 (strong only within PADP), Rimes 1.5 (managed, undetailed).

## GOV-02 — Override & change audit trail
- **Gresham 3.0** (Control Cloud: four-eyes, edit entitlements, investigation history, audit trails — best documented). NeoXam 2.5 (Aro exception logging/escalation), FINBOURNE 2.5 (bi-temporal + Taskize), SimCorp 2.5 / Aladdin 2.5 (platform four-eyes/workflow). Arcesium/GoldenSource 2.0. FactSet 1.5 (customizable checks, workflow depth unproven), MSCI 1.5 (scoped), Rimes 1.5.

## GOV-03 — Governable data / AI-use licensing rights
- **FactSet 3.0 — clear and lone leader:** published GenAI Governance & Security Policy (prompts/responses not used to train LLMs; entitlement-scoped; opt-in/opt-out).
- **Everyone else 1.0-1.5:** FINBOURNE 1.5 (client-populated ⇒ client owns data, but terms unpublished), Aladdin 1.5 (governed but vendor-controlled). Rimes / Arcesium / NeoXam / Gresham / GoldenSource / MSCI / SimCorp 1.0 — derived-data/AI-use licensing rights **not published** (RFP-stage disclosure required). This is the weakest, most uniformly unproven requirement across the field.

## GOV-04 — Institutional security (SOC2/ISO, private networking, entitlements)
- **Strongest (3.0):** Aladdin (enterprise security on AWS/Azure, private networking, largest institutions), SimCorp One (single-tenant Azure SaaS, Deutsche Börse-owned), FactSet (scope-based entitlements + private LLM environments, public co).
- **Institutional-grade implied (2.0-2.5):** Arcesium 2.5, and Rimes/FINBOURNE/Gresham/GoldenSource/MSCI 2.0 — strong client bases but **specific SOC2/ISO/private-networking certs were not confirmed in this pass** (targeted search returned no vendor-specific cert evidence; RFP-stage confirmation needed).
- NeoXam 1.5 (cloud-native, certs not established).

---

### Cross-requirement read
- **Model-independent AI leaders:** FactSet and Arcesium (open MCP, buyer's own LLM), with FINBOURNE and MSCI close behind. FactSet is uniquely strong on AI governance (GOV-03) and permission-aware access (AI-03).
- **Governance/lineage leader:** Gresham (Opus/Prime + Control Cloud) on field-level lineage and override/audit — but its AI story is 2026-roadmap.
- **Vendor-locked / weakest for this buyer's "own-AI" goal:** BlackRock Aladdin (GPT-4, vendor-controlled) and SimCorp (Azure OpenAI, curated) — both strong on security but score low on AI-02/AI-01.
- **Unproven AI:** NeoXam (production 2027) and Gresham (roadmap) sit at the floor on all four AI requirements.
- **Universal gap:** GOV-03 (AI-use licensing rights) — only FactSet has a published, governable policy; all others require RFP disclosure.
