# 14 · Prototype, Pilot, Production: Three Different Games

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-14-stage-gates.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The prototype feedback is good, and yet "let us polish for two more weeks" and "let us watch it another month" both sound right too, and you cannot tell prudence from delay. You have also seen the other extreme, a pilot four months in and still "taking a look," with nobody saying it is dead and nobody daring to say it is alive.
>
> **What You Will Be Able to Do.** Use the stage rules table to see which game you are in and which set of rules you have to keep. Use the three escalation gates to rule in 30 minutes on whether the prototype moves up. Write the kill criteria before entering the pilot, naming what data, once it appears, means stop.

---

> **Part IV Navigation.** Chapters 14 to 18 are arranged by theme, and the weeks jump back and forth.
> The escalation decision meeting (Wednesday of week 9, this chapter) → the two engineers dialed in and the co-build agreement (dialed in week 5, signed Thursday of week 9, Chapter 15) → the last afternoon before the pilot starts (Friday of week 9, Chapter 17) → the pilot starts (Monday of week 10) → one bill (week 12, Chapter 16) → an error that got caught (week 14, Chapter 18) → the pilot closes out (week 17)

## Two Proposals That Both Sound Prudent

Monday of week 9, Grant Whitmore approved three things in 7 minutes (Chapter 13). That afternoon you book the escalation decision meeting for Wednesday, and then two messages arrive.

The engineer in claims-ops IT who leads the writing of the extraction pipeline. "The prototype still has edge cases it does not handle cleanly. Two more weeks of polish and it will be steadier."

Kevin Doyle stops you in the corridor. "Linda's team is getting good use out of it. Why rush into the pilot? How about another month of trying it?"

Here is the background. The queue prototype that grew out of the Field MVP was used informally by Linda's team for about two weeks across weeks 7 and 8, in parallel with the eval co-build, running on the existing read-only view, with data you refreshed by hand every day. The feedback really is good. And both proposals are well meant. Both sound prudent.

But you have watched too many projects die inside that prudence. Always two weeks short, always one more month of watching. Ten months later the prototype is still "in trial," the engineer is still polishing, nobody calls a stop and nobody calls it up a level, because nobody ever defined what the conditions for moving up actually are.

First, clear up one thing you will say out loud on Wednesday. What Grant approved on Monday was the project approval and the budget, whether it is worth investing in, how wide a scope, how many resources. What Wednesday's meeting rules on is a different question, whether the system and the organization are ready now. Budget approved is not the same as ready. The first reads the books, the second reads the evidence. Inside a company the easiest mistake is to run the two as one meeting and settle "let us start the pilot then" at the budget meeting, which is using the books in place of evidence. So the budget meeting stays the budget meeting and the readiness meeting stays the readiness meeting. The two neither repeat nor conflict. One decides whether to do it, the other decides when to change the rules.

## Why This Is Hard: Three Stages Are Three Games with Mutually Exclusive Rules

- **The prototype's game is learning speed.** The goal is to work out "what should be built" on the least investment. Changing fast beats not erring, ten rows of data beat ten thousand, and whether the interface is ugly does not matter.
- **The pilot's game is evidence quality.** The goal is to measure "does it work" under real conditions. Versions freeze into batches, or the data cannot be attributed. Scope stays controlled, or an error has no defense behind it. Users have to depend on it daily, or what you measure is still goodwill.
- **Production's game is operating reliability.** Not erring beats changing fast. Every change is a risk, and the rollback path outranks a new feature.

The three sets of rules are mutually exclusive, which means there is no "good habit that works across all three stages." The prototype's "change anytime" becomes contaminated evidence in the pilot. The pilot's "controlled scope" picks the easy users to serve, and in production that is dodging the hardest ones. The danger is not inside any one stage. It is in changing stage without changing the rules.

