# pattern-selection/schema-check

- Corresponding template: 10.2's "structured extraction + rules" row, 10.3 code hook
- One-sentence purpose: Run schema validation on extraction output (field types / enum values / required fields), pass or reject record by record, log rejections to a CSV. This pattern is usable in near-zero-tolerance steps only when the validation layer really exists
- File list:

| File | What it is | How to use |
|------|--------|--------|
| `check_schema.py` | Schema validation script | `python3 check_schema.py` (runs the sample with no arguments); `--schema --input --log` to point at your own files |
| `sample/schema.json` | Minimal sample schema definition | Field name → `{type, required, enum?}`; type is one of string / number / boolean |
| `sample/extractions.jsonl` | Sample extraction output to validate (Sample data comes from the book's Anchor & Helm case, with 3 rejects) | One JSON object per line |

Schema validation only catches format errors; semantic errors, where the format is right but the content is wrong, are watched for by `../spot-check/`. Identifiable information in the sample has been replaced with placeholders per the privacy line in Template 12.1.
