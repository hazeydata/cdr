# PeopleSoft HRMS Adapter Template

> **System:** PeopleSoft HCM 9.x (GC HRMS)
> **Common Users:** GC federal departments (mandated by Treasury Board)
> **CDR Modes:** Mode 2 (Schema-Only) for federal departments; Mode 1/3 possible for non-GC PeopleSoft users
> **Classification:** Schema patterns only — no Protected B data

---

## Overview

PeopleSoft HCM is the Government of Canada's standard HR system (GC HRMS). Most federal departments use it for employee records, job history, organizational structure, leave management, and compensation. This adapter covers the core tables and query patterns you'll need.

**You will never connect to PeopleSoft directly in Mode 2.** Departments provide CSV exports or schema documentation. This template helps you understand the data structures and build tools that work with them.

---

## Core Tables

### PS_PERSONAL_DATA — Employee Master Record

| Field | Type | Description |
|-------|------|-------------|
| `EMPLID` | VARCHAR(11) | Employee ID — **primary key for most HR joins** |
| `NAME` | VARCHAR(50) | Full name (format: "Last,First Middle") |
| `LAST_NAME` | VARCHAR(30) | Last name |
| `FIRST_NAME` | VARCHAR(30) | First name |
| `MIDDLE_NAME` | VARCHAR(30) | Middle name |
| `NAME_PREFIX` | VARCHAR(4) | Prefix (Mr, Ms, Dr) |
| `NAME_SUFFIX` | VARCHAR(15) | Suffix (Jr, Sr) |
| `SEX` | CHAR(1) | Gender (M/F/U) |
| `BIRTHDATE` | DATE | Date of birth |
| `CITY` | VARCHAR(30) | City |
| `STATE` | VARCHAR(6) | Province/state code |
| `POSTAL` | VARCHAR(12) | Postal code |
| `COUNTRY` | VARCHAR(3) | Country code |
| `PHONE` | VARCHAR(24) | Phone |
| `EMAIL_ADDR` | VARCHAR(70) | Email |
| `LANG_CD` | VARCHAR(3) | Language code (ENG/FRA for GC) |

**⚠️ Protected B.** This table contains personal information. In Mode 2, you work with the schema only.

### PS_JOB — Job/Position Record (Most Important Table)

Stores complete job history using **effective dating** — multiple rows per employee, each representing a job action.

| Field | Type | Description |
|-------|------|-------------|
| `EMPLID` | VARCHAR(11) | Employee ID |
| `EMPL_RCD` | SMALLINT | Employment record number (0 = primary job) |
| `EFFDT` | DATE | Effective date of this action |
| `EFFSEQ` | SMALLINT | Sequence (for multiple actions on same date) |
| `ACTION` | VARCHAR(3) | Action code (HIR, PRO, TER, etc.) |
| `ACTION_REASON` | VARCHAR(3) | Reason for action |
| `DEPTID` | VARCHAR(10) | Department ID |
| `JOBCODE` | VARCHAR(6) | Job code |
| `POSITION_NBR` | VARCHAR(8) | Position number |
| `LOCATION` | VARCHAR(10) | Location code |
| `COMPANY` | VARCHAR(3) | Company code |
| `BUSINESS_UNIT` | VARCHAR(5) | Business unit |
| `EMPL_STATUS` | CHAR(1) | Status (A/I/T/R/D/S/L/P/Q) |
| `HR_STATUS` | CHAR(1) | HR status (A/I) |
| `FULL_PART_TIME` | CHAR(1) | Full/Part time (F/P) |
| `REG_TEMP` | CHAR(1) | Regular/Temporary (R/T) |
| `STD_HOURS` | DECIMAL(6,2) | Standard hours |
| `GRADE` | VARCHAR(3) | Pay grade |
| `STEP` | SMALLINT | Step within grade |
| `COMPRATE` | DECIMAL(18,6) | Compensation rate |
| `SUPERVISOR_ID` | VARCHAR(11) | Supervisor's employee ID |
| `REPORTS_TO` | VARCHAR(8) | Reports-to position number |

