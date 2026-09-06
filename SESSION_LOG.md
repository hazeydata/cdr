# SESSION_LOG — Canadian Digital Railway (CDR)

**Last updated:** 2026-09-06 ~03:00 UTC by Barney (Session 3)
**Purpose:** When starting a new chat with Barney for CDR, point him here first.
**Location:** `hazeydata/cdr/SESSION_LOG.md` (canonical)

---

## Project Background

**What we're building:** The Canadian Digital Railway (CDR) is a network of sovereign, locally-deployed AI agents ("terrys") that help Canadian organizations — from federal departments to municipalities to healthcare providers — build compliant, accessible, institution-ready software tools without compromising security.

**Why it matters:** Organizations across Canada face massive IT backlogs, can't use cloud AI on classified/sensitive data, and each one reinvents the same tools. CDR solves this by deploying local AI nodes that operate within each organization's security boundary, sharing knowledge and compliance standards through the CDR network while keeping data sovereign.

**Who uses it / who buys it:** GC federal departments (Protected B), provincial/territorial governments, municipalities, healthcare organizations, universities, crown corporations, private sector, non-profits. Each gets a compliance profile tailored to their security context.

**How we got here:** CDR was conceived as a parallel track to ACCORD — same architectural DNA (encoding institutional rules as machine-readable standards) but applied to security/compliance policies instead of collective agreements. The project was bootstrapped in mid-March 2026 with a v2 draft including BOOTSTRAP.md (node onboarding protocol), compliance profiles, adapter templates, and pitch materials. A GC Code audit, NemoClaw impact analysis, and sovereignty gap analysis were completed to map the landscape. v3 pitch decks were built incorporating NemoClaw as the foundation layer, the sovereignty gap analysis (60% → 80%), and DGX Spark as reference hardware. HICC proof of concept was identified as the first external deployment target.

**Key findings that still apply:**
- Three operating modes (Full Access, Schema-Only Builder, Hybrid) cover all Canadian institutional security contexts
- Schema publication creates a flywheel — publishing schemas that previously had no consumer creates demand for AI-built tools
- "Trust but verify" principle is critical — terry must independently verify data classification, never take it at face value
- CDR and ACCORD share architectural DNA and can cross-pollinate (compliance profiles ↔ CA rules)
- NemoClaw is the foundation layer for CDR v3 (replaced Hypertec/ThinkOn hybrid cloud model)
- Sovereignty gap analysis: current offerings cover ~60% of Canadian institutional requirements → CDR targets 80%+
- **Every HazeyData project is a pseudo-node** — patterns built in SSD, WTI, ACCORD, and HICC are proto-CDR infrastructure (see `docs/CROSS_POLLINATION.md`)

**Foundational documents:**
| Document | Location | What |
|----------|----------|------|
| README.md | cdr root | Project overview, architecture, principles |
| BOOTSTRAP.md | cdr root | Node initialization protocol (the 15-min onboarding) |
| principles.md | cdr root | CDR Core Principles (expanded 6 principles) |
| CROSS_POLLINATION.md | docs/ | Maps HazeyData patterns → CDR components |
| pitch/concept.md | cdr/pitch | Full concept document |
| pitch/hicc-proof-of-concept.md | cdr/pitch | HICC PoC plan |
| gc-code-audit.md | cdr root | GC Code landscape audit |
| nemoclaw-impact-analysis.md | cdr root | NemoClaw competitive analysis |
| sovereignty-gap-analysis.md | cdr root | Sovereignty requirements vs current offerings |
| Audit & Redesign Playbook | operations/docs | The repeatable process (when CDR is ready for it) |

---

## Current State

**Phase:** Phase 0 — Concept + First Prototype
**Last repo activity:** 2026-09-06 (Session 3 — Phase 0 reframe)
**Discord channel:** `#cdr` — `1482123040140824657`

