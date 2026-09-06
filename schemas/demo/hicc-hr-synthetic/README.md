# Synthetic HICC-like PeopleSoft HR Schema

> **DEMO / SYNTHETIC DATA — NOT REAL HICC DATA**
>
> This schema is inspired by publicly documented Oracle PeopleSoft HCM 9.x table patterns
> and the CDR adapter template at `adapters/peoplesoft-hr.md`. It does not contain, reproduce,
> or claim to reproduce any real HICC database structure, configuration, or data.

## Purpose

Demonstrates the CDR Mode 2 (Schema-Only Builder) pattern: a terry reads this schema and
builds a functional org-chart tool without ever seeing real employee data.

## Files

| File | Description |
|------|-------------|
| `schema.yaml` | Full synthetic schema — tables, columns, types, relationships |
| `README.md` | This file |

## Tables Included

| Table | Description | Inspired By |
|-------|-------------|-------------|
| `PS_PERSONAL_DATA` | Employee master record (structure only) | Public PeopleSoft HCM docs |
| `PS_JOB` | Job/position record with effective dating | Public PeopleSoft HCM docs |
| `PS_DEPT_TBL` | Department hierarchy | Public PeopleSoft HCM docs |
| `PS_JOBCODE_TBL` | Job code definitions | Public PeopleSoft HCM docs |
| `PS_LOCATION_TBL` | Location reference data | Public PeopleSoft HCM docs |
| `PS_EMPLOYMENT` | Employment record (hire/term dates) | Public PeopleSoft HCM docs |

## Usage

```bash
# Read from Python
import yaml
with open("schema.yaml") as f:
    schema = yaml.safe_load(f)

# List tables
for table in schema["tables"]:
    print(table["name"], "-", table["description"])
```

## What This Is Not

- **Not real HICC data or schema** — entirely synthetic
- **Not an Oracle product** — inspired by public documentation only
- **Not Protected B** — contains no classified information
- **Not a claim of publication** — HICC has not published any schema
