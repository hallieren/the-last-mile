# metric-tree

- **Corresponding template**: Template 18 (Metric Tree Template + AI Incident Runbook) ([full appendix](../../../docs/appendices/template-18-metric-tree.md))
- **One-sentence purpose**: Build the metric tree into a one-pager where every metric has an owner and an action on deviation, with the run chart auto-flagging special cause so an improvement claim only gets made when a signal shows up.
- **File list**:

| File | What it is | How to use |
|------|--------|--------|
| `metric-tree.md` | Three-layer structure (North Star / process / balancing + monitoring surface) fillable template | Fill it in line by line following the Anchor & Helm example in 18.1.2; the owner and action-on-deviation columns may not be left blank |
| `run_chart.py` | Run chart SVG generator: baseline median + automatic "six points on one side" flagging | `python3 run_chart.py data.csv --baseline N` (with no arguments, uses the sample/ data) |
| `override-alert-config.json` | Sample override alert threshold config (per category + sudden change + fairness spot check) | Rewrite the thresholds and owners against your own categories |
| `sample/run-chart.csv` | Sample data (CONVENTIONS §2.2 format, Anchor & Helm North Star, 12 weeks) | `run_chart.py`'s default input; the last 6 weeks reproduce a -18% to -22% improvement segment |
| `sample/run-chart.svg` | Sample output: the special cause segment already flagged | Open it in a browser to view |

Data format (cross-directory interface): CSV header `period,value`, defined by this directory and reused by memo-suite. See CONVENTIONS §2.2.
