# Data reality: does this source deserve this action

**Load this reference when:** the business side says "the data is all in our system" or "it is all in the data lake already", two sources disagree about the same fact, the status field says one thing and the handler says another, or permissions have taken months.

Source: chapter 9 (`docs/chapters/ch09-data-fitness.md`); template 9 (`docs/appendices/template-09-data-fitness.md`); `repo/templates/data-fitness/fitness-scorecard.md`.

## Contents

Decisions (why fields lie; the seven rungs; three rules of use; three-way reconciliation; the four inconsistency patterns; convening power; operating half first; the source of truth decision; derived data and AI output) · Procedures · Detectors · Key judgments · Templates · Vendor seat

## Decisions

### Why fields lie, and why that is structural

- Expect the status fields to be a mess and the amount fields to be right almost row for row. Fields exist to leave a trail on the process, not to record reality; a field's update discipline runs only as far as "audit finds nothing", and audit watches amounts. Every previous consumer was a person with error correction built in (check the email, look at the spreadsheet, make a call). AI is the first consumer that takes the fields at their word, so it is the first to fall into the crack.
- "The data is all in our system" is true at the level the speaker can see. It speaks to rung one only. "Fully synced to the data lake" solved the hauling only; permission approvals, definition dictionaries, update latency and cross-system keys were not solved with it. The evidence is you running the target action against that table and reporting its inconsistency rate. On an internal project that sentence is often said by you or your manager at project approval; what you lack is one pair of eyes that does not believe it.

### The seven rungs

Score one column per data source × target action. Judge upward from exists, stopping at the first rung with no evidence. That is where the source really stands.

| Rung | Test question | Qualifying evidence |
|---|---|---|
| exists | Has this information been recorded anywhere? In which system, in which field? | You can point to a specific field or file location |
| accessible | Can you and the future system read it in a compliant, repeatable way (machine access included)? | Permission in hand, not a one-off export |
| interpretable | Does the same value mean one thing across departments and across time? | A value dictionary confirmed by two or more consumers |
| timely | Does the update frequency keep up with the action you want to drive? | Measured update lag ≤ the latency the action allows |
| traceable | Where did this value come from, who changed it? Are two systems talking about the same entity? | Lineage can be stated, and the join-key spot check passes |
| validated | Has it been reconciled against reality? What is the inconsistency rate, and in what pattern? | Three-way reconciliation inconsistency rate + pattern |
| actionable | Holding it, can the "next action" on that row be carried out by a specific person, and can an error be caught? | A trial run of the target action passes, errors detectable and traceable |

- Three rules of use. Judge rung by rung, no skipping: a verbal assurance covers only exists, a successful demo proves only accessible, exactly the two cheapest rungs. Fitness is relative to an action: the same table may top out for a monthly report and reach only rung two for same-day chasing, so write the action down before you score, and ask "does it deserve this action", never "is this data good". Fitness is a state, not a property: validated today is not validated in three months, so date every scorecard.
- Verdicts are pass / fail / unknown, and "unknown is the polite way of writing fail". A launch decision treats it as fail.
- The source is the analytics warehouse or BI store → it fails timely for any same-day action. T+1 data does not deserve a same-day action; a report can be a day late, chasing cannot. Ask "who was this source built to be consumed by?" A source built for people to look at does not, by default, deserve to drive machine action.

### Three-way reconciliation, the only way to validated

- Check every sampled record three ways: the system field (the official version), the private source of truth (the spreadsheet, the email threads dug out in field archaeology), and asking the handler ("where does this claim actually stand right now"). Two ways can only find "they differ". Only the third can rule on "who is right". Inside a company the handler sits two floors away, so the third way costs you nothing.
- Report two outputs, never one number. The inconsistency rate, total rate together with the largest single class ("44% cannot be used at face value, and the largest class, lagging, is about three in ten" (illustrative)), is for the decision. The inconsistency pattern is for the fix, and the prescriptions have nothing in common.
- The inconsistency rate becomes a data asset: it is the floor figure for how much error the data itself contributes when the golden cases are built.

