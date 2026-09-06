#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""A lightweight CLI for maintaining the scope decision log (Template 8.3): add appends one record, list groups them by status."""
import argparse
import csv
import datetime
import pathlib

FIELDS = ["date", "expansion", "proposed_by", "rejection_reason", "revival_condition", "status"]
STATUSES = ["shelved", "revived", "abandoned", "transferred"]
SAMPLE = str(pathlib.Path(__file__).parent / "sample" / "scope-log.csv")

parser = argparse.ArgumentParser(description="Scope decision log maintenance script (Template 8.3): CSV stores the records, add appends / list groups by status")
sub = parser.add_subparsers(dest="cmd")
p_list = sub.add_parser("list", help="List every record, grouped by status")
p_list.add_argument("-f", "--file", default=SAMPLE, help="Records CSV (defaults to the sample/ example)")
p_add = sub.add_parser("add", help="Append one record")
p_add.add_argument("-f", "--file", required=True, help="Records CSV (created if missing)")
p_add.add_argument("expansion")
p_add.add_argument("proposed_by")
p_add.add_argument("rejection_reason", help="Write the cost, not an attitude (Template 8.3 rule)")
p_add.add_argument("revival_condition", help="Write a checkable event, not a date")
p_add.add_argument("--date", default=str(datetime.date.today()), help="Defaults to today")
p_add.add_argument("--status", default="shelved", choices=STATUSES)
args = parser.parse_args()

if args.cmd == "add":
    path = pathlib.Path(args.file)
    new = not path.exists()
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(FIELDS)
        w.writerow([args.date, args.expansion, args.proposed_by, args.rejection_reason, args.revival_condition, args.status])
    print(f"Logged: {args.expansion} ({args.status}) → {path}")
    print("Reminder: send this back to the proposer within 48 hours (Template 8.3 rule).")
else:  # list; falls through here with no subcommand too, demos on the sample
    file = args.file if args.cmd == "list" else SAMPLE
    with open(file, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        assert r["status"] in STATUSES, f"Unknown status '{r['status']}' (choices: {'/'.join(STATUSES)})"
    print(f"Scope decision log: {file} ({len(rows)} records)")
    for st in STATUSES:
        group = [r for r in rows if r["status"] == st]
        if not group:
            continue
        print(f"\n[{st}] {len(group)} records")
        for r in group:
            print(f"- {r['expansion']} ({r['proposed_by']}, {r['date']})")
            print(f"    Rejection reason: {r['rejection_reason']}")
            print(f"    Revival condition: {r['revival_condition']}")
