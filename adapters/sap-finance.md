# SAP S/4HANA Finance Adapter Template

> **System:** SAP S/4HANA Finance (GCfm — Government of Canada Financial Management)
> **Common Users:** GC federal departments (under Financial Management Transformation program)
> **CDR Modes:** Mode 2 (Schema-Only) for federal departments
> **Classification:** Schema patterns only — no Protected B data

---

## Overview

SAP S/4HANA Finance is the Government of Canada's financial management solution. The GC implementation, known as **GCfm** (Government of Canada Financial Management), was developed by TBS's Office of the Comptroller General (OCG). The current digital core is the "A" template (GCfm-A).

SAP S/4HANA introduces the **Universal Journal** (table ACDOCA) which consolidates financial data that was previously spread across multiple tables in SAP ECC. This significantly simplifies financial reporting.

---

## Core Tables

### ACDOCA — Universal Journal (S/4HANA Primary Table)

The single source of truth for all financial postings in S/4HANA. Combines FI (Financial Accounting) and CO (Controlling) entries.

| Field | Type | Description |
|-------|------|-------------|
| `RCLNT` | CHAR(3) | Client |
| `RLDNR` | CHAR(2) | Ledger (0L = leading ledger) |
| `RBUKRS` | CHAR(4) | Company code |
| `GJAHR` | NUMC(4) | Fiscal year |
| `BELNR` | CHAR(10) | Document number |
| `DOCLN` | NUMC(6) | Line item |
| `RYESSION` | CHAR(2) | Session code |
| `RACCT` | CHAR(10) | Account number |
| `RCNTR` | CHAR(10) | Cost centre |
| `PRCTR` | CHAR(10) | Profit centre |
| `RFAREA` | CHAR(16) | Functional area |
| `RBUSA` | CHAR(4) | Business area |
| `KOKRS` | CHAR(4) | Controlling area |
| `KSTAR` | CHAR(10) | Cost element |
| `AUFNR` | CHAR(12) | Internal order |
| `PS_PSP_PNR` | NUMC(8) | WBS element (project) |
| `BUDAT` | DATE | Posting date |
| `BLDAT` | DATE | Document date |
| `CPUDT` | DATE | Entry date |
| `USNAM` | CHAR(12) | User who entered |
| `BLART` | CHAR(2) | Document type |
| `BSCHL` | CHAR(2) | Posting key |
| `HSL` | CURR(23,2) | Amount in local currency |
| `HWAER` | CUKY(5) | Local currency (CAD) |
| `TSL` | CURR(23,2) | Amount in transaction currency |
| `TWAER` | CUKY(5) | Transaction currency |
| `DRCRK` | CHAR(1) | Debit/Credit indicator (S=Debit, H=Credit) |
| `SGTXT` | CHAR(50) | Line item text |
| `ZUONR` | CHAR(18) | Assignment number |

### BKPF — Accounting Document Header

| Field | Type | Description |
|-------|------|-------------|
| `BUKRS` | CHAR(4) | Company code |
| `BELNR` | CHAR(10) | Document number |
| `GJAHR` | NUMC(4) | Fiscal year |
| `BLART` | CHAR(2) | Document type |
| `BLDAT` | DATE | Document date |
| `BUDAT` | DATE | Posting date |
| `MONAT` | NUMC(2) | Fiscal period |
| `CPUDT` | DATE | Entry date |
| `USNAM` | CHAR(12) | Entered by |
| `TCODE` | CHAR(20) | Transaction code |
| `WAERS` | CUKY(5) | Document currency |
| `BSTAT` | CHAR(1) | Document status |
| `XBLNR` | CHAR(16) | Reference document number |
| `BKTXT` | CHAR(25) | Document header text |
| `STBLG` | CHAR(10) | Reversal document number |

### BSEG — Accounting Document Line Items

| Field | Type | Description |
|-------|------|-------------|
| `BUKRS` | CHAR(4) | Company code |
| `BELNR` | CHAR(10) | Document number |
| `GJAHR` | NUMC(4) | Fiscal year |
| `BUZEI` | NUMC(3) | Line item number |
| `BSCHL` | CHAR(2) | Posting key |
| `KOART` | CHAR(1) | Account type (S=GL, D=Customer, K=Vendor) |
| `HKONT` | CHAR(10) | GL account |
| `KOSTL` | CHAR(10) | Cost centre |
| `AUFNR` | CHAR(12) | Internal order |
| `WRBTR` | CURR(13,2) | Amount in document currency |
| `DMBTR` | CURR(13,2) | Amount in local currency (CAD) |
| `SHKZG` | CHAR(1) | Debit/Credit (S/H) |
| `SGTXT` | CHAR(50) | Line item text |
| `ZUONR` | CHAR(18) | Assignment |

