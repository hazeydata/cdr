# The Canadian Digital Railway (CDR)

**Sovereign AI agents helping organizations build better tools — without compromising security.**

---

## What Is the CDR?

The Canadian Digital Railway is a network of local AI agents ("terrys") that help organizations build compliant, accessible, institution-ready software tools. Each terry runs locally — on your hardware, on your terms — and operates within your organization's security boundaries.

Think of it like hiring a new employee: they get onboarded, they learn the systems, they understand their security clearance, and they build things within those boundaries. The difference is that a terry can be onboarded in 15 minutes and start building immediately.

The CDR isn't one AI. It's a **network** of sovereign AI nodes across Canada, each serving a different organization. They share knowledge, compliance standards, and best practices through CDR HQ (Node 0, "Wilma"), but each node operates independently within its own security context.

---

## The Problem

Organizations across Canada — from federal departments to municipalities to healthcare providers — need better software tools. Dashboards, reports, automations, data workflows. But:

1. **Building custom tools is slow and expensive.** IT backlogs stretch months or years.
2. **AI assistants like Copilot or ChatGPT can't access classified/sensitive data.** They run in the cloud. Your data can't go there.
3. **Even when AI could help, the approval process is impossible.** Getting an AI system approved for a Protected B environment requires the kind of compliance effort only billion-dollar companies can afford.
4. **Every organization reinvents the wheel.** A hundred departments need the same HR dashboard, and each one builds it from scratch (or doesn't build it at all).

The CDR solves all four problems simultaneously.

---

## How It Works

### The Core Insight

An AI agent gets onboarded into an organization the same way a human employee does. It learns the role, the systems, the security clearance, the restrictions — and it always respects them.

### Three Operating Modes

Every CDR node operates in one of three modes, determined during onboarding based on the organization's security context:

#### Mode 1: Full Access
The terry has direct access to data. It builds tools that work with data end-to-end.

**Typical for:** Small municipalities, non-profits, startups, personal use, organizations with no data classification restrictions.

**How it works:** You give terry your data, terry builds your tool. Simple.

#### Mode 2: Schema-Only (Builder)
The terry is off-network with no data access. It works with **schemas** (structural metadata) only — table names, column names, data types. It builds complete, compliant tools that get deployed on-network by humans.

**Typical for:** Government of Canada federal departments, provincial departments with classified data, healthcare organizations with patient data.

**How it works:**
1. Organization publishes database schemas (structure, NOT data) to a code repository
2. Terry reads the schema + public compliance standards
3. Terry builds a complete, compliance-ready tool with data adapters
4. Organization clones the tool on-network, connects real data, runs security review
5. No classified data ever leaves the network

**Key insight:** Schemas were never published before because there was no consumer for them. Terry creates the demand side. Publishing a schema now results in a custom tool the next day. This creates a flywheel.

#### Mode 3: Hybrid
Some data is accessible (public/unclassified), some isn't. Terry works directly with what it can see and builds adapters for what it can't.

**Typical for:** Research institutions, crown corporations, organizations with mixed data classification levels.

### Who It Serves

The CDR is NOT just for the Government of Canada. It serves:

- **GC Federal departments** — Protected B compliance, ITSG-33, bilingual requirements
- **Provincial/territorial governments** — Province-specific accessibility and security standards
- **Municipalities** — Open data, citizen-facing tools, lighter compliance frameworks
- **Universities and research institutions** — Research data management, mixed classification
- **Healthcare organizations** — PHIPA, PIPEDA, HL7/FHIR interoperability
- **Crown corporations** — Hybrid government/commercial requirements
- **Private sector** — Industry-specific compliance, PIPEDA
- **Non-profits and community organizations** — Accessibility, open source, limited budgets

Each organization type has a **compliance profile** that terry loads during onboarding. The profile tells terry what standards to follow, what certifications to meet, and what the hard lines are.

---

## Core Principles

Every CDR node follows these six principles. They are non-negotiable.

1. **Know your context.** Understand your security environment and never exceed your clearance.
2. **Sovereign.** Run locally. Your human's data stays on your human's terms.
3. **Compliant by default.** Match your output to your institution's standards, whatever those are.
4. **Transparent.** Your code is readable. Your process is explainable.
5. **Part of the Railway.** HQ and other nodes are your network.
6. **Trust but verify.** NEVER take data classification at face value. Independently verify. Terry is the last line of defence before a compliance breach.

See `principles.md` for the full expanded principles.

---

## The Bootstrap: How a Node Gets Born

Every CDR node starts with `BOOTSTRAP.md` — a structured onboarding conversation between terry and its human. Over ~15 minutes, the bootstrap:

1. **Meets the human** — learns their name, role, organization, and pain points
2. **Maps the environment** — discovers systems, tech stack, data sources, security context
3. **Detects the operating mode** — determines Mode 1, 2, or 3 based on the security context
4. **Independently verifies** — checks network environment, scans for sensitive data patterns, looks up org security policies (trust but verify)
5. **Briefings the human** — explains how they'll work together, adapted to the detected mode
6. **Proposes a first mission** — a concrete first project based on the human's pain points
7. **Establishes identity** — names the node, generates SOUL.md, CONTEXT.md, and FIRST_MISSION.md
8. **Deletes itself** — the bootstrap is consumed. Terry is born.

The bootstrap is simultaneously: configuring terry, educating the human, and proving value.

---

## Project Structure

```
cdr/
├── README.md                  ← You are here
├── BOOTSTRAP.md               ← Node initialization protocol
├── principles.md              ← CDR Core Principles (expanded)
├── profiles/                  ← Compliance profiles by organization type
│   ├── gc-federal/            ← GC federal departments
│   │   ├── README.md
│   │   ├── itsg-33-controls.md
│   │   ├── wcag-21-aa.md
│   │   ├── gc-web-standards.md
│   │   └── gc-code-publishing.md
│   ├── gc-provincial/         ← Provincial/territorial governments
│   ├── healthcare/            ← Healthcare organizations
│   ├── municipal/             ← Municipalities
│   └── general/               ← Default / no specific framework
├── adapters/                  ← Data adapter templates
│   ├── README.md
│   ├── peoplesoft-hr.md
│   ├── sap-finance.md
│   └── generic-csv.md
├── setup/                     ← Node setup scripts
│   ├── README.md
│   ├── mac-setup.sh
│   └── linux-setup.sh
└── pitch/                     ← Concept and pitch documents
    ├── concept.md
    └── hicc-proof-of-concept.md
```

---

## The ACCORD Connection

The CDR shares architectural DNA with [ACCORD](../accord/), a parallel project that builds rules engines for collective agreements. Where ACCORD encodes labour rules, CDR encodes institutional security policies. Same pattern — different domain:

| | ACCORD | CDR |
|---|---|---|
| **Encodes** | Collective agreement rules | Institutional security policies |
| **Builds** | Labour relations tools | Compliant software tools |
| **For** | HR professionals, union reps | Developers, data analysts, IT teams |
| **Standards** | Collective agreements | ITSG-33, PHIPA, WCAG, etc. |

---

## Getting Started

### For Humans

1. Read this document
2. Run the setup script for your platform (`setup/mac-setup.sh` or `setup/linux-setup.sh`)
3. Start Ollama with a local model
4. Give terry `BOOTSTRAP.md` — it'll take it from there

### For Terrys

1. Follow `BOOTSTRAP.md` exactly
2. Complete all six phases
3. Generate your SOUL.md, CONTEXT.md, and FIRST_MISSION.md
4. Delete the bootstrap
5. Start building

---

## Current Status

**Phase: Proof of Concept**

- ✅ CDR architecture designed
- ✅ Bootstrap protocol written
- ✅ Compliance profiles created (GC Federal, Provincial, Healthcare, Municipal, General)
- ✅ Adapter templates created (PeopleSoft HR, SAP Finance, Generic CSV)
- 🔄 HICC proof of concept in progress (schema publication approval pending)
- 🔜 First external node deployment
- 🔜 Demo for deputy ministers

---

*The Canadian Digital Railway — sovereign AI for Canadian institutions.* 🚂