**Critical Pattern — Current Job Query:**
```sql
SELECT J.*
FROM PS_JOB J
WHERE J.EMPLID = :emplid
  AND J.EMPL_RCD = 0
  AND J.EFFDT = (
    SELECT MAX(J2.EFFDT) FROM PS_JOB J2
    WHERE J2.EMPLID = J.EMPLID
      AND J2.EMPL_RCD = J.EMPL_RCD
      AND J2.EFFDT <= CURRENT_DATE
  )
  AND J.EFFSEQ = (
    SELECT MAX(J3.EFFSEQ) FROM PS_JOB J3
    WHERE J3.EMPLID = J.EMPLID
      AND J3.EMPL_RCD = J.EMPL_RCD
      AND J3.EFFDT = J.EFFDT
  )
```

### PS_EMPLOYMENT — Employment Record

| Field | Type | Description |
|-------|------|-------------|
| `EMPLID` | VARCHAR(11) | Employee ID |
| `EMPL_RCD` | SMALLINT | Employment record number |
| `HIRE_DT` | DATE | Original hire date |
| `REHIRE_DT` | DATE | Most recent rehire date |
| `TERMINATION_DT` | DATE | Termination date |
| `LAST_DATE_WORKED` | DATE | Last date worked |
| `SERVICE_DT` | DATE | Service date (seniority) |

### PS_EMPLOYEES — Denormalized Snapshot

Pre-joined view of PS_PERSONAL_DATA + current PS_JOB. Avoids effective-dating complexity. Batch-refreshed, not real-time.

| Field | Type | Description |
|-------|------|-------------|
| `EMPLID` | VARCHAR(11) | Employee ID |
| `NAME` | VARCHAR(50) | Full name |
| `DEPTID` | VARCHAR(10) | Current department |
| `JOBCODE` | VARCHAR(6) | Current job code |
| `EMPL_STATUS` | CHAR(1) | Current status |
| `LOCATION` | VARCHAR(10) | Current location |
| `COMPRATE` | DECIMAL(18,6) | Current compensation |

---

## Lookup Tables

### PS_DEPT_TBL — Department Hierarchy

| Field | Type | Description |
|-------|------|-------------|
| `SETID` | VARCHAR(5) | Set ID |
| `DEPTID` | VARCHAR(10) | Department ID |
| `EFFDT` | DATE | Effective date |
| `DESCR` | VARCHAR(30) | Department name |
| `DESCRSHORT` | VARCHAR(10) | Short name |
| `MANAGER_ID` | VARCHAR(11) | Manager employee ID |
| `LOCATION` | VARCHAR(10) | Default location |

### PS_JOBCODE_TBL — Job Codes

| Field | Type | Description |
|-------|------|-------------|
| `SETID` | VARCHAR(5) | Set ID |
| `JOBCODE` | VARCHAR(6) | Job code |
| `EFFDT` | DATE | Effective date |
| `DESCR` | VARCHAR(30) | Job title |
| `SAL_ADMIN_PLAN` | VARCHAR(4) | Salary admin plan |
| `GRADE` | VARCHAR(3) | Default grade |

### PS_LOCATION_TBL — Locations

| Field | Type | Description |
|-------|------|-------------|
| `SETID` | VARCHAR(5) | Set ID |
| `LOCATION` | VARCHAR(10) | Location code |
| `EFFDT` | DATE | Effective date |
| `DESCR` | VARCHAR(30) | Location name |
| `ADDRESS1` | VARCHAR(55) | Address |
| `CITY` | VARCHAR(30) | City |
| `STATE` | VARCHAR(6) | Province |
| `POSTAL` | VARCHAR(12) | Postal code |

---

## GC-Specific Reference Data

### Action Codes
| Code | Meaning |
|------|---------|
| `HIR` | Hire |
| `REH` | Rehire |
| `PRO` | Promotion |
| `DEM` | Demotion |
| `TER` | Termination |
| `RET` | Retirement |
| `XFR` | Transfer |
| `LOA` | Leave of Absence |
| `RFL` | Return from Leave |
| `PAY` | Pay Rate Change |
| `POS` | Position Change |