| Pattern | Test question | Prescription | Belongs to |
|---|---|---|---|
| Lagging | Is the value true, only slow? | A faster source (the spreadsheet, the mailbox), extract the upstream signal | Engineering can solve it |
| Forgotten | Is the status change forced by any process, and is anyone affected by it? | Operating discipline, plus the system produces a "status in doubt" list to help | Operating; engineering cannot solve it |
| Semantic divergence | Are two departments using one word to record different facts? | Align the semantics first, talk about syncing second | Organizational, not ETL |
| Broken join | Are the two systems talking about the same entity? | Fix the join key; where it cannot be fixed, demote the signal to a reference, keep it out of the priority logic | Engineering |

### Convening power for the alignment meeting

- Semantic divergence needs a cross-department meeting you have no authority to convene. Convening power has three sources only: the sponsor authorizes it and hangs it on his own weekly agenda ("the definitions behind the queue need both departments to confirm", the fastest route); the existing data governance committee or master data management team, whose job it already is, with you as proposer; a personal relationship between the two department heads, usable, but a conclusion that leaves no record does not count.
- None of the three → do not force the meeting. Take the downgrade route: write the two meanings into the value dictionary as separate columns nobody is allowed to merge, then put the divergence and its business consequence into the weekly report that copies the sponsor. Nothing moves the first time. After the second, it becomes the sponsor's agenda.

### Operating half first, and traded for a name

- Half the fix is engineering, half is operating discipline, and you can only fix your half. Inside, both halves drift onto you; taking the operating half in the right order is what keeps them apart. Discuss the operating half first, for two reasons: it runs on ten minutes (illustrative) at the end of another department's day, so every day you delay speaking is a day later it starts; and whether the business owner puts his name to it decides which source the engineering half swaps to. Reverse the order and you finish the engineering half on an assumption nobody maintains.
- The owner cannot be you. Your name on an operating improvement announces that half will not be fixed, and the engineering work is wasted even when done.
- Trade for the name, do not argue for it. Give two things: decision rights over the source of truth (which table is authoritative is his to decide; you lay out the evidence), and a say in the schedule (once the item sits under his name it is a precondition, and the launch schedule moves with it). State the other half plainly: without the name the engineering half will not be built, because it would only spin in place. Hold this conversation in a one-hour meeting (illustrative) without the sponsor, and put the conclusion in the next weekly report that reaches him, so a third person sees the claiming happen.
- "Finding nobody who will put a name to it is a real conclusion, not a failed conversation." Write it in the log as "this class of fact has no operating owner", have engineering design for the worst case, then swap the source, demote it, or shrink the scope.

### The source of truth decision

- One class of business fact, one source of truth, lineage marked on the cell. Log columns: business fact | source of truth | fallback source | reason (cite the reconciliation evidence) | is the derived view read-only | retest cadence | owner (name + date claimed).
- Derived views are read-only without exception, writing back to no source system. A derived view that does not feed the source keeps the audit boundary clean at the security review.
- AI output is derived data too. It may exist only as a decision trail (suggestion, reason, Human Call, timestamp), physically separated from the source fields. Written back into a business field, the next model version learns its own old output as fact. Any AI output in a source field on the architecture diagram → change it to a decision trail today.
- Retest triggers, any one reruns the reconciliation without waiting for the date: rotation in a key role (the maintainer of the source of truth changes); team staffing change (the engineer on your team who owns this line changes, an internal-only trigger); a source system upgrade or process revision; your system live for a month (rule), because the front line then depends on the private source less and your system kills its own source of truth with its own hands; override rate or "status in doubt" list length rising abnormally.
- Nobody inside will ask when a retest date passes, so hang it on a carrier that does not depend on memory: the team's ops checklist, on the same sheet as certificate expiry, reviewed quarterly; or the quarterly data health report to the sponsor, one line per system (source of truth, last reconciliation date, inconsistency rate, retest conclusion), where blank cells speak for themselves.

## Procedures

