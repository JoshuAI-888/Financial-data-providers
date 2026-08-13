# Sayari

## 1. Snapshot
- Owner/parent: **Sayari Labs, Inc.** (privately held; backed by TPG Growth / Centana). HQ **Washington, D.C., USA**; founded **2015**. Positioning: a global commercial-risk and supply-chain-intelligence platform built on the largest open-source collection of corporate ownership and trade data, purpose-built for beneficial-ownership and network-risk resolution.
- **Regions/markets covered:** global — resolves entities across **250+ jurisdictions**; unusually strong on hard-to-reach markets (China, emerging markets, sanctioned/opaque geographies) via primary-source registry extraction.
- **Free tier:** No (enterprise/government subscription; demos available). Some sources are publicly derived, but access is paid.
- Pricing model & known ranges: enterprise subscription, seat- and module-based (Graph, Signal, Map/Supply Chain). Not publicly disclosed.

## 2. Data-domain coverage
- Company reference/firmographics: yes — 500M+ resolved companies from official registries.
- Beneficial ownership: core strength — traces ultimate beneficial owners and ownership chains across jurisdictions.
- KYC/identity: supports KYC/KYB and third-party due diligence workflows (not consumer identity verification).
- Sanctions/PEP/adverse-media: screens OFAC, BIS and 40+ sanctions programs with ownership-chain resolution; UFLPA/forced-labor exposure mapping.
- Private-company sourcing: partial — corporate discovery, not deal-sourcing focused.
- Credit/risk scores: risk signals/flags (sanctions, forced labor, environmental) rather than credit scores.

## 3. Datasets
- Sayari Graph: **12.4B+ primary-source records**, **1.8B+ (up to 4B+) trade/shipment records**, **500M+ resolved companies** across **250+ jurisdictions**. Sources include global corporate registries, US Customs/CBP import-export data, US Commerce/BIS and SEC registries, sanctions/screening lists and 50-state US company data. Proprietary **entity-resolution graph** linking entities, owners, officers and counterparties. Sourcing method: automated registry extraction plus trade-flow ingestion and ownership-linkage modeling.

## 4. APIs & technical integration
- REST **Sayari API** with entity-resolution endpoints (resolve name/registration number/address to a canonical entity ID) plus trade endpoints (`/shipments`, `/suppliers`, `/buyers`) querying billions of trade transactions; JSON. Auth via API key/token. Delivery via API, the Sayari Graph web app, and bulk/data-integration options; supports both real-time lookups and batch screening. Transparent per-source provenance in results. No public MCP server identified.

## 5. Enabling technology
- Automated multilingual entity resolution and transliteration across registries; ownership-network/graph analytics for UBO and network-risk traversal; AI/ML for entity matching and risk classification; trade-flow analytics linking shipments to corporate ownership; compliance tooling for sanctions/UFLPA exposure with full evidence chains.

## 6. Customer / user feedback
- Lower public-review volume than mass-market KYC vendors; recognized in analyst/press coverage (e.g., Memgraph customer story, industry press) for depth of opaque-market ownership data. Pros: unmatched coverage of Chinese/emerging-market registries, transparent source provenance, strong ownership-chain traversal. Cons: enterprise price point, analyst-oriented (not a turnkey consumer-KYC tool), depth can require expertise. User segments: government/national-security, compliance/AML, corporate supply-chain and third-party-risk teams, trade-compliance.

## 7. Edge & positioning
- Leads on beneficial-ownership resolution and supply-chain/trade-linked risk in opaque jurisdictions with primary-source transparency. Lags on consumer identity/KYC, credit scoring and out-of-the-box SME onboarding UX. Best-for: sanctions/forced-labor and UBO due diligence across complex global corporate networks and supply chains.

## 8. Provenance
- https://sayari.com/enterprise/ — enterprise risk-intelligence platform (accessed 2026-08-11)
- https://sayari.com/supply-chain/ — supply-chain risk & 250+ jurisdictions (accessed 2026-08-11)
- https://documentation.sayari.com/api/key-concepts/endpoint-overview — API endpoints & entity resolution (accessed 2026-08-11)
- https://sayari.com/resources/newsroom/official-company-data-from-all-50-us-states-now-searchable-in-sayari-graph/ — 12.4B+ records, 50-state data (accessed 2026-08-11)
- https://sayari.com/platform/graph/ — Sayari Graph corporate intelligence (accessed 2026-08-11)
- https://memgraph.com/customer-stories/real-time-data-processing-for-relationship-mapping — independent graph/tech write-up (accessed 2026-08-11)
