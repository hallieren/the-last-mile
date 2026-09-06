#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Three-way reconciliation summary (Template 9.3): reads a record-by-record reconciliation CSV, prints the overall inconsistency rate plus the largest single class and its share (report both together)."""
import argparse
import csv
import pathlib

PATTERNS = ["lagging", "forgotten", "semantic-divergence", "broken-join"]

parser = argparse.ArgumentParser(description="Three-way reconciliation summary (Template 9.3): reports the overall inconsistency rate alongside the largest single class")
parser.add_argument("file", nargs="?", default=str(pathlib.Path(__file__).parent / "sample" / "reconcile-records.csv"),
                    help="reconciliation record CSV (defaults to the sample/ data)")
args = parser.parse_args()

with open(args.file, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
assert rows, f"no records in {args.file}"

bad = []
for r in rows:
    assert r["verdict"] in ("consistent", "inconsistent"), f"claim {r['claim_id']}: verdict must be consistent/inconsistent, got '{r['verdict']}'"
    if r["verdict"] == "inconsistent":
        assert r["pattern"] in PATTERNS, f"claim {r['claim_id']}: an inconsistent record must carry a pattern ({'/'.join(PATTERNS)}), got '{r['pattern']}'"
        bad.append(r)

total, n_bad = len(rows), len(bad)
print(f"Reconciliation records: {args.file}")
print(f"{total} total, {n_bad} inconsistent, overall inconsistency rate {n_bad / total:.0%}")
if not bad:
    print("No inconsistent records.")
else:
    counts = {m: sum(1 for r in bad if r["pattern"] == m) for m in PATTERNS}
    print("Pattern breakdown: " + "; ".join(f"{m} {c} ({c / n_bad:.0%} of the inconsistent)" for m, c in counts.items() if c))
    top = max(counts, key=counts.get)
    # Book discipline (9.3): report the overall rate and the largest single class together, same denominator (the full set), e.g. ch9's 87/200=44% with lagging at roughly three in ten
    print(f"Report together: overall inconsistency rate {n_bad / total:.0%}, with the largest single class being {top} ({counts[top]}/{total}, {counts[top] / total:.0%} of the full set).")
    quotes = [r["notes"] for r in bad if r.get("notes", "").strip()]
    if quotes:
        print("What the handlers said (worth more than the inconsistency rate):")
        for q in quotes:
            print(f"- {q}")