---

## Master Data Tables

### SKA1 / SKB1 — GL Account Master

| Field | Type | Description |
|-------|------|-------------|
| `KTOPL` | CHAR(4) | Chart of accounts |
| `SAKNR` | CHAR(10) | GL account number |
| `TXT20` | CHAR(20) | Short text |
| `TXT50` | CHAR(50) | Long text |
| `KTOKS` | CHAR(4) | Account group |
| `XBILK` | CHAR(1) | Balance sheet indicator |

### CSKS — Cost Centre Master

| Field | Type | Description |
|-------|------|-------------|
| `KOKRS` | CHAR(4) | Controlling area |
| `KOSTL` | CHAR(10) | Cost centre |
| `DATBI` | DATE | Valid to |
| `DATAB` | DATE | Valid from |
| `KTEXT` | CHAR(20) | Short description |
| `LTEXT` | CHAR(40) | Long description |
| `VERAK` | CHAR(20) | Person responsible |
| `BUKRS` | CHAR(4) | Company code |
| `GSBER` | CHAR(4) | Business area |

### AUFK — Internal Order Master

| Field | Type | Description |
|-------|------|-------------|
| `AUFNR` | CHAR(12) | Order number |
| `AUART` | CHAR(4) | Order type |
| `KTEXT` | CHAR(40) | Short description |
| `BUKRS` | CHAR(4) | Company code |
| `KOSTL` | CHAR(10) | Responsible cost centre |
| `PRCTR` | CHAR(10) | Profit centre |
| `ASTKZ` | NUMC(2) | Order status |

### KNA1 — Customer Master (Accounts Receivable)

| Field | Type | Description |
|-------|------|-------------|
| `KUNNR` | CHAR(10) | Customer number |
| `NAME1` | CHAR(35) | Name |
| `ORT01` | CHAR(35) | City |
| `REGIO` | CHAR(3) | Province |
| `PSTLZ` | CHAR(10) | Postal code |
| `LAND1` | CHAR(3) | Country |

### LFA1 — Vendor Master (Accounts Payable)

| Field | Type | Description |
|-------|------|-------------|
| `LIFNR` | CHAR(10) | Vendor number |
| `NAME1` | CHAR(35) | Name |
| `ORT01` | CHAR(35) | City |
| `REGIO` | CHAR(3) | Province |
| `PSTLZ` | CHAR(10) | Postal code |
| `LAND1` | CHAR(3) | Country |

---

## GC-Specific Patterns

### Common Document Types
| Code | Description |
|------|-------------|
| `SA` | GL Account Document |
| `KR` | Vendor Invoice |
| `KG` | Vendor Credit Memo |
| `DR` | Customer Invoice |
| `DG` | Customer Credit Memo |
| `AB` | Accounting Document |
| `AA` | Asset Posting |

### Common Posting Keys
| Key | Type | Description |
|-----|------|-------------|
| `40` | Debit | GL account debit |
| `50` | Credit | GL account credit |
| `01` | Debit | Customer invoice |
| `11` | Credit | Customer payment |
| `21` | Debit | Vendor invoice (vendor perspective) |
| `31` | Credit | Vendor payment |

### GC Fiscal Year
- GC fiscal year runs April 1 – March 31
- Period 01 = April, Period 12 = March
- Period 13-16 are special periods (adjustments, year-end)

---

## Common Query Patterns

### Budget vs. Actuals by Cost Centre
```sql
-- Actuals from Universal Journal
SELECT 
    RCNTR as cost_centre,
    RACCT as account,
    SUM(CASE WHEN DRCRK = 'S' THEN HSL ELSE -HSL END) as net_amount
FROM ACDOCA
WHERE RBUKRS = :company_code
    AND GJAHR = :fiscal_year
    AND RLDNR = '0L'
GROUP BY RCNTR, RACCT
```

### Monthly Spending Trend
```sql
SELECT 
    SUBSTRING(BUDAT, 1, 7) as month,
    SUM(CASE WHEN DRCRK = 'S' THEN HSL ELSE 0 END) as debits,
    SUM(CASE WHEN DRCRK = 'H' THEN HSL ELSE 0 END) as credits
FROM ACDOCA
WHERE RBUKRS = :company_code
    AND GJAHR = :fiscal_year
    AND RLDNR = '0L'
GROUP BY SUBSTRING(BUDAT, 1, 7)
ORDER BY month
```

