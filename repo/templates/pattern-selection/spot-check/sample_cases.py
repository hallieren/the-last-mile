#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Spot-check sampling (Template 10.3 code hook): randomly samples a JSONL file by rate, produces a to-check list CSV."""
import argparse
import csv
import json
import random
from pathlib import Path


def main():
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Spot-check sampling script (Template 10.3): randomly samples N records from a JSONL file by rate, produces a to-check list")
    p.add_argument("--input", default=str(here / "sample" / "extractions.jsonl"), help="JSONL file that has already passed schema validation")
    p.add_argument("--rate", type=float, default=0.3, help="Sampling rate (0-1], default 0.3")
    p.add_argument("--seed", type=int, default=42, help="Random seed, fixed so the same batch of samples can be reproduced")
    p.add_argument("--out", default="spot-check-list.csv", help="Output path for the to-check list CSV")
    args = p.parse_args()
    assert 0 < args.rate <= 1, "--rate must be within (0, 1]"

    lines = [(i, l) for i, l in enumerate(Path(args.input).read_text(encoding="utf-8-sig").splitlines(), 1) if l.strip()]
    n = max(1, round(len(lines) * args.rate))
    picked = sorted(random.Random(args.seed).sample(lines, n))

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["seq", "line_no", "claim_id", "summary", "verdict", "error_category", "note"])
        for seq, (line_no, line) in enumerate(picked, 1):
            summary = line if len(line) <= 80 else line[:77] + "..."
            writer.writerow([seq, line_no, json.loads(line).get("claim_id", "?"), summary, "", "", ""])

    print(f"{len(lines)} total, sampled {n} (rate={args.rate}, seed={args.seed}) → {args.out}")
    for seq, (line_no, _) in enumerate(picked, 1):
        print(f"  {seq}. line {line_no}")


if __name__ == "__main__":
    main()
