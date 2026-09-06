# 3 · Four Identities: Builder, Advisor, Operator, Teacher

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-03-capability.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** Four things land on you in one day. A bug to fix, a meeting to take, a person to teach, a weekly report to write. Every one is reasonable, every one has someone waiting, and there is only one of you.
>
> **What You Will Be Able to Do.** Use the four identities to see who you are playing in each block of time. Use the identity switching table to decide which identity this moment calls for. Rank conflicts by irreversibility when several arrive at once. Use the five-axis capability radar to find the piece you need to shore up. Label the half of your calendar that belongs to your own department, and compress it.

---

## Four O'Clock, Wednesday Afternoon

A week and a half since the Field MVP readout. The direction is set (an action queue for auto exception claims), the charter is not negotiated until next week (Chapter 4), and you are in the deep end of discovery (the formal stage of finding out how things actually are). After the readout you put a proposal to Kevin Doyle. Every morning the prototype queue runs a batch of the previous day's de-identified exception claims. Data access is nowhere in sight, so Kevin has a subordinate export the batch by hand each day. Linda Marsh's team works with the queue in view but decides by its own judgment, marking as it goes. Nothing goes to production. The point is to keep collecting scores and real reactions.

At four o'clock on Wednesday afternoon, four things arrive within ten minutes of each other.

- **4:00.** You find a bug in the queue prototype. Days waiting counts weekends too, so three claims in this morning's batch were ranked too high. Not hard to fix, under an hour.
- **4:03.** A message from Kevin. "Got a minute? Let's talk direction." When a director asks to "talk direction," it usually means he has a new idea in his head.
- **4:07.** A call from a senior reviewer on Linda's team. Linda is at headquarters for a meeting, and Sam, the new reviewer, took the queue's "suggested next action" as an order and followed it to the letter, sending a request for supporting documents on a claim whose liability is in doubt. By the team's own rules that kind of claim goes through an internal liability check first. The customer has already called in to challenge it.
- **4:10.** You remember that the first weekly report to Grant Whitmore goes out at nine tomorrow morning, and you have not written a word.

All four are urgent. All four are reasonable. Say the obvious part out loud first. Your first instinct is almost certainly to fix the bug. The reason has nothing to do with importance. It is the most fixable. The scope is clear, the path is clear, and an hour later a certain sense of completion is guaranteed. None of the other three offers that.

Choose wrong this afternoon and three months from now you are up all night maintaining a system nobody trusts. This chapter is about choosing right.

## Why This Is Hard: The Four Identities Are Not Four Skills

Chapter 2's inheritance matrix says where this role comes from, its five predecessors. The four identities say how it lives out a single day. The daily work of this role is made of four identities. "You need all four" would be easy enough. The hard part is that they are four conflicting ways to allocate time, carrying four conflicting sources of satisfaction.

| Identity | One-Sentence Definition | Source of Satisfaction | Feedback Cycle | What Being Stuck Looks Like |
|------|------------|------------|----------|--------------|
| **builder** | Build working things with your own hands, prototypes, pipelines, integrations, fixes | It runs | Minutes, certain | Prodigious output, nobody using it |
| **advisor** | Help the business side make better decisions, trade-offs, memos, direction | The business side takes your judgment | Weeks, blurry | More and more advice, less and less landing |
| **operator** | Keep what already runs reliable, monitoring, incidents, rollback | The fire is out | Hours, a strong hit | Always firefighting, never able to leave |
| **teacher** | Make the business side stop needing you, training, co-build, capability transfer | They get it done without calling you | Months, almost silent | The most common problem is never starting |

Look at the feedback cycle column. The builder's feedback comes in minutes and is certain. Tests go green, the queue runs. The teacher's feedback comes in months and is silent. The business side learned, and it shows up as "nothing happened." That is why a deliverer who came up as an engineer defaults to being stuck in builder, and one who came up in consulting defaults to advisor. People do not settle on the most important identity. They settle on the identity with the most comfortable feedback.

