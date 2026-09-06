#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
import argparse
import csv
import pathlib

# Dimension names match Template 3 word for word (CONVENTIONS §2.3)
DIMENSIONS = ["engineering depth", "AI engineering", "business grasp", "narrative", "field judgment"]


def load_scores(path):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert [r["dimension"] for r in rows] == DIMENSIONS, (
        f"{path}: must be five rows, with dimension names and order matching Template 3 word for word: {DIMENSIONS}")
    scores = [float(r["score"]) for r in rows]
    assert all(1 <= s <= 5 for s in scores), f"{path}: score must be between 1 and 5"
    return scores


def main():
    p = argparse.ArgumentParser(
        description="Team self-assessment rollup (Template 3): several §2.3 radar CSVs to a Markdown rollup table, one row per person.")
    p.add_argument("csvs", nargs="*",
                   help="each member's radar CSV, or a directory holding them (default: demos on sample/team/)")
    args = p.parse_args()
    paths = [pathlib.Path(x) for x in args.csvs] or \
            [pathlib.Path(__file__).parent / "sample" / "team"]
    files = []
    for x in paths:
        files += sorted(x.glob("*.csv")) if x.is_dir() else [x]
    assert files, "no CSV files found"

    print("| Member | " + " | ".join(DIMENSIONS) + " | Lowest axis (30-day target) |")
    print("|------" * 7 + "|")
    for f in files:
        scores = load_scores(f)
        low = min(scores)
        print(f"| {f.stem} | " + " | ".join(f"{s:g}" for s in scores)
              + f" | {DIMENSIONS[scores.index(low)]} ({low:g}) |")
    print("\nHow to read this table (Template 3.6): the lowest axis sets how big a project each person can own on "
          "their own. The five axes multiply, they do not add. Strengthen one axis at a time, and the target must "
          "be a verifiable behavior, not an adjective.")


if __name__ == "__main__":
    main()
