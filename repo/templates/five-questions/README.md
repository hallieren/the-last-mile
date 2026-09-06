# five-questions

Corresponding template: Template 7, Five-Question Opportunity Rubric (companion: Chapter 7) ([full appendix](../../../docs/appendices/template-07-five-questions.md)).
Purpose: a fillable five-question scorecard (Markdown/CSV, multiple candidates), plus a script that reads the scorecards and generates the reporting one-pager (elimination table).

| File | What it is | How to use |
|------|--------|--------|
| `scorecard.md` | The 7.1 blank scorecard (Markdown version, with the test questions and scoring discipline) | Copy one per candidate; people read it and fill it in |
| `scorecard.csv` | The 7.1 blank scorecard (CSV version, the script's input format) | Copy one per candidate, fill in scores and evidence; the condition field only needs filling once |
| `onepager.py` | Reporting one-pager generator: several cards → the 7.2 elimination table + the 7.3 one-pager | `python3 onepager.py card1.csv card2.csv [-o output.md]`; with no arguments it uses the samples |
| `sample/*.csv` | Three filled-in scorecards (sample data comes from the book's Anchor & Helm case, see 7.2) | The script's default input; also a reference for how to fill in the CSV |

The hard rule from 7.2 that the script enforces: any question scoring 2 or below eliminates the candidate outright (no weighting, no averaging); a score of 3 is a conditional pass; a blank evidence cell scores 2; eliminating every candidate is a valid outcome.
