#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Reads the stakeholder map's "Last updated" date line and prints a reminder once it is overdue. Template 5: update every two weeks."""
import argparse
import datetime
import pathlib
import re

parser = argparse.ArgumentParser(description="Stakeholder map update reminder (Template 5: draw it in week 1, update every two weeks)")
parser.add_argument("file", nargs="?", default=str(pathlib.Path(__file__).parent / "sample" / "stakeholder-map.md"),
                    help="Path to the map file (defaults to the sample/ example)")
parser.add_argument("--days", type=int, default=14, help="Reminder cycle in days (default 14)")
args = parser.parse_args()

text = pathlib.Path(args.file).read_text(encoding="utf-8")
m = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", text)
assert m, f"{args.file} has no line matching 'Last updated: YYYY-MM-DD'"

last = datetime.date.fromisoformat(m.group(1))
age = (datetime.date.today() - last).days
if age > args.days:
    print(f"Reminder: {args.file}")
    print(f"Not updated in {age} days (last was {last}, cycle is every {args.days} days).")
    print("Two questions to answer when you update it: which name has never been in the meeting room? Which cell's content did you guess?")
else:
    print(f"OK: {args.file} last updated {last}, {age} days ago, within the {args.days}-day cycle.")
