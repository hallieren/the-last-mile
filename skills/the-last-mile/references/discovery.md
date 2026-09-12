# Access deadlock and the unknown workflow: trust first, then dig

**Load this reference when:** the data request sits "in progress" for days, "it's going through the process"; meetings are all pleasantries and nobody cooperates or opposes; the people who matter cannot be booked; "we know the process, it's in the SOP"; the flowchart does not match what you saw at the desk; you hear "I can tell at a glance".

Source: chapters 5, 6 (`docs/chapters/ch05-trust.md`, `docs/chapters/ch06-field-archaeology.md`); templates 5, 6 (`docs/appendices/template-05-stakeholder-map.md`, `docs/appendices/template-06-field-archaeology.md`); `repo/templates/stakeholder-map/stakeholder-map.md`, `repo/templates/field-archaeology/friction-log.md`.

## Contents

Part one, trust: permissions vs trust · the trust equation and the inherited balance · six-role map · two internal extras · contact plan · the "cannot get X" procedure · 12-question self-check. Part two, archaeology: three versions of a workflow · the six-step truth loop · three hiding places · three-layer probing · rule sentences · friction log · the half day · compliance branch · reschedules · expiry. Detectors. Key judgments. Templates. Vendor seat.

## Part one: trust ships first

### Decisions

**Rule on "cannot get the data" as a trust problem before a permissions problem.** The org chart draws the permission system; day to day the company runs on the trust network. Data access, the truth and the front line's time are open only to people whose trust balance is positive; the approval process is trust's bookkeeping, and with no money in the account the process is an indefinite "in progress". Trust accrues one notch per promise-and-delivery cycle, cycles take days and cannot run in parallel, so trust is the slowest step on the critical path and the only gap with no technical accelerator.

