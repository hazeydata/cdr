# GC Code Publishing Requirements

> **Source:** [Guide for Publishing Open Source Code](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/open-source-software/guide-for-publishing-open-source-code.html)
> **Policy:** [Directive on Management of IT](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249) (C.2.3.8, C.2.3.9.5)
> **CDR Context:** All CDR-built tools for GC departments must be publishable to GC Code or a public repository

---

## Core Principle

The GC Directive on Management of IT mandates that **all source code must be released under an appropriate open source software licence**. Open source by default.

---

## Publishing Steps

### 1. Obtain Approval
- [ ] Department or agency approval for open source release
- [ ] Delegation to lowest level possible (to speed releases)
- [ ] Plan for open source from project inception

### 2. Verify Rights
**GC employee code:**
- [ ] Crown Copyright applies automatically (Copyright Act, section 12)
- [ ] Employees retain moral rights

**Contractor code:**
- [ ] Verify licence terms allow open source publication
- [ ] Ensure procurement contract grants Crown the right to release under OSS licence

### 3. Security Review
- [ ] No credentials, API keys, passwords, or tokens in source code
- [ ] No connection strings or infrastructure details
- [ ] No Protected B or higher classified information
- [ ] No personally identifiable information (PII)
- [ ] No real test data — synthetic only
- [ ] Automated secret scanning (`git-secrets`, `truffleHog`, `detect-secrets`)
- [ ] Automated vulnerability scanning
- [ ] Git history clean (no secrets in old commits)

### 4. Choose a Licence

#### Recommended Permissive (CDR Default)
| Licence | When |
|---------|------|
| **MIT** | Small projects, scripts, utilities |
| **Apache 2.0** | Larger projects (includes patent grant) |

#### Recommended Reciprocal
| Licence | When |
|---------|------|
| **GPL 3.0+** | Applications where derivatives should stay open |
| **LGPL 3.0+** | Libraries |
| **AGPL 3.0+** | Web applications and services |

**CDR default for GC web applications:** MIT or Apache 2.0 (maximizes reuse across departments)

**Important:** Check dependency licences for compatibility. Can't use MIT if project includes GPL components.

### 5. Choose Repository

| Platform | Use For |
|----------|---------|
| **GitHub** (github.com) | Most common for public GC projects |
| **GitLab** (gitlab.com) | Alternative public platform |
| **GCcode** (gccode.ssc-spc.gc.ca) | Internal GC — not publicly accessible |

Organize under departmental organization/group on the platform.

### 6. Required and Recommended Files

#### Required

| File | Contents |
|------|----------|
| `LICENCE.txt` | Full licence text + Crown copyright notice |

#### CDR Standard (Treat as Required)

| File | Contents |
|------|----------|
| `README.md` | Bilingual project overview, installation, usage |
| `CONTRIBUTING.md` | How to contribute |
| `SECURITY.md` | Security policy, vulnerability reporting |
| `CODE_OF_CONDUCT.md` | Values and ethics |

#### Crown Copyright Notice
```
Copyright (c) His Majesty the King in Right of Canada, as represented
by the Minister of [Legal Departmental Name], [Year of Publication].
```

### 7. Bilingual Requirements

**Must be bilingual:**
- [ ] README.md (or separate README-en.md / README-fr.md)
- [ ] End-user documentation
- [ ] Application UI text

**Can be English-only:**
- Source code and comments
- CONTRIBUTING.md (bilingual recommended)
- Technical API docs
- Commit messages

**Recommended README pattern:**
```markdown
# Project Name / Nom du projet

([English](#english) | [Français](#français))

## English
### Overview
...

---

## Français
### Aperçu
...
```

### 8. Work in the Open
- [ ] Release early, release often
- [ ] Public repository is single source of truth
- [ ] Branch protection on main branch
- [ ] Review all contributions before merging
- [ ] Use full name and GC email for contributions

### 9. Register
- [ ] Add project to [Open Resource Exchange](https://canada-ca.github.io/ore-ero/en/index.html)

---

## CDR Standard Repository Structure

Every CDR tool ships with this structure:

```
project-name/
├── README.md                  # Bilingual (EN/FR) overview
├── LICENCE.txt                # OSS licence + Crown copyright
├── CONTRIBUTING.md            # How to contribute
├── SECURITY.md                # Security policy + vulnerability reporting
├── CODE_OF_CONDUCT.md         # Values and ethics
├── .gitignore                 # Tech-stack-appropriate
├── .github/
│   ├── workflows/
│   │   ├── ci.yml             # CI: tests, lint, security scan
│   │   └── security.yml       # Dependency vulnerability scanning
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── src/                       # Source code
├── tests/                     # Test suite
├── docs/                      # Documentation
├── i18n/                      # Internationalization
│   ├── en/
│   └── fr/
└── compliance/                # Compliance documentation
    ├── itsg-33-assessment.md
    ├── wcag-21-aa-audit.md
    └── dependency-audit.md
```

---

## Pre-Publication Checklist

```bash
# Search for secrets
grep -rn "password\|secret\|api_key\|token\|private_key" \
  --include="*.py" --include="*.js" --include="*.yml" --include="*.env" .

# Check .gitignore includes .env
grep -q "\.env" .gitignore || echo "WARNING: .env not in .gitignore"

# Dependency scan
pip-audit  # Python
npm audit  # Node.js

# SAST scan
bandit -r src/  # Python
```

---

## References

- [Guide for Publishing Open Source Code](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/open-source-software/guide-for-publishing-open-source-code.html)
- [Directive on Management of IT](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249)
- [Template Repository](https://github.com/canada-ca/template-gabarit)
- [Open Resource Exchange](https://canada-ca.github.io/ore-ero/en/index.html)
- [Guide for Contributing to OSS](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/open-source-software/guide-for-contributing-to-open-source-software.html)

---

*Open source by default. Build in the open. Ship for Canada.*
