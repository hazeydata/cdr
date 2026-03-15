# CDR Data Adapters

## What Are Adapters?

Adapters are the bridge between a CDR-built tool and an organization's real data. They define how to connect to, read from, and write to specific data sources — without the tool needing to know the details of the underlying system.

In the CDR model, adapters are critical for **Mode 2 (Schema-Only)** operation: terry builds the tool with adapter templates based on the published schema, and the deploying organization configures the adapter to connect to their actual data.

---

## How Adapters Work

### The Pattern

Every adapter follows the same pattern:

```
[Published Schema] → [Adapter Template] → [Tool Logic]
                                              ↓
                              [Deploying Org Configures]
                                              ↓
                                    [Real Data Connection]
```

1. **Terry reads the schema** — table names, column names, data types, relationships
2. **Terry builds an adapter** — a pluggable module that defines data access patterns specific to that system
3. **Terry builds the tool** — business logic that works through the adapter interface, never directly with the data source
4. **The deploying organization configures the adapter** — replaces synthetic test data with real connection details

### Why Adapters Matter

- **Separation of concerns:** Business logic doesn't know or care whether data comes from PeopleSoft, a CSV file, or a REST API
- **Security boundary:** The adapter is the ONLY component that touches real data. In Mode 2, terry builds everything except the real data connection — the human handles that last step
- **Reusability:** A tool built with a PeopleSoft adapter works for any organization running PeopleSoft. Only the connection details change.
- **Testability:** Swap the real adapter for a synthetic data adapter during development and testing

---

## Available Adapter Templates

| Template | System | Common Users |
|----------|--------|-------------|
| `peoplesoft-hr.md` | PeopleSoft HCM 9.x (GC HRMS) | GC federal departments |
| `sap-finance.md` | SAP S/4HANA Finance (GCfm) | GC federal departments |
| `generic-csv.md` | CSV/spreadsheet data | Everyone |

---

## Adapter Interface

Every adapter implements these standard methods:

```python
class DataAdapter:
    """Base interface for CDR data adapters."""
    
    def connect(self, config: dict) -> bool:
        """Establish connection to data source. Returns True on success."""
        raise NotImplementedError
    
    def get_schema(self) -> dict:
        """Return the schema definition (tables, columns, types)."""
        raise NotImplementedError
    
    def query(self, table: str, filters: dict = None, 
              columns: list = None, limit: int = None) -> list[dict]:
        """Query data from a table with optional filters."""
        raise NotImplementedError
    
    def count(self, table: str, filters: dict = None) -> int:
        """Count records matching filters."""
        raise NotImplementedError
    
    def validate_schema(self, expected_schema: dict) -> list[str]:
        """
        Validate actual schema against expected.
        Returns list of discrepancies.
        """
        raise NotImplementedError
    
    def disconnect(self) -> None:
        """Clean up connection."""
        raise NotImplementedError
```

### For Mode 2 Development

During Mode 2 development, terry uses a `SyntheticAdapter` that implements the same interface but returns generated test data:

```python
class SyntheticAdapter(DataAdapter):
    """Adapter that returns synthetic test data matching a schema."""
    
    def __init__(self, schema: dict, seed: int = 42):
        self.schema = schema
        self.generator = DataGenerator(schema, seed)
    
    def query(self, table, filters=None, columns=None, limit=None):
        return self.generator.generate(table, filters, columns, limit)
```

When the organization deploys on-network, they swap `SyntheticAdapter` for the real adapter (e.g., `PeopleSoftAdapter`) and configure the connection.

---

## Creating a New Adapter

When you encounter a system that doesn't have a template:

1. **Get the schema** — column names, data types, relationships, any system-specific patterns (effective dating, soft deletes, etc.)
2. **Document system-specific patterns** — how does the system handle history? Multi-tenancy? Character encoding? Date formats?
3. **Build the adapter class** implementing the standard interface
4. **Document schema assumptions** with `[SCHEMA-ASSUMPTION]` tags
5. **Build a synthetic data generator** for testing
6. **Write a deployment guide** explaining how to configure the real connection

### Template for New Adapters

```markdown
# [System Name] Adapter Template

## Overview
- System name and version
- Common users
- CDR operating mode relevance

## Schema
- Table definitions with columns, types, descriptions
- Relationships between tables
- System-specific patterns (effective dating, etc.)

## Adapter Code
- Python adapter class implementing DataAdapter interface
- Connection configuration
- Query patterns

## Schema Assumptions
- [ ] [SCHEMA-ASSUMPTION] items to validate with deploying organization

## Deployment Guide
- How to configure the real data connection
- Required permissions
- Testing steps

## References
- Vendor documentation links
- GC-specific documentation
```

---

## Schema Assumptions

Every adapter template includes `[SCHEMA-ASSUMPTION]` tags marking things that must be verified with the deploying organization before connecting real data. Common assumptions:

- Date format in exports
- Character encoding (UTF-8, CP1252, Latin-1)
- Custom fields added by the organization
- Whether historical data is included
- Specific version/configuration of the system
- Naming conventions for custom objects

**These are not bugs.** They're the expected gap between a generic template and a specific deployment. The deploying organization validates and adjusts.

---

*Adapters are what make the CDR model work. They're the seam between terry's world (schemas and code) and the organization's world (real data on real networks).*