Timing the change of stage has a second trap, using time and gut feel in place of evidence. "We have been trialing it two weeks" only says the calendar turned a page. "The feedback is good" is politeness, not data. Underneath sit incentives. The engineer fears real data exposing weak spots, the owner (the person accountable for operating it in the next stage) fears carrying operating responsibility, the user fears having a way of working locked in. Everyone's "let us wait a bit" has a locally reasonable justification, and added up they make "watch it a while longer" permanent. So the escalation criteria have to be written down in plain words, outside gut feel and ahead of interests.

## Prior Art, and What AI Changed

**The stage-gate tradition (Robert Cooper).** From the 1980s on, new product development was cut into stages with "gates" between them. A gate has written criteria and a gatekeeper with the authority to close it. The core insight is that a project carries its own momentum, investment argues for itself, and with no written gate any project slides into the next stage on its own.

**The lean tradition (Eric Ries).** The discipline of pivot or persevere, keep-or-kill decisions made on a fixed cadence and on evidence, not on mood. "Let us watch a while longer" does not count as a decision. It is the absence of one.

The AI era changed two things. First, eval makes escalation criteria fully objective for the first time. In the stage-gate tradition most gate criteria are still judgment calls at a review meeting, market attractiveness, technical feasibility, scored by people in the end. An AI system has golden cases and per-category thresholds (Chapter 11). Over the line is over the line, and for the first time a gate can exist apart from the mood in the review room.

Second, an AI system's pilot carries a layer of duty traditional software never had. Model behavior only reveals its real error rate under the real data distribution. A traditional pilot mainly validates "will users use it." An AI pilot also has to validate "is the system still right across the full distribution." Fifty golden cases are a carefully proportioned sample. Eight weeks of real claim flow are the distribution itself. So the pilot is eval scaled up, not production scaled down. Clearing the eval line is only the ticket in. Every override during the pilot (a person changing the AI's suggestion) and every human correction is an error sample the golden cases could not catch (Chapter 18 hardens all of this into live monitoring).

## The Framework: One Table, Three Gates, One Trigger

**The stage rules table** (the full printable version is [Template 14.1](../appendices/template-14-stage-gates.md)).

| | Prototype | Pilot | Production |
|---|---|---|---|
| **Optimizing for** | Learning speed | Evidence quality | Operating reliability |
| **Data** | De-identified samples, read-only | Real data, controlled scope | Full real volume, trail closed loop |
| **Users** | A few volunteers, using it and cursing it to your face | A named user group, daily reliance | All target users, the most unwilling included |
| **Change discipline** | Change anytime, ship the same day | Batched releases, announced ahead, rollback available | Follow the process, clear the eval regression first |
| **Typical way to die** | Over-polished into a deluxe demo | The zombie pilot | Demo code shipped with demo discipline |

Mapped onto the outcome ladder (Chapter 1), the prototype sits between L0 and L1, the pilot is L1, and production is L2. That ladder's five rungs are L0 demo, L1 pilot, L2 production, L3 adopted, L4 self-sufficient. The ladder tells you which rung you are on. The rules table tells you which discipline that rung requires. Judge the stage by the "change discipline" row, not by what the system calls itself. A system that can be changed anytime is still a prototype, wherever it runs.

**The three escalation gates** (prototype → pilot).

| Gate | Criterion | Evidence That Does Not Count |
|---|---|---|
| 1. Eval over the line | Golden cases clear the threshold in every category (the Chapter 11 table as is) | "It feels a lot more accurate overall" |
| 2. Willingness to use it daily | Two consecutive weeks of unprompted daily use, a behavioral signal that taking it away would hurt | A high score on a satisfaction survey |
| 3. Owner in place | The person accountable for operating it in the next stage claims it by name, on the spot | "We will assign someone when the time comes" |

The three each test one thing. Eval tests the system, willingness tests workflow embedding, owner tests responsibility. All three are required, and there is no "basically passed."

**Pilot kill criteria**, the stop standard written hard before entering the pilot. What data, once it appears, means stop, with no "assess as the situation warrants." It has to be written in the same meeting as the escalation resolution and signed the same day. Kill criteria are written during the excited period. They cannot be written during the disappointed one (failure mode 4 does that math).

