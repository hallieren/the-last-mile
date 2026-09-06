#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Run chart short notice: reads a §2.2 format CSV, detects whether the latest point forms "N points on one side" (Template 19)."""
import argparse
import csv
import pathlib
import statistics

p = argparse.ArgumentParser(
    description='Run chart short notice generator: detects "N points on one side" and prints a one-line short notice (Template 19; data format is CONVENTIONS §2.2)')
p.add_argument("csv_path", nargs="?",
               default=str(pathlib.Path(__file__).parent / "sample" / "runchart.csv"),
               help="§2.2 format CSV (period,value); defaults to sample/runchart.csv")
p.add_argument("--baseline", type=int, default=8, help="baseline segment is the first N points (default 8)")
p.add_argument("--run", type=int, default=6,
               help='N in "N points on one side" (default 6, rule from the Health Care Data Guide)')
a = p.parse_args()

rows = list(csv.DictReader(open(a.csv_path, encoding="utf-8-sig")))
assert rows and set(rows[0]) == {"period", "value"}, "format must be CONVENTIONS §2.2: period,value"
assert len(rows) > a.baseline, "must have more points than the baseline segment"
periods = [r["period"] for r in rows]
values = [float(r["value"]) for r in rows]
median = statistics.median(values[:a.baseline])

# Count consecutive same-side points back from the latest one; a point sitting on the median neither counts nor breaks the streak (run chart rule)
streak, side = 0, None
for v in reversed(values[a.baseline:]):
    if v == median:
        continue
    s = "below" if v < median else "above"
    if side is None:
        side = s
    if s != side:
        break
    streak += 1

n = len(values)
print(f"Baseline: first {a.baseline} points ({periods[0]}–{periods[a.baseline - 1]}), median {median:g}")
if side and streak >= a.run:
    print(f'[Short notice draft] Point {n} ({periods[-1]}): the latest {streak} consecutive points sit '
          f'{side} the baseline median {median:g}, "{a.run} points on one side" holds. This is a shift, not fluctuation.')
    print("Send discipline: one line plus one chart, no request attached (Template 19.4's promise-delivered notice).")
else:
    print(f"Latest same-side streak: {streak} points (threshold {a.run}), no special cause yet, hold the short notice, keep watching.")
