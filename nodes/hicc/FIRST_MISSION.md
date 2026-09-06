# First Mission: GC Org-Chart Tool from PeopleSoft HR Schema

> **Status:** DEMO — synthetic mission spec for Phase 0 prototype
> **Node:** Terry-HICC (Node 1)
> **Mode:** 2 (Schema-Only Builder)

---

## Problem

HICC staff need to understand organizational structure — who reports to whom, which teams exist, where people sit. This information lives in PeopleSoft HR (PS_JOB, PS_DEPT_TBL) but is locked behind Protected B access controls. There is no self-service org-chart tool. Staff either ask HR directly, consult outdated PDF charts, or guess. This wastes time and creates confusion during reorgs, onboarding, and cross-team coordination.

## Solution

Build a bilingual (EN/FR), accessible, GC-compliant organizational chart tool that:

1. Reads PeopleSoft HR schema (table structures, not data)
2. Generates a complete tool with data adapters for PS_JOB, PS_DEPT_TBL, PS_PERSONAL_DATA
3. Renders an interactive, navigable org-chart when connected to live data
4. Meets ITSG-33, WCAG 2.1 AA, and Official Languages Act requirements out of the box

Terry builds it off-network from the schema. HICC IT deploys it on-network, connects it to PeopleSoft, and runs it behind their security boundary.

## What I Need

**From HICC (Mode 2 — schema only):**

- PeopleSoft HR table schemas for: `PS_JOB`, `PS_PERSONAL_DATA`, `PS_DEPT_TBL`, `PS_JOBCODE_TBL`, `PS_LOCATION_TBL`
- Confirmation of any custom fields HICC has added to these tables
- Confirmation of HICC-specific action codes or status codes (or confirmation that standard GC codes apply)
- Any department-specific SETID values or business unit codes

**For Phase 0 demo:** Using synthetic schema from `schemas/demo/hicc-hr-synthetic/` — no real HICC data needed.

## What I'll Deliver

1. **Org-chart web application** — static HTML/CSS/JS with Python backend
   - Tree view of organizational hierarchy (department → position → person placeholder)
   - Bilingual toggle (EN/FR)
   - Accessible navigation (keyboard, screen reader, WCAG 2.1 AA)
   - Search by department or job code
2. **Data adapter** — Python module that reads PeopleSoft HR exports (CSV or direct query) and produces the org-chart data structure
3. **Deployment guide** — step-by-step instructions for HICC IT to deploy on-network
4. **Recipe** — published to CDR recipe index so other GC departments with PeopleSoft can fork it

## Compliance

| Standard | Requirement | How |
|----------|------------|-----|
| ITSG-33 | No data exfiltration | Mode 2 — terry never sees data |
| WCAG 2.1 AA | Accessible UI | Semantic HTML, keyboard nav, ARIA labels, sufficient contrast |
| Official Languages Act | Bilingual | EN/FR toggle on all user-facing strings |
| GC Code Publishing | Open source ready | MIT or GC-compatible license, no secrets in code |

## Estimated Build Time

- **Phase 0 demo (synthetic data):** Built — see `prototypes/org-chart-demo/`
- **Phase 1 live (real HICC schema):** 3–5 days after schema received

## What You Need to Do

1. **Phase 0 (now):** Nothing — the demo runs on synthetic schema
2. **Phase 1 (when ready):**
   - Get schema publication approved through your IT security process
   - Export PeopleSoft HR table structures (column names + types, no data rows)
   - Share exported schemas with Terry-HICC
   - After Terry builds the tool: review, test on-network, run security assessment

## Recipe Link

[`recipes/gc-org-chart-peoplesoft/RECIPE.md`](../../recipes/gc-org-chart-peoplesoft/RECIPE.md)

---

> **DEMO NOTICE:** This mission spec is a synthetic demonstration. The actual first mission will be defined during live BOOTSTRAP.md onboarding with a HICC staff member.