---

## Adapter Code

### CSV Export Adapter

```python
import csv
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

@dataclass
class JournalEntry:
    """Represents a SAP financial journal entry."""
    company_code: str
    fiscal_year: str
    document_number: str
    line_item: str
    account: str
    cost_centre: Optional[str]
    posting_date: Optional[date]
    amount_local: Optional[Decimal]
    currency: str
    debit_credit: str  # 'S' = Debit, 'H' = Credit
    text: Optional[str]
    
    @classmethod
    def from_csv_row(cls, row: dict) -> 'JournalEntry':
        return cls(
            company_code=row.get('RBUKRS', row.get('BUKRS', '')).strip(),
            fiscal_year=row.get('GJAHR', '').strip(),
            document_number=row.get('BELNR', '').strip(),
            line_item=row.get('DOCLN', row.get('BUZEI', '')).strip(),
            account=row.get('RACCT', row.get('HKONT', '')).strip(),
            cost_centre=row.get('RCNTR', row.get('KOSTL', '')).strip() or None,
            posting_date=cls._parse_date(row.get('BUDAT', '')),
            amount_local=cls._parse_amount(
                row.get('HSL', row.get('DMBTR', ''))
            ),
            currency=row.get('HWAER', row.get('WAERS', 'CAD')).strip(),
            debit_credit=row.get('DRCRK', row.get('SHKZG', '')).strip(),
            text=row.get('SGTXT', '').strip() or None,
        )
    
    @staticmethod
    def _parse_date(val: str) -> Optional[date]:
        val = val.strip()
        if not val:
            return None
        for fmt in ('%Y-%m-%d', '%Y%m%d', '%m/%d/%Y', '%d.%m.%Y'):
            try:
                return datetime.strptime(val, fmt).date()
            except ValueError:
                continue
        return None
    
    @staticmethod
    def _parse_amount(val: str) -> Optional[Decimal]:
        val = val.strip().replace(',', '')
        if not val or val == '-':
            return None
        try:
            return Decimal(val)
        except Exception:
            return None
    
    @property
    def signed_amount(self) -> Optional[Decimal]:
        """Return signed amount (positive for debit, negative for credit)."""
        if self.amount_local is None:
            return None
        if self.debit_credit == 'H':
            return -self.amount_local
        return self.amount_local


def load_journal_entries(filepath: str) -> list[JournalEntry]:
    """Load journal entries from SAP CSV/Excel export."""
    for encoding in ('utf-8-sig', 'cp1252', 'utf-8', 'latin-1'):
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                entries = []
                for row in reader:
                    entry = JournalEntry.from_csv_row(row)
                    if entry.document_number:
                        entries.append(entry)
                return entries
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not decode {filepath}")
```

---

## Schema Assumptions

- [ ] `[SCHEMA-ASSUMPTION]` SAP version (S/4HANA vs ECC — table structures differ significantly)
- [ ] `[SCHEMA-ASSUMPTION]` Whether ACDOCA (Universal Journal) is available (S/4HANA only)
- [ ] `[SCHEMA-ASSUMPTION]` GCfm template version ("A" template vs. customized)
- [ ] `[SCHEMA-ASSUMPTION]` Chart of accounts structure (GC standard vs. department-specific)
- [ ] `[SCHEMA-ASSUMPTION]` Fiscal year variant (standard April-March for GC)
- [ ] `[SCHEMA-ASSUMPTION]` Currency handling (CAD assumed; multi-currency possible)
- [ ] `[SCHEMA-ASSUMPTION]` Export format and encoding
- [ ] `[SCHEMA-ASSUMPTION]` Whether department uses CO module extensively (internal orders, cost centres)
- [ ] `[SCHEMA-ASSUMPTION]` Custom fields (Z-fields) added by the department
- [ ] `[SCHEMA-ASSUMPTION]` Ledger configuration (which ledgers are in use)

---

## References

- [SAP S/4HANA Finance Documentation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE)
- [GC Financial Management Transformation (DFO)](https://www.dfo-mpo.gc.ca/transparency-transparence/atip-aiprp/privacy-privee/materiel-solution-eng.html)
- [SAP FI Important Tables](https://erp-top.com/financial-accounting/)

---

*GC departments customize SAP extensively. The GCfm "A" template provides a baseline, but always validate schema assumptions with the specific department's configuration.*
