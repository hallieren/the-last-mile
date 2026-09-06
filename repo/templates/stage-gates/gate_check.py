#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Eval-over-the-line auto-check (Template 14.2, Gate one): reads the §2.4 replay report and threshold JSON, outputs a per-item checklist and an overall verdict."""
import argparse
import csv
import json
from pathlib import Path


def main():
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Eval-over-the-line auto-check script (Template 14.2, Gate one): compares each category against its threshold, outputs a checklist")
    p.add_argument("--report", default=str(here / "sample" / "replay.csv"), help="Replay report CSV (case_id,category,verdict)")
    p.add_argument("--thresholds", default=str(here / "sample" / "thresholds.json"), help='Threshold JSON, e.g. {"unsafe": 0, "concern": 0.10, "useless": 0.20}')
    args = p.parse_args()

    with open(args.report, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    total = len(rows)
    assert total > 0, "Replay report is empty"
    thresholds = json.loads(Path(args.thresholds).read_text(encoding="utf-8-sig"))
    counts = {v: sum(1 for r in rows if r["verdict"] == v) for v in ("unsafe", "concern", "useless")}

    # unsafe is always zero tolerance: judged by count = 0, ignoring share
    checks = [(f"unsafe: 0 cases (actual {counts['unsafe']}/{total})", counts["unsafe"] == 0)]
    for cat in ("concern", "useless"):
        share = counts[cat] / total
        checks.append((f"{cat}: within threshold ({share:.0%} vs ≤{thresholds[cat]:.0%})", share <= thresholds[cat]))

    print(f"Gate one: eval over the line (Template 14.2; {total} cases replayed)")
    for text, ok in checks:
        print(f"  [{'✓' if ok else '✗'}] {text}")
    print("  [ ] useless trend has not risen across three consecutive replays, needs a manual check of the last three replays")
    print('  [ ] the version replayed = the version that will enter the pilot, needs manual confirmation (no "we tested the previous build")')

    passed = sum(ok for _, ok in checks)
    if passed == len(checks):
        print(f"\nOverall: {passed}/{len(checks)} auto-checks passed; after the 2 manual items clear, run Gate two and Gate three per the 14.2 ruling rules")
    else:
        print(f"\nOverall: ✗ not cleared ({passed}/{len(checks)} auto-checks passed). Write down which evidence is missing, the action to fill it and who owns it, and set a date to reconsider; \"basically passed, start it first\" is not allowed")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()
