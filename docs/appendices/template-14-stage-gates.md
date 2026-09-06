# Template 14 · Stage Gate Checklist and Pilot Kill Criteria

> Companion chapter(s): Chapter 14. The three tools are in order of use. Use 14.1 first to judge which game you are in and which rules you have to keep, rule item by item with 14.2 at the escalation decision meeting, and in the same meeting where the resolution passes, use 14.3 to write the stop standard hard.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 14.1 Stage Rules Table (Printable)

| | Prototype | Pilot | Production |
|---|---|---|---|
| **Optimizing for** | Learning speed, changing fast beats not erring | Evidence quality, measurable and attributable under real conditions | Operating reliability, not erring beats changing fast |
| **Data** | De-identified samples / synthetic claims, read-only | Real data, controlled scope (one team, one claim type) | Full real data, decision trail, closed-loop write-back |
| **Users** | A few volunteers, using it and cursing it to your face | A named real user group that depends on it in daily work | All target users, the most unwilling group included |
| **Change discipline** | Change anytime, ship the same day, redo it if wrong | Changes released in batches, announced ahead, rollback available | Changes follow the process, clear the eval regression before shipping |
| **Typical way to die** | Over-polished into a deluxe demo | The zombie pilot, no definition of graduation or death | Demo code shipped carrying demo discipline |

**Rules**:

- Judge the stage by the "change discipline" row, not by what the system calls itself. Change anytime = prototype, batched with rollback = pilot, regression first = production, whichever environment it runs in.
- Mapped onto the outcome ladder (the five-rung outcome ladder from L0 demo to L4 business-side self-sufficiency, defined in Chapter 1), prototype sits between L0 and L1, pilot = L1, production = L2.
- The danger is not inside a cell. It is in changing column without changing the rules. Changing stage = changing the whole column of discipline, checked row by row.

---

## 14.2 Three Escalation Gates Checklist (prototype → pilot)

Standing agenda for the escalation decision meeting. Go through the three gates item by item → rule → write 14.3 in the same meeting. Fill the evidence into each column before the meeting, and do only the ruling in it.

### Gate One: Eval Over the Line

- [ ] The five-part eval spec is complete (Template 11), and the per-category threshold table is signed off by both sides
- [ ] Most recent golden case replay, unsafe class **0 cases**
- [ ] Every concern-class item inside its threshold
- [ ] The useless class inside its threshold, and the trend has not risen across three consecutive replays
- [ ] The version replayed = the version that will enter the pilot (no "we tested the previous build")

### Gate Two: Willingness to Use It Daily

- [ ] The target user group used it on its own for ≥2 consecutive weeks (no reminders), with usage records as proof
- [ ] At least one behavioral signal that taking it away would hurt (someone asks when the system is missing, someone complains)
- [ ] The evidence comes from behavior records, not from a satisfaction survey
- [ ] At least one user can say "which next action of mine it changed"

### Gate Three: Owner in Place

- [ ] The pilot's operating owner (the business line's head) claims it by name and is present in person (not assigned in absentia)
- [ ] The owner's three items go into the minutes, schedule protection for the users' input / ownership of the operating discipline / first signatory on "stop or not"
- [ ] Consistent with the charter's owner field, or the charter is updated on the spot

### Ruling Rules

- All three gates **clear** → set the pilot launch day (within a week is a good default), and write 14.3 in the same meeting.
- Any one not cleared → write down which evidence is missing, the action to fill it and who owns it, and set a date to reconsider.
- **No "basically passed, start it first"**, and no using "more polish / more watching" in place of a ruling. Ask first, which gate is the polishing for?

### Reusing It for pilot → production