The three gates are the door into the pilot. There is another door out of it, the graduation criteria this chapter uses over and over from here, pilot → production. It looks at five things. The charter's North Star hits target on real data across the whole pilot, the acceptance rate for suggestions holds up without reminders propping it, the unsafe zero-tolerance class was never broken end to end, kill criteria had zero triggers or triggered and were closed out, plus the production operating owner and budget ownership are settled (the end of [Template 14.2](../appendices/template-14-stage-gates.md) writes these into a checklist). Past that door the system moves from L1 into L2, and the acceptance rate line already measures the same thing as L3 adopted (users' daily actions really have changed), while gate two's "taking it away would hurt" is that thing's first reading on the pilot's scale.

## At Anchor & Helm: Wednesday of Week 9, the Escalation Decision Meeting

In the room sit you, Kevin Doyle, Linda Marsh and four engineers, two from the Digital Center and two from claims-ops IT. You put the three-gate table on the screen and go through it one by one.

**Gate one, eval over the line.** The prototype's most recent replay on the 50 golden cases. Missed risk 0, line-crossing suggestion 0, unsafe zero tolerance, over the line. Material error and wrong action both sit inside the 10% threshold, over the line. Empty suggestion is inside 20% and the trend has not risen across three consecutive replays, over the line. All three of unsafe, concern and useless clear, with no exceptions. What you used is the threshold table handed to Kevin on Friday of week 8. No new number system. The escalation criteria are the acceptance criteria rehearsed early.

**Gate two, willingness to use it daily.** You sent no survey, because everyone scores a survey high. What you produce is behavior. Linda's team opened the queue on their own every morning for two straight weeks, with no reminders. The harder evidence came from Monday morning of week 9. You were busy preparing Grant's 10-minute meeting, the view refreshed forty minutes late, and by 8:40 a member of her team was at your desk asking why today's queue had not come yet. Linda added a line at the meeting. "Kevin, honestly, the team is not used to a Monday morning without this queue any more." That is the first thread of Chapter 1's L3 adopted, taking it away would hurt.

**Gate three, owner in place.** A pilot is "the business side's operation running inside a controlled scope." "The Digital Center's system being tried out over at the business side" does not reach that bar, so the person accountable for operating it in the next stage has to claim it by name. Kevin claims pilot owner on the spot. What he claims goes into the minutes, three things. Two hours a week of schedule protection for Linda's team. The status write-back discipline, the review team clearing status in the last ten minutes before leaving each day, and he reviews the "status in doubt" list the queue produces every week. On every "stop or not" ruling during the pilot, he is the first signatory. The item the memo asked Grant to confirm by Friday (two hours a week of schedule protection for Linda's team), he claimed himself on Wednesday.

Claiming pilot owner internally means claiming a responsibility that does not enter his KPIs, so claiming it needs something in return, given on the spot. Three things. These three go into his goals for the quarter, the sponsor is present as witness, and claiming it brings priority scheduling rights. In this session at Anchor & Helm, two of the three are already in the minutes. The schedule protection is the priority scheduling right, and the line in the memo asking Grant to confirm by Friday is the witness slot. Writing it into this quarter's goals is the one still undone. Put the return on the table first, and the claim stops being a verbal favor.

All three gates clear. Now the two proposals. You ask that engineer, "Which gate is the polishing for?" He thinks it over against the table. Edge cases fall in the concern class, already inside the threshold. More polishing would push the number lower, but no gate asks for lower. You say, "All three gates are clear. Polishing is delay. I know you were not trying to stall. The word 'steadier' can always be said. Kevin's 'another month of trying it' is the same. What new evidence, for which gate, would another month produce? None. It would only produce more 'the feedback is good,' and 'the feedback is good' we already have." Kevin laughs. "Fine. We start Monday."

