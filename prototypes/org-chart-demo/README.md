# Org-Chart Demo — CDR Phase 0 Prototype

> **DEMO** — reads synthetic PeopleSoft HR schema and renders a placeholder org-chart.
> No real data. No real HICC connection.

## What This Proves

**Schema → Tool.** A terry reads a YAML schema describing PeopleSoft HR tables and produces a functional org-chart UI with bilingual strings — without ever seeing real employee data.

## How to Run

### Prerequisites

- Python 3.9+
- No external dependencies beyond the standard library and PyYAML

### Install & Run

```bash
cd prototypes/org-chart-demo
pip install -r requirements.txt
python main.py
```

Then open `http://localhost:8000` in your browser.

### CLI Mode (no browser)

```bash
python main.py --cli
```

Prints the org-chart hierarchy to the terminal.

## What You'll See

- A web page showing a demo organizational hierarchy
- Bilingual toggle (English / Français)
- Expandable/collapsible department tree
- Placeholder names and positions (synthetic — not real people)
- Search by department or job title

## File Structure

```
org-chart-demo/
├── README.md           ← You are here
├── requirements.txt    ← Python dependencies (PyYAML only)
├── main.py             ← Entry point — schema parser + web server + CLI
├── schema_reader.py    ← Reads and validates the synthetic YAML schema
├── org_builder.py      ← Builds org-chart hierarchy from schema + synthetic data
├── templates/
│   └── index.html      ← Bilingual org-chart UI
└── strings.yaml        ← EN/FR bilingual UI strings
```

## Limitations

- Uses synthetic placeholder data (fake names, fake departments)
- No real PeopleSoft connection — demonstrates the pattern, not the integration
- Minimal styling — production tool would use GC Web Experience Toolkit (WET/CDTS)
- No authentication — production tool would sit behind department SSO