Same structure, three gates with different evidence sources. Eval over the line becomes per-category targets met on live data across the whole pilot (kill criteria zero triggers, or triggered and closed out). Willingness to use it daily becomes willingness to roll out beyond the controlled group with balancing metrics not worsening (metric tree, Template 18). Owner becomes the production operating owner and confirmed budget ownership (the budget line lands in the business side's annual budget, Chapter 16's four ledgers, Chapter 22's handoff).

---

## 14.3 Pilot Kill Criteria Template

**Timing rule**. Written in the same meeting as the escalation resolution, signed the same day. Kill criteria are written during the excited period. They cannot be written during the disappointed one. After entering the pilot, adding items is allowed, loosening existing ones is not.

**Header**:

| Item | Fill In |
|---|---|
| Pilot name / start, end and duration | e.g. the auto exceptions queue pilot, 8 weeks |
| Owner (first signatory) | By name |
| Signatures | The delivery side's lead + the business owner, filed with the sponsor, dated |
| Relationship to the charter's resource reassessment conditions | This sheet is a pilot-level operating trigger, and a trigger is executed by the action in its own row. Project-level shutdown is still ruled by the charter's resource reassessment conditions (Template 4, element 7), and the power to shut down runs one way, to the sponsor / the project approval committee. Neither replaces the other |
| Resource renewal point | [The approval conditions for the next round of people and compute budget, written as the three gates and the graduation criteria, no dates] |
| Reassessment date | [Set together with the pilot launch day; if it comes due with no escalation resolution, settle on the graduation criteria and convert to formal project approval or shut down] |

**Item table** (every row must carry a hard number, no "assess as the situation warrants"):

| # | Trigger (the data appears, it stops) | Data Source | Action on Trigger | Recovery Condition | Recheck Cadence |
|---|---|---|---|---|---|
| 1 (Anchor & Helm example, unsafe) | Unsafe-class errors ≥2 in a single week | Weekly retrospective record of suspected unsafe claims | Pilot pauses for rework, that whole class of suggestion is degraded to human review, root cause retrospective | Golden case replay passes after the fix, owner signs the restart | Every Friday |
| 2 (Anchor & Helm example, North Star) | Weekly median of first-touch handling time above the eight-week pre-pilot baseline, two consecutive weeks | Weekly points on the run chart (Template 18) | Pause the expansion, check the data source (fitness retest) before the system | Two consecutive weeks back below the baseline | Every Friday |
| 3 (Anchor & Helm example, cost) | System cost per claim above half the value of the labor hours that claim saves, two consecutive weeks | The cost page of the four ledgers (Template 16.2), not waiting for the month-end bill | Pause the expansion, cost review | Cost per claim back under half the value line and held two weeks | Every Friday |
| 4 (candidate, rewrite as needed) | The target user group's weekly usage rate below the agreed line, two consecutive weeks | Usage logs | Pause the expansion, go back to users to locate the reason | The reason is closed out and usage recovers for a week | Weekly |
| 5 (required, business-side input) | The business side's committed data access or people go two consecutive weeks unmet | Scheduling records | Triggers the charter's resource reassessment conditions (Template 4, element 7), handled at the matching tier | Input resumes | Weekly |

**Rules**:

- [ ] A trigger means executing the action in its row, with no meeting reopening the standard itself. The time to argue the standard has passed.
- [ ] A trigger is not a failure, it is the defense holding. The first sentence of the outward notice says the mechanism held, then the root cause investigation.
- [ ] Record every recheck (triggered / not triggered), and archive the whole sheet when the pilot ends. This sheet gets checked line by line again in the incident retrospective after launch (a fixed action of Chapter 18's AI incident runbook).
- [ ] A case that has triggered goes into the golden cases permanently (Template 11.2, third category, historical incident cases).

---

## 14.4 Counterexample: A Tidy-Looking Wrong Answer

An excerpt from the minutes of an escalation decision meeting. All three gates "cleared," and the pilot has a launch day:

```
Gate one: eval basically over the line. Unsafe class 1 case, an edge case, the team judged it acceptable;
  the replay used the build from two weeks back (this week's build did not change much).
Gate two: satisfaction survey 4.6/5, users generally said "very helpful."
Gate three: owner, Kevin Doyle's team will arrange a dedicated person later.
Ruling: basically meets the bar, start the pilot first, fill the open items while running.
Kill criteria: assess flexibly as the pilot runs.
```

Item by item:

1. The gate one unsafe threshold is 0 cases. There is no "edge case" discount, and the definition of unsafe is that not one is acceptable (Template 11.1.3). "The team judged it acceptable" steals the ruling power back from the threshold table and hands it to people in the excited period.
2. The replayed version ≠ the version that will enter the pilot, landing exactly on gate one's prohibition, "we tested the previous build."
3. The satisfaction survey is the evidence gate two names and excludes. What it wants is behavior records, two consecutive weeks of use with no reminders, someone asking when the system is missing.
4. "The team will arrange a dedicated person later" = owner not in place. Gate three requires a claim by name with the person present. There is no name in the minutes, so during the pilot "stop or not" has no first signatory.
5. "Basically passed, start it first" and "assess flexibly" are the exact phrases 14.2 and 14.3 forbid. Kill criteria must be written with hard numbers in the same meeting as the escalation resolution, and they can only be written during the excited period, because they cannot be written during the disappointed one.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/stage-gates/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/stage-gates/): the eval-over-the-line automatic check script (reads the eval replay report, compares thresholds category by category, and outputs the checkbox state for 14.2's gate one directly)
- [`templates/stage-gates/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/stage-gates/): the kill criteria weekly report template
