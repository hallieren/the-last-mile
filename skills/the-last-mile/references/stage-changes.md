# Changing stage: prototype, pilot, production

**Load this reference when:** a pilot is past its date, "roll out next month" or "two more weeks of polish" is on the table, the budget has just been approved and someone wants to start the pilot in the same breath, or a prototype is being called production (L0 → L1 → L2).

Source: chapter 14 (`docs/chapters/ch14-prototype-pilot-production.md`); template 14 (`docs/appendices/template-14-stage-gates.md`); `repo/templates/stage-gates/kill-criteria-weekly-report.md`; template 4 element 7 (`docs/appendices/template-04-deployment-charter.md`); chapter 16 budget-handoff paragraphs (`docs/chapters/ch16-production-engineering.md`).

## Contents

Decisions (the stage rules table, budget vs readiness, the three gates, ruling rules, owner as a trade, kill criteria discipline, kill criteria vs resource reassessment, graduation criteria, the three resource gates, calendar vs gates, where to hang the gates, budget ownership) · Procedures (the escalation meeting; writing kill criteria; a trigger fires; a pilot past its duration; mining the last zombie) · Detectors · Key judgments · Templates · Vendor seat

## Decisions

**Judge the stage by the change discipline row, not by what the system calls itself.** Change anytime = prototype, batched with rollback = pilot, regression before shipping = production, whichever environment it runs in. Prototype sits between L0 and L1, pilot = L1, production = L2. The ladder says which rung; the rules table says which discipline that rung requires.

| | Prototype | Pilot | Production |
|---|---|---|---|
| Optimizing for | Learning speed, changing fast beats not erring | Evidence quality, measurable and attributable under real conditions | Operating reliability, not erring beats changing fast |
| Data | De-identified samples or synthetic cases, read-only | Real data, controlled scope (one team, one case type) | Full real data, decision trail, closed-loop write-back |
| Users | A few volunteers, using it and cursing it to your face | A named real user group that depends on it in daily work | All target users, the most unwilling group included |
| Change discipline | Change anytime, ship the same day, redo it if wrong | Changes released in batches, announced ahead, rollback available | Changes follow the process, clear the eval regression before shipping |
| Typical way to die | Over-polished into a deluxe demo | The zombie pilot, no definition of graduation or death | Demo code shipped carrying demo discipline |

The three sets of rules are mutually exclusive; there is no good habit that works across all three. The danger is not inside a cell. It is in changing column without changing the rules. Changing stage = changing the whole column of discipline, checked row by row.

**Keep the budget meeting and the readiness meeting apart.** "Budget approved is not the same as ready. The first reads the books, the second reads the evidence." The budget meeting decides whether to do it; the readiness meeting decides when to change the rules. Settling "let us start the pilot then" at the budget meeting is using the books in place of evidence.

**Rule prototype → pilot on three gates in 30 minutes (rule). Each tests one thing, and each names the evidence it excludes.**

