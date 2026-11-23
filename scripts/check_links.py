#!/usr/bin/env python3
"""Check that relative Markdown links in the repository point to files that exist.

Usage: python scripts/check_links.py
External links (http, https, mailto) and GitHub-relative issue links are skipped.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_PREFIX = ("http://", "https://", "mailto:", "#")


def main() -> int:
    bad: list[str] = []
    checked = 0
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        in_code = False
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for target in LINK.findall(line):
                if target.startswith(SKIP_PREFIX) or "/issues" in target:
                    continue
                path_part = unquote(target.split("#", 1)[0])
                if not path_part:
                    continue
                resolved = (md.parent / path_part).resolve()
                checked += 1
                if not resolved.exists():
                    bad.append(f"{md.relative_to(ROOT)}:{lineno}: broken link -> {target}")
    if bad:
        print(f"{len(bad)} broken link(s):")
        for b in bad:
            print(" -", b)
        return 1
    print(f"OK: {checked} relative links checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