Now look at the teacher row. Its output is your own replaceability, and the outcome ladder's L4 (self-sufficient) is where the teacher identity settles. Of the four identities, teacher is the only one that never cries out on its own.

An internal reader hits the word "replaceability" and reads career risk. Do the arithmetic before deciding whether to be afraid. A system that no longer needs you releases your capacity, and capacity cashes out as one more department covered this year. That is the first line of Chapter 23's capacity ledger (the account of how many projects your team can run in a year). A system that cannot run without you costs next year's headcount one person who could have opened a new project. That is Chapter 2's trap one. Inside a company, being irreplaceable is not a charm. It is the prelude to permanent ops. For someone who arrives with an exit date, replaceability is a medal. For you, it is next year's capacity.

## Prior Art, and What AI Changed

**The Trusted Advisor spectrum.** Maister, Green, and Galford drew a spectrum in *The Trusted Advisor*. At one end is the subject-matter expert, brought in to answer because he knows one technical problem. At the other end is the trusted advisor, brought in to help define the problem because his judgment is trusted. Move right along the spectrum and the questions the business side asks you get bigger. From "how do I build this," to "which one should I do," to "what do you make of our whole portfolio," and the source of value moves from knowledge to judgment. The spectrum spans three of the four identities. builder lives at the expert end, advisor and teacher live at the other. It was drawn for people who are invited in. You were not invited, you were assigned, and nobody pays extra for your judgment, so the "questions get bigger" signal distorts inside a company. Use a different test. The business side quotes your judgment when you are not in the room.

If Kevin repeats your view on exception claims at a department meeting you did not attend, you are at the right end. If he asks only when you are in the room, you are still at the left.

**Maister's time leverage.** In *Managing the Professional Service Firm*, Maister points out that the economics of a professional service firm is a structure of time leverage, which he calls finder (winning the work), minder (managing the relationship), and grinder (doing the work). Senior people spend their time on judgment and relationships, and the grunt work is pushed down the leverage. A professional's value is largely equal to which layer of the leverage his time sits on.

