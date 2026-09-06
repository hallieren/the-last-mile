#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Memo send-timing reminder: works back from "48 hours before the meeting" to the delivery deadline (Template 19.4's send-timing table)."""
import argparse
import csv
import datetime
import pathlib

p = argparse.ArgumentParser(
    description='Memo send-timing reminder: reads the milestone calendar and prints a reminder line working back from "48 hours before the meeting" (Template 19)')
p.add_argument("csv_path", nargs="?",
               default=str(pathlib.Path(__file__).parent / "sample" / "milestones.csv"),
               help="milestone calendar CSV (date,meeting,memo); defaults to sample/milestones.csv")
p.add_argument("--today", default="2026-07-19",
               help="reference date YYYY-MM-DD (defaults to the sample's reference date; pass today's date for real use)")
a = p.parse_args()

today = datetime.date.fromisoformat(a.today)
print(f"Reference date: {today} (the document comes before the meeting, the executive reads the one-pager beforehand, so the meeting is where the call gets made)")
for r in csv.DictReader(open(a.csv_path, encoding="utf-8-sig")):
    meet = datetime.date.fromisoformat(r["date"])
    due = meet - datetime.timedelta(days=2)
    left = (due - today).days
    if left < 0:
        state = f"! {-left} days past the delivery deadline"
    elif left == 0:
        state = "→ must go out today"
    else:
        state = f"{left} days left"
    print(f'{r["memo"]:<8}| {r["meeting"]} ({meet}): delivery deadline {due} (48 hours before the meeting), {state}')
