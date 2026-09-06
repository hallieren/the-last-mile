# eval-spec

Corresponding template: Template 11, Eval Spec, Golden Case Collection List, Annotation Disagreement Log (companion: Chapter 11) ([full appendix](../../../docs/appendices/template-11-eval-spec.md)).
Purpose: the Eval Spec five-part fillable template, plus a minimal running scaffold for "golden cases × system output → replay report → per-category threshold table."

| File | What it is | How to use |
|------|--------|--------|
| `eval-spec-template.md` | The Template 11.1 five-part fillable template, section by section | One per task. Fill in 11.1.1 first, then collect cases |
| `run_eval.py` | Eval running scaffold | Compares the golden cases CSV against the system output CSV, produces a CONVENTIONS §2.4 format replay report |
| `threshold_report.py` | Per-category threshold report script | Reads the replay report plus the threshold JSON, outputs a table of each category's share vs. threshold (unsafe is always zero tolerance); exit code 0 if everything clears, 1 otherwise |
| `sample/golden_cases.csv` | Golden cases sample (10 rows). Sample data comes from the book's Anchor & Helm case | Columns: case_id, input, expected_category, mismatch_verdict |
| `sample/system_output.csv` | System output sample | Columns: case_id, output_category |
| `sample/thresholds.json` | Threshold table sample (CONVENTIONS §2.4 format) | `{"unsafe": 0, "concern": 0.10, "useless": 0.20}` |
| `sample/replay.csv` | Replay report sample (the output of `run_eval.py` on the samples above) | Feeds the `threshold_report.py` no-argument demo; also the input format for `../stage-gates/` |

Data format notes:
- The replay report = CONVENTIONS §2.4: `case_id,category,verdict`, verdict is one of pass/concern/unsafe/useless. The stage-gates threshold check script consumes the same format.
- The golden cases `mismatch_verdict` column is the cost-family verdict (unsafe/concern/useless) pre-assigned for when this case gets judged wrong, following the 11.1.3 error taxonomy's rule to layer by cost. A correct judgment is pass.
- No overall score (the 11.1.4 rule): thresholds compare category by category. Any "overall accuracy" is the shortest path to burying unsafe.
