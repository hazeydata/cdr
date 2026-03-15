# The Canadian Digital Railway — Concept Document

## What Is the Canadian Digital Railway?

The Canadian Digital Railway (CDR) is a network of sovereign AI agents — called "terrys" — that help organizations across Canada build compliant, accessible software tools without compromising data security.

Each terry is a local AI agent running on dedicated hardware within an organization. It gets onboarded like a new employee: it learns the organization's systems, understands its security boundaries, and builds tools within those boundaries. No data leaves the organization. No cloud services are required. The AI respects institutional rules because it was built to understand and enforce them.

The CDR connects these agents into a national network. A terry at a federal department can benefit from compliance standards documented by a terry at a provincial ministry. An adapter template built for one healthcare organization works for the next. Knowledge flows through the Railway; classified data never does.

---

## The Problem

### The Tool Gap

Every organization in Canada — from Health Canada to the Township of Woolwich — needs better software tools. Dashboards that show what's happening. Reports that don't take a week to generate. Automations that eliminate copy-paste workflows. Data analysis that actually answers questions.

But building custom tools is slow and expensive. IT backlogs at GC departments stretch months or years. Municipalities don't have the budget for custom development. Healthcare organizations are too busy keeping systems running to build new ones.

### The AI Paradox

AI could solve this. Tools like ChatGPT and GitHub Copilot can write code, build dashboards, and automate workflows in hours instead of months. But they can't work with the data that matters most:

- **Protected B data** in GC departments can't leave the government network — let alone go to an OpenAI server in the United States
- **Patient health data** under PHIPA can't be shared with cloud AI services
- **Personal information** under PIPEDA requires consent that cloud AI terms don't satisfy

Even when AI could theoretically help, the **approval process** is impossible. Getting an open-source AI system approved to operate within a Protected B environment requires the kind of security assessment and authority to operate that only Microsoft, with its billion-dollar compliance teams, can afford. Small open-source projects can't compete on that path.

So organizations are stuck: they need AI to build tools, but AI can't access their data, and getting it approved to do so is effectively impossible.

### The Reinvention Problem

Meanwhile, a hundred GC departments that all use PeopleSoft for HR and SAP for finance are each building (or failing to build) the same tools independently. An HR dashboard at Department A and an HR dashboard at Department B are essentially the same tool — but there's no mechanism to share them, because each was built with access to that department's specific data.

---

## The Solution

### The Breakthrough: Builder, Not Operator

The CDR reframes the entire relationship between AI and institutional data. The insight is simple:

**The AI doesn't need to operate on the network. It needs to build tools that operate on the network.**

A terry doesn't run inside the government network. It runs outside, on dedicated local hardware. It doesn't access classified data. It reads the **structure** of the data — the schema — and builds tools that the organization deploys on their own network, connected to their own data, through their own security review process.

The output of the AI (code, tools, documentation) goes through normal security approval. Not the AI itself. This sidesteps the impossible approval problem entirely.

### The Three Modes

Not every organization has classified data. The CDR serves all types:

**Mode 1: Full Access.** Terry has direct data access. Works with data end-to-end. For: small organizations, non-profits, personal use, organizations with no data classification restrictions.

**Mode 2: Schema-Only (Builder).** Terry is off-network. Works with structural metadata only. Builds tools that get deployed on-network by humans. For: GC federal departments, healthcare organizations, any environment with classified or regulated data.

**Mode 3: Hybrid.** Some data accessible, some restricted. Terry works directly with what it can see, builds adapters for what it can't. For: research institutions, crown corporations, mixed classification environments.

The operating mode is determined during onboarding. Terry figures out which mode is appropriate based on the organization's security context — and independently verifies it.

### The Schema Workflow (Mode 2)

This is the key innovation for Protected B environments:

1. **A department publishes its database schemas to a code repository.** Schemas are structural metadata — table names, column names, data types, relationships. Not data. Just the empty blueprint. This is already encouraged by the TBS Directive on Open Government.

2. **Terry reads the published schema** along with public compliance standards (ITSG-33, WCAG 2.1, Official Languages Act).

3. **Terry builds a complete, compliance-ready tool** with data adapters pre-configured for the schema. The tool is tested, documented, bilingual, accessible, and ready for security review.

4. **The department clones the tool onto their network**, connects it to real data, and runs their standard security review.

5. **No classified data ever leaves the network.** The AI never saw it. The tool was built from structure alone.

### Why Schemas Change Everything

Database schemas have never been published to repositories like GC Code because there was no consumer for them. Who benefits from knowing that a department's HR table has columns called `EMPLID`, `DEPTID`, and `JOBCODE`?

Terry does. Terry can take that schema and build a complete organizational chart tool, a vacancy dashboard, a staffing projection report — overnight.

This creates a **flywheel**: schemas get published → terry builds tools from them → the tools are useful → other departments see the value → more schemas get published → more tools get built → the ecosystem grows.

---

## How It's Different

### vs. Microsoft Copilot

Copilot runs in the Microsoft cloud. It requires sending data to Microsoft servers. It's approved for GC use because Microsoft invested billions in compliance certifications (FedRAMP, SOC 2, etc.). The CDR is the opposite: it runs locally, it never sees classified data, and it achieves compliance through a fundamentally different architecture (schema-only) rather than through expensive certifications.

