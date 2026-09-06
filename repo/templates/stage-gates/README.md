# stage-gates

- Corresponding template: Template 14, Stage Gate Checklist and Pilot Kill Criteria (companion: Chapter 14) ([full appendix](../../../docs/appendices/template-14-stage-gates.md))
- Purpose: auto-check Template 14.2 Gate one (eval over the line) before the escalation decision meeting, and track kill-criteria red lines weekly during the pilot
- File list:

| File | What it is | How to use |
|------|--------|--------|
| `gate_check.py` | Eval-over-the-line auto-check script | Reads the §2.4 replay report plus threshold JSON, outputs a per-item ✓/✗ checklist for 14.2 Gate one plus an overall verdict; exit code 1 if not cleared |
| `kill-criteria-weekly-report.md` | Kill criteria weekly report template | Copy and fill in at each Friday review; the red line comes from the 14.3 Anchor & Helm sample entry 1 |
| `sample/replay.csv` | Replay report sample (Sample data comes from the book's Anchor & Helm case) | Same format as `../eval-spec/`'s output (CONVENTIONS §2.4) |
| `sample/thresholds.json` | Threshold table sample | `{"unsafe": 0, "concern": 0.10, "useless": 0.20}` |

Interface note: `gate_check.py`'s input is in the exact same format as `../eval-spec/threshold_report.py` (CONVENTIONS §2.4): eval-spec produces the report, stage-gates makes the escalation ruling. Two Gate one items (flat trend, matching version) cannot be judged from a single replay, so the script lists them as pending manual confirmation. Gate two (willingness to use it daily) and Gate three (owner in place) are decided at the meeting, per Template 14.2, and are not automated.
