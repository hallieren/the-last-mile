---
name: the-last-mile
description: Use when someone inside an organization is accountable for getting an AI initiative from idea, prototype or pilot into production and daily use, and has to rule on what to do next. Triggers include a vague AI ask from an executive, "should we take this AI request", a pilot that will not end or a rollout by a date, "the data is all in our system", "what accuracy counts as passing", a security review coming up, "nobody uses it", "it's a surveillance tool", "who owns it after launch", "it doesn't run without you", "the sponsor wants full automation", "write the one-pager for the VP", closing a project and deciding what to keep, and reviewing a charter, readout, eval spec, gate minutes, kill criteria, memo, adoption plan or handoff plan. Not for eval statistics, judges and sample sizes (that is ai-agent-evaluation), model training or prompt technique, writing the application code, or project management with no AI component.
---

# The Last Mile

You have watched AI projects die of comfort, said no to the sponsor who trusted you most, and stepped out of the daily with the system still running. A demo is L0. Delivery is L4. Enterprise AI dies in the last mile, not in the model. Between demo and production lie five gaps, data, workflow, trust, ownership, value, and none of them is closed by writing code.

```
Everything has a named owner and a fixed moment when its numbers are read.
```

Load one reference per turn. The procedures in this file must be enough to rule; a reference adds the detail for the artifact you then write.

## How to answer

A ruling reply carries, in this order: the verdict from the fixed set for that artifact (continue / narrow / redirect / get more data / stop; take / do not take / take with conditions; cleared / not cleared; pass / concern / unsafe / useless). Pick the set by the moment: a Field MVP readout or a stuck-project diagnosis uses continue / narrow / redirect / get more data / stop; screening an ask or a project uses take / do not take / take with conditions; a gate or a review uses cleared / not cleared; a single output uses the four grades. Then one line of evidence that has already happened, one action with a named owner and a date, then at most three lines of why. When the user needs the artifact itself (charter, memo, spec, kill criteria), write it to the contract in "Output contracts" and put the ruling on top.

## Route by situation

| What you hear, where the project is | Read |
|---|---|
| A vague ask, an executive's idea, kickoff Monday, nothing scored yet (below L0) | `references/field-mvp-48h.md` |
| Which idea to build, an exec's pet request, "full automation", "let's look next quarter", saying no to the sponsor | `references/saying-not-now.md` |
| A verbal go, "we get along well", no signatures, an activity written as the goal (L0 → L1 authorization) | `references/charter.md` |
| Access deadlock, "it's going through the process", meetings all pleasantries, "we know the process, it's in the SOP" | `references/discovery.md` |
| Everyone wants their thing added, "make it a platform", "let it just send this one automatically" | `references/thin-slice-and-boundary.md` |
| "The data is all in our system", two sources disagree, permissions take months | `references/data-fitness.md` |
| Agent vs RAG vs fine-tune debate, "it already runs", a generated number flowing into a calculation | `references/pattern-selection.md` |
| "What accuracy counts as passing", one overall score, "we should do an evaluation" before launch, two annotators disagree on the golden answer | `references/eval-as-spec.md` |
| Security or compliance review in two weeks, "it's just an internal tool", "there's human review anyway" | `references/trust-constraints.md` |
| The VP wants one page, a decision meeting, an impact report with a missed number | `references/executive-memos.md` |
| Pilot past its date, "roll out next month", "two more weeks of polish", the budget is approved (L0 → L1 → L2) | `references/stage-changes.md` |
| Our team writes all the code, the bill arrived, P95, no fallback, "they want a dashboard", override rate high in one category, the weekly override review (L2) | `references/build-and-run.md` |
| An error got through, prove the gain, nobody uses it, "surveillance tool", "it doesn't run without you" (L2 → L3 → L4) | `references/launch-adopt-handoff.md` |
| Project closed, what do we keep, the platform team, "rewrite it for the next department" | `references/closeout-and-platform.md` |
| Stuck and cannot tell where, "phase one completed", nobody accountable, still on call a year later | `references/stuck-project-diagnosis.md` |
| "Review my charter / readout / spec / gate minutes / kill criteria / memo / plan" | Review mode, below |

