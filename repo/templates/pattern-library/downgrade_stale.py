#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Asset register auto-downgrade: updated more than 183 days before the baseline date and status=active → pending-reverify (Template 23.2)."""
import argparse
import csv
import datetime
import pathlib

FIELDS = ["category", "name", "description", "origin",
          "verified_count", "owner", "updated", "status"]  # CONVENTIONS §2.5, word for word

p = argparse.ArgumentParser(
    description='Auto-downgrade asset register entries not updated in six months (Template 23.2: mechanizes '
                 '"an asset with no owner rots in six months"; CSV format is CONVENTIONS §2.5)')
p.add_argument("csv_path", nargs="?",
               default=str(pathlib.Path(__file__).parent / "sample" / "assets.csv"),
               help="Register CSV in §2.5 format, defaults to sample/assets.csv")
p.add_argument("--today", default="2026-07-19",
               help="Baseline date YYYY-MM-DD (passed as an argument so this is testable; defaults to the sample "
                    "baseline date, pass today's date for real use)")
p.add_argument("--write", action="store_true", help="Write the downgrades back to the CSV (default only prints the change list)")
a = p.parse_args()

today = datetime.date.fromisoformat(a.today)
with open(a.csv_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == FIELDS, "Column names must match CONVENTIONS §2.5 word for word"
    rows = list(reader)

changed = []
for r in rows:
    age = (today - datetime.date.fromisoformat(r["updated"])).days
    if r["status"] == "active" and age > 183:
        r["status"] = "pending-reverify"
        changed.append(f'{r["name"]} (owner {r["owner"]}): active → pending-reverify'
                       f' (updated {r["updated"]}, {age} days before the baseline date)')

print(f"Baseline date {today}, {len(rows)} total, {len(changed)} downgraded:")
print(*(["  " + c for c in changed] or ["  (none)"]), sep="\n")
if a.write and changed:
    with open(a.csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"Written back to {a.csv_path}")
