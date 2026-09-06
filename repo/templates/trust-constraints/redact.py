#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Redaction rule demo (Template 12.1 privacy row): applies placeholder/hash/drop to each JSONL record per JSON rules."""
import argparse
import hashlib
import json
from pathlib import Path


def redact(record, rules):
    out = dict(record)
    for field, rule in rules.items():
        if field.startswith("_") or field not in out:  # skip comment keys such as _note
            continue
        if rule["strategy"] == "placeholder":
            out[field] = rule["placeholder"]
        elif rule["strategy"] == "hash":
            # truncated hash as a stable pseudonym, keeps cross-claim linkage (e.g. a phone number's third appearance); a real deployment should add salt
            out[field] = "h_" + hashlib.sha256(str(out[field]).encode()).hexdigest()[:12]
        elif rule["strategy"] == "drop":
            del out[field]
        else:
            raise AssertionError(f"{field}: unknown strategy {rule['strategy']} (supported: placeholder/hash/drop)")
    return out


def main():
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Redaction rule demo script (Template 12.1): applies field-level redaction rules to JSONL")
    p.add_argument("--rules", default=str(here / "redaction-rules.json"), help="Rule JSON: field → {strategy, placeholder?}")
    p.add_argument("--input", default=str(here / "sample" / "claims.jsonl"), help="Pre-redaction JSONL")
    p.add_argument("--out", default="claims-redacted.jsonl", help="Post-redaction JSONL output path")
    args = p.parse_args()

    rules = json.loads(Path(args.rules).read_text(encoding="utf-8-sig"))
    lines = [l for l in Path(args.input).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    redacted = [redact(json.loads(l), rules) for l in lines]
    Path(args.out).write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in redacted) + "\n", encoding="utf-8")

    print(f"Applied {sum(1 for k in rules if not k.startswith('_'))} rules to {len(redacted)} records → {args.out}")
    print("First record, before and after:")
    print("  before: " + lines[0])
    print("  after:  " + json.dumps(redacted[0], ensure_ascii=False))
    print("Verification reminder: sample N redacted records for a re-identification test and record the result (Template 12.2 §5)")


if __name__ == "__main__":
    main()
