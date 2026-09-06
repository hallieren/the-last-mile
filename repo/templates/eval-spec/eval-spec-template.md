# Eval Spec (Five-Part Fillable Template)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
> Source: Template 11.1 (companion: Chapter 11). **One eval spec evaluates one task.** Collect cases per the 11.2 collection list, log annotation disagreements per 11.3.

| Item | Fill In |
|----|----|
| Project name | ____ |
| Version and date | ____ |
| Co-builder (actual user, named) | ____ |
| Next retest trigger condition | ____ |

## 1. Task Definition (11.1.1)

| Item | Fill In |
|----|----|
| One-sentence task (workflow claim level) | ____ |
| Input (data source and fields; cite the source-of-truth decision log, Template 9.4) | ____ |
| Output (field list; suggestion + reason + Human Call column must be present) | ____ |
| User (named down to the team) | ____ |
| Red line (what this task does not do; cite the scope decision log, Template 8) | ____ |

## 2. Golden Cases List (11.1.2, 50-200 cases)

| Case ID | Source Type (typical / edge / historical incident / annotation disagreement) | Input Summary | Correct Answer | Answer Basis (reconciliation evidence / party confirmation) | Annotator | Date |
|---------|------|----------|----------|----------|--------|------|
| | | | | | | |

Rules:
- [ ] Every fact a "correct answer" cites must sit at or above validated on the data fitness ladder. If it does not reconcile, run the three-way reconciliation first (Template 9.3); drop it if it still cannot be settled.
- [ ] Cite the annotation guide entry the answer rests on. The guide carries a dated version.
- [ ] Check the set's composition against the 11.2 mix line: typical cases under half, edge cases at least 30%, historical incident cases at least 10%, disagreement cases added on an ongoing basis.

## 3. Error Taxonomy (11.1.3)

| Error Category | Definition | Business Consequence | Error Severity Vocabulary (unsafe / concern / useless) | Tolerance |
|----------|------|----------|-----------------------------------|--------|
| | | | | |

Rules: derive the unsafe category by first asking the actual user "which kind of error can you not accept even once." Write the "consequence" for each category, not the "technical reason." The taxonomy is layered by cost, not by bug type.

## 4. Per-Category Thresholds and Acceptance Line (11.1.4)

| Error Category | Threshold (on golden cases) | Acceptance Line | Retest Cadence |
|----------|------------------------|--------|----------|
| | | | |

Rules: **no overall score**. Thresholds and the charter's acceptance clause cite each other (Chapter 4). The machine-readable threshold table is at `sample/thresholds.json` (CONVENTIONS §2.4 format, unsafe always 0).

## 5. Human Review Path (11.1.5)

| Item | Fill In |
|----|----|
| Trigger condition | ____ |
| Destination and owner | ____ |
| Time limit (how soon the review must happen) | ____ |
| Flow-back mechanism (review conclusions are added to the golden cases monthly; suspected unsafe-class errors are reviewed weekly) | ____ |