**Completed:**
- CDR architecture designed (3 operating modes, compliance profiles, adapter system)
- Bootstrap protocol written (BOOTSTRAP.md — 6-phase onboarding)
- Compliance profiles created (GC Federal with ITSG-33, Provincial, Healthcare, Municipal, General)
- Adapter templates created (PeopleSoft HR, SAP Finance, Generic CSV)
- GC Code audit completed
- NemoClaw impact analysis completed
- Sovereignty gap analysis completed
- Pitch materials written (concept.md, HICC PoC)
- v3 pitch decks built (Executive Pitch + Technical Architecture) — served from wilma-server
- HICC Open Source Code Publishing Guidelines added as reference
- Cross-pollination map created (docs/CROSS_POLLINATION.md) — maps HazeyData patterns to CDR components
- HICC Homelessness Dashboard built (Mode 2 / off-network) — Barney + Fred, outside Dino/Wilma scope
- **Sep 2026 Phase 0 reframe** — vision, Node 1 demo, synthetic schema, first recipe, runnable prototype, DTC one-pager
- **Synthetic PeopleSoft HR schema** — `schemas/demo/hicc-hr-synthetic/schema.yaml`
- **First recipe** — `recipes/gc-org-chart-peoplesoft/RECIPE.md` (org-chart from PeopleSoft HR)
- **Runnable prototype** — `prototypes/org-chart-demo/` (Python, schema → bilingual org-chart)
- **DTC one-pager** — `docs/DTC-ONE-PAGER.md`

**Pending:**
- HICC schema publication approval (real schema for live pilot)
- First live node deployment
- Second department forks the org-chart recipe
- No cron jobs, no pipelines, no API — this is concept + prototype stage

**No active infrastructure.** CDR has no server processes, no database, no crons. One runnable prototype exists (`prototypes/org-chart-demo/`).

---

## Last Session Summary

**Session 3 (2026-09-06) — Phase 0 Reframe**
- Full Sep 2026 vision reframe: terry-first, Mode 2 lead, recipe index, soft-pedal hardware
- Created `docs/VISION-2026-09.md` — reworked vision with keep/cut table, landscape, DTC fit, roadmap
- Created Node 1 (HICC) demo: `nodes/hicc/` — NODE.md, SOUL.md, CONTEXT.md, FIRST_MISSION.md
- Created synthetic PeopleSoft HR schema: `schemas/demo/hicc-hr-synthetic/schema.yaml`
- Created first recipe: `recipes/gc-org-chart-peoplesoft/RECIPE.md`
- Created runnable prototype: `prototypes/org-chart-demo/` — Python app, schema → bilingual org-chart
- Created DTC one-pager: `docs/DTC-ONE-PAGER.md`
- Updated README.md with Phase 0 links and corrected status
- Landscape encoding: SCIP, GC AI Platform, Cohere, TELUS/OpenText, DGX Spark acknowledged; CDR positioned in whitespace (Mode 2 + recipes + local nodes)
- NemoClaw/DGX soft-pedaled to optional engine, not brand
- No overclaims: no GC accreditation, no endorsements, all demo data clearly labeled synthetic

**Session 2 (2026-04-02) — Cross-Pollination + Strategic Direction**
- Fred's key insight: each HazeyData project is a pseudo-node; mine existing code as CDR fodder
- Created `docs/CROSS_POLLINATION.md` — maps HazeyData operational patterns to CDR architecture
- Identified HICC Homelessness Dashboard as de facto Mode 2 CDR demo (strongest proof-of-concept material)
- HICC Workplace BI tool: no update yet, may move Tuesday when Fred returns to office
- No code/infrastructure work — strategic alignment session

**Session 1 (2026-04-02) — Project Setup**
- Created SESSION_LOG.md
- Created PROJECT_INSTRUCTIONS_CDR.md in operations repo
- Set up Claude Desktop project following the standard HazeyData pattern

---

## In Progress

| Item | Status | Details |
|------|--------|---------|
| Phase 0 reframe | Complete | Vision, Node 1 demo, schema, recipe, prototype, DTC one-pager |
| HICC schema publication | Pending | Real schema needed for live pilot — Fred to follow up |
| HICC Homelessness Dashboard | Built | Mode 2 build by Barney + Fred (outside Dino/Wilma) |
| Cross-pollination inventory | Complete | `docs/CROSS_POLLINATION.md` committed |

---

## Next Actions (Priority Order)