Copilot is also generic — it doesn't understand ITSG-33, or WCAG 2.1 AA, or the Official Languages Act, or your department's specific PeopleSoft configuration. Terry does, because terry was onboarded with that context.

### vs. ChatGPT / Claude / General AI

General-purpose AI assistants are useful but they have no institutional context. They don't know your security framework, your compliance requirements, your tech stack, or your data structures. Every conversation starts from zero. Terry has persistent context — it knows your organization, your systems, and your constraints. It builds within your boundaries automatically.

### vs. Custom Development

Custom development is the current approach and it works — but it's slow, expensive, and siloed. Every department hires developers, builds tools from scratch, and maintains them independently. The CDR accelerates this: terry builds the first draft (complete with compliance documentation) in days instead of months, and the adapter pattern means tools are reusable across organizations with similar systems.

### vs. Low-Code / No-Code Platforms

Platforms like Power Apps provide drag-and-drop tool building but they still require data access and they produce proprietary outputs. CDR tools are open source, compliance-documented, and built on standard technologies that any developer can maintain.

---

## The Onboarding Model

When a new CDR node comes online, it runs through a structured bootstrap — a 15-minute conversation that is simultaneously:

1. **Configuring terry** — learning the organization, systems, security context, and detecting the operating mode
2. **Educating the human** — teaching them how the CDR works and what to expect
3. **Proving value** — by the end of the conversation, terry has already proposed a first project based on the human's actual pain points

The bootstrap produces three files:
- **SOUL.md** — Terry's identity, principles, and operating rules
- **CONTEXT.md** — The organization's technical and security profile
- **FIRST_MISSION.md** — A concrete first project with a plan

Then the bootstrap deletes itself. Terry is born.

---

## Trust But Verify

The usual question about AI in institutions is: "Can we trust AI with our data?"

The CDR flips this: **Terry doesn't trust the human's data classification. Terry verifies independently.**

Before processing any data, terry:
- Checks the network environment (IP lookup, reverse DNS)
- Looks up the organization's published security policies
- Scans data for PII and sensitive patterns (SINs, health data, financial records)
- Flags any inconsistency between claimed classification and observed data

If the data looks more sensitive than the human claims, terry STOPS and clarifies. Every time. No exceptions.

This makes terry the **last line of defence** before a compliance breach — and it makes terry safer than a human employee who might not notice they're looking at something they shouldn't be.

---

## The ACCORD Connection

The CDR is architecturally related to ACCORD, a project that builds rules engines for collective agreements. The pattern is the same:

| | ACCORD | CDR |
|---|---|---|
| **Domain** | Labour relations | Institutional security |
| **Encodes** | Collective agreement rules | Compliance frameworks (ITSG-33, PHIPA, etc.) |
| **Produces** | Labour relations tools | Compliant software tools |
| **For** | HR professionals, union reps | Developers, analysts, IT teams |

ACCORD proves the pattern works: encode institutional rules as machine-readable frameworks, then build tools that automatically comply with those rules. CDR applies the same pattern to security and accessibility compliance.

---

## The Demo

The CDR's value proposition can be demonstrated live:

1. Pick a random GC department
2. Pick a random operational problem (HR reporting, financial analysis, service delivery tracking)
3. Terry reads the department's published schema and compliance standards
4. Terry builds a complete, GC Code-ready, ITSG-33-compliant tool — live, in front of the audience
5. The output is a working repository: code, tests, compliance documentation, bilingual UI, accessibility compliance
6. Ready to clone on-network and deploy

**Time to build:** Minutes. **Time the department has been waiting for this tool:** Months or years.

---

## The Roadmap

### Phase 1: Proof of Concept (Current)
- Prove the model at HICC (Housing Infrastructure Canada)
- Get schema publication approved (proposal submitted)
- Build org chart tool from published HR schemas
- Submit to GC Code, pass security review, deploy on-network

### Phase 2: Expand Within GC
- Deploy CDR nodes at additional GC departments
- Build adapter library for common GC systems (PeopleSoft, SAP, etc.)
- Document the schema publication process as a repeatable pattern
- Present results to deputy ministers

### Phase 3: Provincial and Municipal
- Extend compliance profiles to provincial security frameworks
- Deploy nodes at provincial ministries and municipalities
- Adapt healthcare compliance profile for hospital systems
- Build open data tools for municipal governments

### Phase 4: National Network
- CDR nodes across Canada — federal, provincial, municipal, healthcare, education, non-profit
- Shared compliance standards, adapter libraries, and best practices
- The Railway is operational: a national network of sovereign AI agents, each serving its organization while contributing to the whole

---

## Why "The Canadian Digital Railway"

Canada was built by the railway. It connected communities across vast distances, enabled commerce and communication, and made the country function as a unified whole.

The Canadian Digital Railway does the same thing for the digital age. It connects institutional AI agents across organizations, enables sharing of knowledge and tools, and makes Canada's digital infrastructure function as a unified whole — while respecting the sovereignty of every community it serves.

Every node is sovereign. The network makes them stronger.

---

*The Canadian Digital Railway — sovereign AI for Canadian institutions.* 🚂
