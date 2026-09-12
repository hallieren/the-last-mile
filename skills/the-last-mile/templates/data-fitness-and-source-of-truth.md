# Data fitness scorecard and source of truth decision log

Source: `docs/appendices/template-09-data-fitness.md` §9.1, 9.2, 9.4, with the §9.5 counterexample (and `repo/templates/data-fitness/fitness-scorecard.md`; the repo wins on conflict).

| Field | Value |
|---|---|
| Data source | <system, field or file> REQUIRED |
| Target action | <the next action this source must drive> REQUIRED |
| Scored by | <owner name> |
| Score date | <date> REQUIRED (fitness is a state, not a property; the conclusion has a shelf life) |

**Data source inventory** (inventory first, score second; anything that carries a business fact counts, private spreadsheets, mailboxes, chat groups, paper ledgers included)

| Data source | Type | Business owner | Key holder (permission path) | Coverage | Update method and frequency | Known problems | Target action supported |
|---|---|---|---|---|---|---|---|
| <source> | core system field / private spreadsheet / unstructured | <owner name> | <team + process> | <all records / one team only / one business line only> | <triggered at process nodes, lags by <period> / manual, same day / real time> | <what lies> | <action> |

**Fitness scorecard** (one column per data source × target action; judge upward from exists, stopping at the first rung that cannot produce evidence)

| Rung | Test question | Qualifying evidence | Verdict (pass / fail / unknown) | Evidence record |
|---|---|---|---|---|
| exists | Has this information been recorded? In which system, in which field? | A specific field or file location | | |
| accessible | Can it be read in a compliant, repeatable way, machine access included? | Permission in hand, not a one-off export | | |
| interpretable | Does the same value mean one thing across departments and across periods? | A value dictionary confirmed by two or more consumers | | |
| timely | Does the update frequency keep up with the target action? | Measured update lag ≤ the latency the action allows | | |
| traceable | Where did the value come from, who changed it? Can the same entity be matched across systems? | Lineage stated, join key spot check passes | | |
| validated | Has it been reconciled against reality? | Three-way reconciliation inconsistency rate + pattern (§9.3) | | |
| actionable | Holding it, can the "next action" be carried out by a specific person, and can an error be caught? | A trial run of the target action passes, errors detectable and traceable | | |

**Source of truth decision log** (one class of business fact, one source of truth)

| Business fact | Source of truth | Fallback source | Reason for the decision (cite reconciliation evidence) | Is the derived view read-only | Retest cadence | Owner (name + date claimed) |
|---|---|---|---|---|---|---|
| <fact> | <source> | <source> | <e.g. "<n>/<N> system statuses lagging; <source> updated same day"> | yes, writes back to no source | <monthly during the pilot / quarterly spot check after launch> | <owner name>, <date> |
| <operating repair item, e.g. status write-back> | / | / | <the half engineering cannot fix> | / | / | <business-side owner name>, <date> REQUIRED |

**Rules**
- Fill in business owner and key holder separately. The one holding the key (IT) approves the permission. Only the data's business owner can make the approval move.
- Coverage is required. Using a local source of truth as a global one is another way of lying.
- "Target action supported" is required. Fitness is relative to an action, and with no target action there is nothing to score.
- Always ask one question in an inventory interview: "Outside the system, where else do you record this yourselves?"
- "Unknown" is not a middle state. It is the polite way of writing fail. A launch decision treats it as fail.
- exists and accessible are the two cheapest rungs, and an organizational assurance or a successful demo proves only this far. validated has no shortcut. It goes only through the reconciliation in §9.3.
- Derived views are read-only without exception, writing back to no source system. AI output exists as a decision trail (suggestion + reason + Human Call + timestamp), physically separated from the source fields.
- Operating-side repair items name the business-side owner and the action. That half is not something your system can fix.
- Retest triggers (any one reruns §9.3 without waiting for the retest date): rotation in a key role; team staffing change (the engineer on your team who owns this line changes); a source system upgrade or a process revision; your system live for a month; the override rate or the "status in doubt" list length rises abnormally.

**What a wrong filling looks like** (a full table, not one cell blank, and every cell wrong)
- accessible = pass on "IT confirmed verbally": an organizational assurance, not evidence.
- interpretable and timely = "under confirmation": unknown is fail, and once interpretable fails the four rows below it carry no verdict at all.
- traceable = pass on "<the director> says every change goes through approval", actionable = pass on "<the director> thinks the approach is workable": a title's endorsement in place of evidence; actionable needs a trial run of the target action.
- validated = pass on "the demo ran on last month's export with no errors": a demo proves only as far as accessible.
- No scoring date anywhere: no shelf life, no retest.
- exists evidence "the data platform says it is all synced over": syncing solved the hauling only.

Filled in → goes to: the reconciliation checklist (§9.3) for the validated rung; the eval spec (the inconsistency rate is the floor figure for how much error the data contributes to the golden cases); the charter's data boundary (approver names and dates); the quarterly data health report to the sponsor (one line per system).