The last fifteen minutes, write the kill criteria. You say, "Right now every number looks good and everyone wants to run forward. Precisely because of that, this is the only moment to write the stop standard. Wait until the data looks bad and everyone can work backward from the standard to the conclusion they want. The discussion turns into a negotiation."

The first row goes down on the spot. Two or more unsafe-class errors in a single week, and the pilot pauses for rework. That whole class of suggestion is degraded to human review, the retrospective locates the root cause, and after the fix clears a golden case replay the owner signs the restart. This line is a line at the advise layer. It counts once only when a person catches the suggestion. The day the system moves up to the act layer (that cell in week 29, Chapter 22), this row gets rewritten to one occurrence and it stops, because by then the error has already landed.

A complete set of kill criteria is more than that one row. It covers at least four kinds of signal, one row each, all with hard numbers.

- North Star. The weekly median of first-touch handling time above the eight-week pre-pilot baseline for two consecutive weeks, pause the expansion, check the data source before the system. The data comes from the weekly points on Chapter 18's run chart (a metric plotted week by week as a line, read for trend and not for single points).
- unsafe. The row above. Trigger means the pilot pauses for rework, root cause retrospective.
- Acceptance. The target user group's weekly usage rate below the agreed line for two consecutive weeks, pause the expansion, go back to users to locate the reason.
- Cost. The system cost per claim above half the value of the labor hours that claim saves, for two consecutive weeks, pause the expansion, cost review. Chapter 16's four-fold bill (that chapter goes into it) did not hit this row. Cost per claim was still under the value line. What it hit was the budget line of the four ledgers (also Chapter 16). The trigger governs "is this still worth running," the ledgers govern "is the money being spent right." Two pages, one job each.

Kevin asks how this relates to the charter's resource reassessment conditions. You answer that resource reassessment conditions are project-level and govern "should the resources go back to the company." When the business side's committed input goes two consecutive weeks unmet, it runs in three tiers, escalate to the sponsor for a resource reassessment, the project turns to "awaiting inputs" on the PMO register, release your team's people and record it publicly (defined in Chapter 4). Inside a company it is one-directional. Only the sponsor or the project approval committee can shut a project down, and what your team can do is write the missing inputs into the ledger and pull your people back. Kill criteria are a pilot-level operating trigger and govern "should we pause this week." The trigger is an order of magnitude more sensitive than a resource reassessment, and an order of magnitude gentler. Triggering it means the defense held, not that it failed.

This page was never triggered once across the pilot's eight weeks. It was not written for nothing. In an incident retrospective after launch it gets pulled out and checked line by line (Chapter 18). That day it is still not triggered, and the fact itself, that the stop standard was written long ago and has not been triggered, becomes the hardest sentence in that storm over trust.

## The Resource Gates, How the Resource Cadence Meshes with the Three Gates

Up to here the chapter has deliberately not touched the question sitting on the other table, resources. That is what Grant's 7 minutes on Monday approved. The three gates hold the system. They do not hold a business department that sends no people. When the business side sends nobody, "let us take a look" is free, and an internal zombie pilot outlives any external project, because no bill reminds anyone it is still alive and salaries get paid either way. The three below translate the gates into resources.

**1. Named commitments, claimed in writing before the pilot.** People, hours per week, schedule protection, claimed by the counterpart's supervisor with the sponsor present, written into the pilot launch resolution. Where a company has showback or chargeback (showback only shows the bill, chargeback actually deducts budget), compute and labor are booked straight to the department using them. What this manufactures is a person watching the progress. Whoever's name is in the commitment column will come asking in week 3 whether this thing actually works, because what is being spent is his people's time. The first mover behind a zombie pilot is usually that nobody bears the cost. Technology comes second.

**2. Renewed funding tied to the gates, not to the calendar.** The approval conditions for the next round of people and compute budget are written as the three gates and the graduation criteria, with no dates. A sentence in the annual plan like "add headcount in the second half" is a down payment on failure mode 3 (escalating by the calendar). Rewrite it as a conditional. The three gates cleared and the escalation resolution signed corresponds to the pilot period's people and compute. The graduation criteria met corresponds to the round of resources that comes with formal project approval. That sentence is awkward to say at a budget meeting, and it protects both sides at once. The business side does not send people for a system that is not ready, and your team does not burn schedule on an open-ended "another month of trying it."