**Work the equation on the one variable you control.** trust = (credibility × reliability × intimacy) / self-orientation. Credibility: what you say can be believed. Reliability: you do what you say. Intimacy: the other person dares to tell you the truth. Self-orientation: how visibly you are working for yourself; no numerator survives division to zero. At the start of an AI project the balance is negative, not zero: fear of replacement plus black-box suspicion. Inside a company the start is an inherited balance (the last system's reputation, every prior collaboration, "system builders" as a type), occasionally positive, usually negative, and the ceiling is lower (no prophet at home; a colleague cannot draw credibility on a title). Credibility cannot be rushed and intimacy needs the other side to open first, so reliability is the only variable fully in your hands from day one: say Friday, deliver Friday. Presence compresses one cycle to half a day; others bank three notches a week, you can bank six (illustrative). Say the fear of replacement out loud to the front line's face: "every output has a Human Call column, and the call stays with you."

**Draw the six-role map with real names, three cells per person: the name, what they fear, what they win.** Departments do not fear and do not win; a department name counts as blank. One person can fill several cells; mark him with an asterisk, he is a high-leverage node. The map's value is in the blanks and the wrong cells.

| Role | Test | Common mistake | Contact note |
|---|---|---|---|
| Decision-maker | Who can, in one sentence, fund the next phase or kill it? Whom does he answer to? | Writing only the sponsor, forgetting the sponsor answers to someone too; forgetting your own manager, who cannot kill the project but can reassign you tomorrow | A one-page memo on a fixed cadence; judgments and decision requests only |
| Actual user | Whose daily actions change after launch? | A department name instead of a person | Go to the desk, not the meeting room; a fixed slot written into the charter; say the fear of replacement to his face |
| Data owner | Who owns the data you need on the business side? | Going only to IT, who holds the key, not to the data's business owner | Solve one of his own data pains first, then talk about access |
| Risk owner | When something goes wrong, whose name is on the accountability email? | Treating review as process and assuming nobody really cares | Invite him into the project team in week 2 (rule), never send it for review passively at the end; hand-deliver the pre-mortem |
| Maintainer | A year after launch, whose annual goals list this system? | Writing yourself in (kills the cell's diagnostic power); leaving it blank (nobody there at handoff) | Co-build from the first line of code, not a handoff document in the final week |
| Blocker | Without whose nod does everything stop, even though he never attends? | Reading "never attends" as "not involved" | One on one, early, in person; never ambush a blocker in a big meeting; behind the blocking there is always something he is protecting, find it and write it into the plan |

**Add two internal cells; the six tests stay unchanged.** The peer competitor (another AI team or a sister unit's digital group): fears your project becoming the benchmark he is measured against next year; wins a place he can write into his own reporting. First contact in the opening week: show him your scope boundary, ask what he has that you can reuse; the competitor becomes your first reuser. The predecessor's legacy (this unit was hurt by a digital project before, and to the front line you are the same kind of person): fears it happening again; wins someone admitting the last time first. First contact: find the last project's real cause of death (the files and the people are in the building, one afternoon settles it) and say it out loud in front of the front line. Get it right and half the debt moves off your account; get it wrong and the correction is the start of intimacy.

**Fill the opening trust balance first (- / 0 / +), inherited, then add your deposits on top.** Then ask the two mandatory questions: which name has never been in the meeting room (the blind spot and the future cause of death); which cell's content did you guess (go verify; a wrong guess at what they fear is more dangerous than a blank). If the actual user's fear cell does not mention being replaced or taking the blame for AI, you did not ask.

**Keep a contact plan: person, frequency, format, what to bring next time (what he wants, not what you want), last contact date.** Bring something useful to him every time; contact empty-handed spends trust. A key cell with no contact for two weeks (rule) is marked red. Contact ≠ meeting; a hallway, a desk, a three-line email count.

**Never invoke the charter clause first.** Invoking the contract is a trust withdrawal; whoever pulls out the clause on day ten finds every door shut tighter on day thirty, and the same people are in the building next year. The clause gives you a floor, not a key.

### Procedures

**Break the "cannot get X" standoff.**
1. Go back to the map's data owner cell. IT holds the key; the business owner of the data holds the trust network.
2. Ask three questions: who is X's business owner; what fight is he fighting; can I help him win once first, and where is the exit for that once?
3. Settle the exit before you touch anything. One-off (the script stays with them and they run it from now on) is the only form you take on the spot. A long-term commitment goes into the intake list and waits its turn; the waiting is itself the price. In "help him win once first", the word "once" is the gate.
4. Help visibly and cheaply, at his desk: data never leaves their machine; the script stays under his staffer's name and the credit goes to his department; errors you find are not turned into talking points in other meetings. Not touching unauthorized data is the floor, not a signal.
5. Do not mention the request. Let the person with the power speak for you, in his own language of power.
6. Bank what you saw: the true face of the fields is first-hand material for data reconciliation.

**Run the 12-question self-check every two weeks (rule); read the answers for the gaps, not the total.**
- Credibility: in the past two weeks, did you say to someone's face "I do not know, I will have an answer by X" and deliver on time? Of your last three judgments, how many carried evidence from this unit's floor (numbers, cases, users' own words) rather than industry boilerplate? Has the business side quoted you in a meeting you were not in?
- Reliability: of your last five "you will have it Friday" commitments, how many landed on time? Are meeting action items sent in writing within 24 hours (rule)? Have you once shrunk a commitment you could not keep, early and unprompted, instead of explaining on the deadline?
- Intimacy: has anyone told you something at the level of "I am only telling you this"? Have you once said the tension in the room out loud, to people's faces? Has the front line complained to you about their own department or boss? (The jargon test does not count for a colleague.)
- Self-orientation, lower is better: in your last meeting, how many times "our system / our plan" versus "your claims / your metrics"? When the business side suggests shrinking scope, is your first reaction defense or curiosity? When did you last advise "let's not do this yet"? If never, the denominator is quietly rising.
- One blank question = the next behavior to create this week, one action covers it. All three blank under one variable = a line you are not working at all; it goes on next week's calendar.

**After launch, change the deposit method.** No longer say Friday, deliver Friday. It is alerts get answered, there is a name on the oncall rotation, someone shows up at the retrospective. One unanswered alert in month 14 (illustrative) empties every notch the charter period banked; any cell the responsibility transfer agreement leaves unclear is charged to your account.

## Part two: field archaeology

### Decisions

**Design against the actual version of the workflow, never the SOP or the reporting version.** Every organization holds three at once. The SOP version says what should happen; its job is compliance, audit and onboarding, and by design it does not describe reality. The reporting version is what management sees; each step up the chain smooths away more workarounds, because reporting one means confessing a violation or inviting "systematization". The actual version lives only at the desk, in exception handling, private spreadsheets and the feel of veteran staff, and it updates every month without telling anyone. The three coexist indefinitely and never correct each other. Interviews return the SOP version even from the front line; the real workflow is in nobody's words, only in their actions. The version you already know, as an insider, is precisely the one that traveled up the reporting chain to you.

**Run the six-step truth loop in order; it is a loop, not a pipeline.**

| Step | Action | Key discipline |
|---|---|---|
| observe | Be present and watch them work, do not interrupt | Write questions down, do not ask on the spot; keep the friction log as you go |
| shadow | Follow a person for half a day (rule) | Follow the person, not the process; a process does not open a spreadsheet, a person does |
| trace | Follow one case end to end | Across people, systems and tools; count how many hands and how many systems it passes through |
| ask | Ask about exceptions | "When would you not do it this way?" anchored on the concrete action you just saw |
| reconstruct | Draw the real process | Including workaround tools and verbal coordination, not one step prettified |
| validate | Have the person correct it | Ask "where is it drawn wrong", not "is it right"; the former gets corrections, the latter gets politeness |

Three rules: the order cannot be skipped (jumping straight to ask returns the recited version); run it two or three times, the rate of convergence tells you when it is enough; trace speaks through a case, and only the two cross-sections (one person's day, one case's whole life) together make a workflow.

**Dig in the three hiding places of tacit knowledge.** Exception handling: the SOP covers the main path, all the judgment is on the branches. Workaround tools: anything open on the screen that is not on the IT asset register (private spreadsheets, sticky notes, personal folders, small group chats); each one is a requirements document written over years; ask for its first version and the email that proposed it. "I can tell at a glance" judgments: trigger phrases "I can tell at a glance", "from experience", "hard to say", "obviously fake", "gut feeling", "do it long enough and you get it", and any judgment made within ten seconds whose reason you cannot derive; mark the time, probe in the wrap-up window.

**Probe in three layers; hypothetical questions are banned throughout.**
1. Anchor on an instance, replay the actions, do not ask why: "That case just now, you looked at [action 1] first, then went through [action 2], and then you [judgment]. Right?" A stock phrase does not match actions.
2. Compare two similar cases: "This one and the one just now are both [same type], the [surface indicator] is about the same. Why did you [flag] this one and not that one?" Then "any other difference?"; the second answer is often worth more. The real shape of the rule is in the difference.
3. Ask for boundary counterexamples: "When would you not [judge it this way], no matter how [extreme the indicator]?" and "Have you ever [judged it this way] and been wrong? What did you change after that?" The second digs out the rule's update mechanism, the key evidence against hardcoding. If the answer is "never been wrong", switch to "when you train new people, what mistake do they make most often on this kind of case?"

**Restate every judgment in the rule sentence form.** `When <observable signal> appears, I <action>, because the risk of not doing so is <consequence>. (Boundary: <when not>; source: <name, date, case>; stability: stable | drifts with <X>)`. Stable rules can become suggestion logic. Drifting rules (list types, threshold types) keep the Human Call and a decision trail for overrides; the decision trail is the drift detector. Every rule notes its destination: the real flowchart, an eval error category, or the risk list. A rule with no destination dies in the notes.

**Keep the friction log: # | time | paper version | field version | type | follow-up.** Type is one of data (a field does not match reality → reconcile), tool (a workaround carries the formal system's function → into the data source inventory), process (steps added, removed or changed against the SOP → the real flowchart), judgment (a human call not derivable from rules → the three-layer probe). Follow-up is one of reconcile / probe / into eval / report risk. One line per friction; keywords on the spot, complete within 24 hours (rule), details recalled the next day are invented; facts not conclusions ("status field lags on 3 cases", not "their system is terrible"); every line has a follow-up or the log is a gripe list. AI organizes archaeology notes; it does not produce archaeology facts.

**Read a reschedule by its reason, not its count.** If the reason changes every time, you are being brushed off; escalate. If the reason is backlog every time, the place you want to look is exactly where it hurts most; wait. Escalate only after three or more in a row (rule), talk about schedule protection and not attitude, and land it in the charter's business-side commitment row. A half day bought with a supervisor's authority is a half day the user treats as an evaluation; the spreadsheet you need to see stays closed.

**Report only the four compliance risks; everything else is a scar of underdesigned process.** Must be reported: individually matchable data on a personal computer or in a personal mailbox; outbound sending that bypasses approval; operating under someone else's account; a step that requires a record being skipped. Not violations: sorting in a spreadsheet, color-coding priority, calling a contact you know; these go to the real flowchart and the data reconciliation. When unsure: would this become a problem if audit saw it, not whether it looks proper. Not correcting on the spot governs the half day, not the half year; noting without calling out is not permanent secrecy. If you must report, tell the person first, face to face, and write down why she needs the tool and what breaks if it is shut down before a replacement exists. You get exactly one chance to build that credit.

**Date every flowchart and every rule, and book the next dig.** The system you build kills its own source of truth; some workaround steps get taken over, the rest grow new workarounds nobody reports. Sit once in week 4 and once in week 12 after launch (rule), one hour each, doing two things only: count the steps again, ask whether any new spreadsheet appeared this month. After that, every six months (rule) as the periodic review. A flowchart with no date is the same thing as an SOP three months later.

### Procedures

**Book and run the half day.**
1. Book the actual user, not the supervisor; if the supervisor arranges it, name the person explicitly. Use the three-element opening (apprentice posture, capped duration, zero-interruption promise): "I would like to sit with you for half a day and watch how you normally handle these cases. I am here to learn. I am not here to evaluate you, and I am not here to sell a system. Work as you normally do. I will sit to the side and take notes, save my questions, and ask when you have a free moment. I will take at most 30 minutes (rule) of your wrap-up time."
2. The day before: print the SOP as the dig map; print a blank friction log; confirm screen and note permission, and where sensitive data is involved default to no recording and no screen photos even with permission; fix your red lines (no promising features, no judging, no suggestions on the spot); pick 1–2 candidate cases to trace.
3. 0:00–0:10 opening; 0:10–2:00 pure observation, no interruptions; 2:00–2:15 tea-break window, only about actions you observed, no more than 3 questions (rule) at a time; 2:15–3:30 continue observing and trace one case; 3:30–4:00 wrap-up, three-layer probing plus the three closing questions.
4. Count: real steps vs official steps (the difference is the width of the workflow gap); tool switches; off-screen actions (phone calls, calling a colleague over, paper files; easiest to miss, often most valuable); workaround tools; ten-second judgments with the time marked.
5. Code of conduct, break any one and the half day is wasted: no suggesting; no correcting; no selling the system, not even one "the system will be able to do this for you later"; no promising features; noting without calling out is not permanent secrecy.
6. Close with three questions: "Was today a typical day? What was not typical about it?" "If you took a week off, who would do this work? Which step would they get stuck on?" "Of everything in this half day, which thing did you feel was least worth your time?"
7. Within 48 hours (rule), take the real flowchart and the rule sentences back and ask "where is it drawn wrong?" Mark each rule's stability and destination.
8. As an insider, split the half day into five one-hour visits on different days if you can; pull the QA reviews and complaint log for the counterexamples she cannot remember; ask for the first version of the workaround tool.

**Tag your existing requirements document.** Mark every line as manager interview, SOP, or firsthand observation. If the first two make up more than ninety percent (rule), you are writing software for a parallel universe. In discovery the actual user accounts for more than half of interview time (rule); if you cannot book them, wait.

## Detectors

- If you have an excellent relationship with the sponsor and your manager and the front-line team cannot say your name, then you are cultivating only the boss. The sponsor gives you the project; the front line gives you the outcome. After launch neither boss logs in.
- If "the data is worse than expected" has sat in your mouth for two weeks, then you have booked bad news as a credibility expense; it is a double deposit when delivered early, unprompted, with a plan. Bad news does not disappear, it only appreciates.
- If "our system" shows up in your sentences more and more, then self-orientation is leaking; the frequency of "our system" is the leak meter. Put the motive on the table: "If this succeeds, of course that is good for our team. But it only counts when your handling time really drops." A motive said out loud is a boundary.
- If your reporting says "the system we built" rather than "their queue", then the denominator is rising.
- If you are about to take the resource reassessment clause to the sponsor on day ten, then you are about to make a trust withdrawal; go to the data owner's fight first.
- If discovery met eight directors (illustrative) and never sat at a desk, then you are looking at the field through two layers of distortion.
- If you designed the state machine straight from the SOP, then you are building for a parallel universe; the SOP is the starting point of the dig, not the end.
- If you asked "what features do you want", then you got a solution projected onto the old tool; users can order from the menu, but users are not the chef.
- If five rules of thumb became five if-else branches, then you shipped a snapshot of living rules with nowhere to put responsibility when it errs; put them in the suggestion and reason columns, keep the decision with the person, record overrides in the decision trail.
- If you hear yourself say "I'm not an outsider, why would I need to sit for half a day", then familiarity is deciding for you; the version you know is the reporting version.
- If the real flowchart has no date and no next-dig date, then it is already an SOP.
- If the reason for the reschedule changes each time, then you are being brushed off.

## Key judgments

- "The org chart draws the permission system. Day to day, the company runs on the trust network."
- "At the start of an AI project, the trust balance is negative, not zero."
- "The sponsor gives you the project. The front line gives you the outcome."
- "Let the person with the power speak for you, in his own language."
- "The official flowchart is not wrong. It belongs to a parallel universe."
- "Users can order from the menu, but users are not the chef."
- "AI cannot shadow. 'Seeing that the Excel exists' is in no dataset."
- "The SOP is the starting point of the dig, not the end."

## Templates

- `docs/appendices/template-05-stakeholder-map.md` (and `repo/templates/stakeholder-map/stakeholder-map.md`): the six-role map with fear / win, trust balance, contact plan, and the 12-question self-check.
- `docs/appendices/template-06-field-archaeology.md` (and `repo/templates/field-archaeology/friction-log.md`): the half-day guide, the friction log, the three-layer probing script and the rule sentence form.
- `templates/pre-mortem.md`: what to hand-deliver to the risk owner and to the name that has never been in the room.

## Vendor seat

The stakeholder map and field archaeology apply as is, change nothing. As the hired expert you open negative with a high ceiling, and the last failed project's cause of death takes weeks to unearth, so probe for it with a pre-mortem; helping the data owner for 40 minutes and no more is a strong signal, since not overstepping is itself evidence. A line in a contract is not a working mechanism.
