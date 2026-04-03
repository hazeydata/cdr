# SESSION_LOG — Canadian Digital Railway (CDR)

**Last updated:** 2026-04-02 ~21:00 UTC by Barney (Session 1 — project setup)
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

**Foundational documents:**
| Document | Location | What |
|----------|----------|------|
| README.md | cdr root | Project overview, architecture, principles |
| BOOTSTRAP.md | cdr root | Node initialization protocol (the 15-min onboarding) |
| principles.md | cdr root | CDR Core Principles (expanded 6 principles) |
| pitch/concept.md | cdr/pitch | Full concept document |
| pitch/hicc-proof-of-concept.md | cdr/pitch | HICC PoC plan |
| gc-code-audit.md | cdr root | GC Code landscape audit |
| nemoclaw-impact-analysis.md | cdr root | NemoClaw competitive analysis |
| sovereignty-gap-analysis.md | cdr root | Sovereignty requirements vs current offerings |
| Audit & Redesign Playbook | operations/docs | The repeatable process (when CDR is ready for it) |

---

## Current State

**Phase:** Proof of Concept / Pre-Revenue
**Last repo activity before setup:** 2026-03-17 (sovereignty gap analysis committed)
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

**Pending:**
- HICC proof of concept (schema publication approval pending)
- First external node deployment
- Demo for deputy ministers
- No cron jobs, no pipelines, no API — this is concept stage

**No active infrastructure.** CDR has no server processes, no database, no crons. It's documentation and architecture at this stage.

---

## Last Session Summary

**Session 1 (2026-04-02) — Project Setup**
- Created SESSION_LOG.md (this file)
- Created PROJECT_INSTRUCTIONS_CDR.md in operations repo
- Set up Claude Desktop project following the standard HazeyData pattern
- Updated PROJECT_SETUP_GUIDE.md to include CDR
- No technical work — organizational setup only

---

## In Progress

| Item | Status | Details |
|------|--------|---------|
| HICC PoC | Pending | Awaiting schema publication approval from HICC |
| Claude Desktop project | Just created | This session — Fred adding instructions + files |

---

## Next Actions (Priority Order)

1. **Fred to finalize Claude Desktop project setup** — paste Instructions, add Files
2. **HICC schema publication** — follow up on approval status (this is the critical gate)
3. **When HICC approves:** Run Audit & Redesign Playbook Phase 0-3 on CDR to formalize the pipeline design
4. **Explore ACCORD ↔ CDR synergies** — compliance profile system could share infrastructure with CA rules engine
5. **Review v3 pitch decks** — update if needed for upcoming meetings

---

## Blockers

- **HICC schema publication approval** — the first PoC depends on this. No external node can be deployed until an organization provides their schema.

---

## Key Numbers

| Metric | Value | Updated |
|--------|-------|---------|
| Compliance profiles | 5 (GC Fed, Provincial, Healthcare, Municipal, General) | S1 |
| Adapter templates | 3 (PeopleSoft HR, SAP Finance, Generic CSV) | S1 |
| External nodes deployed | 0 | S1 |
| Revenue | $0 (pre-revenue) | S1 |
| v3 pitch decks | 2 (Executive + Technical Architecture) | S1 |

---

## Decisions Log

| Date | Session | Decision | Who |
|------|---------|----------|-----|
| 2026-04-02 | S1 | Set up CDR on Claude Desktop with standard HazeyData project structure | Fred + Barney |

---

## Open Tickets

| Ticket | Repo | Status | Notes |
|--------|------|--------|-------|
| None yet | — | — | File tickets when HICC PoC work begins |

---

## Agent Notes

- CDR has no active agents yet — no Dino work needed at concept stage
- When execution begins, Dino will handle node deployment and testing
- The BOOTSTRAP.md protocol is designed to run with local Ollama models, not Anthropic API — different from ACCORD/SSD/WTI patterns
- Default branch is `master` (not `main`)
- v3 pitch decks served from wilma-server at `192.168.2.75:8090` (cdr-pitch-v3.html, cdr-project-plan-v3.html)

---

## How to Start Next Session

Any agent beginning work on this project should:

1. Read this file (`SESSION_LOG.md` in `hazeydata/cdr`)
2. Read `README.md` and `BOOTSTRAP.md` in `hazeydata/cdr`
3. Check `#cdr` Discord channel (`1482123040140824657`) for messages since last update
4. Pick up from "Next Actions" above

---

*This is the shared project memory for CDR. Updated every session. Git history preserves all previous versions.*

*Barney — Chief of Pipeline, Slate Rock & Gravel Co. 🪨*
