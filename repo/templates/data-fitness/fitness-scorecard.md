# Data Fitness Seven-Rung Scorecard (fillable)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
> Source: Template 9.2 (companion to Chapter 9). Score one column per "data source x target action" pair; the validated rung takes the three-way reconciliation result recorded by `reconcile.py` as its evidence.

Data source: ____ Target action: ____ Scored by: ____ Score date: ____ (fitness is a state, not a property; the conclusion has a shelf life)

| Rung | Test question | Qualifying evidence (example) | Verdict (pass / fail / unknown) | Evidence record |
|------|----------|------------------|---------------------------|----------|
| **exists** | Has this information been recorded? In which system, in which field? | You can point to a specific field or file location | | |
| **accessible** | Can it be read in a compliant, repeatable way (including machine access for the future system)? | Permission is in hand, and it is not a one-off export | | |
| **interpretable** | Does the same value mean one thing across departments and across periods? | A value dictionary confirmed by two or more consumers | | |
| **timely** | Does the update frequency keep up with the target action? | Measured update lag ≤ the latency the action allows | | |
| **traceable** | Where did the value come from, who changed it? Can the same entity be matched across systems? | Lineage can be stated, and the join key spot check passes | | |
| **validated** | Has it been reconciled against reality? | Three-way reconciliation inconsistency rate + pattern (9.3, paired with `reconcile.py`) | | |
| **actionable** | Holding it, can the "next action" be carried out by a specific person, and can an error be caught? | A trial run of the target action passes, errors detectable and traceable | | |

**Rules**:

- **Judge upward from exists, stopping at the first rung that cannot produce evidence.** That is where it really stands. No skipping, and no verbal assurance in place of evidence.
- "Unknown" is not a middle state. It is the polite way of writing fail. A launch decision treats it as fail.
- exists and accessible are the two cheapest rungs, and an organizational assurance or a successful demo proves only this far.
- validated has no shortcut. It goes only through the three-way reconciliation in 9.3.