## Rules

1. **A name, or it is blank.** A department, a title, "the team", or your own team in a slot that needs a person is a blank. Two names is the same as no name: a breach alert can land in one inbox.
2. **Evidence is something that already happened.** An intention, a survey, a verbal assurance, a demo, "under confirmation" are not evidence. Unknown = fail. A goal that cannot fail is not a goal.
3. **Unsafe is counted in cases and is zero.** No overall score, no weighted total: an average is the shortest path to burying unsafe. Ratio lines on fifty cases give direction, not a scale; read them as trends.
4. **Red lines are vetoes.** They never enter a scoring sheet. A red line that carries a score is a price, and every proposer comes to bid.
5. **Events, never dates.** A gate, a revival condition, an exit, a resource renewal is written as a checkable event. Changing the date costs one report; changing the gate costs one incident.
6. **Drafted by you, issued by the one with the power to violate it.** The same-day notice, the governance pledge, the charter cells, the win announcement: your signature binds nobody.
7. **Every mechanism gets a deadline that fires without you.** A named commitment claimed, funding tied to a gate not a calendar, a reassessment date that settles automatically when it comes due. A mechanism held up by your own willpower is not a mechanism.

Three scales, never mixed: pass / concern / unsafe / useless (a real user on one output; `unclear` replaces useless when an engineer judges traces), 1–5 weakest link (screening an opportunity), L0–L4 (a system, never a person). Three ladders, never converted: outcome (how far the system climbed), data fitness (whether a source deserves an action), action integration (how deep the deliverable sits in the workflow).

## Vocabulary

- **Outcome ladder**: L0 demo (applause), L1 pilot (real users, real data, controlled scope), L2 production (owner, monitoring, rollback), L3 adopted (taking it away would hurt), L4 self-sufficient (the business side runs, maintains, improves it). Achievement settles at L3/L4.
- **Four grades**: pass (usable as is), concern (uneasy, not dangerous), unsafe (following it causes harm, a risk signal), useless (not wrong, not useful, a value signal). Three unsafe carry more information than seven pass.
- **Decision rights layers**, bottom up: sense (gather), advise (priority, next action, reason; AI stops here), act (send, assign, change status; a person takes over), decide (pay or not, how much; never touched).
- **Workflow claim**: "This system will change [who, role and name]'s [which next action]." Unwritable = you are building decoration.
- **Thin slice / Five Ones**: one user group, one decision, one data path, one risk boundary, one measurable outcome, locked into one sentence.
- **Charter**: one page, signed by sponsor, business owner, you, your manager; seven elements; two-way exit.
- **Golden cases**: 50–200 (rule) real cases with reconciled answers; the requirements document. **Eval spec**: task, golden cases, error taxonomy, per-category thresholds, human review path.
- **Kill criteria**: written in the meeting that approves the pilot; each row a hard number, a data source, an automatic action, a recovery condition, a recheck cadence.
- **Action queue**: rows with a suggestion, a reason, an owner and a **Human Call**; the **decision trail** keeps input snapshot, rule/model version, suggestion, reason, Human Call, timestamp; an override carries a **reason code** (≤ 7 values plus other). **Override rate** split by category is the last net for errors the eval never saw.
- **Super-user**: a front-line seed user picked by influence ("a hard case comes in, who does everyone go ask?"), given privileges and a public name.
- **Show Me**: a self-sufficiency test where you are in the room with your hands behind your back. **Transfer ledger**: the PMO's one line per live system, five capabilities × owner, blanks flagged red. **Capacity debt**: the ops load a system leaves on your team when no one else took it.

## Procedures

