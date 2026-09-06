# thin-slice

Corresponding template: Template 8, Thin Slice Definition Sheet and Scope Decision Log (companion: Chapter 8) ([full appendix](../../../docs/appendices/template-08-thin-slice.md)).
Purpose: a fillable scaffold for the Five Ones definition sheet and the scope decision log, plus a lightweight CLI for maintaining the scope decision log.

| File | What it is | How to use |
|------|--------|--------|
| `thin-slice.md` | The 8.1 Five Ones definition sheet plus the 8.3 scope decision log (fillable Markdown, with rules) | Fill the definition sheet at project approval, review it at every milestone |
| `scope_log.py` | Scope decision log maintenance script: CSV stores the records, `add` appends / `list` groups by status | `python3 scope_log.py add -f log.csv expansion proposed_by rejection_reason revival_condition`; `list -f log.csv`; with no arguments it demos on the sample |
| `sample/scope-log.csv` | Three shelved records (sample data comes from the book's Anchor & Helm case, see 8.3) | The script's default input; also a reference for how to fill in the CSV |