**3. A fixed reassessment date that settles automatically when it comes due.** Beyond graduation and kill, the most common third state in reality is "it came due and nobody ruled." Set the reassessment date on the pilot launch day, write it into the launch resolution, and when it comes due with no escalation resolution, settle on how much of the graduation criteria was actually met, convert to formal project approval or shut it down. "Another month of watching" has to go through project approval again. This is the internal version of the price tag. Not deciding is no longer free here. It amounts to an automatic shutdown, and whoever wants a continuation goes and gets project approval again, with the reason written on the form. It works better than any chase email.

Beyond the three there is one question left, who dares say stop. Stopping a pilot internally costs someone face, and whoever says "this should stop" first carries the conclusion for everyone. That is exactly what the zombie pilot failure mode is about. So a kill criteria trigger is written as an automatic action, not as a person's decision. Two unsafe in a single week, the system automatically degrades to human review. The North Star above the baseline two consecutive weeks, the expansion pauses automatically. The action comes before the meeting, and nobody has to call a stop. The row written on Wednesday reads exactly that way. Trigger means degradation, the retrospective locates the root cause, and what the owner signs is the restart, not the stop. The data does the stopping. People only sign the restart.

These three need no new process built. Most companies already have stage-gate reviews or project approval reviews. The PMO's quarterly stocktake, the project approval committee's review meeting, the annual budget and headcount review, the gates are all there, and all that is missing is the criteria on the gate. Write the three gates, the graduation criteria and the kill criteria onto one page, hand it to the PMO or the budget owner, and let them become a standing agenda item of an existing review. How the criteria get into their form is their business. What the criteria are has to come from you, because they cannot write them. This is the internal reader's own lever. The company spent years building these gates, and once you hang your project on them, the review's force is your force. In a company with none of these gates, hang the three on the sponsor's standing meeting and write the reassessment date into the minutes, so it goes on the agenda automatically when it comes due. Chapter 2 said it. The carrier can change. The source of enforcement cannot go missing.

You also have two things an outsider does not. How the last zombie pilot died in this company, you can look up, and its cause of death goes into the candidate rows of this project's kill criteria. The eight-week pre-pilot baseline you pull from the warehouse yourself, without waiting for anyone to hand it over.

These three will make your own manager uncomfortable. After the escalation decision meeting breaks up you call Owen Hartley and say the kill criteria are in the minutes. His first reaction. "You put 'it can be stopped' into the minutes in black and white. Do you still want next year's project approval allowance for this line?" You can answer this way. Grant was willing to approve the pilot in week 9 precisely because the conditions for stopping were on the table. Daring to write the stop standard is what buys a budget someone dares to approve. And renewed funding (that meeting in Chapter 22) rests on the number really coming down on the run chart. Whether the minutes left you a way out will not help.

## Failure Modes

**1. Prototype straight into production.** On demo day the executive says "great, roll it out to the whole department next month," and so prototype code goes into production carrying prototype discipline, no monitoring, no rollback, no change process, a hand-rolled data pipeline. From outside, the organization sees only "it runs," and cannot see the five gaps (Chapter 1). The definition of a prototype is data, workflow, trust, ownership and value papered over temporarily, and "let us run a pilot after all" sounds like going backward in reporting language. One discipline, hold up the change discipline row as a mirror. "What process does changing one line of code in this system take right now?" If the answer is "change anytime," it is still a prototype, wherever it runs.