1. **Fred reviews Phase 0 PR** — vision, Node 1 demo, synthetic schema, recipe, prototype, DTC one-pager. Merge when satisfied.
2. **HICC schema publication** — Fred to follow up with HICC IT. Real PeopleSoft HR schema (structure only) unlocks the live pilot.
3. **Share DTC one-pager** — `docs/DTC-ONE-PAGER.md` ready for DTC/ISED staffers.
4. **Package HICC Homelessness Dashboard as CDR case study** — needs HICC permission. Strongest existing demo material.
5. **When building CDR-OS:** Use CROSS_POLLINATION.md as extraction inventory — start with Playbook → Terry onboarding, ACCORD → compliance engine.
6. **Consider Phase 1 stack decisions** — Ollama wrapper, default model, Terry UI approach. After HICC gate clears.

---

## Blockers

- **HICC schema publication approval** — the live pilot depends on HICC IT publishing PeopleSoft HR table structures (schema only, no data).
- **HICC permission to use Homelessness Dashboard as case study** — needed to package as CDR demo material.

---

## Key Numbers

| Metric | Value | Updated |
|--------|-------|---------|
| Compliance profiles | 5 (GC Fed, Provincial, Healthcare, Municipal, General) | S1 |
| Adapter templates | 3 (PeopleSoft HR, SAP Finance, Generic CSV) | S1 |
| External nodes deployed | 0 | S1 |
| Revenue | $0 (pre-revenue) | S1 |
| v3 pitch decks | 2 (Executive + Technical Architecture) — archived, replaced by DTC one-pager | S3 |
| HazeyData patterns mapped to CDR | 15+ (see CROSS_POLLINATION.md) | S2 |
| De facto Mode 2 demos | 1 (HICC Homelessness Dashboard) | S2 |
| Solution recipes | 1 (gc-org-chart-peoplesoft) | S3 |
| Synthetic schemas | 1 (hicc-hr-synthetic) | S3 |
| Runnable prototypes | 1 (org-chart-demo) | S3 |
| Demo node cards | 1 (HICC — Node 1) | S3 |

---

## Decisions Log

| Date | Session | Decision | Who |
|------|---------|----------|-----|
| 2026-04-02 | S1 | Set up CDR on Claude Desktop with standard HazeyData project structure | Fred + Barney |
| 2026-04-02 | S2 | Treat each HazeyData project as a pseudo-node; mine patterns for CDR-OS | Fred |
| 2026-04-02 | S2 | HICC Homelessness Dashboard is the strongest CDR demo material | Barney |
| 2026-09-06 | S3 | Phase 0 reframe: terry-first, Mode 2 lead, recipe index, soft-pedal hardware | Fred |
| 2026-09-06 | S3 | NemoClaw/DGX = optional engine, not the CDR brand | Fred |
| 2026-09-06 | S3 | Archive v3 pitch decks; replace with DTC one-pager for Phase 0 | Fred |
| 2026-09-06 | S3 | HICC as Node 1 (demo) — synthetic configuration for prototype | Fred |

---

## Open Tickets

| Ticket | Repo | Status | Notes |
|--------|------|--------|-------|
| None yet | — | — | File tickets when HICC PoC work or CDR-OS build begins |

---

## Agent Notes

- CDR has no active agents yet — no Dino work needed at concept stage
- When execution begins, Dino will handle node deployment and testing
- The BOOTSTRAP.md protocol is designed to run with local Ollama models, not Anthropic API — different from ACCORD/SSD/WTI patterns
- Default branch is `master` (not `main`)
- v3 pitch decks served from wilma-server at `192.168.2.75:8090` (cdr-pitch-v3.html, cdr-project-plan-v3.html)
- HICC Homelessness Dashboard was built by Barney + Fred directly, outside the Dino/Wilma pipeline
- Fred's Phase 0 thinking: Ollama wrapper, MLX/llama.cpp for Apple Silicon, React or plain HTML/JS for Terry UI, Python/Node backend, SQLite audit log. Under $10K CAD.

---

## How to Start Next Session

Any agent beginning work on this project should:

1. Read this file (`SESSION_LOG.md` in `hazeydata/cdr`)
2. Read `CROSS_POLLINATION.md` in `docs/`
3. Read `README.md` and `BOOTSTRAP.md` in `hazeydata/cdr`
4. Check `#cdr` Discord channel (`1482123040140824657`) for messages since last update
5. Pick up from "Next Actions" above

---

*This is the shared project memory for CDR. Updated every session. Git history preserves all previous versions.*

*Barney — Chief of Pipeline, Slate Rock & Gravel Co. 🪨*
