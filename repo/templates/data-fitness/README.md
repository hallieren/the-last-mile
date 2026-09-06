# data-fitness

Corresponding template: Template 9, Data Source Inventory, Fitness Scorecard, Reconciliation Checklist, Source of Truth Decision Log (companion: Chapter 9) ([full appendix](../../../docs/appendices/template-09-data-fitness.md)).
Purpose: a fillable scaffold for the seven-rung fitness scorecard, plus a record-by-record three-way reconciliation log and a summary script (reports the overall rate together with the largest single class).

| File | What it is | How to use |
|------|--------|--------|
| `fitness-scorecard.md` | The 9.2 fillable seven-rung scorecard (with rules) | Copy one per "data source x target action" pair, and judge rung by rung going up |
| `reconcile-records.csv` | The 9.3 blank CSV for record-by-record reconciliation (the second row is fill-in instructions, delete before use) | One row per sampled record: claim_id / system_value / private_source_value / handler_account / verdict / pattern / notes |
| `reconcile.py` | Reconciliation summary script: reads the record CSV, prints the overall inconsistency rate plus the largest single class and its share | `python3 reconcile.py records.csv`; with no arguments it demos on the sample |
| `sample/reconcile-records.csv` | 10 filled-in reconciliation records (sample data comes from the book's Anchor & Helm case: the core system x the review team's Excel tracker x the handler) | The script's default input; each of the four inconsistency patterns has an example |