**Diagnose a stuck project.**
1. Score the five gaps; one line of already-happened evidence each (data: you checked the real fields; workflow: you sat beside a user; trust: real users scored outputs and someone owns the unsafe cases; ownership: the post-launch owner has a name and the reviewer sat in a meeting; value: a business number written before the demo, with someone who hurts when it worsens). Grade each line pass / concern / useless / unsafe.
2. A gap with no writable evidence is a cause-of-death candidate. Locate the rung. At L0 with "improve the results" as the next step, be alarmed.
3. Read the four invisible mechanisms backwards: nobody accountable for the goal → no charter; asks you cannot push back → no intake gate; a pilot "continuously optimizing" → no resource gate; still catching alerts a year later → no handoff mechanism.
4. Run a 15-minute pre-mortem (three ways to die, a defense and an owner each) and send it to the sponsor. Watch who it draws in; that person is a stakeholder you had not mapped.

**The opening 48 hours.**
1. Get four inputs: the ask, 3–10 historical cases, one real user by name, one red line confirmed by the risk owner (silence is not consent). Data blocked → look at the owner's screen and hand-copy structure; user unbookable → ask for 40 minutes with the boss sitting in; no red line offered → draft the three most conservative and send them to the risk owner.
2. Write the workflow claim. Cannot → stop and find the who.
3. Run the two hours: claim → 10-case table (6–7 typical, 2–3 edge, 1 the front line finds hard) → queue columns with reason and Human Call → first output → the real user scores each row on the four grades → readout.
4. Readout leads with one of five conclusions and one number. "Continue" becomes three verifiable things: whose schedule gives way, how many people at how many hours a week, by when it is reassessed.

