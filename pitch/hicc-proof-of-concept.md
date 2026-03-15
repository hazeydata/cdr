# HICC Proof of Concept — CDR Demonstration

## Overview

The first CDR proof of concept will be built at **Housing Infrastructure Canada (HICC)**, demonstrating the complete schema-to-tool workflow in a real GC federal department.

**Goal:** Prove that an AI agent can build a compliant, deployable GC tool from a published database schema — without ever accessing Protected B data.

---

## The Plan

### Step 1: Get Schema Publication Approved

**Status:** Proposal submitted to HICC management

**What:** Approval to publish HICC's HR and Finance database schemas (structure only — table names, column names, data types, relationships) to a GC code repository.

**Document:** The one-pager proposal is at `/docs/cdr-schema-publishing-proposal.md`. It covers:
- What would be published (structural metadata only, no data)
- Why (enable open-source tool development, align with TBS directives)
- Security considerations (schemas are not Protected B)
- Precedent (GC Cloud Guardrails on GitHub, GC InfoBase datasets, PeopleSoft/SAP data models publicly documented by vendors)
- Benefit to HICC

**Key argument:** The TBS Directive on Open Government encourages publication of non-sensitive information assets. The Guide for Publishing Open Source Code directs departments to make non-sensitive information open. Schemas are structural metadata — they contain no data.

**What approval looks like:** Written confirmation from management that HICC HR and Finance database schemas (structure only) may be published to a GC code repository.

**Timeline estimate:** 2–4 weeks for review and approval

### Step 2: Publish HICC HR/Finance Schemas

**What:** Extract and publish the structural schemas from HICC's PeopleSoft HR and SAP Finance systems to GC Code.

**For PeopleSoft HR (GC HRMS):**
- Table definitions: PS_JOB, PS_PERSONAL_DATA, PS_DEPT_TBL, PS_JOBCODE_TBL, PS_LOCATION_TBL, PS_EMPLOYEES, PS_EMPLOYMENT
- Column names, data types, and relationships
- GC-specific customizations (custom fields, action codes, status codes, classification groups)
- Effective-dating patterns documented

**For SAP Finance (GCfm):**
- Table definitions for relevant FI/CO modules
- General ledger structure (ACDOCA Universal Journal)
- Cost centre hierarchy
- Chart of accounts structure
- GCfm "A" template specifics

**Output:** Schema files published to GC Code (gccode.ssc-spc.gc.ca or departmental GitHub organization)

**Timeline estimate:** 1–2 weeks after approval

### Step 3: Build the Org Chart Tool

**What:** Wilma (CDR HQ / Node 0) reads the published schemas and builds a complete organizational chart tool for HICC.

**The tool will:**
- Display HICC's organizational hierarchy (from PS_DEPT_TBL + PS_JOB reporting relationships)
- Show positions, classifications, vacancy status
- Allow filtering by department, location, classification group
- Provide search functionality
- Export to PDF/CSV
- Meet all GC compliance requirements:
  - ITSG-33 security controls (from `profiles/gc-federal/itsg-33-controls.md`)
  - WCAG 2.1 AA accessibility
  - Bilingual (English/French)
  - GCWeb theme
  - GC Code-ready repository structure

**Built from:** The published schema + PeopleSoft adapter template + GC compliance profile. No real data.

**Tech stack:**
- Python 3.11+ / Flask
- HTML/CSS/JS with WET/GCWeb
- SQLite for local data storage
- Data adapters pre-configured for PeopleSoft CSV exports
- i18n with Flask-Babel
- All dependencies bundled (sovereign — works offline)

**Timeline estimate:** 3–5 days after schemas are published

### Step 4: Submit to GC Code for Security Review

**What:** The completed tool is submitted as a GC Code repository for departmental security review.

