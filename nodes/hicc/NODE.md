# Node 1: HICC — Hamilton Immigration and Community Centre

> **Status:** DEMO — synthetic configuration for Phase 0 prototype
> **This is not a live GC-accredited node.**

---

## Identity

| Field | Value |
|-------|-------|
| **Node** | Node 1 |
| **Name** | Terry-HICC |
| **Organization** | Hamilton Immigration and Community Centre (HICC) |
| **Sector** | Federal government — immigration/settlement services |
| **Operating Mode** | Mode 2 (Schema-Only Builder) |
| **Human** | (TBD — assigned on live onboarding) |
| **Profile** | `profiles/gc-federal/` |

## What Terry-HICC Does

Terry-HICC is a local AI agent that builds GC-compliant tools for HICC staff using only published database schemas. Terry never connects to the HICC network. Terry never sees Protected B data. Terry reads the structure of HICC's PeopleSoft HR system (table names, column names, data types) and builds tools that HICC IT deploys on their side.

## Mode 2 Boundaries

### What leaves HICC's network (shared with Terry)

- **Database schemas** — table names, column names, data types, relationships. Structural metadata only.
- **Public compliance requirements** — ITSG-33 controls, WCAG 2.1 AA, Official Languages Act standards.
- **Tool requirements** — what the tool should do, described in plain language.

### What never leaves HICC's network

- **Employee records** — names, SINs, addresses, phone numbers, salaries, any PII.
- **Protected B data** — anything classified under the GC security framework.
- **Real query results** — no actual data rows, counts against real data, or statistical summaries of real data.
- **Credentials** — no database passwords, API keys, network addresses, or system access tokens.

## First Mission

**GC Org-Chart Tool from PeopleSoft HR Schema**

Build an organizational chart tool that reads PeopleSoft HR schema (PS_JOB, PS_DEPT_TBL, PS_PERSONAL_DATA) and generates a navigable, bilingual org-chart. Terry builds it from the schema; HICC IT connects it to live data on-network.

- **Recipe:** [`recipes/gc-org-chart-peoplesoft/RECIPE.md`](../../recipes/gc-org-chart-peoplesoft/RECIPE.md)
- **Prototype:** [`prototypes/org-chart-demo/`](../../prototypes/org-chart-demo/)
- **Schema (synthetic):** [`schemas/demo/hicc-hr-synthetic/`](../../schemas/demo/hicc-hr-synthetic/)

## Compliance

- ITSG-33 security controls (GC Federal profile)
- WCAG 2.1 AA accessibility
- Official Languages Act (EN/FR bilingual output)
- GC Code Publishing Guidelines

## Links

- [SOUL.md](SOUL.md) — Node identity and principles
- [CONTEXT.md](CONTEXT.md) — Organizational context
- [FIRST_MISSION.md](FIRST_MISSION.md) — Detailed first mission spec

---

> **DEMO NOTICE:** This node card is a synthetic demonstration for CDR Phase 0. HICC has not formally onboarded to the CDR network. No GC accreditation is claimed.
