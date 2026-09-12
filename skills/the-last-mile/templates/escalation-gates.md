# Stage rules and the three escalation gates

Source: `docs/appendices/template-14-stage-gates.md` §14.1–14.2.

Standing agenda for the escalation decision meeting (30 minutes, rule). Fill the evidence into each gate before the meeting; do only the ruling in it. The kill criteria (`templates/kill-criteria.md`) are written in the same meeting.

| Header field | Fill in |
|---|---|
| System and scope | <system>, <user group>, <case type> |
| Stage claimed → stage requested | <prototype → pilot> or <pilot → production> REQUIRED |
| Meeting date, chair | <date>, <name> |
| Present | <sponsor>, <business owner>, <delivery lead>, <engineers by name> |

**Stage rules table (judge the stage by the change discipline row)**

| | Prototype | Pilot | Production |
|---|---|---|---|
| Optimizing for | Learning speed, changing fast beats not erring | Evidence quality, measurable and attributable under real conditions | Operating reliability, not erring beats changing fast |
| Data | De-identified samples / synthetic cases, read-only | Real data, controlled scope (one team, one case type) | Full real data, decision trail, closed-loop write-back |
| Users | A few volunteers, using it and cursing it to your face | A named real user group that depends on it in daily work | All target users, the most unwilling group included |
| Change discipline | Change anytime, ship the same day, redo it if wrong | Changes released in batches, announced ahead, rollback available | Changes follow the process, clear the eval regression before shipping |
| Typical way to die | Over-polished into a deluxe demo | The zombie pilot, no definition of graduation or death | Demo code shipped carrying demo discipline |

**Three-gate checklist (prototype → pilot)**

| Gate | Item | Evidence (already happened) | Clear? |
|---|---|---|---|
| 1 Eval over the line | Five-part eval spec complete, per-category threshold table signed by both sides | <spec version, signers> | |
| 1 | Most recent golden case replay, unsafe class 0 cases (rule) | <replay date, count> | |
| 1 | Every concern-class item inside its threshold | <values> | |
| 1 | Useless inside its threshold, trend not risen across three consecutive replays (rule) | <three values> | |
| 1 | Version replayed = version entering the pilot (no "we tested the previous build") | <build id> | |
| 2 Willingness to use it daily | Target group used it on its own ≥2 consecutive weeks (rule), no reminders, usage records as proof | <records> | |
| 2 | At least one behavioral signal that taking it away would hurt (someone asks when it is missing) | <event, date> | |
| 2 | Evidence from behavior records, not a satisfaction survey | <source> | |
| 2 | At least one user can say "which next action of mine it changed" | <user name, action> | |
| 3 Owner in place | The pilot's operating owner claims it by name, present in person (not assigned in absentia) | <owner name> REQUIRED | |
| 3 | Into the minutes: schedule protection for the users' input / ownership of the operating discipline / first signatory on "stop or not" | <three lines> | |
| 3 | The return, on the table first: priority scheduling rights, the sponsor present as witness, a line in the owner's quarterly goals | <three lines> | |
| 3 | Consistent with the charter's owner field, or the charter updated on the spot | <charter version> | |

**Ruling** (one of two): all three clear → pilot launch day <date, within a week (rule)>, kill criteria written now. Any one not cleared → missing evidence <what>, action <what>, owner <name>, reconsider on <date>.

**Rules**
- Judge the stage by the "change discipline" row, not by what the system calls itself. Change anytime = prototype, batched with rollback = pilot, regression first = production, whichever environment it runs in.
- Prototype sits between L0 and L1, pilot = L1, production = L2. The danger is not inside a cell. It is in changing column without changing the rules. Changing stage = changing the whole column of discipline, checked row by row.
- All three gates clear → set the pilot launch day (within a week is a good default), and write the kill criteria in the same meeting.
- Any one not cleared → write down which evidence is missing, the action to fill it and who owns it, and set a date to reconsider.
- No "basically passed, start it first," and no using "more polish / more watching" in place of a ruling. Ask first, which gate is the polishing for?

**Reusing it for pilot → production** (same structure, different evidence sources): gate one becomes per-category targets met on live data across the whole pilot, kill criteria zero triggers or triggered and closed out; gate two becomes willingness to roll out beyond the controlled group with balancing metrics not worsening; gate three becomes the production operating owner plus confirmed budget ownership, the budget line landing in the business side's annual budget.

**What a wrong filling looks like**
- "Eval basically over the line, unsafe 1 case, an edge case, the team judged it acceptable." Unsafe is 0 with no edge-case discount; "the team judged" steals the ruling from the threshold table.
- "The replay used the build from two weeks back." The excluded "we tested the previous build."
- "Satisfaction survey 4.6/5." The evidence gate two names and excludes.
- "The owner's team will arrange a dedicated person later." No name, so "stop or not" has no first signatory.
- "Basically meets the bar, start first, fill the open items while running." The exact forbidden phrase.

Filled in → goes to: `templates/kill-criteria.md`, written in the last fifteen minutes of the same meeting and signed the same day; the launch resolution carries the reassessment date and the resource renewal point.
