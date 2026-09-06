# Field Kit: Companion Templates for The Last Mile

This directory holds the companion assets for *The Last Mile: A Field Guide to Deploying AI Systems That Survive the Enterprise*, working implementations of every part of the book's 24 appendix templates that can be turned into scaffolding. **Readers may modify the templates and scripts freely and use them at work, no attribution needed** (see LICENSE in this directory, MIT).

## How to Use

- Each `templates/<name>/` directory maps to one appendix template, and the README inside states the mapping and what each file is for.
- Every script runs on Python 3.9+ with the standard library alone, zero third-party dependencies: `python3 <script>.py --help`. With no arguments it demonstrates itself on the built-in sample data.
- Charts are written as SVG. Open them straight in a browser.

## Directory to Template Map

(Template numbers match the chapter numbers; the index page is `../docs/appendices/template-library-index.md`)

| Directory | Template | Contents |
|------|------|------|
| field-mvp | Template 0 | Field MVP Pack table scaffold + prompt |
| role-charter | Template 2 | Role boundary walkthrough + one-pager template |
| self-assessment | Template 3 (3.0–3.6) | Five-axis radar script + team roll-up template |
| f-levels | Template 3 (3.7–3.8) | F-level rating questionnaire + radar to F-level comparison script |
| deployment-charter | Template 4 (4.1–4.2) | Charter scaffold + meeting-notes-to-charter prompt |
| premortem | Template 4 (4.3–4.6) | Pre-mortem facilitation prompt |
| stakeholder-map | Template 5 | Six-role table scaffold + update reminder script |
| field-archaeology | Template 6 | Friction log template + transcript cleanup prompt |
| five-questions | Template 7 | Five-question scorecard + reporting one-pager script |
| thin-slice | Template 8 | Five Ones table + scope decision log script |
| data-fitness | Template 9 | Scorecard scaffold + three-way reconciliation log script |
| pattern-selection | Template 10 | Decision table template + schema check + spot-check log |
| eval-spec | Template 11 | Eval run scaffold + per-category threshold report |
| trust-constraints | Template 12 | Audit log schema + redaction rule config sample |
| stage-gates | Template 14 | Automatic eval threshold check + kill criteria weekly report |
| cobuild | Template 15 | Repo/CI ownership list + PR template (the three explain-it questions) |
| production-readiness | Template 16 | Unit cost dashboard + drift alert + trace fields |
| action-queue | Template 17 | Decision trail DDL + reason code config + override weekly query |
| metric-tree | Template 18 | Run chart script + override alert config |
| memo-suite | Template 19 | Three-memo outline prompt + run chart short notice script |
| adoption | Template 21 | Daily-active and depth weekly query + retrospective one-pager script |
| handoff | Template 22 | Machine-readable handoff checklist + validation script |
| pattern-library | Template 23 | Asset register in two versions + demotion script + packaging sample |
| f2p-memo | Template 24 | F2P memo template + candidate register |
| asset-recovery | Template 24 | Closeout asset recovery checklist |
| intake | Template 25 | Five-dimension rubric + red line checklist + kill register + expiry reminder |

Template 20 (the resistance decoder) has no code companion; the queue-side config samples are in `action-queue/`.

## Notes

- Sample data comes from the book's fictional Anchor & Helm Insurance case (a composite, matching no real company).
- Prompts are bound to no specific model or vendor.
- The data formats shared across directories (decision trail tables, run chart CSV, radar CSV, eval report, asset register) are defined in Section 2 of `CONVENTIONS.md`.
