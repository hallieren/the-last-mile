# Template 9 · Data Source Inventory, Fitness Scorecard, Reconciliation Checklist, Source of Truth Decision Log

> Companion chapter(s): Chapter 9. The four tools are in order of use. Inventory first (9.1), then score (9.2), verify the most expensive rung by reconciliation (9.3), and finally settle the conclusion into a source of truth decision (9.4).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 9.1 Data Source Inventory

Inventory first, score second. Anything that carries a business fact counts as a data source, including the ones you are embarrassed to call data sources, private Excel files, mailboxes, chat groups, paper ledgers. In the LLM era they are legitimate candidate sources, and often the only ones telling the truth.

| Data Source | Type | Business Owner | Key Holder (Permission Path) | Coverage | Update Method and Frequency | Known Problems | Target Action Supported |
|--------|------|-----------|------------------------|----------|----------------|----------|----------------|
| e.g. core claims system, claim status | Core system field | Director of Claims Operations | IT data team (request process + business owner sign-off) | All claims | Triggered at process nodes, lags by the week | "In progress" carries inconsistent meanings | Exception queue ordering |
| e.g. review team tracking Excel | Private spreadsheet | Review team lead | The team lead herself | This team's auto exception claims only | Manual, same day | Maintained by one team only, manual daily backup only | Candidate source of truth for claim status |
| e.g. survey-to-review mailbox traffic | Unstructured | / | Mailbox administrator + compliance | Document request correspondence | Real time | Needs LLM extraction, carries an error rate | "Waiting on documents" signal |

**Rules**:

- **Fill in business owner and key holder separately**. The one holding the key (IT) approves the permission. Only the data's business owner (the business lead) can make the approval move. The way out of a permission standoff lies with the latter (Chapter 5).
- **Coverage is required**. The most common trap with a private source of truth is that it covers one team only, or one line of business only. Using a local source of truth as a global one is another way of lying.
- **"Target action supported" is required**. Fitness is relative to an action, and with no target action there is nothing to score.
- Always ask one question in an inventory interview: **"Outside the system, where else do you record this yourselves?"** A private source of truth never appears on any architecture diagram of its own accord.

---

## 9.2 Fitness Scorecard

Score one column per "data source × target action" pair. **Judge upward from exists, stopping at the first rung that cannot produce evidence.** That is where it really stands. No skipping, and no verbal assurance in place of evidence.

| Rung | Test Question | Qualifying Evidence (Example) | Verdict (pass / fail / unknown) | Evidence Record |
|------|----------|------------------|---------------------------|----------|
| **exists** | Has this information been recorded? In which system, in which field? | You can point to a specific field or file location | | |
| **accessible** | Can it be read in a compliant, repeatable way (including machine access for the future system)? | Permission is in hand, and it is not a one-off export | | |
| **interpretable** | Does the same value mean one thing across departments and across periods? | A value dictionary confirmed by two or more consumers | | |
| **timely** | Does the update frequency keep up with the target action? | Measured update lag ≤ the latency the action allows | | |
| **traceable** | Where did the value come from, who changed it? Can the same entity be matched across systems? | Lineage can be stated, and the join key spot check passes | | |
| **validated** | Has it been reconciled against reality? | Three-way reconciliation inconsistency rate + pattern (9.3) | | |
| **actionable** | Holding it, can the "next action" be carried out by a specific person, and can an error be caught? | A trial run of the target action passes, errors detectable and traceable | | |

**Rules**:

- "Unknown" is not a middle state. It is the polite way of writing fail. A launch decision treats it as fail.
- exists and accessible are the two cheapest rungs, and an organizational assurance or a successful demo proves only this far.
- validated has no shortcut. It goes only through the reconciliation in 9.3.
- Date the scorecard. **Fitness is a state, not a property, and a scoring conclusion has a shelf life** (retest triggers in 9.4).

---

## 9.3 Three-Way Reconciliation Checklist

### Before the Reconciliation

- [ ] **Define the standard first**: write down in black and white what counts as inconsistent (suggested standard = cannot drive the target action at face value; report the total rate and the largest single class together). Define it before you touch the data.
- [ ] Choose the sample: 50–200 records, covering typical cases + edge cases + aged claims (the longest-waiting records, where field discipline is worst).
- [ ] Assemble all three sources: the system field export, the private source of truth (spreadsheet or email threads), the list of handlers and the interview times.
- [ ] Give the data's business owner a heads-up: the reconciliation is for assigning a source of truth, not for assigning blame, and sensitive fields and handler names in the report are all de-identified, with nobody named. Say this in advance, or you will be handed a "tidied up" second version of the scene.

### During the Reconciliation (Record Row by Row)

| # | Record ID | System Field Version | Private Source of Truth Version | Handler's Version | Verdict (consistent / inconsistent = cannot drive the target action at face value) | Pattern (lagging / forgotten / semantic divergence / broken join) | Notes (the handler's own words) |
|---|---------|--------------|----------------|------------|--------------------------------------------|-------------------------------------------|---------------------|

