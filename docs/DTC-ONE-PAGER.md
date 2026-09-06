# Canadian Digital Railway — DTC One-Pager

**For:** Digital Transformation Centre / ISED staffers
**Date:** September 2026
**From:** HazeyData (Fred Hazey)

---

## The Problem

GC departments sit on massive IT backlogs. Staff need custom tools — org-charts, dashboards, reports — but building them takes months and costs hundreds of thousands. Cloud AI (Copilot, ChatGPT) can't help because the data is Protected B: it can't leave the network. Every department reinvents the same wheel independently.

## The Solution: Mode 2 Schema-Only AI

Put a small local AI agent ("terry") in a middle worker's hands. Terry builds tools from **published database schemas** — table names, column types, relationships — without ever seeing real data. The department's IT team deploys the finished tool on-network and connects it to live data.

**Schema in → compliant tool out → data never leaves the building.**

## How It Works

1. Department publishes a database schema (structural metadata — not classified data)
2. Terry reads the schema + GC compliance standards (ITSG-33, WCAG 2.1 AA, Official Languages Act)
3. Terry builds a complete, bilingual, accessible tool with data adapters
4. Department IT reviews and deploys on-network
5. The **recipe** (how to build this tool from this schema type) is published to an index so other departments can fork it

## Why This Is Different

| Existing approach | CDR approach |
|-------------------|-------------|
| Cloud AI — can't touch Protected B | Local AI — runs within the security boundary |
| Top-down platform — departments wait in line | Bottom-up — middle workers build their own tools |
| One-off builds — no reuse | Recipe index — solutions compound across departments |
| Vendor lock-in — proprietary systems | Open source — forkable, auditable, no lock-in |

## The HICC-Shaped Pilot

**Node 1:** Hamilton Immigration and Community Centre (HICC)
**First tool:** Org-chart built from PeopleSoft HR schema
**Mode:** 2 (Schema-Only) — terry never sees employee data

The pilot proves the pattern with one department. The recipe is published so any GC department running PeopleSoft HR can fork the org-chart tool immediately. Second department forks within the 90-day window.

## Complements GC AI Platform

CDR does **not** replace GC AI Platform or SSC. GC AI Platform serves cloud-ready, unclassified workloads. CDR serves the workloads that can't go to cloud — the Protected B, on-network, schema-only use cases. They're complementary layers:

| Layer | Serves |
|-------|--------|
| SSC | Infrastructure (compute, network, hosting) |
| GC AI Platform | Cloud-accessible AI workloads |
| CDR | On-premise, schema-only AI for Protected B environments |

## 90-Day Ask

1. **Support one pilot node** at HICC (or equivalent department willing to publish a PeopleSoft HR schema)
2. **Terry builds the org-chart tool** from published schema — zero Protected B exposure
3. **Recipe published** to the index — second department forks it
4. **Outcome:** Demonstrated "schema → tool" flywheel with two departments, one recipe, zero data breaches

**Cost:** Minimal — CDR runs on commodity hardware. No platform buildout. No vendor contract. One pilot, one recipe, proof of pattern.

## What We Do NOT Claim

- No GC accreditation or SA&A certification (Phase 0 is a concept + demo)
- No endorsement from any minister or deputy minister
- No replacement for SSC, GC AI Platform, or existing enterprise systems
- No access to or handling of real Protected B data in Phase 0
- No proprietary technology — everything is open source and auditable

---

*Canadian Digital Railway — sovereign AI for Canadian institutions.*
*Contact: Fred Hazey, HazeyData — fred@hazeydata.com*