**2. The zombie pilot.** Month four of the pilot, and the report still says "pilot in progress, optimization continuing." Pilot status is locally optimal for every participant. The engineer has work, the owner need not carry full-volume responsibility, and "currently piloting" is always safe in an executive report. Meanwhile nobody ever defined graduation criteria or death criteria, and whoever says "this should end" first has to own the conclusion (the same shape as Chapter 4's "whoever calls a stop first is the villain"). Discipline, on the pilot launch day write the duration and two exits hard, the graduation criteria and the kill criteria. When it comes due it must take one exit. An "extension" must go through project approval again.

**3. Escalating by the calendar.** "Live in Q3" went into the annual plan, at the end of August the system "goes into production on schedule," and the error categories that never cleared the line get "continuous optimization after launch." The organization's scheduling system eats dates and not conditions, and once a date enters an executive report it takes on a life of its own. A delay needs a written explanation, staying on schedule needs only silence, and error rates do not read the calendar. Discipline, always write outward commitments as conditionals, "live within X weeks of clearing the three gates." When a date and a gate conflict, remember this. Changing the date costs one report. Changing the gate costs one incident.

**4. Kill criteria written after the fact.** Only once the pilot data looks bad does anyone meet to discuss "under what conditions should we stop." By then the standard cannot possibly be neutral. Everyone knows which line kills the project, and the discussion inevitably becomes a negotiation of positions. Whoever wants to continue proposes a loose line, whoever wants to stop proposes a strict one, and the final "standard" is only a mark of power. Writing during the excited period is the opposite. Nobody knows which side the data will land on, and only then can the standard be fair. This is a veil of ignorance you set for your future self, meaning you do not let yourself know in advance which way the data will tip. Discipline, kill criteria are a standing agenda item of the escalation decision meeting, signed the same day as the escalation resolution. A stop standard written only after entering the pilot is void.

!!! note "Vendor View"
    The vendor side's version of this gate is called the money gate, and the three are the same shape. Charge for the pilot, even symbolically, because a free pilot is a zero-cost option for the client. Tie payment milestones to the three gates and the graduation criteria, not to the calendar. Write the expiry exit into the contract, and when it comes due with no decision, settle on the graduation criteria and convert to a paid extension or terminate.

## Next Monday

1. Label the project in front of you. Which stage does it claim to be in? Then use the stage rules table to check line by line which set of discipline it actually keeps. The cell where the claim and the practice disagree is your biggest risk right now.
2. Have a prototype "in trial"? Write down the current evidence for each of the three gates, one line each. The one you cannot write is what you should go fill in this week.
3. Have a pilot running past its planned duration? Today, write out its graduation criteria and its death criteria, that is, the kill criteria, one sentence each. If you cannot write them, admit it is a zombie. Kill it, or take it back through project approval.
4. About to enter a pilot? Use [Template 14.3](../appendices/template-14-stage-gates.md) to write the kill criteria this week, while everyone is still excited.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 14 Next Monday actions. First run python3 templates/stage-gates/gate_check.py
with the built-in sample to show the gate one check output, then copy kill-criteria-weekly-report.md to the working directory I name. I tell you the stage the project
claims, and you go line by line through Template 14's stage rules table asking which discipline it actually keeps, marking the cells that do not match.
The graduation criteria and the kill criteria are one sentence each, written by me. You only check whether each sentence can be ruled on by a number or an event, and send back the ones that cannot.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The stage rules table (three stages × goal / data / users / change discipline / ways to die); the three escalation gates (eval over the line / willingness to use it daily / owner in place); the pilot kill criteria discipline (written in the same meeting as the escalation resolution, signed the same day); the three resource gates (named commitments claimed / renewed funding tied to the gates, not the calendar / a fixed reassessment date that settles automatically when it comes due)
- **Templates.** [Template 14](../appendices/template-14-stage-gates.md), Stage Gate Checklist and Pilot Kill Criteria
- **Key judgments**
  - "The danger is not inside a stage. It is in changing stage without changing the rules."
  - "All three gates are clear. Polishing is delay."
  - "Kill criteria are written during the excited period. They cannot be written during the disappointed one."
  - "The pilot is eval scaled up, not production scaled down."
