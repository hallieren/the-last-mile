#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Kill register revival-condition due-date reminder (Template 25.4). Conditions written as
dates are compared against a baseline date; conditions written as events are flagged for a
manual pass through the table."""
import argparse
import csv
import datetime
import pathlib
import re

p = argparse.ArgumentParser(
    description="Revival-condition due-date reminder: scans the kill register, compares rows "
                "whose revival condition holds a date against the baseline date and prints a "
                "reminder; rows written as events, not dates, get flagged for a manual pass "
                "through the table (Template 25.4)")
p.add_argument("csv_path", nargs="?",
               default=str(pathlib.Path(__file__).parent / "sample" / "kill-log.csv"),
               help="kill register CSV (five columns, see Template 25.4), defaults to sample/kill-log.csv")
p.add_argument("--today", default="2026-07-19",
               help="baseline date YYYY-MM-DD (passed as an argument for testing; defaults to the "
                    "sample baseline date, pass today's date for real use)")
a = p.parse_args()

today = datetime.date.fromisoformat(a.today)
print(f"Baseline date {today} (review discipline: once a year, ask two questions per row; "
      f"this script only reminds on date-type conditions, Template 25.4)")
for r in csv.DictReader(open(a.csv_path, encoding="utf-8-sig")):
    cond = r["revival_condition"]
    m = re.search(r"\d{4}-\d{2}-\d{2}", cond)
    if not m:
        print(f'{r["candidate"]}: event-triggered ({cond}), manual pass through the table')
        continue
    due = datetime.date.fromisoformat(m.group(0))
    left = (due - today).days
    if left <= 0:
        print(f'{r["candidate"]}: review date {due} is {-left} day(s) overdue, remind {r["proposed_by"]} to redo the rubric')
    else:
        print(f'{r["candidate"]}: review date {due} not yet due ({left} day(s) left)')
