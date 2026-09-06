# pattern-selection/spot-check

- Corresponding template: 10.2's "structured extraction + rules" row, 10.3 code hook
- One-sentence purpose: After schema validation catches format errors, manual spot-checking watches for semantic errors (format is right but the content is wrong); the sampling script produces a to-check list, the record table captures the verdicts
- File list:

| File | What it is | How to use |
|------|--------|--------|
| `sample_cases.py` | Sampling script (fixed seed, reproducible) | `python3 sample_cases.py` (runs the sample with no arguments); `--input --rate --seed --out` to customize |
| `spot-check-record.md` | Spot-check record template (sample / verdict / semantic error category columns) | Copy one per spot-check batch, fill it in against the to-check list |
| `sample/extractions.jsonl` | Sample extraction output that has already passed schema validation (Sample data comes from the book's Anchor & Helm case) | The sampling script's default input |

The sampling pool should be records that **have already passed schema validation** (format errors are already rejected by `../schema-check/`). The threshold for the semantic error rate and the response action cite the eval spec (Template 11.1.4); this directory does not set its own separate standard.
