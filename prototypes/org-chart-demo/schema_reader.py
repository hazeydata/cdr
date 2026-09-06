"""Read and validate a CDR synthetic PeopleSoft HR schema (YAML)."""

from pathlib import Path
from typing import Any

import yaml

REQUIRED_TABLES = {"PS_JOB", "PS_DEPT_TBL", "PS_PERSONAL_DATA"}


def load_schema(schema_path: str | Path) -> dict[str, Any]:
    """Load a YAML schema file and return the parsed dict."""
    schema_path = Path(schema_path)
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    if not schema or "tables" not in schema:
        raise ValueError("Schema must contain a 'tables' key with table definitions.")

    return schema


def validate_schema(schema: dict[str, Any]) -> list[str]:
    """Validate schema has the minimum tables needed for an org-chart.

    Returns a list of warnings (empty if clean).
    """
    warnings: list[str] = []
    table_names = {t["name"] for t in schema.get("tables", [])}

    missing = REQUIRED_TABLES - table_names
    if missing:
        warnings.append(f"Missing required tables: {', '.join(sorted(missing))}")

    for table in schema.get("tables", []):
        if not table.get("columns"):
            warnings.append(f"Table {table['name']} has no columns defined.")

    return warnings


def get_table(schema: dict[str, Any], table_name: str) -> dict[str, Any] | None:
    """Retrieve a table definition by name."""
    for table in schema.get("tables", []):
        if table["name"] == table_name:
            return table
    return None


def get_column_names(table: dict[str, Any]) -> list[str]:
    """Return column names for a table."""
    return [col["name"] for col in table.get("columns", [])]
