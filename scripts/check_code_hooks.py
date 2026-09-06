#!/usr/bin/env python3
"""Code hooks sync check: appendix Code hooks mentions and repo/templates/ dirs must match both ways (template 20 has no scaffold by design)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

mentions = {}
for f in sorted((ROOT / "docs" / "appendices").glob("template-*.md")):
    for d in re.findall(r"`templates/([a-z0-9-]+)/[a-z0-9/._-]*`", f.read_text(encoding="utf-8")):
        mentions.setdefault(d, set()).add(f.name)

dirs = {p.name for p in (ROOT / "repo" / "templates").iterdir() if p.is_dir()}

errors = []
for d in sorted(set(mentions) - dirs):
    errors.append(f"appendix mentions templates/{d}/ but repo/templates/{d}/ does not exist ({', '.join(sorted(mentions[d]))})")
for d in sorted(dirs - set(mentions)):
    errors.append(f"repo/templates/{d}/ is not mentioned by any appendix Code hooks")
for d in sorted(dirs & set(mentions)):
    if not (ROOT / "repo" / "templates" / d / "README.md").exists():
        errors.append(f"repo/templates/{d}/ is missing README.md")

for e in errors:
    print("FAIL:", e)
print(f"{'FAIL' if errors else 'OK'}: {len(dirs)} scaffold dirs / {len(mentions)} mentioned by appendices")
sys.exit(1 if errors else 0)
