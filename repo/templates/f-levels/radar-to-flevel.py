#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
import argparse
import csv
import pathlib

# Axis names match Template 3 word for word (CONVENTIONS §2.3)
DIMENSIONS = ["engineering depth", "AI engineering", "business grasp", "narrative", "field judgment"]


def load_scores(path):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert [r["dimension"] for r in rows] == DIMENSIONS, (
        f"{path}: must be five rows with dimension names and order matching Template 3 word for word: {DIMENSIONS}")
    scores = [float(r["score"]) for r in rows]
    assert all(1 <= s <= 5 for s in scores), f"{path}: score must be between 1 and 5"
    return scores


def f_level(score):
    # Score rounds down to an F level: a level only counts once every anchor has evidence (Template 3.7 rule 1), so no rounding
    return int(score)


def main():
    p = argparse.ArgumentParser(
        description="Historical radar to F-level mapping (Template 3): reads several CONVENTIONS §2.3 radar CSVs "
                    "(sorted by filename as a time series), and prints each axis's trend plus the F-level verdict "
                    "under the 'overall level = the lowest axis' rule.")
    p.add_argument("csvs", nargs="*",
                   help="historical self-assessment CSVs, or a directory containing them (defaults to demoing on sample/)")
    args = p.parse_args()
    paths = [pathlib.Path(x) for x in args.csvs] or [pathlib.Path(__file__).parent / "sample"]
    files = []
    for x in paths:
        files += sorted(x.glob("*.csv")) if x.is_dir() else [x]
    assert files, "no CSV files found"
    files.sort(key=lambda f: f.name)
    history = [(f.stem, load_scores(f)) for f in files]

    names = [name for name, _ in history]
    print(f"{len(history)} historical self-assessments (sorted by filename as a time series): {' → '.join(names)}\n")
    print("| Axis | " + " | ".join(names) + " | Trend | Latest F Level |")
    print("|------" * (len(names) + 3) + "|")
    latest = history[-1][1]
    for i, dim in enumerate(DIMENSIONS):
        series = [scores[i] for _, scores in history]
        trend = "/" if len(series) == 1 else \
            ("↑" if series[-1] > series[0] else "↓" if series[-1] < series[0] else "→")
        print(f"| {dim} | " + " | ".join(f"{s:g}" for s in series)
              + f" | {trend} | F{f_level(series[-1])} |")

    low = min(latest)
    low_dims = ", ".join(d for d, s in zip(DIMENSIONS, latest) if s == low)
    print(f"\nOverall level = the lowest of the five axes (Template 3.7 rule 2) → **F{f_level(low)}** (weak axis: {low_dims})")
    print("Reminder: the score is only a lead. The rating is decided by behavioral-anchor evidence. Verify it cell by cell with questionnaire.md before writing it into the annual growth agreement (Template 3.8).")


if __name__ == "__main__":
    main()
