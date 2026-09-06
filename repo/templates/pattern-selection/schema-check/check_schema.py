#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Extraction output schema validation (Template 10.3 code hook): pass or reject record by record, log rejections to a CSV."""
import argparse
import csv
import json
from pathlib import Path

TYPES = {"string": str, "number": (int, float), "boolean": bool}


def check(record, schema):
    problems = []
    for field, spec in schema.items():
        if field not in record:
            if spec.get("required"):
                problems.append((field, "missing required field"))
            continue
        value = record[field]
        # bool is a subclass of int; catch it separately so true doesn't sneak into number
        if (spec["type"] == "number" and isinstance(value, bool)) or not isinstance(value, TYPES[spec["type"]]):
            problems.append((field, f"type should be {spec['type']}, got {type(value).__name__}"))
            continue
        if "enum" in spec and value not in spec["enum"]:
            problems.append((field, f"value outside enum: {value}"))
    return problems


def main():
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Extraction output schema validation script (Template 10.3): validates a JSONL file record by record against a minimal schema, logs rejections to a CSV")
    p.add_argument("--schema", default=str(here / "sample" / "schema.json"), help="Schema definition: field name -> {type, required, enum?}")
    p.add_argument("--input", default=str(here / "sample" / "extractions.jsonl"), help="JSONL file to validate")
    p.add_argument("--log", default="rejects.csv", help="Output path for the reject log CSV")
    args = p.parse_args()

    # Keys starting with an underscore (like the _note license line) are not field definitions
    schema = {k: v for k, v in json.loads(Path(args.schema).read_text(encoding="utf-8-sig")).items() if not k.startswith("_")}
    for field, spec in schema.items():
        assert spec.get("type") in TYPES, f"{field}: type must be one of {sorted(TYPES)}"

    rejects, total = [], 0
    for line_no, line in enumerate(Path(args.input).read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        total += 1
        record = json.loads(line)
        tag = record.get("claim_id", "?")
        problems = check(record, schema)
        if problems:
            print(f"Line {line_no} {tag}: rejected, " + "; ".join(f"{f}: {msg}" for f, msg in problems))
            rejects += [(line_no, tag, f, msg) for f, msg in problems]
        else:
            print(f"Line {line_no} {tag}: passed")

    with open(args.log, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["line_no", "claim_id", "field", "problem"])
        writer.writerows(rejects)
    rejected = len({r[0] for r in rejects})
    print(f"\n{total} total: passed {total - rejected}, rejected {rejected}; reject log → {args.log}")


if __name__ == "__main__":
    main()
