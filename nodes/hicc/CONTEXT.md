# Context: Hamilton Immigration and Community Centre (HICC)

> **Status:** DEMO — synthetic context for Phase 0 prototype
> **This is not based on privileged HICC system information.**

---

## Organization

- **Name:** Hamilton Immigration and Community Centre (HICC)
- **Type:** Federal government — funded settlement services agency
- **Sector:** Immigration, settlement, and community integration services
- **Size:** ~100–200 staff (estimate based on public information)
- **Location:** Hamilton, Ontario, Canada

## Security Environment

- **Data classification:** Protected B (federal HR/personnel data)
- **Operating mode:** Mode 2 — Schema-Only Builder
- **Security framework:** ITSG-33 (GC Federal)
- **Network:** Terry operates off-network; tools deployed on-network by HICC IT

## Systems

- **HR:** PeopleSoft HCM 9.x (GC HRMS — standard across federal departments)
- **Finance:** SAP (GC Financial Management — assumed standard)
- **Other:** TO BE CONFIRMED on live onboarding
- **Databases:** Oracle (PeopleSoft backend — assumed standard)

## Tech Stack

- **Languages:** Python 3.11+ (terry builds); department stack TBD on onboarding
- **Frameworks:** Flask / static HTML+CSS+JS (lightweight, no heavy dependencies)
- **Deployment:** On-premise within HICC network (deployed by HICC IT, not terry)

## Compliance Requirements

- [x] ITSG-33 security controls
- [x] WCAG 2.1 AA accessibility
- [x] Official Languages Act (EN/FR bilingual)
- [ ] HICC-specific security review (pending live onboarding)
- [ ] SA&A (Security Assessment & Authorization — not started, not claimed)

## Data Sources

| Source | Accessibility | Notes |
|--------|--------------|-------|
| PeopleSoft HR (PS_JOB, PS_PERSONAL_DATA, PS_DEPT_TBL, etc.) | Schema only | Protected B — structure shared, data never leaves network |
| Organizational hierarchy | Schema only | Derived from PS_JOB.REPORTS_TO and PS_DEPT_TBL |
| Location/department lookups | Schema only | PS_LOCATION_TBL, PS_DEPT_TBL — reference data |

## Contacts

- **Primary:** TBD (assigned on live onboarding)
- **IT Contact:** TBD
- **Security Contact:** TBD

## Notes

- All system assumptions are based on standard GC PeopleSoft patterns from `adapters/peoplesoft-hr.md` and publicly available GC IT standards.
- HICC's actual PeopleSoft configuration may include custom fields, custom action codes, or departmental extensions. These will be discovered during live onboarding.
- The synthetic schema in `schemas/demo/hicc-hr-synthetic/` is inspired by public PeopleSoft documentation and the CDR adapter template. It does not contain or claim to contain real HICC data structures.

---

> **DEMO NOTICE:** This context file is a synthetic demonstration for CDR Phase 0. Real HICC system details will be populated during a live BOOTSTRAP.md onboarding session.
