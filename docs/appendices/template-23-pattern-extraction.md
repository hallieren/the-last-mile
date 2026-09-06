# Template 23 · Pattern Extraction Sheet, Asset Register, Library Admission Checklist

> Companion chapter(s): Chapter 23. The three tools are arranged in flywheel order. At the closeout retrospective, use the extraction sheet to turn hero stories into candidate patterns (23.1), register them once they pass review (23.2), and let the review checklist keep the door (23.3).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

## 23.1 Pattern Extraction Sheet

One page per candidate pattern, six fields.

**Blank template**:

| Field | What to Fill In |
|----|---------|
| **Phenomenon** | Which project, which scene, at what frequency. Record it in the business side's own words as they were said, do not abstract yet |
| **Strip the field context** | Swap the business side's nouns for structural nouns, and state the transferable judgment in one sentence |
| **Applies when** | What structural features have to be present for it to be usable |
| **Does not apply when** | Where using it breaks. Required. Cannot write it, cannot admit it |
| **Field provenance** | Project, date, link to the validation record, who was there |
| **owner** | Real name plus date claimed. The owner is responsible for revisions and the quarterly recheck |

**Anchor & Helm example** (using "chase ≠ risk"):

| Field | Anchor & Helm's Entry |
|----|----------|
| **Phenomenon** | The Anchor & Helm Field MVP. All 3 unsafe items Linda marked came from the system treating "chased many times" as a high-priority signal |
| **Strip the field context** | In any ranking scenario where the people being served can apply pressure, pressure intensity and business risk are two independent variables, and they must be modeled separately and shown separately |
| **Applies when** | Queue ranking scenarios with an outside party applying pressure (chasing a claim, chasing an assignment, chasing an order) |
| **Does not apply when** | Scenarios where the party applying the pressure is the risk (safety incident reporting, for example, where the most urgent caller is often the most dangerous case) |
| **Field provenance** | The week 1 Anchor & Helm MVP scoring sheet (Linda's original annotations). The week 31 re-verification at Swiftway (drivers chasing assignments ≠ waybill risk) |
| **owner** | [name] |

**The three stripping steps** (the operational definition of the generalize step):

1. **Swap the nouns**: exception claim → queue item, reviewer → handler, repair shop → outside party;
2. **Drop the numbers**: -31% is Anchor & Helm's result, not a property of the pattern. Numbers go into "field provenance," not into the judgment;
3. **Keep the structure**: after stripping, read it out to a colleague who never worked that project. If he can repeat back when to use it and when not to, the stripping is done.

## 23.2 Asset Register

Nine columns: class / name / one-line description / source project / validation count / owner / last updated / status (active, pending-reverify, retired) / force level (reference, recommended, mandatory, and with nothing declared it is taken as mandatory). The upstream entrance to this sheet is Template 24.2, the closeout asset recovery checklist, and the field mapping between the two sheets is in the last table of 24.2.

**Anchor & Helm's first batch admitted** (first admitted at the internal closeout retrospective in week 30. The validation counts below are a snapshot updated in week 34, covering the home property business side's own build and the items already field-tested at Swiftway. Swiftway's queue has not launched, so the queue-class components' reuse at Swiftway is not counted yet and gets added after launch. The sample table drops the "last updated" and "force level" columns):

| Class | Name | In One Line | Source | Validations | owner | Status |
|------|------|-----------|------|------|-------|------|
| Component | Queue skeleton | Column structure = the projection of the four layers of the decision rights boundary, the decide layer gets no column | Anchor & Helm | 2* | [name] | active |
| Component | Decision trail schema | Suggestion and fact tables kept separate, append-only, reason codes enumerated | Anchor & Helm | 2* | [name] | active |
| Component | Extraction pipeline interface | Unstructured input in, schema out, validation, spot-check tool. The interface is independent of the business domain | Anchor & Helm | 2* | [name] | active |
| Template | Three-way reconciliation checklist | System field / private source of truth / asking the handler, producing the inconsistency rate and pattern | Anchor & Helm | 2 | [name] | active |
| Template | Four adoption mechanisms plan | super-user / operating cadence / announcing wins / institutional anchoring | Anchor & Helm | 2* | [name] | active |
| Template | Three-layer probing script | anchor on an instance → compare → boundary counterexample | Anchor & Helm | 3* | [name] | active |
| Judgment rule | "Chase priority ≠ risk priority" | Pressure intensity and business risk modeled separately | Anchor & Helm | 2 | [name] | active |
| Judgment rule | "If you cannot say it, do not merge it." | AI-written code merges only after the maintaining side passes the explanation | Anchor & Helm | 2 | [name] | active |
| Metric model | Metric tree three-tier structure | North Star (outcome) / Process (mechanism) / Balancing (cost), every metric carrying an owner and an action | Anchor & Helm | 2* | [name] | active |
| Metric model | Error severity vocabulary | pass/concern/unsafe/useless plus the per-category threshold structure | Anchor & Helm | 2* | [name] | active |

\* Starred entries have one validation carried out by the business side (Anchor & Helm's home property team built it themselves). **The reuser does not have to be you. A third party's reuse counts as validation too, and it is the highest-grade kind.**

**Maintenance rules**:

- Entries with a validation count of 1 are marked "awaiting a second field test" and are down-weighted when a coding agent packs them;
- Every owner sweeps the assets in his name once a quarter. Anything not updated in over six months is automatically demoted to "pending-reverify" (the mechanized form of "an asset with no owner rots in six months");
- Retirement is not deletion. A retired entry keeps its original text and states why it was retired (the mirror of failure mode 4, a dead pattern is teaching material too).

## 23.3 Library Admission Checklist

When to review, in the same session as the closeout retrospective, no separate meeting (capture comes with its own review). Reviewers, the library owner plus one peer deliverer **who did not work on that project**. A pattern an outsider cannot read is a pattern whose stripping is not finished.

**The three criteria, item by item**:

- [ ] **Field validation**: at least one record of real use on the business side's floor. A demo, an internal team rehearsal, or a sandbox test does not count
- [ ] The validation record is linkable and checkable (scoring sheet, run chart, retrospective notes, decision trail data)
- [ ] **Boundary**: both the applies-when and the does-not-apply-when fields are filled in
- [ ] At least one does-not-apply condition comes from a real "we used it and it did not work" or from serious reasoning, not from boilerplate
- [ ] **owner**: claimed by name, with the owner knowing and agreeing (assignment without consent is not a claim)
- [ ] The owner can state the next expected reuse scenario for this asset

**AI pollution check** (any one unanswered and it is refused):

- [ ] Can you say which project, which weeks, who was in the room?
- [ ] Is there someone who can verify it? When the proposer was the only person present, it needs an endorsement from the business side or a teammate at the time
- [ ] Is there a failure record or a does-not-apply condition? A pattern with only upsides is a promotional piece, not an asset
- [ ] Does the content carry any "industry best practice" statement that cannot be traced back to a field? If so, delete it line by line or add the provenance

**Where AI's share stops**: AI may draft, structure, rewrite the language, and fill in formatting to the template. AI does the grunt work. People make the calls (Chapter 0's division of labor, recurring at library scale). AI may not supply "field provenance" or "validation record." Those two fields can only be filled in by someone who was on site.

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/pattern-library/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-library/): asset register structure (table and machine-readable versions), sample script that automatically demotes anything not updated in six months to "pending-reverify"
- [`templates/pattern-library/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-library/): fillable Pattern Extraction Sheet (includes the three-step stripping check)
- [`templates/pattern-library/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-library/): packing sample for feeding a component-class asset to a coding agent, the asset itself plus its boundary plus its validation record traveling with the package
