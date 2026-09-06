> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/handoff

- Corresponding template: Template 22 (Handoff Plan, Five Self-Sufficiency Tests, Handoff Cadence Sheet; Chapter 22) ([full appendix](../../../docs/appendices/template-22-handoff.md))
- One-sentence purpose: Turn handoff from a verbal promise into a machine-checkable checklist. An empty name is an alarm, and a failed item cannot pass without a rework action attached.

| File | What it is | How to use |
|------|--------|--------|
| `checklist.yaml` | Machine-readable handoff checklist template: the four owners and the three AI items named by name, the five self-sufficiency capability state machine (pending/failed/passed), the response window (Anchor & Helm week 25 snapshot sample) | Copy and fill in; flat key: value, no nesting |
| `check_handoff.py` | Validation script: alarms on an empty name; a failed item must have `cap_<capability>_rework` and `cap_<capability>_retest` attached | `python3 check_handoff.py [checklist.yaml]`; exits 1 on an alarm |
| `sample/checklist.yaml` | Alarm demo sample: maintenance owner left blank, plus a failed teach capability with no rework attached | The script's default input |
| `help-log.md` | Response-window help-request log template (Markdown table) | Log every request during the window; review before it closes |

Design note: the standard library has no YAML parser. The checklist is deliberately kept as flat key: value pairs, and the validation script hand-writes a ten-line parser. That is the book practicing its own dependency discipline, not cutting corners.
