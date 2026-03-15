# GC Federal Compliance Profile

**For:** Government of Canada federal departments and agencies
**Default Operating Mode:** Mode 2 (Schema-Only) unless explicitly cleared for Mode 1 or Mode 3
**Security Framework:** ITSG-33 (Protected B / Medium Integrity / Medium Availability)

---

## Overview

This profile covers the compliance requirements for building software tools for Government of Canada federal departments. It is the most prescriptive CDR profile because GC federal departments operate under the most comprehensive set of standards.

**When a CDR node is onboarded at a GC federal department, it loads this profile and follows every requirement listed here. These are not suggestions.**

---

## Applicable Standards

### Mandatory (Non-Negotiable)

| Standard | What It Covers | Reference |
|---|---|---|
| **ITSG-33** | Information security controls | `itsg-33-controls.md` |
| **WCAG 2.1 Level AA** | Web accessibility | `wcag-21-aa.md` |
| **Official Languages Act** | Bilingual (English/French) requirements | `gc-web-standards.md` |
| **GC Web Standards** | Canada.ca design, FIP, WET/GCWeb | `gc-web-standards.md` |
| **GC Code Publishing** | Open source requirements, licensing | `gc-code-publishing.md` |
| **Privacy Act** | Personal information handling | See ITSG-33 for technical controls |
| **Directive on Management of IT** | Open source by default | `gc-code-publishing.md` |

### Best Practice (Strongly Recommended)

| Standard | What It Covers |
|---|---|
| **GC Digital Standards** | User-centred design, iterative development, open by default |
| **GC Cloud Guardrails** | Cloud-specific security controls (if deploying to GC Cloud) |
| **OWASP Top 10** | Web application security risks |
| **OWASP ASVS** | Application security verification standard |

---

## Default Operating Mode: Mode 2 (Schema-Only)

GC federal departments typically handle Protected B data. Unless a specific dataset has been confirmed as Unclassified and the department has explicitly approved direct data access, **default to Mode 2.**

### What Mode 2 Means for GC Federal

1. **You never access real data.** You work with schemas published to GC Code (gccode.ssc-spc.gc.ca or GitHub).
2. **You build complete, GC Code-ready tools.** Every output includes compliance documentation.
3. **The department deploys on-network.** They clone your repo, connect real data, run SA&A.
4. **No Protected B data ever leaves the GC network.**

### When Mode 1 or Mode 3 Might Apply

- **Mode 1:** The department has explicitly confirmed that specific data is Unclassified AND you're running on the same machine/network as the data AND there are no additional access restrictions.
- **Mode 3:** The department works with a mix of Unclassified (accessible) and Protected B (not accessible) data.

**Always verify independently.** Even if a human says data is Unclassified, scan for PII patterns before processing.

---

## Common GC Enterprise Systems

Most GC departments use these systems. Adapter templates are available:

### PeopleSoft HCM 9.x (GC HRMS)
- **What:** The Government of Canada's standard HR system
- **Data:** Employee records, job history, organizational structure, leave, compensation
- **Adapter:** `adapters/peoplesoft-hr.md`
- **Key tables:** PS_JOB, PS_PERSONAL_DATA, PS_DEPT_TBL, PS_EMPLOYEES
- **Note:** PeopleSoft uses effective-dating for historical records. The adapter template includes the standard query pattern.

### SAP S/4HANA Finance (GCfm)
- **What:** The Government of Canada's financial management solution
- **Data:** General ledger, accounts payable/receivable, cost centres, budgets, commitments
- **Adapter:** `adapters/sap-finance.md`
- **Key tables:** ACDOCA (Universal Journal), BKPF/BSEG, KNA1/LFA1, CSKS
- **Note:** The GC runs the GCfm "A" template developed by TBS Office of the Comptroller General.

### Other Common Systems
- **GCdocs:** Document management (OpenText Content Server)
- **GCcase:** Case management
- **GCcollab/GCconnex:** Collaboration platforms
- **Phoenix:** Pay system (PeopleSoft-based)
- **MyGCHR:** HR self-service portal

---

## Compliance Checklist for Every GC Federal Tool

Before a CDR-built tool is submitted for GC deployment, verify ALL of the following:

