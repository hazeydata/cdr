# Recipe: GC Org-Chart from PeopleSoft HR

> **First railway car** — the first reusable solution recipe in the CDR network.

---

## Summary

Build a bilingual, accessible organizational chart tool for any GC department running PeopleSoft HCM. The terry reads the PeopleSoft HR schema (Mode 2 — no data access), builds the tool, and the department deploys it on-network against live data.

**Any GC department with PeopleSoft HR can fork this recipe.**

---

## Inputs

| Input | Source | Classification |
|-------|--------|----------------|
| PeopleSoft HR schema (PS_JOB, PS_DEPT_TBL, PS_PERSONAL_DATA, PS_JOBCODE_TBL, PS_LOCATION_TBL) | Department IT publishes table structures | Unclassified (schema only — no data rows) |
| GC Federal compliance profile | `profiles/gc-federal/` | Public |
| CDR PeopleSoft HR adapter template | `adapters/peoplesoft-hr.md` | Public |
| Synthetic demo schema (for Phase 0) | `schemas/demo/hicc-hr-synthetic/schema.yaml` | Public / synthetic |

## Output Tool Shape

**Type:** Web application (static HTML/CSS/JS + Python backend)

**Features:**
- Tree-view org-chart: department → position → person
- Bilingual toggle (English / Français)
- Search by department name or job code
- Expandable/collapsible hierarchy
- Accessible: keyboard navigable, screen-reader compatible, WCAG 2.1 AA compliant
- Print-friendly view

**Data flow (on-network, after deployment):**
```
PeopleSoft HR DB → CSV export or query → Python adapter → JSON hierarchy → HTML/JS renderer
```

**Data flow (Mode 2 build, off-network):**
```
Schema YAML → Python adapter (placeholder data) → JSON hierarchy → HTML/JS renderer
```

## GC Federal Profile References

| Standard | Requirement | Implementation |
|----------|------------|----------------|
| ITSG-33 | No data exfiltration; access controls | Mode 2 build — terry never sees data; tool runs on-network only |
| WCAG 2.1 AA | Perceivable, operable, understandable, robust | Semantic HTML, keyboard nav, ARIA, contrast ratios, focus indicators |
| Official Languages Act | Bilingual (EN/FR) | All UI strings in both languages; toggle in header |
| GC Web Standards | Standard look-and-feel | GC-compatible layout (not full WET/CDTS — can be wrapped later) |

## Mode 2 Constraints

1. **Terry never connects to the department's network** — build happens off-network.
2. **Terry never sees real data** — only schema (table names, column names, types, relationships).
3. **Terry never receives query results** — no row counts, no aggregates, no samples from real data.
4. **All PII fields are structural only** — terry knows `PS_PERSONAL_DATA.FIRST_NAME` exists as `VARCHAR(30)` but never sees a real name.
5. **Deployment is human-controlled** — HICC IT (or equivalent) reviews, deploys, and connects to live data.

## Fork Instructions

To adapt this recipe for your department:

### 1. Publish your schema

Export your PeopleSoft HR table structures. You need:
- `PS_JOB` — job/position records (the hierarchy source)
- `PS_DEPT_TBL` — department definitions
- `PS_PERSONAL_DATA` — employee identity fields (structure only)
- `PS_JOBCODE_TBL` — job code lookups
- `PS_LOCATION_TBL` — location lookups

**Format:** YAML (preferred — see `schemas/demo/hicc-hr-synthetic/schema.yaml` for template) or CSV column headers.

**What to include:** table name, column name, data type, nullable, description, foreign key references.

**What NOT to include:** actual data rows, row counts, sample values, or any Protected B content.

### 2. Check for custom fields

GC departments extensively customize PeopleSoft. Note any:
- Custom columns your department added to standard tables
- Department-specific action codes or status codes
- Non-standard SETID values or business unit codes
- French-language description columns (e.g., `DESCRFRA`)

### 3. Clone the prototype

```bash
cp -r prototypes/org-chart-demo/ my-dept-org-chart/
```

### 4. Point terry at your schema

Replace the synthetic schema path with your department's published schema:

```python
# In main.py, update the schema path
SCHEMA_PATH = "path/to/your-department-schema.yaml"
```

### 5. Build and deploy

- Terry builds the tool off-network from your schema
- Your IT team reviews the generated code
- Deploy on-network, connect to PeopleSoft (CSV export or direct query)
- Run your standard security assessment

### 6. Publish back to the recipe index

If your department discovers custom patterns, schema quirks, or improvements:
- Fork this recipe
- Document what changed and why
- Submit back to the CDR recipe index (append-only — your contribution compounds for the next department)

---

## Recipe Metadata

| Field | Value |
|-------|-------|
| **Recipe ID** | `gc-org-chart-peoplesoft` |
| **Version** | 0.1.0 (Phase 0 demo) |
| **Author** | CDR / HazeyData |
| **Source system** | PeopleSoft HCM 9.x |
| **Target profile** | GC Federal (`profiles/gc-federal/`) |
| **Mode** | 2 (Schema-Only Builder) |
| **Prototype** | `prototypes/org-chart-demo/` |
| **Schema** | `schemas/demo/hicc-hr-synthetic/schema.yaml` |
| **Status** | Demo — synthetic data only |