| Gate | Checklist | Evidence that does not count |
|---|---|---|
| 1. Eval over the line (tests the system) | The five-part eval spec is complete and the per-category threshold table signed by both sides; most recent golden case replay, unsafe 0 cases (rule); every concern item inside its threshold; useless inside its threshold with the trend not risen across three consecutive replays (rule); the version replayed = the version that enters the pilot | "It feels a lot more accurate overall"; "we tested the previous build"; an "edge case" discount on an unsafe |
| 2. Willingness to use it daily (tests workflow embedding) | The target group used it on its own for ≥2 consecutive weeks (rule) with no reminders, usage records as proof; at least one behavioral signal that taking it away would hurt (someone at your desk asking why today's queue has not come); at least one user can say "which next action of mine it changed" | A high score on a satisfaction survey; "the feedback is good" |
| 3. Owner in place (tests responsibility) | The next stage's operating owner claims it by name, present in person; three items into the minutes, schedule protection for the users' input, ownership of the operating discipline (status cleared before leaving each day, the doubt list reviewed weekly), first signatory on every "stop or not"; consistent with the charter's owner field or the charter updated on the spot | "We will assign someone when the time comes"; assigned in absentia |

**Ruling rules.** All three clear → set the pilot launch day, inside a week (rule) is the default, and write the kill criteria in the same meeting. Any one not cleared → write which evidence is missing, the action to fill it, who owns it, a date to reconsider. No "basically passed, start it first," no "more polish / more watching" in place of a ruling. Ask first, "Which gate is the polishing for?" and "What new evidence, for which gate, would another month produce?" All three clear and polishing is delay.

**Claim the owner role as a trade, and put the return on the table first.** Claiming pilot owner internally means claiming a responsibility that does not enter his KPIs. Three returns, given on the spot: priority scheduling rights (the schedule protection is that right), the sponsor present as witness, a line in his goals for the quarter. Without the return the claim is a verbal favor, and a verbal favor is not a first signatory.

**Write the kill criteria in the excited period, and only then.** In the same meeting as the escalation resolution, signed the same day; a stop standard written only after entering the pilot is void. Written later, everyone knows which line kills the project and the discussion becomes a negotiation of positions, the loose line against the strict line, the final "standard" a mark of power. Written now, nobody knows which side the data will land on, a veil of ignorance you set for your future self. After entering the pilot, adding rows is allowed, loosening existing ones is not. A trigger executes the action in its row, with no meeting reopening the standard; the data does the stopping, people only sign the restart. A trigger is not a failure, it is the defense holding, and the first sentence of the outward notice says so.

**A complete sheet covers at least four signals, one row each, every row a hard number.**

| Signal | Trigger (worked shape) | Action | Recovery |
|---|---|---|---|
| unsafe | ≥2 unsafe-class errors in a single week (illustrative, at the advise layer); rewritten to one occurrence the day the step moves up to the act layer, because by then the error has already landed | Pilot pauses for rework, that whole class of suggestion degraded to human review, root cause retrospective | Golden case replay passes after the fix, the owner signs the restart |
| North Star | Weekly median above the 8-week pre-pilot baseline (rule) two consecutive weeks (rule) | Pause the expansion, check the data source before the system | Two weeks back below the baseline |
| Cost | System cost per case above half the value of the labor hours that case saves (illustrative) two consecutive weeks (rule); read from the cost ledger, not the month-end bill | Pause the expansion, cost review | Back under the value line and held two weeks |
| Acceptance | The target group's weekly usage rate below the agreed line two consecutive weeks (rule) | Pause the expansion, go back to users to locate the reason | Reason closed out, usage recovered for a week |
| Business-side input (required) | Committed data access or people unmet two consecutive weeks (rule) | Triggers the charter's resource reassessment at the matching tier | Input resumes |

**Keep kill criteria and resource reassessment on two pages, one job each.** Kill criteria are a pilot-level operating trigger, "should we pause this week." The charter's resource reassessment conditions are project-level, "should the resources go back to the company," raised by any of three parties with a written trigger each and running in three tiers (the full tiers are in `references/charter.md`). Shutdown power runs one way, only the sponsor or the project approval committee can shut a project down. A kill trigger is an order of magnitude more sensitive than a reassessment, and an order of magnitude gentler: it pauses this week's expansion, it does not send the people home.

**Graduate pilot → production on five things, through the same three gates.** The charter's North Star hits target on real data across the whole pilot; the acceptance rate for suggestions holds without reminders propping it; the unsafe class was never broken end to end; kill criteria had zero triggers or triggered and were closed out; the production operating owner and budget ownership are settled. Reused gates: eval over the line becomes per-category targets met on live data across the whole pilot (kill criteria zero triggers or closed out); willingness becomes willingness to roll out beyond the controlled group with balancing metrics not worsening; owner becomes the production operating owner plus confirmed budget ownership, the budget line landing in the business side's annual budget. Past that door the system moves from L1 to L2, and the acceptance-rate line already measures what L3 measures.

**Translate the gates into resources with three resource gates, all firing without you.**
1. Named commitments claimed in writing before the pilot. People, hours per week, schedule protection, claimed by the counterpart's supervisor with the sponsor present, written into the pilot launch resolution. Where showback or chargeback exists, compute and labor are booked to the using department. This manufactures a person watching the progress; the first mover behind a zombie pilot is that nobody bears the cost.
2. Renewed funding tied to the gates, not to the calendar. The next round of people and compute is approved on "the three gates cleared and the escalation resolution signed" (the pilot's resources) and "the graduation criteria met" (the round that comes with formal project approval), with no dates. "Add headcount in the second half" in the annual plan is a down payment on escalating by the calendar; rewrite it as a conditional.
3. A fixed reassessment date that settles automatically when it comes due. Set it on the pilot launch day, write it into the launch resolution; when it comes due with no escalation resolution, settle on how much of the graduation criteria was met and convert to formal project approval or shut down. "Another month of watching" goes through project approval again, reason on the form. Not deciding is no longer free.

**Write every outward commitment as a conditional.** "Live within N weeks of clearing the three gates," never "live in Q3." The organization's scheduling system eats dates and not conditions; a delay needs a written explanation, staying on schedule needs only silence, and error rates do not read the calendar. Changing the date costs one report. Changing the gate costs one incident.

**Hang the gates on a review the company already holds.** Write the three gates, the graduation criteria and the kill criteria on one page, hand it to the PMO or the budget owner, and let them become a standing agenda item of the stage-gate review, the PMO quarterly stocktake, the project approval committee or the annual budget and headcount review. How the criteria get into their form is their business; what the criteria are has to come from you, they cannot write them. No such review → the sponsor's standing meeting, with the reassessment date in the minutes so it comes onto the agenda on its own.

**Settle budget ownership before the production gate, and split usage first.** The business side is a real owner only once it takes the budget; whoever holds the budget holds the priorities. If he does not take it, the money stays on your project funds, your cost center feeds it forever, and the team that feeds it ends up being its ops team; that is the financial source of permanent ops. He will not accept a total mixed into a shared gateway account he cannot read, so tag the system's calls (FinOps or a showback report) before you ask; split usage by system first, then talk about moving it. Owning the line puts a number on his cost sheet that gets asked about at the quarterly business review; the four-ledger page becomes that budget account at handoff.

**Your manager objects, "you put 'it can be stopped' in the minutes, do you still want next year's allowance for this line?"** → "Daring to write the stop standard is what buys a budget someone dares to approve." The sponsor approved the pilot because the conditions for stopping were on the table, and renewed funding rests on the run chart, not on a way out left in the minutes.

## Procedures

**Run the escalation decision meeting (30 minutes, rule).**
1. Fill the evidence into every gate before the meeting. Do only the ruling in it.
2. Put the three-gate table on the screen and go gate by gate, reading each gate's excluded evidence out loud.
3. Gate three: the owner claims by name, in person; the three items and the three returns go into the minutes.
4. "Two more weeks of polish" or "another month of trying it" → "Which gate is the polishing for?" Edge cases inside the concern threshold serve no gate.
5. All three clear → launch day inside a week (rule). Any one not → the missing evidence, the action, the owner, the reconsider date.
6. The last fifteen minutes (rule): write the kill criteria, at least four rows, sign the same day, the owner as first signatory, filed with the sponsor.
7. Write the reassessment date and the resource renewal point (the gates and graduation criteria, no dates) into the same launch resolution.

**A kill criteria row fires.**
1. Execute the action in the row that week. No meeting on the standard; the time to argue it has passed.
2. First sentence of the outward notice, the mechanism held. Then the root cause investigation.
3. The triggered case goes into the golden cases permanently as a historical incident case.
4. Recovery condition met → the owner signs the restart. Nobody signs a stop.
5. Record the recheck every week whether triggered or not, on the weekly report; archive the sheet at pilot end. The post-launch incident retrospective checks it row by row again.

**A pilot is past its planned duration.**
1. Today, write its graduation criteria and its kill criteria, one sentence each. Cannot → it is a zombie; kill it or take it back through project approval.
2. Check the calendar for the reassessment date. Due with no resolution → settle on the graduation criteria met, convert or shut down.
3. "Extend" → through project approval again, reason on the form.

**Before your first pilot, mine the last zombie.** Look up how the company's last zombie pilot died; its cause of death goes into the candidate rows of this project's kill criteria. Pull the 8-week pre-pilot baseline (rule) from the warehouse yourself.

**Someone calls a prototype production.** Ask "What process does changing one line of code in this system take right now?" Change anytime → it is still a prototype, wherever it runs. The definition of a prototype is data, workflow, trust, ownership and value papered over temporarily.

## Detectors

- If the cell where the claimed stage and the practiced discipline disagree can be pointed at, that cell is your biggest risk right now.
- If "we have been trialing it two weeks" is the evidence, the calendar turned a page; if "the feedback is good," that is politeness, not data.
- If the report reads "pilot in progress, optimization continuing" with no graduation criteria and no kill criteria written, it is a zombie, and whoever says so first owns the conclusion; only a reassessment date that settles on its own spares him.
- If "live in Q3" is in the annual plan, error categories that never cleared will get "continuous optimization after launch."
- If the kill criteria discussion is happening after the data looked bad, every proposed line is a position.
- If the budget meeting and the readiness meeting were the same meeting, the books stood in for the evidence.
- Counterexample, gate one: "unsafe 1 case, an edge case, the team judged it acceptable" steals the ruling from the threshold table and hands it to people in the excited period; unsafe is 0 with no edge-case discount.
- Counterexample, gate one: "the replay used the build from two weeks back" is the excluded "we tested the previous build."
- Counterexample, gate two: "satisfaction survey 4.6/5" (illustrative) is the evidence gate two names and excludes; two weeks of unprompted use and someone asking when it is missing is what counts.
- Counterexample, gate three: "will arrange a dedicated person later" is no owner, so "stop or not" has no first signatory.
- Counterexample, ruling: "basically meets the bar, start first, fill the open items while running" and "assess flexibly as the pilot runs" are the exact forbidden phrases.

## Key judgments

- "The danger is not inside a stage. It is in changing stage without changing the rules."
- "All three gates are clear. Polishing is delay."
- "Kill criteria are written during the excited period. They cannot be written during the disappointed one."
- "The pilot is eval scaled up, not production scaled down."
- "The escalation criteria are the acceptance criteria rehearsed early."
- "Changing the date costs one report. Changing the gate costs one incident."
- "The data does the stopping. People only sign the restart."
- "Daring to write the stop standard is what buys a budget someone dares to approve."

## Templates

- Stage rules table, three-gate checklist, ruling rules, reuse for pilot → production: `templates/escalation-gates.md`.
- Kill criteria header, item table, weekly report: `templates/kill-criteria.md`; `repo/templates/stage-gates/kill-criteria-weekly-report.md`.
- The charter's exit and resource reassessment conditions: `templates/deployment-charter.md` element 7; `docs/appendices/template-04-deployment-charter.md`.
- Gate one reads `templates/eval-spec.md`; `scripts/gate_check.py` outputs the gate-one checkbox state from a replay CSV.
- Budget ownership and the four ledgers: `docs/appendices/template-16-production-readiness.md` §16.1–16.2.

## Vendor seat

The three resource gates are the vendor's three money gates: charge for the pilot even symbolically (a free pilot is a zero-cost option), tie payment milestones to the three gates and the graduation criteria and not to the calendar, write the expiry exit into the contract and settle on the graduation criteria when it comes due. The three tiers of resource reassessment are the contract's exit clauses. Money has a shape outside, so a zombie pilot dies faster; a payment milestone is still one line, and a line in a contract is not a working mechanism.