**Inventory the sources.**
1. List everything that carries a business fact, including private spreadsheets, mailboxes, chat groups, paper ledgers. The truth often lives there.
2. Ask every interviewee "outside the system, where else do you record this yourselves?" A private source of truth never appears on an architecture diagram of its own accord.
3. Fill business owner and key holder separately. The key holder (IT) approves the permission; only the business owner can make the approval move.
4. Fill coverage. A source that covers one team only used as a global source is another way of lying.
5. Fill the target action supported. No target action, nothing to score.
6. Send the access request in week one of the project; approval duration is owned by nobody and data access is the hidden critical path. The fix lives in the trust network, not the ticketing system.

**Reconcile.**
1. Define the standard first, in black and white: inconsistent = cannot drive the target action at face value; report the total rate and the largest single class together. Reverse the order and you will tune the standard until the result looks good.
2. Give the data's business owner a heads-up: the reconciliation assigns a source of truth, not blame; fields and handler names are de-identified. Skip this and you are handed a tidied-up second version of the scene.
3. Sample 50–200 records (rule), covering typical, edge and aged cases; the longest-waiting records are where field discipline is worst.
4. Assemble the three sources: the system export, the private source of truth, the handler list with interview times.
5. Record row by row: record ID, system version, private version, handler's version, verdict, pattern, the handler's own words ("we never look at that field" is worth more than the rate).
6. Take every disputed record to the third way before ruling on who is right.
7. Spot-check the join key while you are at it: match 20 random records (rule) across systems and record the match failure rate.
8. Produce the two outputs, rate and pattern distribution, and triage by pattern.
9. Turn the result into decisions: one source of truth per class of fact, the engineering half and the operating half named, the retest date written.

**Settle the source of truth.**
1. Discuss the operating half first, in a one-hour meeting (illustrative) with the business owner and the actual user.
2. Offer the trade: source-of-truth decision rights and a say in the schedule, for a name and a date in the owner column.
3. Name the operating item and its action (e.g. status cleared before the team leaves each day, helped by a "status in doubt" list the system produces).
4. Only then set the engineering half: which source to swap to, the derived view read-only.
5. No name offered → log "no operating owner" and design for the worst case.
6. Put the conclusion in the next weekly report to the sponsor, and the retest on a carrier that fires without you.

## Detectors

- If the queue chases items resolved yesterday every morning, you are pulling from the analytics warehouse; T+1 does not deserve same-day action.
- If the schedule says three days for "data access" and the architecture diagram is finished with the data untouched, you underestimated permission time; each step takes days and no one owns the total.
- If "the data is fine" has gone into every report since discovery, you reconciled once and took a one-time verdict for a permanent conclusion.
- If the accessible cell says "IT confirmed verbally", that is an organizational assurance, not evidence; the bar is permission in hand and not a one-off export.
- If any cell says "under confirmation", it is unknown, and unknown is fail; and every rung below the first failing rung should carry no verdict at all.
- If traceable or actionable reads "the director says" or "the director thinks", a title's endorsement has replaced evidence; actionable needs a trial run of the target action.
- If validated reads "the demo ran on last month's export with no errors", a demo proves only accessible; validated has no shortcut but the three-way reconciliation.
- If the scorecard carries no date, the conclusion has no shelf life and no retest to speak of.
- If the exists cell reads "the data platform says it is all synced", that too is an organizational assurance; syncing solved the hauling only.
- If an AI-generated field appears in a source table, the next model will learn its own output as fact.

## Key judgments

- "A field's update discipline runs only as far as 'audit finds nothing.' AI is the first consumer that takes the fields at their word."
- "Half the fix for a data problem is engineering, half is operating discipline."
- "Fitness is a state, not a property, and it degrades."
- "A source built for people to look at does not, by default, deserve to drive machine action."

## Templates

- `templates/data-fitness-and-source-of-truth.md`: the inventory, the seven-rung scorecard, the source of truth decision log, and the counterexample's lesson.
- `docs/appendices/template-09-data-fitness.md` §9.3: the three-way reconciliation checklist with the row-by-row record; `repo/templates/data-fitness/reconcile.py` computes the total rate and the largest single class.

## Vendor seat

Data fitness applies as is, change nothing. The one thing a vendor has that you do not is the division-of-labor sheet, where the engineering half is the deliverable and the operating half is the client's housekeeping; inside, sequence replaces that boundary. A line in a contract is not a working mechanism.