**The repository will include:**
```
hicc-org-chart/
├── README.md                  # Bilingual
├── LICENCE.txt                # MIT + Crown copyright
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── src/                       # Application code
├── tests/                     # Test suite (with synthetic data)
├── i18n/                      # EN/FR translation files
├── docs/
│   ├── deployment-guide.md    # How to deploy on-network
│   └── data-connection.md     # How to connect real data
└── compliance/
    ├── itsg-33-assessment.md  # Control-by-control assessment
    ├── wcag-21-aa-audit.md    # Accessibility audit results
    ├── dependency-audit.md    # Third-party library analysis
    └── sast-results.md        # Static analysis results
```

**What makes this different from a normal submission:** The compliance documentation is already done. The SA&A team gets a pre-documented assessment mapped to ITSG-33 controls, not just code.

**Timeline estimate:** Security review typically 2–6 weeks (department-dependent)

### Step 5: Deploy On-Network

**What:** HICC IT clones the approved repository onto the GC network, connects it to real PeopleSoft data, and runs it.

**Steps:**
1. Clone repository from GC Code
2. Configure data adapter with real PeopleSoft connection details
3. Run initial data load
4. Verify output against known organizational structure
5. Make available to HICC users

**Timeline estimate:** 1–2 days for deployment, 1 week for testing and validation

---

## Timeline Summary

| Step | What | Estimated Time |
|------|------|----------------|
| 1 | Schema publication approval | 2–4 weeks |
| 2 | Publish schemas | 1–2 weeks |
| 3 | Build org chart tool | 3–5 days |
| 4 | Security review | 2–6 weeks |
| 5 | Deploy on-network | 1–2 weeks |
| **Total** | **End to end** | **~8–15 weeks** |

**Compare to traditional approach:** A custom org chart tool through normal IT procurement/development would typically take 6–18 months and cost $50K–$200K. The CDR approach delivers the tool in weeks, at near-zero marginal cost.

---

## What Success Looks Like

### Immediate
- A working organizational chart tool deployed at HICC
- Built from published schemas by an AI agent, without any Protected B data leaving the network
- Fully compliant with ITSG-33, WCAG 2.1 AA, Official Languages Act
- Passed departmental security review

### Strategic
- **Proof that the CDR model works.** Schema publication → AI-built tool → security review → on-network deployment. The complete workflow, proven.
- **A reusable pattern.** Every GC department that uses PeopleSoft (which is most of them) can deploy the same tool with minimal customization.
- **Precedent for schema publication.** Once HICC publishes schemas and gets a useful tool from it, other departments will want to do the same.
- **The flywheel begins.** More schemas → more tools → more value → more schemas.

### Demo Value
- Pick any GC department with PeopleSoft
- Show them the HICC org chart tool
- "We can build one for your department too. We just need your schema."
- Time from schema to tool: days, not months

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Management doesn't approve schema publication | The one-pager addresses all concerns. Schemas are not Protected B. TBS directives support publication. Escalate with evidence. |
| Security review takes too long | The pre-documented compliance assessment should speed review. Engage SA&A team early to set expectations. |
| Schema is more complex than expected | PeopleSoft adapter template covers common patterns. GC-specific customizations may need additional discovery. |
| Tool doesn't match actual data perfectly | Schema assumptions are documented with `[SCHEMA-ASSUMPTION]` tags. Deploying team validates and adjusts during Step 5. |
| Political resistance ("AI building GC tools?") | Frame as "open-source tool development using modern practices" — the AI is the builder, the output goes through normal approval. The tool, not the AI, gets deployed. |

---

## What Comes After HICC

If the proof of concept succeeds:

1. **Expand within HICC** — Build additional tools (finance dashboards, leave tracking, staffing projections)
2. **Share the org chart tool** — Other departments using PeopleSoft can adopt it (just need their schema)
3. **Document the process** — Write up the schema publication → tool deployment workflow as a repeatable guide
4. **Present to leadership** — Show deputy ministers what's possible. Demo the complete workflow.
5. **Deploy CDR nodes** — Stand up CDR nodes at additional departments, each with their own terry
6. **Build the adapter library** — Every new schema and tool adds to the CDR's capabilities

---

*The HICC proof of concept is the first stop on the Canadian Digital Railway. One department, one schema, one tool — and the proof that this model works for all of them.* 🚂