Move the three layers inside a company and the structure holds, but the top two change content. Inside, finder is not winning work, it is screening work. Your service carries no price, so requests come to you on their own (Chapter 2's ask inflation), and a senior person's first layer of time goes to deciding what not to take. Chapter 25's intake gate is the institutional version of this layer. Inside, minder is not maintaining a counterpart who pays, it is maintaining cross-department relationships and political capital. Whether Kevin gives you people, whether Victor Reyes lets you through, whether Owen Hartley protects your schedule, all of it draws on the balance in this layer. grinder changes not one word. Doing the work is doing the work.

What did AI change? The grinder collapsed into the tools. AI coding agents compress the grunt layer inside the builder identity hard. Scaffolding, integration, tests, refactoring, the work that used to eat most of this role's time, is now mostly AI doing and you reviewing. Maister's leverage pyramid, which needed a whole team, can for the first time fold into one person. AI is your grinder, and your scarce time is forced up into advisor and teacher. That is where the discomfort comes from when senior engineers move into this role. Twenty years of accumulated satisfaction rests on builder output, while the role's time structure pushes them toward the two identities with the blurriest feedback. The discomfort says the leverage is moving. It says nothing about whether you are good enough.

builder depth did not lose value in the process. Reviewing AI output, vetoing a bad architecture, smelling a problem in a data pipeline, all of it rests on having written enough code with your own hands. Moving up the leverage assumes you can actually do the work at the layer below (the "engineering depth" axis of the five-axis radar guards exactly this floor).

## Core Framework One: The Identity Switching Table

The core muscle of the four identities is switching at the right moment. Being able to do all four is only the entry ticket. Switching runs on two things. The stage sets the default, and a signal triggers the exception. The handoff in the table's last row means the stretch where the system, together with responsibility for running it, goes to the business side. On a first read, look only at the row for the stage you are in. This book is at discovery right now, the other rows are for later, so give them one scan.

| Project Stage | Default Primary Identity | Switching Signal → Switch To |
|----------|------------|---------------------|
| Opening and Field MVP (Chapter 0) | advisor (using builder's hands to produce the basis for judgment) | The discussion slides into implementation detail → pull it back to the workflow claim, hold advisor |
| discovery (Chapters 4 to 7) | advisor | The parties disagree on how the data is defined → switch to builder and reconcile it yourself<br>The front line worries "how will this thing use me" → switch to teacher and spell out the boundary and the red lines |
| Design (Chapters 8 to 13) | advisor (using builder's hands to verify feasibility) | The argument over the plan hangs in the air → switch to builder and settle it with a thin slice (one narrow but complete slice)<br>The risk owner keeps pressing → switch to teacher and show where the constraints entered the design |
| prototype → pilot (Chapters 14 to 16) | builder | The same question is asked a third time → switch to teacher<br>Scores or human overrides (a reviewer overturning the queue's suggestion) come out abnormal several times in a row → switch to advisor and back to the judgment layer<br>Two days running with no conversation with a user → force yourself out of builder, switch to advisor |
| Launch and adoption (Chapters 17 to 21) | operator and teacher equally | The second incident of the same kind is still handled by your own hands → switch to teacher<br>Metrics steady for two weeks → hand over the operator duties |
| handoff and stepping out of the daily (Chapter 22 onward) | teacher | The business side says "build us another one" → switch to advisor and back to opportunity judgment, instead of saying yes on reflex |

Three rules for using it.

1. **The default identity follows the stage, the switch follows the signal.** No signal, no switch. Switching to whoever shouts loudest is not flexibility, it is the absence of a strategy.
2. **When conflicts arrive at once, rank them by irreversibility, trust > direction > code.** Wrong code can be rolled back. A wrong direction can be corrected, at a price. Burned trust has no rollback button. Of Chapter 1's five gaps, the trust gap is the only one with no technical remedy.
3. **Switching has a cost.** Four identities in one hour means none of the four got done properly. Switch in blocks of time (half a day is best, two hours minimum), not in message notifications.

The table's last row needs two more sentences inside a company. The first is about teacher. That cell defaults to teacher on the assumption that an exit date is forcing it. You have no exit date. Nobody will take your write access away on some given day, so teacher can always start next week, and "the most common problem is never starting" holds double inside a company. You have to hardcode the forcing period yourself. On the day of launch release (Chapter 11), set the teacher deadline at the same time, write it into your own quarterly goals, and when it comes due run the five self-sufficiency tests (Chapter 22, which test whether the business side can run this system on its own). Whatever fails is claimed by the business side, not carried on by you. You can verify this more easily than anyone. Three months on, whether Linda's team still reads the reason column (the column in the queue that says why the suggestion came out the way it did) is something you can see by walking over to the desks, with no report to wait for.

The second is about operator. Finishing a project and going back to zero is the privilege of someone who arrived with an exit date. You cannot leave. Every system you launch adds one operator allotment to your calendar that never expires, and N launched systems means N of them. At some count the table starts failing you. You are in several stages of several projects at once, the operator blocks are permanently held by the systems launched first, and the advisor blocks of new projects get squeezed off the calendar. Set the steady-state ratio yourself. Operator gets at most one half-day a week, and going over says the previous system's handoff is not finished. Go back to Chapter 22's transfer ledger and find the red cell.

## Core Framework Two: The Five-Axis Capability Self-Assessment Radar

The table answers "who should I be right now." The five-axis radar answers "who can you actually be." The five axes follow.

- **Engineering depth.** Without AI, can you still stand a system up. Data, APIs, debugging, deployment.
- **AI engineering.** The engineering capability to manage uncertainty. Eval, error taxonomy, human oversight, drift.
- **Business grasp.** Read the business side's process, metrics, and money, and say which business number your system moved.
- **Narrative.** Get every level of the organization the judgment it needs, from the front line's own words to an executive memo.
- **Field judgment.** Make the right trade-off on incomplete information. Red lines, priorities, when to switch, when to say no.

One to five points per axis. Look first at what a 3 looks like, and give yourself one rough score against it.

- Engineering depth 3. You can take a prototype to a working pilot on your own, data integration, deployment, logging, basic monitoring.
- AI engineering 3. You can write an eval for one feature, golden cases (sample cases with the correct answer settled in advance), acceptance thresholds, error categories (the method in Chapter 11).
- Business grasp 3. You know the real workflow, workarounds, exception handling, how the front line gets around the system (the output of Chapter 6's archaeology).
- Narrative 3. Answer first. The memo leads with the conclusion and the decision you want, then the evidence (Chapter 13's pyramid structure).
- Field judgment 3. You can make trade-offs under time pressure, ranking by irreversibility, with a steady sense of the red lines.

An internal reader's first scoring has a roughly predictable shape. Business grasp runs naturally high. How the metrics are defined, the cause of death of the last failed project, which team lead's word counts, you were present for all of it, and this axis starts higher for you than for an outsider. What to guard against is mistaking familiarity for understanding. Do Chapter 6's archaeology as written, and work only the increment. Field judgment runs naturally low. It is the only one of the five that grows by saying no, and saying no is most expensive inside a company. Across the table is a colleague you will still be in meetings with next year, and a manager who sets your schedule, so most people substitute "let me look into it" for a judgment. A reader who came up as an engineer will see a shape with engineering depth and business grasp both high and field judgment at the bottom, and by reading rule one below, the bottom axis decides how large a project you can own alone. For internal readers the shoring-up move is usually not in the technical column, it is in Chapter 25's saying no scripts.

The full level anchors, self-check questions, and score-by-score shoring-up advice are in [Template 3](../appendices/template-03-capability.md). Three rules for reading the chart follow.

1. **The lowest axis decides how large a project you can own alone**, and the highest axis decides nothing. The five axes multiply, they do not add.
2. **The radar's shape predicts your failure mode.** Both technical axes high with narrative and judgment low is high risk for coder mode. Narrative high with thin engineering depth is high risk for consultant mode (the "Failure Modes" section unpacks both).
3. **This coordinate system gets used again.** Chapter 26 uses the same five axes to define the deliverer's F1 to F5 capability levels (F for field, the prefix marking a person's capability level, as distinct from the outcome ladder's L0 to L4 for system outcomes). Today's radar is your starting archive. Keep it.

One sentence for how identities and axes relate. Identity is how your time is spent, and the axes are whether spending it has any effect. The table governs the first, the radar the second.

## At Anchor & Helm: One Week of the Real Calendar

This is your real calendar at Anchor & Helm in the second week after the readout, with the primary identity marked on each block.

| Time Block | Item | Identity |
|--------|------|------|
| Monday morning | Sit in on Linda's team's morning meeting; collect last week's queue annotations, and probe two concern cases for the reviewer's own words | advisor |
| Monday afternoon | Have AI rewrite the case extraction script and load this week's 30 de-identified claims; spot-check 6 by hand | builder |
| Tuesday morning | Go through the business definition of the "reason stuck" categories with Kevin; clean up the friction log (the list of places where reality and paper do not match), and escalate 3 entries to risk items | advisor |
| Tuesday afternoon | Tune the queue's ranking logic, have AI produce three versions with the trade-offs written out, and veto two of them | builder |
| Wednesday morning | Answer round two of Victor's security questionnaire, de-identification method and log retention period | advisor |
| Wednesday 4 p.m. | Four things arrive at once (see below) | See the retrospective |
| Thursday morning | Give Linda's team 30 minutes on "how to read the queue's reason column and Human Call column" | teacher |
| Thursday afternoon | An upstream export format change breaks the batch run; restore it, and add an automatic validation check | operator → builder |
| Friday morning | The weekly report to Grant, AI drafts, you rewrite the conclusion | advisor |
| Friday afternoon | Prepare next week's charter meeting, three candidate definitions of the North Star metric, meaning how the metric is defined and how it is computed | advisor |

Count them. builder holds fewer than three blocks outright, and its main action is reviewing and vetoing. In the years before AI coding agents, most blocks in a week like this would have been builder. The leverage did not disappear. It folded into the division of labor between you and AI. Now look at teacher. One block, and even that was forced out by Wednesday's incident. teacher never shows up on the default calendar unless, when you lay out next week, you reserve a block for it before anything else.

The table also misses one kind of block. It is not on the table, and it is on your calendar. The Digital Center's own weekly meeting, OKR alignment, reviews for other projects. Chapter 2 said your calendar is torn in half. This is the other half, and none of the four identities can claim it. Most of the time it is pure loss. It produces no production outcome, it changes no business action, and you still have to attend. Loss has to be named before it can be squeezed. Give it a label of its own, own-department business, count its share alongside the four identities when you lay out the calendar, and do not let it slip into advisor to pad the number.

Only two cases are not loss. One, you are asking Owen for schedule protection, or explaining why you are taking no new requests this week. That is advisor, with your manager as the audience. Two, you are teaching the Anchor & Helm eval method to someone on your team working a different project. That is teacher, with a colleague as the audience, and Chapter 23's pattern library starts accumulating here. Compress everything else, merge it into one half-day, and do not let it shred the half that belongs to the business side.

### Four O'Clock Wednesday, the Retrospective

**4:00 to 4:10, the judgment.** Each of the four belongs to an identity. The bug (builder), Kevin (advisor), Sam (operator first, then teacher), the weekly report (advisor). Rank by irreversibility. The Sam item burns trust, and the third way to die you wrote in the pre-mortem a week and a half ago ("One wrong suggestion gets followed, a customer complains, and from then on the front line trusts no suggestion") is rehearsing in front of you. The bug burns code, and fixing it before tomorrow morning's batch run is enough. Kevin burns time, and rescheduling does not make it worse. The report has all evening. The order is not in doubt. The hard part is resisting the feel of "fix the bug first."

**4:10 to 5:20, the field.** Ten minutes as operator first, calling the customer back together with the senior reviewer and putting the claim back on the internal liability check track. Then fifty minutes as teacher. You did not take Sam aside to criticize him. You asked the half of the team that was there to go through the claim together as teaching material.

Why the suggestion was wrong (the system cannot see the internal signal for "liability in doubt"). How to read the reason column (if the reason does not hold, override it). Why the Human Call column exists (advise the person, do not decide for the person). Sam's mistake turned from "the new guy caused trouble" into one calibration for the whole team, and the next day's 30-minute session was its formal version.

**5:30.** Back to Kevin. "Something came up in the field today. Would 9:30 tomorrow morning work?" advisor can be moved, it cannot be canceled. Only the next day do you learn he wanted to talk about "whether we should put up a big screen." You did not veto it on the spot. You put it on the charter meeting agenda. The idea comes back in Chapter 17.

**9 to 10 p.m.**, the weekly report. AI drafts, you rewrite the conclusion, and you put the Sam incident in as it happened. "One misuse of the prototype, closed the same day. It exposed a training gap, and a session for the whole team is scheduled." Telling the bad news yourself first is a deposit you make on the trust gap.

The next day you fix the bug at 8:20, ship it at 8:40, and the nine o'clock batch run is clean.

In a parallel universe, the you who chose to fix the bug at four o'clock has it fixed an hour later, and it feels good. The Sam item slides to the next day, and the version Linda hears when she gets back from her meeting has already become "the system had the new guy fire off notices." She says nothing, but from that week on her team rechecks every suggestion by hand. The system still runs. It is just no longer trusted. Three months later you are up all night tuning a ranking algorithm nobody believes. The bug got fixed. The project died.

## Failure Modes

**1. Coder mode.** The calendar is all development blocks, the weekly report is all "what got fixed," and a full week passes with no conversation with a user. builder is the only identity that can hand you an "I finished something" confirmation at any moment, and its output is the most visible. In the AI era this pit is deeper, not shallower. AI doubles the output, so anesthetizing yourself with volume got easier. The self-check signal. Two days running with no substantive conversation with any user or stakeholder (a party with a stake in the outcome) is a red light.

**2. Consultant mode.** The memos get better looking and the hands-on work gets rarer. You advise that "the data should be reconciled," and nobody actually reconciles it, you included. Advice never throws an error. The advisor's output has no feedback loop from production and will never wake you at three in the morning, which makes it the safest hiding place of the four identities. But the deliverer's unit of value is the production outcome, and achievement is settled only at L3/L4 (Chapter 1). Give advice without carrying the result and you fall back into the one self-imposed mold Chapter 2 warned about, internal consulting. One self-check. How long has it been since you verified the feasibility of your own advice with your own hands?

**3. Firefighter mode.** Always handling incidents, the first call the business side makes when something breaks, and quietly proud of it. Firefighting feedback is a strong hit on an hourly cycle, it feels heroic, and the business side reinforces it. Every fire you put out teaches them your phone number, not fire prevention. Nobody will take that phone number back for you, and every extra year you stay at this company adds one more system in the address book that answers only to you. Every fire you put out by hand postpones the handoff. The better the operator identity performs, the less chance the teacher identity gets to start. The self-check signal. The second incident of the same kind still handled by your own hands means what should have been taught has not been taught (Chapter 22's handoff scene shows this again).

**4. Busyness in place of judgment.** All four hats worn every day, the calendar packed, everything nudged forward a little, nothing finished. Switching itself produces the illusion of being well rounded, and fragmented switching denies every identity a solid block. builder needs two uninterrupted hours to get into state, and one teacher session needs half a day of preparation. A week with no default primary identity is a week with no strategy. In Maister's terms this is the loss of leverage. Your time is not going to the things only you can do. On Friday ask yourself which three judgments you made this week that nobody else could have made. No answer is a red light.

## Next Monday

1. Open last week's calendar, mark each block with an identity, and compute the shares. Compare against the default identity for your stage in the table. The largest gap is where your inertia lives.
2. Find the question that has already been asked three times, and teach it out this week. One 30-minute session, a one-page FAQ, one pairing, so the person asking becomes a person who can answer.
3. Run a five-axis self-assessment with [Template 3](../appendices/template-03-capability.md), find your lowest axis, and set one verifiable 30-day shoring-up action ("improve communication" is too vague, "the next three weekly reports draw zero follow-up questions" counts).
4. Write "trust > direction > code" somewhere you will see it the next time conflicts arrive at once. Use it to rank once, then review afterward whether the ranking was right.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 3 Next Monday actions. First run python3
templates/self-assessment/radar.py to produce a radar chart SVG from the built-in sample, tell me where the file is and open it
for me. Then copy sample/radar.csv into my own self-assessment file. I score the five axes myself against Template 3's behavior
anchors. You only ask me for the behavioral evidence on each axis and record it, you do not score for me. Once the scores are in,
rerun radar.py pointed at my file. The 30-day shoring-up action for my lowest axis is mine to write. You only check whether it can
be verified, and send adjectives back. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The four identities (builder / advisor / operator / teacher) and their table of conflicting satisfactions; the identity switching table (stage × default primary identity × trigger signal); the conflict ranking rule (by irreversibility, trust > direction > code); the five-axis capability self-assessment radar (engineering depth / AI engineering / business grasp / narrative / field judgment)
- **Templates.** [Template 3](../appendices/template-03-capability.md) Capability Self-Assessment and F1–F5 Rating, the self-assessment half (3.0 to 3.6), 1 to 5 behavior anchors per axis plus self-check questions plus score-by-score shoring-up advice, re-scored and archived each quarter
- **Key judgments**
  - "Code gives certain feedback and people do not. That is why engineers hide in the builder identity."
  - "The same question asked a third time means what should have been taught has not been taught."
  - "When conflicts collide, rank by irreversibility, trust > direction > code."
