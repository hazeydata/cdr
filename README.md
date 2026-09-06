# The Canadian Digital Railway (CDR)

**Bottom-up sovereign AI: local agents ("terrys") build GC-compliant tools from published schemas. Sensitive data never leaves the org. Reusable solution recipes compound across Canada.**

> **September 2026 — Phase 0 reframe.** See [`docs/VISION-2026-09.md`](docs/VISION-2026-09.md) for the full vision, [`nodes/hicc/`](nodes/hicc/) for the first demo node, and [`prototypes/org-chart-demo/`](prototypes/org-chart-demo/) for a runnable prototype.

---

## What Is the CDR?

The Canadian Digital Railway is a network of local AI agents ("terrys") that help organizations build compliant, accessible, institution-ready software tools. Each terry runs locally — on your hardware, on your terms — and operates within your organization's security boundaries.

Think of it like hiring a new employee: they get onboarded, they learn the systems, they understand their security clearance, and they build things within those boundaries. The difference is that a terry can be onboarded in 15 minutes and start building immediately.

The CDR isn't one AI. It's a **network** of sovereign AI nodes across Canada, each serving a different organization. They share knowledge and compliance standards through the recipe index, but each node operates independently within its own security context.

---

## Phase 0 Quick Links

| Resource | Description |
|----------|-------------|
| [`docs/VISION-2026-09.md`](docs/VISION-2026-09.md) | Full Sep 2026 vision — thesis, landscape, roadmap |
| [`nodes/hicc/NODE.md`](nodes/hicc/NODE.md) | Node 1 (HICC) — demo terry identity and boundaries |
| [`recipes/gc-org-chart-peoplesoft/RECIPE.md`](recipes/gc-org-chart-peoplesoft/RECIPE.md) | First recipe — org-chart from PeopleSoft HR schema |
| [`schemas/demo/hicc-hr-synthetic/`](schemas/demo/hicc-hr-synthetic/) | Synthetic PeopleSoft HR schema (demo, not real data) |
| [`prototypes/org-chart-demo/`](prototypes/org-chart-demo/) | Runnable prototype — schema → org-chart |
| [`docs/DTC-ONE-PAGER.md`](docs/DTC-ONE-PAGER.md) | DTC/ISED staffer one-pager |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Node initialization protocol |

---

## The Problem

Organizations across Canada — from federal departments to municipalities to healthcare providers — need better software tools. Dashboards, reports, automations, data workflows. But:

