#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Unit cost dashboard (Template 16.1 cost ledger): per-claim distribution, per-stage breakdown, over-budget claim flags.

Call log CSV header: claim_id,stage,usage,unit_price
  usage = token count or call count; unit_price = unit price (dollars per unit, same unit as usage).
Sample data illustrates the book's Anchor & Helm case (AH-2026-104 reproduces the extraction retry-loop-out-of-control claim).
"""
import argparse
import csv
import pathlib

HERE = pathlib.Path(__file__).parent


def main():
    ap = argparse.ArgumentParser(
        description="Read a call log CSV, output the per-claim cost distribution plus a stage breakdown table (Template 16)")
    ap.add_argument("csv", nargs="?", default=str(HERE / "sample" / "calls.csv"),
                    help="Call log CSV (defaults to the sample/ Anchor & Helm data)")
    ap.add_argument("--budget", type=float, default=0.60,
                    help="Per-claim cost budget line ($/claim; derived from business value, not from last month's bill)")
    args = ap.parse_args()

    claims, stages = {}, {}
    with open(args.csv, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            assert {"claim_id", "stage", "usage", "unit_price"} <= row.keys(), \
                "CSV needs header claim_id,stage,usage,unit_price"
            cost = float(row["usage"]) * float(row["unit_price"])
            per_stage = claims.setdefault(row["claim_id"], {})
            per_stage[row["stage"]] = per_stage.get(row["stage"], 0) + cost
            stages[row["stage"]] = stages.get(row["stage"], 0) + cost

    totals = sorted(sum(s.values()) for s in claims.values())
    n = len(totals)
    p95 = totals[-(-95 * n // 100) - 1]
    grand = sum(totals)

    print(f"== Per-claim cost distribution ({n} claims, budget line ${args.budget:.2f}/claim) ==")
    print(f"min ${totals[0]:.2f}  median ${totals[n // 2]:.2f}  "
          f"P95 ${p95:.2f}  max ${totals[-1]:.2f}  total ${grand:.2f}")

    over = {c: s for c, s in claims.items() if sum(s.values()) > args.budget}
    if over:
        print(f"\nOver-budget claims ({len(over)}). The month-end bill should only ever be a confirmation, never news:")
        for cid, s in sorted(over.items(), key=lambda kv: -sum(kv[1].values())):
            detail = " / ".join(f"{k} {v:.2f}" for k, v in s.items())
            print(f"  {cid}  ${sum(s.values()):.2f} ({detail})")
    else:
        print("\nNo over-budget claims")

    print("\n== Stage Breakdown ==")
    print("stage | total cost ($) | share | per-claim ($)")
    for stage, total in sorted(stages.items(), key=lambda kv: -kv[1]):
        print(f"{stage} | {total:.2f} | {100 * total / grand:.1f}% | {total / n:.3f}")


if __name__ == "__main__":
    main()