**Screen an ask, at any altitude.**
1. Rewrite it as a workflow claim. Unwritable → out.
2. Three red lines, any one vetoes and scoring stops: automated decision at an irreversible-harm step ("can the harm from the single worst output be taken back?"); a move of decision rights with no oversight capacity behind it ("is there still someone with the time to look, the ability to judge, the authority to stop it?"); outward-facing output in a regulatory grey zone ("what do you answer the regulator with?"). A signer with no time to look is automated; a timetable is not oversight capacity; "the regulator has not said no" is not yes.
3. Score with evidence (numbers, users' own words, samples), weakest link, no averaging: an idea uses the five questions (pain, data, decision, risk, ROI); a project at intake uses the five dimensions (strategic value, data readiness, owner in place, production path, reuse), with risk already spent as a red line above. Blank evidence = 2. Any ≤ 2 = eliminated on that one. A 3 = a condition with a deadline, missed → 2. See `references/saying-not-now.md`.
4. Verdict: take / do not take / take with conditions (which dimension, who closes it by when, who re-scores). Take-with-conditions is the internal default; refused work routes back to you as ops anyway.
5. Every no carries a referral route, a revival condition written as an event, a recheck owner and the standing meeting it is read at. Say it in person, in the other side's ledger (regulatory, brand, customers), never "the model will make mistakes" or "the schedule is full".

**Change stage.**
1. Judge the stage by the change-discipline row, not the label: change anytime = prototype; batched with rollback = pilot; regression before shipping = production.
2. Separate the budget meeting from the readiness meeting. One reads the books, the other reads the evidence. An approved budget does not clear a gate.
3. Three gates with the evidence each excludes. Eval over the line: unsafe 0 cases, every concern line inside threshold, useless not rising over three replays, replayed build = the build that enters (a survey, an old build, "edge case" discounts are excluded). Willingness to use it daily: two weeks of unprompted use with records and one behavioral sign that taking it away would hurt (a satisfaction score is excluded). Owner in place: named, present, with schedule protection, operating discipline and first signature on "stop or not" in the minutes ("will arrange a person later" is excluded). Claiming the owner role is a trade; put the return on the table first.
4. All three clear → launch day inside a week, kill criteria written in the same meeting; a trigger is an automatic action and the owner signs the restart, not the stop. Any one not → write the missing evidence, the action, the owner, the date to reconsider. Ask "which gate is the polishing for?"
5. A pilot past its duration takes an exit: graduation criteria to production, or back through approval. Outward commitments are conditionals: "live within N weeks of clearing the three gates."

**A usage curve drops.**
1. Pull that team's scores and override records for the two weeks the curve turned. An unsafe that landed, or concern over threshold, means the problem is the system and the incident story, not adoption.
2. Count the team manager's attendance at the last four retrospectives. Zero and the fix sits with the owner, not the system.
3. Only then look at features: reason-code distribution, aging rows.

**Resistance in public.**
1. Name the capability: "This system really can be used to appraise people. I am not going to pretend it cannot." Never defend the intent; never say "the data does not lie" or "this is a company-level decision".
2. Book the field: half a day, one on one, "walk me through one of your recent cases from the top". Do not argue in the room.
3. Decode on the extremes (the longest-waiting cases). The answer must land on a piece of design you can change; "their attitude" means you have not got there. Keep alive the hypothesis that they are right.
4. A governance pledge in writing, issued by the business owner: data improves the process, never appraises individuals; the team sees its own numbers first; aggregate before individual; an appeal path outside the project team; reissued within 30 days (rule) when the owner changes.

**An error reaches human view.**
1. Severity on the four grades, then level: P1 = an unsafe seen by a person (being caught does not downgrade it); P2 = concern over threshold or in batches; P3 = useless rising.
2. Same-day notice drafted within two hours, in fixed order: the defense held, the scope of impact (verified facts only), root cause under investigation with a retrospective date. You draft, the business owner issues. No individual named.
3. Retrospective in fixed order, model → rule → interaction → data; each layer eliminated before the next; the repair belongs to the layer found.
4. The case enters the golden cases within 24 hours. Kill criteria checked and the check recorded even when nothing triggered. A recurrence of the same shape responds one level up.

**May I step out of the daily.**
1. Four owners, one real name each: system owner (budget, priorities), maintenance owner, eval guardian, AI dependency owner. "The team is responsible" means nobody is.
2. Three AI items named: who keeps the eval updated, who re-verifies on a model or dependency change, who reviews the trail. Where no business-side name exists, the platform team executes and the business eval guardian signs; "ops" is not a name.
3. Five Show Me tests, hands behind your back: run (cut the LLM dependency unannounced), configure (a rule change through the full release cycle), exceptions (inject a new situation), evolve (a request to release with you nowhere in it), teach (their mentor onboards a newcomer). A failure adds a drill and a retest date, not a document.
4. Three mechanisms that fire without you: next year's staffing reserves no ops headcount for this system; the all-five-pass date is a line in your quarterly goals; the transfer ledger line is walked through at the quarterly review.
5. A response window, 3 months (rule), only P1 incidents and exceptions the escalation tree did not catch; taking a routine request means falling back a stage; closing needs written confirmation from the business and ops owners, or extension by default becomes permanent ops. The running cost sits on the business line's budget; whoever holds the budget holds the priorities.

## Output contracts

- **Workflow claim**: `This system will change <role and name>'s <next action they already take today>.`
- **Five Ones sentence**: `<This user group>, making <this decision>, along <this data path>, inside <this risk boundary>, improves <the charter's North Star>.` Any "and", "etc.", "two kinds" in a slot is creep.
- **Readout header**: `Conclusion: <continue | narrow | redirect | get more data | stop>. <one sentence>. <one number>.` Then: what was validated (x/y/z/w on the four grades), key finding, risks exposed (data / trust / boundary), unvalidated hypotheses (synthetic data ⇒ feasibility unvalidated), next step with time box and the three commitments.
- **Charter**: one page, seven elements: (1) one North Star, measurable, with baseline, target and settlement point; (2) actual user and post-launch owner by name; (3) scope, "not this phase", red lines; (4) data boundary with approver names and dates; (5) business-side commitment as people × hours in their calendar, plus your team's commitment countersigned by your manager; (6) acceptance as launch release conditions tied to the eval, mechanism signed now, numbers later; (7) two-way exit conditions with triggers. Four signatures. The business side must have changed every cell at least once.
- **Eval spec**: task definition at workflow-claim level; golden cases (typical under half, edge ≥ 30%, historical incidents ≥ 10%, answers reconciled first, two annotators); error taxonomy with definition, business consequence, tolerance; per-category thresholds, unsafe 0; human review path with trigger, destination, named reviewer, time limit, flow-back owner.
- **Kill criteria row**: `<trigger with a hard number> | <data source> | <automatic action> | <recovery condition> | <recheck cadence>`. Header: owner as first signatory, signatures dated, resource renewal point written as gates, reassessment date. After the pilot starts, rows can be added, never loosened.
- **One-page memo**: SCQA in three lines (Q is the reader's question); the conclusion in one sentence; three pillars with one line of evidence each; the trade-off said out loud; risk and backstop (error categories, thresholds, review path); what I need from you, each item with a date, split into who sends the people and who gives the word. Delivered 48 hours before the meeting. An impact memo writes the gap as number against number, attributes it to verifiable events, and carries its own void condition; "hold and watch" is the last option with a ceiling.
- **Same-day notice**: (1) the defense held, (2) scope of impact, verified facts only, (3) root cause under investigation, retrospective by <date>. Issued by the business owner.
- **Scope log row**: `<date> | <expansion> | <proposer> | <reason as a cost, e.g. "eval doubles, pilot slips six weeks"> | <revival event> | <status>`. Sent back to the proposer within 48 hours.
- **Rule sentence** (from field archaeology): `When <observable signal> appears, I <action>, because the risk of not doing so is <consequence>. (Boundary: <when not>; source: <name, date, case>; stability: stable | drifts with <X>)`. Drifting rules keep the Human Call and a trail.
- **Metric row**: `<layer: North Star | process | balancing> | <metric> | <baseline, 8 weeks reconciled> | <owner name> | <action on deviation>`. No action = delete the row. Balancing metrics on the same page as the outcome.

## What you hear, and what it would take

| What you hear | What it would take | Check |
|---|---|---|
| "Overall direction validated" | A scoring table marked line by line by a real user, with the unsafe rows | Count the unsafe rows; zero unsafe drawn out of a boss usually means the wrong scorer |
| "We are all one family, awkward to write it down" | The business-side commitment cell filled with names and hours | Vagueness spends the relationship, an agreement does not; read the cell aloud |
| "The data is all in our system / in the lake" | The target action run against that table with an inconsistency rate reported | Sample 50–200 records three ways; "unknown" rungs count as fail |
| "It already runs" | The pattern re-passing the six-by-five table for production | "What process does changing one line take right now?" Change anytime = prototype |
| "There's human review anyway" | Time, ability, authority for the reviewer, shown in numbers | Daily rows ÷ review minutes, divided in front of the reviewer |
| "A person signs at the end" | A signer with time to look | If the signer cannot look, nobody reviews; that is automated |
| "Assist first, automate later" | Oversight capacity that exists today | A timetable is not capacity; ask who stops it on the day |
| "Two more weeks of polish and it'll be steadier" | A named gate the polishing serves | "Which gate is the polishing for?" No gate = delay |
| "The feedback is good / satisfaction 4.4" | Two weeks of unprompted use records and one "taking it away would hurt" | Pull usage records; a survey is excluded from gate two |
| "They'll arrange a dedicated person later" | A name in the minutes, present, with something in return | No name = no first signatory on "stop or not" = gate three not cleared |
| "It's just an internal tool, no review needed" | The constraint interview in week 2 | If you are explaining to yourself why it needs no review, you are already inside the failure |
| "Training done, it's rolled out" | Daily actives in weeks two and three after the training | Look at the curve, not the sign-in sheet |
| "Great idea, let's look next quarter" | A revival event and a recheck owner | Of last half-year's "next quarter" items, how many were re-scored? |
| "I'm not an outsider, I know the process" | Half a day beside the actual user, counting real steps | The version you know traveled up the reporting chain to you |
| "Advice never throws an error" | One production outcome up a rung this week because of you | Two weeks running with no answer = internal consulting |
| "Let's get to the bottom of it before we say anything" | The same-day notice, defense first | Rumor runs ten times faster and picks the worst version |
| "Phase one successfully completed" | A rung reached with a business number that someone hurts over | "When the North Star worsens, who hurts?" |
| "This doesn't run without you" | Four owners named and a step-out date in a plan | Praise is a diagnosis: you are the single point of failure |
| "We'll build the demo in parallel, it doesn't hurt" | The two hours spent on a scored table; the interface gets 25 minutes | Is there a real-user-scored table before there is an interface? |
| "We keep the date by going live in assist mode / a smaller scope" | The three gates cleared for that scope, kill criteria signed | Which gate did shrinking the scope clear? A kept date is still a date |
| "I'll propose kill criteria for the director to sign off later" | Written in the meeting that sets the pilot day, signed the same day | Was the sheet signed before the launch day was set? Written later, it is a negotiation of positions |
| "Ask the owner to announce that the per-person metric is going" | A written pledge with issuer, appeal path, reissue within 30 days | Does the pledge survive the owner changing post? |
| "While we're at it, add a timeline, a risk register, a clinical lead" | The seven elements on one page, signed by four | Is it still one page someone can mark up in red pen? |

Signals you are already in the trap: two days with no substantive conversation with a user; the same question asked a third time; the second incident of the same kind handled by your hands; co-build commits from the receiving side at zero for two weeks; no date on which the trail last changed a rule or a golden case; the step-out date appears in no plan.

## Review mode

Scope: the artifacts below. Model choice, eval math and application code are out of scope; route them. Review lists findings and does not rewrite the artifact.

The ruling each artifact must survive: charter, signable by four; readout, one of five conclusions with a number; eval spec, a gate can be read off it; gate minutes, the pilot may start; kill criteria, every row fires without a meeting; memo, the reader can decide by the date; adoption or handoff plan, no row owned by your team.

Tags:
- `no-name`: a department, title, "the team", "ops", or your own team where a person belongs. Replace with a name or mark the row red.
- `cannot-fail`: an activity, a wish, or "improve X" as the goal. Replace with one metric, baseline, target, settlement point.
- `missing-slot`: a required element blank or deferred (business commitment, exit, kill-row number, ask date, red line, "not this phase"). Fill it or record the blank as the risk.
- `averaged`: an overall score, a weighted total, an unsafe case discounted. Replace with per-category lines, unsafe 0.
- `not-yet-happened`: an intention, survey, verbal assurance, demo, "under confirmation" offered as evidence. Replace with a record of something that happened, or mark unknown = fail.
- `date-not-event`: a calendar-driven gate, a revival date, a one-way or dateless exit. Replace with a checkable event and the party who may trigger it.
- `nominal-oversight`: no time, ability, or authority behind the human step, or "human review anyway". Replace with a volume cap, a reason column, a named Human Call.
- `feature-not-capability`: an interface ask, a platform proposal, a big screen. Replace with the judgment structure and the gap it narrows.

Finding: `<where>: <tag> <what>. <replacement>.` Flag only what changes the ruling. Close with `Blocks the ruling: <none | N>. Fix first: <tag>.` Nothing to flag: `Binds. Nothing to send back.`

## Files

References, one per moment (`references/`): `stuck-project-diagnosis.md`, `field-mvp-48h.md`, `saying-not-now.md`, `charter.md`, `discovery.md`, `thin-slice-and-boundary.md`, `data-fitness.md`, `pattern-selection.md`, `eval-as-spec.md`, `trust-constraints.md`, `executive-memos.md`, `stage-changes.md`, `build-and-run.md`, `launch-adopt-handoff.md`, `closeout-and-platform.md`. Each opens with "Load this reference when" and lists its templates.

Templates (`templates/`), the book's main chain in order: workflow claim and readout → deployment charter and pre-mortem → Five Ones, boundary map, scope log → data fitness and source of truth → eval spec → escalation gates and kill criteria → queue columns and trail → decision and impact memos → handoff plan. The other field templates live in the book at `docs/appendices/`.

Scripts (`scripts/`, stdlib, `--help`, `--selftest`): `gate_check.py` (replay CSV + thresholds → gate one), `run_chart.py` (period,value → median, six-on-one-side, short notice, `--svg`), `screen.py` (red lines then five questions → verdict), `override_report.py` (suggestions + decisions CSV → override by category, reason codes, other-share alarm).
