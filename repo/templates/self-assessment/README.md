# self-assessment, Capability Self-Assessment Companion Tools

Corresponding template: Template 3, Capability Self-Assessment and F1–F5 Rating, sections 3.0–3.6, the self-assessment part (companion: Chapter 3) ([full appendix](../../../docs/appendices/template-03-capability.md)).
Purpose: turn the five-axis self-assessment scores (engineering depth / AI engineering / business grasp / narrative / field judgment) into a radar chart and a team rollup. Data format: CONVENTIONS §2.3; archive it for reuse by the rating step in Template 3 (f-levels/).

| File | What it is | How to use |
|------|--------|--------|
| radar.py | Five-axis radar chart SVG generator (standard library only) | `python3 radar.py [my.csv] [-o out.svg]`; with no arguments, demos on sample/ |
| team-summary.py | Multiple CSVs to Markdown rollup table | `python3 team-summary.py <directory-or-csvs>`; with no arguments, demos on sample/team/ |
| sample/radar.csv | Single-person sample (sample data comes from the book's Anchor & Helm case: the Chapter 26 closeout self-assessment, F2, near F3 on AI engineering and narrative) | Copy it and change the scores to make your own self-assessment archive |
| sample/team/*.csv | Three team samples (member-a same as above; b and c are placeholder demo data) | Team rollup demo input |

Scoring method (behavior anchors, self-rating questions, blind calibration) is in the Template 3 text. Re-score every quarter and archive the CSV by date.
