> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Asset Register (Markdown Version, Template 23.2)

The machine-readable version is `sample/assets.csv` (column names match CONVENTIONS §2.5 word for word). The two versions stay in sync; the machine-readable version is the source of truth, this table is for people to read and project during review.

Status enum: active / pending-reverify (pending re-verification) / retired. Category enum: template / component / judgment-rule / metric-model.

| Category | Name | One-Line Description | Origin | Verified Count | Owner | Last Updated | Status |
|------|------|-----------|----------|----------|-------|----------|------|
| component | queue skeleton | column structure = a projection of the four-layer decision rights boundary; the decide layer has no column | Anchor & Helm | 2* | [name] | 2026-06-28 | active |
| component | the decision trail schema | suggestion and fact in separate tables, append-only, reason code enum | Anchor & Helm | 2* | [name] | 2026-06-28 | active |
| component | the extraction pipeline interface | unstructured input in, schema out, validation and spot-check tooling; interface is domain-agnostic | Anchor & Helm | 2* | [name] | 2026-05-20 | active |
| template | three-way reconciliation checklist | system field / private source of truth / ask the handler, produces a discrepancy rate and pattern | Anchor & Helm | 2 | [name] | 2025-12-01 | active |
| template | four adoption mechanisms plan | super-user / operating cadence / announcing wins / institutional anchoring | Anchor & Helm | 2* | [name] | 2026-06-20 | active |
| template | three-layer probing script | anchor on an instance → compare → boundary counterexample | Anchor & Helm | 3* | [name] | 2026-07-01 | active |
| judgment-rule | "chase priority ≠ risk priority" | model chase pressure and business risk separately | Anchor & Helm | 2 | [name] | 2026-05-10 | active |
| judgment-rule | "if you cannot say it, do not merge it" | AI-written code only merges after the maintainer can explain it | Anchor & Helm | 2 | [name] | 2026-04-02 | active |
| metric-model | metric tree three-layer structure | North Star (outcome) / process (mechanism) / balancing (cost), every metric carries an owner and an action | Anchor & Helm | 2* | [name] | 2026-06-10 | active |
| metric-model | error severity vocabulary | pass/concern/unsafe/useless + a per-category threshold structure | Anchor & Helm | 2* | [name] | 2025-11-15 | pending-reverify |

\* Starred entries have one verification run by the business side itself (Anchor & Helm's home-property line, built in-house); reuse by a third party counts the same way, and carries the most weight. (Sample: from the book's Anchor & Helm case, week 34 snapshot.)

**Maintenance rules** (Template 23.2): a verified count of 1 is marked "awaiting a second live test" and gets weighted down when packed; the owner sweeps their own assets once a quarter; anything unrevised past six months auto-downgrades to pending-reverify (run `downgrade_stale.py`); a retired asset is never deleted, keep the original text and note the reason for retirement.
