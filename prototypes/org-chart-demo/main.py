#!/usr/bin/env python3
"""CDR Phase 0 Prototype — Org-Chart Demo.

Reads a synthetic PeopleSoft HR schema (YAML) and renders a bilingual
organizational chart. Demonstrates the "schema -> tool" pattern without
any real employee data.

Usage:
    python main.py            # Start web server on http://localhost:8000
    python main.py --cli      # Print org-chart to terminal
    python main.py --port 3000  # Custom port
"""

from __future__ import annotations

import argparse
import json
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Any

import yaml

from org_builder import build_org_tree, org_tree_to_json, print_org_tree
from schema_reader import load_schema, validate_schema

ROOT = Path(__file__).resolve().parent
DEFAULT_SCHEMA = ROOT.parent.parent / "schemas" / "demo" / "hicc-hr-synthetic" / "schema.yaml"
TEMPLATE_PATH = ROOT / "templates" / "index.html"
STRINGS_PATH = ROOT / "strings.yaml"


def load_strings() -> dict[str, Any]:
    with open(STRINGS_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_html(org_json: str, strings: dict[str, Any]) -> str:
    """Inject org data and strings into the HTML template."""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("/*ORG_DATA*/null", org_json)
    html = html.replace("/*STRINGS*/null", json.dumps(strings, ensure_ascii=False))
    return html


class OrgChartHandler(SimpleHTTPRequestHandler):
    """Serve the org-chart page."""

    html_content: str = ""

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(self.html_content.encode("utf-8"))

    def log_message(self, format: str, *args: Any) -> None:
        print(f"[org-chart-demo] {args[0]}" if args else "")


def run_web(html: str, port: int) -> None:
    OrgChartHandler.html_content = html
    server = HTTPServer(("", port), OrgChartHandler)
    print(f"Org-chart demo running at http://localhost:{port}")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


def run_cli(schema: dict[str, Any]) -> None:
    root = build_org_tree(schema)
    print("=== Organizational Chart (EN) ===\n")
    print_org_tree(root, lang="en")
    print("\n=== Organigramme (FR) ===\n")
    print_org_tree(root, lang="fr")


def main() -> None:
    parser = argparse.ArgumentParser(description="CDR Org-Chart Demo")
    parser.add_argument("--cli", action="store_true", help="Print org-chart to terminal instead of starting web server")
    parser.add_argument("--port", type=int, default=8000, help="Web server port (default: 8000)")
    parser.add_argument("--schema", type=str, default=str(DEFAULT_SCHEMA), help="Path to schema YAML file")
    args = parser.parse_args()

    schema_path = Path(args.schema)
    print(f"Loading schema from: {schema_path}")

    schema = load_schema(schema_path)
    warnings = validate_schema(schema)
    if warnings:
        for w in warnings:
            print(f"  WARNING: {w}", file=sys.stderr)

    print(f"Schema loaded: {len(schema.get('tables', []))} tables")

    if args.cli:
        run_cli(schema)
    else:
        root = build_org_tree(schema)
        org_json = org_tree_to_json(root)
        strings = load_strings()
        html = build_html(org_json, strings)
        run_web(html, args.port)


if __name__ == "__main__":
    main()
