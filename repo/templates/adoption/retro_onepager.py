#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Retro one-pager: reason code distribution plus the aging top rows (Template 21; CSV column names in CONVENTIONS §2.1)."""
import argparse
import csv
import datetime
import pathlib

base = pathlib.Path(__file__).parent
p = argparse.ArgumentParser(
    description="Generate the retro one-pager: reason code distribution plus the aging top rows, printed as Markdown (Template 21; input is a CSV export of the §2.1 decision trail tables)")
p.add_argument("--decisions", default=str(base / "sample" / "decisions.csv"),
               help="CSV export of the decisions table (column names match §2.1)")
p.add_argument("--suggestions", default=str(base / "sample" / "suggestions.csv"),
               help="CSV export of the suggestions table (column names match §2.1)")
p.add_argument("--today", help="Reference date for the aging calculation, YYYY-MM-DD (defaults to the latest date in the data, handy for testing)")
a = p.parse_args()

dec = list(csv.DictReader(open(a.decisions, encoding="utf-8-sig")))
sug = list(csv.DictReader(open(a.suggestions, encoding="utf-8-sig")))
assert dec and sug, "sample data is empty"
day = lambda s: datetime.date.fromisoformat(s[:10])
today = day(a.today) if a.today else max(
    [day(r["decided_at"]) for r in dec] + [day(r["created_at"]) for r in sug])
overrides = [r for r in dec if r["decision"] == "override"]

print("# Queue Retro One-Pager (auto-generated draft)\n")
print(f"Data as of {today}. {len(dec)} decisions, {len(overrides)} overrides"
      f" (override rate {len(overrides) / len(dec):.0%}).\n")

print("## Override Reason Code Distribution\n\n| Reason Code | Count | Share |\n|------|----|----|")
counts = {}
for r in overrides:
    code = r["reason_code"] or "(blank, required on override, needs follow-up)"
    counts[code] = counts.get(code, 0) + 1
for code, n in sorted(counts.items(), key=lambda kv: -kv[1]):
    print(f"| {code} | {n} | {n / len(overrides):.0%} |")
print('\n> An "other" share over three in ten means the enum is due for a revision (Template 17.2).\n')

decided = {r["suggestion_id"] for r in dec}
pending = sorted((((today - day(r["created_at"])).days, r)
                  for r in sug if r["suggestion_id"] not in decided), key=lambda t: t[0])
print("## Aging Top 5 (Pending Suggestions)\n\n| suggestion_id | category | Raised On | Days Pending |\n|----|----|----|----|")
for age, r in reversed(pending[-5:]):
    print(f'| {r["suggestion_id"]} | {r["category"]} | {day(r["created_at"])} | {age} |')
print("\n(Four things happen in the meeting: reason code distribution, aging top rows, the disputed-status list, "
      "and naming one improvement, Template 21.3. The last two need a person, the script only does the grunt work.)")
