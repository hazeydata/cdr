# CDR Cross-Pollination Map
## HazeyData Projects as Proto-CDR Infrastructure

**Created:** 2026-04-02 (Session 2)
**Author:** Barney
**Purpose:** Map existing HazeyData operational patterns to CDR architecture components so we mine real code and processes when building CDR-OS, rather than starting from scratch.

---

## The Insight

Every HazeyData project is a pseudo-node on the Canadian Digital Railway. Each one has data pipelines, quality gates, audit logging, agent coordination, and governance structures. The patterns Fred and the agents have built through SSD, WTI, ACCORD, and HICC are proto-CDR infrastructure — they just weren't designed with that label.

When CDR-OS development begins, this document is the extraction inventory.

---

## Pattern Map

### Governance & Process

| HazeyData Pattern | CDR Equivalent | Source | Notes |
|---|---|---|---|
| Audit & Redesign Playbook (8 phases) | Terry onboarding (BOOTSTRAP.md, 6 phases) | operations repo | Same DNA: assess → audit → design → review → implement → validate |
| 4-tier architecture (Fred/Barney/Dino/Wilma) | Node governance model | operations repo | Strategy / orchestration / execution / compute separation |
| SESSION_LOG.md (shared project memory) | SOUL.md + CONTEXT.md (node identity + state) | all projects | Persistent state across sessions = persistent node identity |
| GitHub as governing spec ("spec wins over code") | CDR-OS governance layer | all projects | Signed, versioned, auditable governing documents |
| Rule 17: proof-batch-first | Principle 6: Trust but verify | all projects | Small sample → human review → scale. Never trust summary stats. |
| Discord inter-agent messaging | Inter-node mesh communication | all projects | Lightweight, async, multi-agent coordination |

### Data Pipelines

| HazeyData Pattern | CDR Equivalent | Source | Notes |
|---|---|---|---|
| SSD pipeline (scrape → extract → validate → store) | Terry data processing pattern | data-hub | Tiered collection (cheap → expensive), quality gates at each stage |
| WTI confidence scoring | Terry quality/confidence assessment | TPCR | Every extracted value gets a quality score — not just pass/fail |
| Tiered API approach (Sonnet → Opus, HTTP → Firecrawl) | Terry resource optimization | SSD, WTI | Start cheap, escalate only on failure. Cost discipline. |
| Background jobs in screen/nohup | Terry long-running task management | all projects | Agent sessions crash; background jobs survive |
| Cron scheduling + automated reporting | Terry scheduled operations | all projects | Automated execution + daily status reports to Discord |

### Compliance & Security

| HazeyData Pattern | CDR Equivalent | Source | Notes |
|---|---|---|---|
| ACCORD CA rules engine | CDR compliance profile engine | accord | Same architecture: encode institutional rules as machine-readable standards |
| HICC Homelessness Dashboard (Mode 2 build) | **De facto CDR Mode 2 demo** | CDR/HICC | Barney built a GC-compliant tool off-network using schema-only approach |
| HICC Open Source Code Publishing Guidelines | CDR open-source governance reference | CDR references/ | GC rules for sharing code on GitHub — directly applicable |
| Evidence over claims ("100% success means nothing") | Audit log integrity principle | all projects | CDR audit logs must be independently verifiable, not self-reported |

### Knowledge Sharing

| HazeyData Pattern | CDR Equivalent | Source | Notes |
|---|---|---|---|
| Playbook as repeatable process doc | CDR-OS documentation standards | operations repo | Codified methodology that any agent can follow |
| Cross-project learnings (SSD bugs informing WTI design) | Inter-node knowledge sharing (the Flywheel) | all projects | Station 1 builds → shares → Station 2 adapts → improvements flow back |
| Agent specialization (Barney=strategy, Dino=orchestration, Wilma=compute, Gazoo=audit, Pebbles=visual) | Terry capability modules | operations repo | Different terrys may specialize based on institution type |

---

## The HICC Homelessness Dashboard as CDR Demo

This deserves special attention. The Homelessness Dashboard work is the strongest proof-of-concept material CDR has, because it IS a CDR deployment:

- **Mode 2 (Schema-Only Builder):** Barney worked off-network, never touching real Protected B data
- **Compliant by default:** Built to GC standards from the first line
- **Transparent:** Code is readable, process is explainable
- **Sovereign:** Tool runs locally within HICC's security boundary
- **Trust but verify:** Data classification was respected throughout

When pitching CDR to deputy ministers or ISED, this is the story: "We already did this. Here's what it looked like. Now imagine every department has one."

---

## Extraction Priority (When CDR-OS Build Begins)

Ordered by what to extract first:

1. **Audit & Redesign Playbook → Terry onboarding automation** — The 8-phase playbook can be encoded as Terry's self-guided setup process
2. **ACCORD compliance rules engine → CDR compliance profiles** — Same parsing/application architecture, different rule domain
3. **SSD/WTI pipeline patterns → Terry data processing templates** — Tiered collection, quality gates, confidence scoring
4. **SESSION_LOG pattern → Node state persistence** — How terrys maintain identity and context across sessions
5. **Discord messaging patterns → Inter-node communication protocol** — Message formats, channel structure, async coordination

---

## Open Questions

- How much of the tier architecture translates to a single-node terry? (A terry is more like a collapsed Barney+Dino+Wilma than a full 4-tier system)
- Should ACCORD and CDR share a common compliance engine, or are they different enough to stay separate?
- Can the HICC Homelessness Dashboard be packaged as a CDR case study with HICC's permission?

---

*This is a living document. Update as new patterns emerge from project work.*

*Barney — Chief of Pipeline, Slate Rock & Gravel Co. 🪨*
