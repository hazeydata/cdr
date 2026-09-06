"""Build an org-chart hierarchy from a synthetic PeopleSoft HR schema.

Generates placeholder data to demonstrate the schema-to-tool pattern.
No real employee data is used or required.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any

from schema_reader import get_table

# Synthetic demo data — fake departments, positions, and people.
# These names are entirely fictional and do not represent real individuals.
SYNTHETIC_DEPARTMENTS = [
    {"id": "D001", "name_en": "Executive Office", "name_fr": "Bureau de la direction", "location": "Hamilton HQ"},
    {"id": "D002", "name_en": "Settlement Services", "name_fr": "Services d'établissement", "location": "Hamilton HQ"},
    {"id": "D003", "name_en": "Employment Programs", "name_fr": "Programmes d'emploi", "location": "Hamilton HQ"},
    {"id": "D004", "name_en": "Language Training", "name_fr": "Formation linguistique", "location": "Hamilton East"},
    {"id": "D005", "name_en": "Community Integration", "name_fr": "Intégration communautaire", "location": "Hamilton Central"},
    {"id": "D006", "name_en": "Information Technology", "name_fr": "Technologie de l'information", "location": "Hamilton HQ"},
    {"id": "D007", "name_en": "Finance and Administration", "name_fr": "Finances et administration", "location": "Hamilton HQ"},
]

SYNTHETIC_POSITIONS = [
    {"id": "P001", "dept": "D001", "title_en": "Executive Director", "title_fr": "Directeur(trice) exécutif(ve)", "grade": "EX-03", "name": "A. Tremblay", "supervisor": None},
    {"id": "P002", "dept": "D002", "title_en": "Director, Settlement", "title_fr": "Directeur(trice), Établissement", "grade": "EX-01", "name": "B. Chen", "supervisor": "P001"},
    {"id": "P003", "dept": "D003", "title_en": "Director, Employment", "title_fr": "Directeur(trice), Emploi", "grade": "EX-01", "name": "C. Okafor", "supervisor": "P001"},
    {"id": "P004", "dept": "D004", "title_en": "Manager, Language Training", "title_fr": "Gestionnaire, Formation linguistique", "grade": "AS-07", "name": "D. Nguyen", "supervisor": "P002"},
    {"id": "P005", "dept": "D005", "title_en": "Manager, Community Programs", "title_fr": "Gestionnaire, Programmes communautaires", "grade": "PM-06", "name": "E. Fournier", "supervisor": "P002"},
    {"id": "P006", "dept": "D006", "title_en": "IT Team Lead", "title_fr": "Chef d'équipe TI", "grade": "CS-03", "name": "F. Hassan", "supervisor": "P001"},
    {"id": "P007", "dept": "D007", "title_en": "Finance Manager", "title_fr": "Gestionnaire des finances", "grade": "FI-04", "name": "G. Whiteduck", "supervisor": "P001"},
    {"id": "P008", "dept": "D002", "title_en": "Settlement Counsellor", "title_fr": "Conseiller(ère) en établissement", "grade": "PM-03", "name": "H. Rivera", "supervisor": "P002"},
    {"id": "P009", "dept": "D002", "title_en": "Settlement Counsellor", "title_fr": "Conseiller(ère) en établissement", "grade": "PM-03", "name": "I. Kowalski", "supervisor": "P002"},
    {"id": "P010", "dept": "D003", "title_en": "Employment Counsellor", "title_fr": "Conseiller(ère) en emploi", "grade": "PM-03", "name": "J. Abdi", "supervisor": "P003"},
    {"id": "P011", "dept": "D004", "title_en": "Language Instructor", "title_fr": "Instructeur(trice) de langue", "grade": "IS-03", "name": "K. Lavoie", "supervisor": "P004"},
    {"id": "P012", "dept": "D005", "title_en": "Community Outreach Worker", "title_fr": "Agent(e) de sensibilisation communautaire", "grade": "CR-05", "name": "L. Singh", "supervisor": "P005"},
    {"id": "P013", "dept": "D006", "title_en": "IT Analyst", "title_fr": "Analyste TI", "grade": "CS-02", "name": "M. Bouchard", "supervisor": "P006"},
    {"id": "P014", "dept": "D007", "title_en": "Financial Analyst", "title_fr": "Analyste financier(ère)", "grade": "FI-02", "name": "N. Kim", "supervisor": "P007"},
]


@dataclass
class OrgNode:
    """A node in the org-chart tree."""
    id: str
    name: str
    title_en: str
    title_fr: str
    department_en: str
    department_fr: str
    grade: str
    location: str
    children: list[OrgNode] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["children"] = [c.to_dict() for c in self.children]
        return d


def build_org_tree(schema: dict[str, Any]) -> OrgNode:
    """Build an org-chart tree from schema + synthetic data.

    In a real deployment, the adapter would query PeopleSoft and build
    the same tree structure from live PS_JOB.SUPERVISOR_ID / REPORTS_TO
    relationships. Here we use synthetic data to demonstrate the pattern.
    """
    ps_job = get_table(schema, "PS_JOB")
    ps_dept = get_table(schema, "PS_DEPT_TBL")
    if not ps_job or not ps_dept:
        raise ValueError("Schema missing PS_JOB or PS_DEPT_TBL — cannot build org-chart.")

    dept_map = {d["id"]: d for d in SYNTHETIC_DEPARTMENTS}
    pos_map = {p["id"]: p for p in SYNTHETIC_POSITIONS}

    node_map: dict[str, OrgNode] = {}
    for pos in SYNTHETIC_POSITIONS:
        dept = dept_map.get(pos["dept"], {})
        node = OrgNode(
            id=pos["id"],
            name=pos["name"],
            title_en=pos["title_en"],
            title_fr=pos["title_fr"],
            department_en=dept.get("name_en", ""),
            department_fr=dept.get("name_fr", ""),
            grade=pos["grade"],
            location=dept.get("location", ""),
        )
        node_map[pos["id"]] = node

    root = None
    for pos in SYNTHETIC_POSITIONS:
        node = node_map[pos["id"]]
        supervisor_id = pos["supervisor"]
        if supervisor_id is None:
            root = node
        elif supervisor_id in node_map:
            node_map[supervisor_id].children.append(node)

    if root is None:
        raise ValueError("No root node found (no position without a supervisor).")

    return root


def org_tree_to_json(root: OrgNode) -> str:
    """Serialize org tree to JSON for the web UI."""
    return json.dumps(root.to_dict(), indent=2, ensure_ascii=False)


def print_org_tree(node: OrgNode, indent: int = 0, lang: str = "en") -> None:
    """Print the org-chart tree to the terminal (CLI mode)."""
    prefix = "  " * indent
    title = node.title_en if lang == "en" else node.title_fr
    dept = node.department_en if lang == "en" else node.department_fr
    print(f"{prefix}├── {node.name} — {title} ({node.grade})")
    print(f"{prefix}│   {dept} | {node.location}")
    for child in node.children:
        print_org_tree(child, indent + 1, lang)
