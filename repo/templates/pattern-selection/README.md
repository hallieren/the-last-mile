# pattern-selection

- Corresponding template: Template 10 (Pattern Decision Table and Anti-pattern List; Chapter 10) ([full appendix](../../../docs/appendices/template-10-pattern-decision.md))
- One-sentence purpose: Pick a pattern for every AI intervention point, and give the "structured extraction + rules" pattern a validation and spot-check scaffold
- File list:

| File | What it is | How to use |
|------|--------|--------|
| `decision-table/` | Fillable decision table template + a prompt that generates a candidate intervention point list | List intervention points with the prompt first, then fill the decision table for each one (10.2/10.3) |
| `schema-check/` | Schema validation script for extraction output | Rejects malformed records one by one and logs them to a CSV (the "validation layer" for the structured-extraction-plus-rules row in 10.2) |
| `spot-check/` | Spot-check record template + sampling script | Schema check catches format errors; spot-check watches for semantic errors (10.3 code hook) |

The order of these three tools is the 10.3 filling-in process, list intervention points first, then run the decision table for each one, then for any point that picks "structured extraction + rules," use schema-check to build the validation layer and spot-check to build the sampling process.
