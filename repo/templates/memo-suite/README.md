> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/memo-suite

- Corresponding template: Template 19 (Three-Memo Set, with ADR; Chapters 13, 19) ([full appendix](../../../docs/appendices/template-19-memo-suite.md))
- One-sentence purpose: hand the structural grunt work of the kickoff / decision / impact memos to a tool, the outline to a prompt, the short notice and send timing to scripts, and leave the conclusion in one sentence to a person, always.

| File | What it is | How to use |
|------|--------|--------|
| `prompt-memo-scaffold.md` | Three-memo outline scaffold prompt (the conclusion in one sentence is forced blank) | Hand the whole thing, together with your phase data, to whatever model you use |
| `runchart_signal.py` | Run chart short notice script: detects "N points on one side," prints a one-line "point N" short notice | `python3 runchart_signal.py [csv] [--baseline N] [--run N]` |
| `remind_milestones.py` | Send-timing reminder: works back from "48 hours before the meeting" to the delivery deadline | `python3 remind_milestones.py [csv] [--today YYYY-MM-DD]` |
| `sample/runchart.csv` | §2.2 format sample data (sample data comes from the book's Anchor & Helm case: first-touch handling time, weekly points) | Default input for both scripts |
| `sample/milestones.csv` | Sample milestone calendar (date,meeting,memo) | Default input for `remind_milestones.py` |

Note: kickoff's formal timing is "Monday of the week the phase starts" (19.4); the calendar reminds 48 hours before the meeting too, and reminding early does no harm. The sample CSVs are pure data files, with no license line added, to keep the §2.2 format clean.