- [ ] Two ways can only find "they differ." Every disputed item has to reach the third way (asking the handler) before "who is right" can be ruled on.
- [ ] Spot-check the cross-system join key while you are at it: match 20 random records across systems and record the match failure rate.
- [ ] Write down the handler's own words. A line like "we never look at that field" is worth more than the inconsistency rate.

### After the Reconciliation

- [ ] Produce the **inconsistency rate**, total rate and largest single class reported together ("44% cannot be used at face value, and the largest class, the lagging pattern, is about three in ten" is more honest than a single number).
- [ ] Produce the distribution of **inconsistency patterns**, and triage by pattern:

| Pattern | Signature | Prescription | Belongs To |
|------|------|------|------|
| Lagging | The value is true, only slow | A faster source / extract the upstream signal | Engineering |
| Forgotten | An update that no process forces and that nobody is affected by gets skipped | Operating discipline + the system produces a "status in doubt" list to help | Mostly operating |
| Semantic divergence | One word, two departments, two meanings | Hold a semantic alignment meeting first, talk about syncing second | Organizational |
| Broken join | The same entity cannot be matched across systems | Fix the join key, and where it cannot be fixed, demote the signal | Engineering |

- [ ] Write the result up as a source of truth decision (9.4) and set the retest date.

---

## 9.4 Source of Truth Decision Log

One class of business fact, one source of truth. Every row is a defensible decision, formatted after the scope decision log (Template 8):

| Business Fact | Source of Truth | Fallback Source | Reason for the Decision (Cite Reconciliation Evidence) | Is the Derived View Read-Only | Retest Cadence | Owner (Name + Date Claimed) |
|----------|--------|--------|--------------------------|------------------|----------|----------------------------|
| e.g. claim status | Review team Excel | Core system | Reconciliation, 61/200 system statuses lagging; Excel updated same day | Yes, writes back to no source | Monthly during the pilot | You (during the pilot) → claims-ops IT after handoff (note the date claimed, Chapter 15) |
| e.g. payout amount | Core system | / | Runs through finance reconciliation, covered by audit discipline | / | Quarterly spot check after launch | Director of Claims Operations (note the date claimed) |

**Rules**:

- [ ] **Derived views are read-only without exception**, writing back to no source system. AI output exists as a decision trail (suggestion + reason + Human Call + timestamp), physically separated from the source fields (Chapter 17 works it out).
- [ ] Operating-side repair items (such as "status write-back") name the business-side owner and the action. That half is not something your system can fix.
- [ ] **Retest triggers** (any one of them hit reruns 9.3, without waiting for the retest date):
  - Rotation in a key role (the maintainer of the source of truth changes)
  - Team staffing change (the engineer on your team who owns this line changes, an internal-only trigger, counted separately from the business-side rotation above)
  - A source system upgrade or a process revision
  - Your system has been live for a month (it changes the front line's motivation to maintain the private source of truth, and your system will kill its own source of truth with its own hands)
  - The override rate or the length of the "status in doubt" list rises abnormally (Chapter 18's monitoring signal)

---

## 9.5 Counterexample: A Tidy-Looking Wrong Answer

Scoring target: the core system's "claim status" × exception queue ordering. The table is full, not one cell blank:

| Rung | Verdict | Evidence Record |
|---|---|---|
| exists | pass | The core system has this field, and the data platform says it is all synced over |
| accessible | pass | IT confirmed verbally that read-only access can be opened |
| interpretable | under confirmation | Emails already sent to the departments asking about the value meanings |
| timely | under confirmation | Waiting for IT to reply on update frequency |
| traceable | pass | Kevin says every change goes through approval |
| validated | pass | The demo ran on last month's export with no errors |
| actionable | pass | Kevin thinks the approach is workable |

Item by item:

1. accessible: a verbal confirmation is an organizational assurance, not evidence. The bar is "permission is in hand, and it is not a one-off export."
2. The two "under confirmation" entries: unknown is not a middle state, it is the polite way of writing fail, and a launch decision treats it as fail. And the rule is to stop at the first rung that cannot produce evidence. interpretable did not pass, so the four rows below it should carry no verdict at all.
3. traceable and actionable substitute a title's endorsement ("Kevin says," "Kevin thinks") for evidence. The qualifying evidence for actionable is a trial run of the target action, not anyone's opinion.
4. validated is scored pass on the strength of a demo running. A successful demo proves only as far as accessible, and validated has no shortcut, only the three-way reconciliation in 9.3. Chapter 9's lesson is exactly this. After the reconciliation, nearly half of this field cannot be used at face value.
5. No scoring date anywhere on the table. Fitness is a state, not a property, and a conclusion with no date has no shelf life and no retest to speak of.
6. The exists evidence, "the data platform says it is all synced over," is equally an organizational assurance, not field-level evidence. A data platform solves the hauling. Permission approvals, definition dictionaries, update latency and cross-system keys are equally unsolved (Chapter 9).

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/data-fitness/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/data-fitness/): this appendix's scorecard scaffolding and three-way reconciliation record script
