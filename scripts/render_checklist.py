#!/usr/bin/env python3
"""Render the human-readable checklist tables from checklist/*.yaml.

Usage:
  python scripts/render_checklist.py          # write docs/fa/03-checklist-table.md and docs/en/checklist-table.md
  python scripts/render_checklist.py --check  # exit 1 if the files on disk are out of date (for CI)
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT_FA = ROOT / "docs" / "fa" / "03-checklist-table.md"
OUT_EN = ROOT / "docs" / "en" / "checklist-table.md"

LEVEL_FA = {1: "۱", 2: "۲", 3: "۳"}
CHECK_FA = {"auto": "خودکار", "declared": "اظهار", "reviewed": "بازبینی"}
EVID_FA = {
    "url": "آدرس", "document": "سند", "screenshot": "تصویر صفحه", "config": "پیکربندی",
    "log-sample": "نمونهٔ ثبت", "interview": "مصاحبه", "contract": "قرارداد",
    "test-result": "نتیجهٔ آزمون", "scan": "اسکن",
}


def load() -> list[dict]:
    return [yaml.safe_load(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "checklist").glob("*.yaml"))]


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def mapping_text(m: dict | None) -> str:
    if not m:
        return "-"
    parts = []
    if m.get("gdpr"):
        parts.append("GDPR " + "، ".join(m["gdpr"]))
    if m.get("iso27701"):
        parts.append("ISO 27701 " + "، ".join(m["iso27701"]))
    if m.get("asvs"):
        parts.append("ASVS " + "، ".join(m["asvs"]))
    if m.get("local"):
        refs = "؛ ".join(m["local"]["refs"]) or "نیازمند بررسی حقوقی"
        parts.append(f"محلی ({refs}، پیش‌نویس)")
    return "<br>".join(parts) if parts else "-"


def mapping_text_en(m: dict | None) -> str:
    if not m:
        return "-"
    parts = []
    if m.get("gdpr"):
        parts.append("GDPR " + ", ".join(m["gdpr"]))
    if m.get("iso27701"):
        parts.append("ISO 27701 " + ", ".join(m["iso27701"]))
    if m.get("asvs"):
        parts.append("ASVS " + ", ".join(m["asvs"]))
    if m.get("local"):
        parts.append("local (draft, pending legal review)")
    return "<br>".join(parts) if parts else "-"


def counts(domains: list[dict]) -> dict:
    c = {1: 0, 2: 0, 3: 0}
    for d in domains:
        for ctl in d["controls"]:
            c[ctl["level"]] += 1
    return c


def render_fa(domains: list[dict]) -> str:
    c = counts(domains)
    total = sum(c.values())
    out = [
        "<div dir=\"rtl\">",
        "",
        "# جدول کنترل‌ها",
        "",
        "> این فایل **خودکار** از `checklist/*.yaml` تولید می‌شود. آن را دستی ویرایش نکنید؛ فایل‌های YAML را تغییر دهید و `python scripts/render_checklist.py` را اجرا کنید.",
        "",
        f"مجموع **{total} کنترل** در ۹ حوزه: سطح ۱ ({c[1]} کنترل)، سطح ۲ ({c[2]} کنترل افزوده)، سطح ۳ ({c[3]} کنترل افزوده). سطح ۲ همهٔ کنترل‌های سطح ۱ و ۲ را می‌خواهد ({c[1] + c[2]} کنترل).",
        "",
        "نوع بررسی: **خودکار** (ابزار)، **اظهار** (شرکت اعلام می‌کند)، **بازبینی** (بازبین انسانی).",
        "",
    ]
    for d in domains:
        dom = d["domain"]
        out += [f"## حوزهٔ {dom['number']}: {dom['title_fa']} ({dom['id']})", "", dom["summary_fa"], ""]
        if dom.get("status") == "draft-pending-legal-review":
            out += ["> **وضعیت: پیش‌نویس. هنوز هیچ وکیلی این بخش را بازبینی نکرده است.**", ""]
        out += ["| شناسه | سطح | بررسی | عنوان و الزام | شواهد | نگاشت |", "| --- | --- | --- | --- | --- | --- |"]
        for ctl in d["controls"]:
            ev = "، ".join(EVID_FA[e] for e in ctl["evidence"])
            out.append(
                f"| `{ctl['id']}` | {LEVEL_FA[ctl['level']]} | {CHECK_FA[ctl['check']]} | "
                f"**{cell(ctl['title_fa'])}**<br>{cell(ctl['requirement_fa'])} | {ev} | {mapping_text(ctl.get('mappings'))} |"
            )
        out.append("")
    out += ["</div>", ""]
    return "\n".join(out)


def render_en(domains: list[dict]) -> str:
    c = counts(domains)
    total = sum(c.values())
    out = [
        "# Control table",
        "",
        "> Generated from `checklist/*.yaml`. Do not edit by hand; change the YAML and run `python scripts/render_checklist.py`.",
        "",
        f"**{total} controls** in 9 domains: Level 1 ({c[1]} controls), Level 2 (+{c[2]}), Level 3 (+{c[3]}). Level 2 requires every Level 1 and Level 2 control ({c[1] + c[2]}).",
        "",
        "Check type: **auto** (scanner), **declared** (company attests), **reviewed** (human reviewer).",
        "",
    ]
    for d in domains:
        dom = d["domain"]
        out += [f"## Domain {dom['number']}: {dom['title_en']} ({dom['id']})", "", dom["summary_en"], ""]
        if dom.get("status") == "draft-pending-legal-review":
            out += ["> **Status: draft, not yet reviewed by a lawyer.**", ""]
        out += ["| ID | Level | Check | Control | Evidence | Mappings |", "| --- | --- | --- | --- | --- | --- |"]
        for ctl in d["controls"]:
            out.append(
                f"| `{ctl['id']}` | {ctl['level']} | {ctl['check']} | "
                f"**{cell(ctl['title_en'])}**<br>{cell(ctl['requirement_en'])} | {', '.join(ctl['evidence'])} | "
                f"{mapping_text_en(ctl.get('mappings'))} |"
            )
        out.append("")
    return "\n".join(out)


def main() -> int:
    domains = load()
    fa, en = render_fa(domains), render_en(domains)
    if "--check" in sys.argv:
        stale = [p.name for p, t in ((OUT_FA, fa), (OUT_EN, en)) if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("Out of date:", ", ".join(stale), "- run: python scripts/render_checklist.py")
            return 1
        print("Checklist tables are up to date.")
        return 0
    OUT_FA.write_text(fa, encoding="utf-8")
    OUT_EN.write_text(en, encoding="utf-8")
    print(f"Wrote {OUT_FA.relative_to(ROOT)} and {OUT_EN.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
