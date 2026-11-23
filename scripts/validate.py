#!/usr/bin/env python3
"""Validate the IOP repository: checklist files, templates and company documents.

Usage:  python scripts/validate.py
Needs:  pip install pyyaml jsonschema
Exit code 0 = all good, 1 = problems found.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load_schema(name: str) -> Draft202012Validator:
    with open(ROOT / "schemas" / name, encoding="utf-8") as f:
        return Draft202012Validator(json.load(f))


def schema_errors(validator: Draft202012Validator, data, where: str) -> None:
    for e in sorted(validator.iter_errors(data), key=lambda x: list(x.path)):
        path = "/".join(str(p) for p in e.path) or "(root)"
        err(f"{where}: {path}: {e.message}")


# ---------------------------------------------------------------- checklist
def check_checklist() -> dict:
    validator = load_schema("checklist.schema.json")
    files = sorted((ROOT / "checklist").glob("*.yaml"))
    if not files:
        err("checklist/: no YAML files found")
        return {}
    seen_ids: set[str] = set()
    seen_domains: set[str] = set()
    seen_numbers: set[int] = set()
    stats = {"total": 0, "l1": 0, "l2": 0, "l3": 0}
    for path in files:
        rel = path.relative_to(ROOT)
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        before = len(errors)
        schema_errors(validator, data, str(rel))
        if len(errors) != before:
            continue
        dom = data["domain"]
        if dom["id"] in seen_domains:
            err(f"{rel}: duplicate domain id {dom['id']}")
        seen_domains.add(dom["id"])
        if dom["number"] in seen_numbers:
            err(f"{rel}: duplicate domain number {dom['number']}")
        seen_numbers.add(dom["number"])
        expected = 0
        for c in data["controls"]:
            expected += 1
            if not c["id"].startswith(dom["id"] + "-"):
                err(f"{rel}: control {c['id']} does not start with domain id {dom['id']}")
            if c["id"] != f"{dom['id']}-{expected:02d}":
                err(f"{rel}: control {c['id']} is out of sequence (expected {dom['id']}-{expected:02d})")
            if c["id"] in seen_ids:
                err(f"{rel}: duplicate control id {c['id']}")
            seen_ids.add(c["id"])
            if c["level"] == 1 and c["check"] == "reviewed":
                err(f"{rel}: {c['id']} is level 1 but check is 'reviewed' (level 1 has no human review)")
            if c["level"] >= 2 and c["check"] != "reviewed":
                err(f"{rel}: {c['id']} is level {c['level']} but check is '{c['check']}' (must be 'reviewed')")
            if c["check"] == "auto" and not (set(c["evidence"]) & {"scan", "url"}):
                err(f"{rel}: {c['id']} is 'auto' but has no scan/url evidence")
            stats["total"] += 1
            stats[f"l{c['level']}"] += 1
    if len(seen_domains) != 9:
        err(f"checklist/: expected 9 domains, found {len(seen_domains)}")
    return stats


# ------------------------------------------------------- company documents
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_version(v: str) -> tuple[int, int, int]:
    a, b, c = v.split(".")
    return int(a), int(b), int(c)


def check_bump(rel: str, fm: dict) -> None:
    ct, cur, prev = fm["change_type"], fm["document_version"], fm["previous_version"]
    if ct == "initial":
        if prev is not None:
            err(f"{rel}: change_type 'initial' requires previous_version null")
        return
    if prev is None:
        err(f"{rel}: change_type '{ct}' requires previous_version")
        return
    p, c = parse_version(prev), parse_version(cur)
    ok = {
        "patch": c == (p[0], p[1], p[2] + 1),
        "minor": c == (p[0], p[1] + 1, 0),
        "major": c == (p[0] + 1, 0, 0),
    }[ct]
    if not ok:
        err(f"{rel}: change_type '{ct}' does not match version bump {prev} -> {cur}")


def check_documents() -> int:
    validator = load_schema("company-document.schema.json")
    paths = list((ROOT / "templates").glob("privacy-document.*.md"))
    paths += list((ROOT / "company-docs").glob("*/privacy.*.md"))
    for path in sorted(paths):
        rel = str(path.relative_to(ROOT))
        m = FRONT.match(path.read_text(encoding="utf-8"))
        if not m:
            err(f"{rel}: missing YAML front matter")
            continue
        fm = yaml.safe_load(m.group(1))
        before = len(errors)
        schema_errors(validator, fm, rel)
        if len(errors) != before:
            continue
        check_bump(rel, fm)
        if path.parent.parent.name == "company-docs" and fm["slug"] != path.parent.name:
            err(f"{rel}: slug '{fm['slug']}' does not match folder '{path.parent.name}'")
    return len(paths)


def check_meta() -> None:
    required = {"slug", "company", "domain", "domain_proof", "contact_email", "level", "document_versions"}
    levels = {"none", "declared", "verified", "continuously-verified"}
    for path in sorted((ROOT / "company-docs").glob("*/meta.yaml")):
        rel = str(path.relative_to(ROOT))
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        missing = required - set(data)
        if missing:
            err(f"{rel}: missing keys {sorted(missing)}")
            continue
        if data["slug"] != path.parent.name:
            err(f"{rel}: slug does not match folder name")
        if data["level"] not in levels:
            err(f"{rel}: level must be one of {sorted(levels)}")
        if data["level"] != "none" and not (data.get("level_granted") and data.get("level_expires")):
            err(f"{rel}: a granted level needs level_granted and level_expires")


def main() -> int:
    stats = check_checklist()
    n_docs = check_documents()
    check_meta()
    if errors:
        print(f"FAILED with {len(errors)} problem(s):")
        for e in errors:
            print(" -", e)
        return 1
    print(
        f"OK: {stats['total']} controls (L1 {stats['l1']}, L2 {stats['l2']}, L3 {stats['l3']}), "
        f"{n_docs} privacy documents checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