### Security (ITSG-33)
- [ ] All controls in `itsg-33-controls.md` addressed (controls not applicable are documented as N/A with justification)
- [ ] No credentials, API keys, or tokens in source code
- [ ] No Protected B data in the repository (including test data)
- [ ] All inputs validated server-side
- [ ] All outputs encoded to prevent XSS
- [ ] All database queries parameterized
- [ ] Session management meets ITSG-33 requirements
- [ ] Authentication meets ITSG-33 requirements (MFA support for PB)
- [ ] Encryption at rest and in transit (AES-256, TLS 1.2+)
- [ ] Audit logging for all security-relevant events
- [ ] HTTP security headers set (HSTS, CSP, X-Content-Type-Options, etc.)
- [ ] Dependency vulnerability scan clean (`pip-audit`, `npm audit`, etc.)
- [ ] SAST scan clean (Bandit, Semgrep, etc.)

### Accessibility (WCAG 2.1 AA)
- [ ] All criteria in `wcag-21-aa.md` met
- [ ] Keyboard navigation works for all functionality
- [ ] Screen reader testing completed (NVDA or VoiceOver)
- [ ] Colour contrast meets minimum ratios (4.5:1 normal text, 3:1 large text)
- [ ] Content reflows at 320px width
- [ ] All form elements have visible labels
- [ ] All images have alt text
- [ ] Focus indicators visible on all interactive elements
- [ ] WET/GCWeb components used where possible (pre-tested for accessibility)

### Official Languages
- [ ] All UI text available in English and French
- [ ] Language toggle in header
- [ ] Both language versions launched simultaneously (not English-first)
- [ ] French version is equal quality (not machine-translated-and-shipped)
- [ ] Date formats respect locale (March 15, 2026 / 15 mars 2026)
- [ ] Error messages, validation text, and notifications are bilingual
- [ ] `<html lang="">` attribute correctly set per page language
- [ ] Mixed-language content marked with `lang` attribute
- [ ] i18n implemented from day one (no hardcoded strings)

### GC Web Standards
- [ ] Canada.ca design (GCWeb theme) for public-facing applications
- [ ] GC header with FIP signature
- [ ] GC footer with required links and wordmark
- [ ] Responsive design (mobile-friendly)
- [ ] HTML5, UTF-8 encoding
- [ ] Noto Sans font (GCWeb default)

### Open Source / Publishing
- [ ] `LICENCE.txt` with chosen OSS licence + Crown copyright notice
- [ ] `README.md` (bilingual)
- [ ] `CONTRIBUTING.md`
- [ ] `SECURITY.md` with vulnerability reporting process
- [ ] `CODE_OF_CONDUCT.md`
- [ ] `.gitignore` appropriate for tech stack
- [ ] No secrets in git history
- [ ] Compliance documentation in `compliance/` directory

---

## Security Assessment and Authorization (SA&A)

Tools built by CDR nodes still require departmental security assessment before deployment. The CDR advantage: the tool arrives with compliance documentation already written, mapped to specific ITSG-33 controls.

### What CDR Provides for SA&A

1. **Security controls mapping** — Each ITSG-33 control addressed with specific code references
2. **Threat assessment** — Common threats addressed in the design
3. **Dependency analysis** — All third-party libraries documented with licence and vulnerability status
4. **Architecture documentation** — How the application is structured and why
5. **Test results** — SAST scan results, accessibility audit results, dependency audit results

### What the Department Provides

1. **Authority to Operate** — Departmental sign-off
2. **Network assessment** — How the tool fits in their network architecture
3. **Data flow documentation** — How real data connects (this is the only part that touches actual data)
4. **Risk acceptance** — Any residual risks accepted by the department

---

## References

- [ITSG-33 Annex 3A — Security Control Catalogue](https://www.cyber.gc.ca/en/guidance/annex-3a-security-control-catalogue-itsg-33)
- [ITSG-33 Annex 4A — Profile 1 (PB/MI/MA)](https://www.cyber.gc.ca/en/guidance/annex-4a-profile-1-protected-b-medium-integrity-medium-availability-itsg-33)
- [GC Digital Standards](https://www.canada.ca/en/government/system/digital-government/government-canada-digital-standards.html)
- [Directive on Management of IT](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249)
- [Standard on Web Accessibility](http://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=23601)
- [Official Languages Act](https://laws-lois.justice.gc.ca/eng/acts/o-3.01/)
- [Guide for Publishing Open Source Code](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/open-source-software/guide-for-publishing-open-source-code.html)

---

*GC federal tools are held to the highest standard. Every output from a CDR node in this profile meets all requirements listed above. No exceptions.*
