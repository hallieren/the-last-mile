# f-levels, F1–F5 Rating Tool

Corresponding template: Template 3, Capability Self-Assessment and F1–F5 Rating, sections 3.7–3.8 (companion: Chapter 26) ([full appendix](../../../docs/appendices/template-03-capability.md)).
Purpose: first rate yourself with the questionnaire's behavior anchors (overall level = the lowest of the five axes), then use the comparison script to turn Template 3's quarterly self-assessment archive into an axis-by-axis trend plus F-level verdict, feeding into the annual growth agreement.

| File | What it is | How to use |
|------|--------|--------|
| `questionnaire.md` | The F-level rating questionnaire (a fillable version of the 3.7 anchor table: check anchors, write evidence) | Copy it, verify each cell's "you as the subject" evidence, then set the overall level |
| `radar-to-flevel.py` | Historical radar to F-level mapping comparison script | `python3 radar-to-flevel.py [directory or CSV files]`; with no arguments it demos on sample/ |
| `sample/2025-q*.csv` | Three historical self-assessment samples (CONVENTIONS §2.3 format, sorted by filename as a time series) | The last one matches Chapter 26's Anchor & Helm closeout self-assessment (overall level F2); the first two are placeholder demo data |

Data format matches `templates/self-assessment/` exactly (CONVENTIONS §2.3): the quarterly self-assessment archive runs directly, no conversion needed.
Score to F-level mapping rule: round down (2.8 → F2); a level counts only once every anchor has evidence (3.7 rule 1). The script's output is a lead, not a verdict; the rating is settled by the questionnaire.
