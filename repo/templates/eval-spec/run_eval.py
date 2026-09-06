#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Eval running scaffold (Template 11): compares golden cases against system output case by case, produces a CONVENTIONS §2.4 replay report."""
import argparse
import csv
from pathlib import Path

VERDICTS = {"pass", "concern", "unsafe", "useless"}


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def main():
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Eval running scaffold (Template 11): compares golden cases against system output, produces a §2.4 format replay report")
    p.add_argument("--golden", default=str(here / "sample" / "golden_cases.csv"), help="Columns: case_id,input,expected_category,mismatch_verdict")
    p.add_argument("--output", default=str(here / "sample" / "system_output.csv"), help="Columns: case_id,output_category")
    p.add_argument("--report", default="replay.csv", help="Replay report output path (case_id,category,verdict)")
    args = p.parse_args()

    golden = read_csv(args.golden)
    outputs = {r["case_id"]: r["output_category"] for r in read_csv(args.output)}

    rows = []
    for g in golden:
        cid = g["case_id"]
        assert cid in outputs, f"System output is missing case {cid} (the replay version must equal the version being evaluated, no partial output allowed)"
        assert g["mismatch_verdict"] in VERDICTS - {"pass"}, f"{cid}: mismatch_verdict must be one of unsafe/concern/useless"
        got = outputs[cid]
        verdict = "pass" if got == g["expected_category"] else g["mismatch_verdict"]
        rows.append((cid, g["expected_category"], verdict))
        note = "=" if verdict == "pass" else f'≠ actual "{got}"'
        print(f"{cid}  expected \"{g['expected_category']}\"  {note}  → {verdict}")

    with open(args.report, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["case_id", "category", "verdict"])
        writer.writerows(rows)

    counts = {}
    for _, _, v in rows:
        counts[v] = counts.get(v, 0) + 1
    print(f"\n{len(rows)} cases total: " + ", ".join(f"{k} {n}" for k, n in sorted(counts.items())) + f"; replay report → {args.report}")
    print("Run threshold_report.py for the pass/fail call (per category, no overall score, Template 11.1.4)")


if __name__ == "__main__":
    main()
