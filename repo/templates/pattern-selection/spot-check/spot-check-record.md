# Spot-Check Record (Extraction Output Semantic Errors)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
> Source: Template 10.3. Schema validation (`../schema-check/`) catches format errors; this table watches for **semantic errors**, where the format is right but the content is wrong.

## Batch Information

| Item | Fill In |
|----|------|
| Source file / batch | ____ |
| Total records / sampling rate / sample size | ____ |
| Random seed (to reproduce the same batch of samples) | ____ |
| Checked by / date | ____ |

## Record by Record (transcribed from the to-check list `sample_cases.py` generates, or filled in directly on the CSV)

| Seq | Line No | claim_id | Verdict (Pass / Semantic Error) | Error Category | Note |
|------|------|----------|------------------------|--------------|------|
| | | | | | |

Semantic error category enum (≤7 categories + other, rewrite to fit the field and then keep fixed):

Field value miscopied / Category misjudged / Missed extraction (present in the source, not extracted) / Fabricated (not in the source, made up) / Unit or format ambiguity / other

## Batch Conclusion

| Item | Fill In |
|----|------|
| Semantic error rate (error count divided by sample size) | ____ |
| Whether it triggers a response (threshold and action cite the eval spec, Template 11.1.4) | ____ |
| Feedback loop (semantic-error records get folded into golden cases, Template 11.2) | ____ |