### Employee Status Codes
| Code | Meaning |
|------|---------|
| `A` | Active |
| `I` | Inactive (on leave) |
| `T` | Terminated |
| `R` | Retired |
| `D` | Deceased |
| `S` | Suspended |
| `L` | Leave of Absence |
| `P` | Leave With Pay |
| `Q` | Leave Without Pay |

### GC Classification Groups
| Group | Description |
|-------|-------------|
| `CS` | Computer Systems (IT) |
| `EX` | Executive |
| `AS` | Administrative Services |
| `PM` | Programme Administration |
| `EC` | Economics |
| `FI` | Financial Management |
| `PE` | Personnel Administration |
| `IS` | Information Services |
| `CR` | Clerical and Regulatory |

---

## Adapter Code

### CSV Export Adapter

```python
import csv
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Employee:
    """Represents a PeopleSoft employee record."""
    emplid: str
    name: str
    deptid: str
    jobcode: str
    location: str
    empl_status: str
    hire_dt: Optional[date]
    comprate: Optional[float]
    supervisor_id: Optional[str] = None
    reports_to: Optional[str] = None
    
    @classmethod
    def from_csv_row(cls, row: dict) -> 'Employee':
        return cls(
            emplid=row.get('EMPLID', '').strip(),
            name=row.get('NAME', '').strip(),
            deptid=row.get('DEPTID', '').strip(),
            jobcode=row.get('JOBCODE', '').strip(),
            location=row.get('LOCATION', '').strip(),
            empl_status=row.get('EMPL_STATUS', '').strip(),
            hire_dt=cls._parse_date(row.get('HIRE_DT', '')),
            comprate=cls._parse_decimal(row.get('COMPRATE', '')),
            supervisor_id=row.get('SUPERVISOR_ID', '').strip() or None,
            reports_to=row.get('REPORTS_TO', '').strip() or None,
        )
    
    @staticmethod
    def _parse_date(val: str) -> Optional[date]:
        val = val.strip()
        if not val:
            return None
        for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%d-%b-%Y', '%Y%m%d'):
            try:
                return datetime.strptime(val, fmt).date()
            except ValueError:
                continue
        return None
    
    @staticmethod
    def _parse_decimal(val: str) -> Optional[float]:
        val = val.strip().replace(',', '')
        if not val:
            return None
        try:
            return float(val)
        except ValueError:
            return None


def load_employees(filepath: str) -> list[Employee]:
    """Load employees from PeopleSoft CSV export.
    Handles common GC encoding issues.
    """
    for encoding in ('utf-8-sig', 'cp1252', 'utf-8', 'latin-1'):
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                employees = []
                for row in reader:
                    emp = Employee.from_csv_row(row)
                    if emp.emplid:
                        employees.append(emp)
                return employees
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not decode {filepath}")
```

---

## Schema Assumptions

When receiving PeopleSoft data, verify these with the deploying organization:

- [ ] `[SCHEMA-ASSUMPTION]` EMPLID format and length (standard: 11 chars; some departments use shorter)
- [ ] `[SCHEMA-ASSUMPTION]` Date format in exports (varies by department)
- [ ] `[SCHEMA-ASSUMPTION]` Character encoding (UTF-8, CP1252, or Latin-1)
- [ ] `[SCHEMA-ASSUMPTION]` Whether PS_EMPLOYEES snapshot is available or only PS_JOB
- [ ] `[SCHEMA-ASSUMPTION]` Custom fields added by the department (GC departments extensively customize PeopleSoft)
- [ ] `[SCHEMA-ASSUMPTION]` French descriptions available (PS tables have `_LNG` variants)
- [ ] `[SCHEMA-ASSUMPTION]` Which SETID values are in use
- [ ] `[SCHEMA-ASSUMPTION]` Whether historical data is included or current only
- [ ] `[SCHEMA-ASSUMPTION]` Which action codes are department-specific vs. standard

---

## References

- [PeopleSoft HCM Documentation (Oracle)](https://docs.oracle.com/en/applications/peoplesoft/human-capital-management/)
- [GC HRMS — PeopleSoft (DND)](https://www.canada.ca/en/department-national-defence/maple-leaf/defence/2024/07/update-personal-information-hrms-peoplesoft.html)

---

*Every GC department customizes PeopleSoft. Always validate schema assumptions before connecting real data.*