1. **Building custom tools is slow and expensive.** IT backlogs stretch months or years.
2. **AI assistants like Copilot or ChatGPT can't access classified/sensitive data.** They run in the cloud. Your data can't go there.
3. **Even when AI could help, the approval process is impossible.** Getting an AI system approved for a Protected B environment requires the kind of compliance effort only billion-dollar companies can afford.
4. **Every organization reinvents the wheel.** A hundred departments need the same HR dashboard, and each one builds it from scratch (or doesn't build it at all).

## The Core Idea: Mode 2 Schema-Only

Terry builds tools from **published database schemas** — table names, column types, relationships — without ever seeing real data. The department deploys the finished tool on-network. Schema in → compliant tool out → data never leaves the building.

Schemas were never published before because there was no consumer for them. Terry creates the demand side. Publishing a schema now results in a custom tool the next day. This creates a **flywheel**.

**Solution recipes** capture how to build a tool from a schema type. They're published to an append-only index so other organizations can fork them. Solutions compound across Canada organically.

---

## How It Works

### Three Operating Modes

| Mode | Data Access | Typical For |
|------|------------|-------------|
| **Mode 2: Schema-Only** (lead) | Schema metadata only — no data | GC federal departments, provincial departments with classified data, healthcare |
| Mode 1: Full Access | Direct data access | Small municipalities, non-profits, personal use |
| Mode 3: Hybrid | Mixed — some direct, some schema-only | Research institutions, crown corporations |

### Who It Serves

GC Federal departments, provincial/territorial governments, municipalities, universities, healthcare organizations, crown corporations, private sector, non-profits. Each organization type has a **compliance profile** that terry loads during onboarding.

---

## Core Principles

1. **Know your context.** Understand your security environment and never exceed your clearance.
2. **Sovereign.** Run locally. Your human's data stays on your human's terms.
3. **Compliant by default.** Match your output to your institution's standards.
4. **Transparent.** Your code is readable. Your process is explainable.
5. **Part of the Railway.** The recipe index is your network. Share what you learn.
6. **Trust but verify.** NEVER take data classification at face value. Terry is the last line of defence.

See `principles.md` for the full expanded principles.

---

## Try the Prototype

```bash
cd prototypes/org-chart-demo
pip install -r requirements.txt
python main.py          # Web UI at http://localhost:8000
python main.py --cli    # Terminal output
```

Reads the synthetic PeopleSoft HR schema and renders a bilingual org-chart with placeholder data. No real data needed.

---

## Project Structure

```
cdr/
├── README.md                  ← You are here
├── BOOTSTRAP.md               ← Node initialization protocol
├── principles.md              ← CDR Core Principles (expanded)
├── docs/
│   ├── VISION-2026-09.md      ← Sep 2026 vision + roadmap
│   ├── DTC-ONE-PAGER.md       ← DTC/ISED staffer one-pager
│   └── CROSS_POLLINATION.md   ← HazeyData patterns → CDR components
├── nodes/
│   └── hicc/                  ← Node 1 (HICC) — demo
│       ├── NODE.md            ← Identity, mode, boundaries
│       ├── SOUL.md            ← Birth certificate
│       ├── CONTEXT.md         ← Organizational context
│       └── FIRST_MISSION.md   ← First mission spec
├── schemas/
│   └── demo/
│       └── hicc-hr-synthetic/ ← Synthetic PeopleSoft HR schema
├── recipes/
│   └── gc-org-chart-peoplesoft/ ← First recipe
├── prototypes/
│   └── org-chart-demo/        ← Runnable Phase 0 prototype
├── profiles/                  ← Compliance profiles by organization type
│   └── gc-federal/            ← GC federal departments
├── adapters/                  ← Data adapter templates
│   ├── peoplesoft-hr.md
│   └── sap-finance.md
└── pitch/                     ← Concept and pitch documents
```

---

## Current Status

**Phase: 0 — Concept + First Prototype (Sep 2026)**

- ✅ CDR architecture designed (3 operating modes, compliance profiles, adapter system)
- ✅ Bootstrap protocol written (BOOTSTRAP.md — 6-phase onboarding)
- ✅ Sep 2026 vision reframe (Mode 2 lead, recipe index, terry-first)
- ✅ Node 1 demo (HICC — synthetic configuration)
- ✅ Synthetic PeopleSoft HR schema
- ✅ First recipe (gc-org-chart-peoplesoft)
- ✅ Runnable prototype (org-chart-demo)
- ✅ DTC one-pager
- 🔜 HICC schema publication approval (real schema, formal pilot)
- 🔜 First live node deployment

**No active infrastructure.** CDR is documentation, architecture, and one prototype at this stage. No servers, no databases, no crons.

---

## Landscape Position

CDR complements — does not replace — existing Canadian AI infrastructure:

- **GC AI Platform** — serves cloud-ready workloads; CDR serves the on-premise, Protected B workloads that can't go to cloud
- **SSC** — provides infrastructure; CDR provides the AI agent layer on top
- **SCIP** — shared cloud; CDR nodes can run on SCIP infra with the recipe layer added
- **DGX Spark / Faraday appliances** — optional hosting hardware for a terry; not the CDR brand

CDR's whitespace: locally owned node network + Mode 2 schema-only pattern + recipe index + auditable compliance profiles.

---

*The Canadian Digital Railway — sovereign AI for Canadian institutions.*
