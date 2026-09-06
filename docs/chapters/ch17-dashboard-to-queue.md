# 17 · From Dashboard to Action Queue: Put the Next Action in Front of the User

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-17-action-queue.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The business side loved the dashboard you delivered. Three months later nobody opens it. What is missing between "we can see it" and "someone acts on it"?
>
> **What You Will Be Able to Do.** Measure how deeply a deliverable is embedded in the workflow with the action integration ladder. Translate "I want a big screen" into queue columns. Design an action queue with a decision trail, so that override data becomes the fuel that makes the system smarter.

---

## Friday of Week 9, the Last Afternoon Before the Pilot Starts

The prep meeting is breaking up. Kevin Doyle, packing his things, says as if in passing, "It goes live next week. I still want a big screen, up on the wall in the department. Backlog, where things stand, all at a glance. And when Grant Whitmore asks, I have something to show him."

You know this sentence. In Chapter 0 it was Kevin's first ask, "Ideally with a dashboard..." In Chapter 8 the "not this phase" list kept it out. This is the big screen's third appearance, and this time there is no way around it. Next Monday Kevin is the pilot's owner. Leave the wish hanging and sooner or later he will build a big screen of his own, one that is always greener, competing with the queue for the right to explain. When two screens disagree, nobody knows which one to believe.

This time you did not block it. You asked three questions, and the conversation is replayed in the second half of this chapter. First, the reasoning.

## Why This Is Hard: Four Organizational Things Stand Between Seeing and Acting

For an insight (one conclusion read out of the data) to become an action, it has to clear four organizational gates.

- Owner. Who does this piece of information belong to?
- Next action. What is the specific thing to do right now?
- Reason. Why should he trust this judgment?
- Capture. Where is it recorded that it was done or not done, and where does the next person pick up?

All four are organizational matters, not information matters. And the dashboard's design choice is to leave all four to the viewer to solve on his own, so the viewer chooses not to solve them. Do not blame the viewer for laziness. This is structure. The people who look usually have no power to act, and the people who can act are usually not looking. The screen is visible to everyone, so everyone can assume "whoever should act will act." Information present, responsibility absent.

Chapter 0 gave the user version of this judgment, the workflow claim, whose next action the system will change. This chapter is its system design version.

> **A system's value is not in what it knows. It is in whose next action it changes.**

By that standard a dashboard delivers "knowing," and clears none of the four gates. It is not useless. Watching trends and giving managers a sense of presence (Kevin's real need, see below) are both real uses. It has only one way to die, being treated as the deliverable meant to change front-line action.

## Prior Art, and What AI Changed

**The lean tradition. A kanban is a next action, not an information display.** A Toyota kanban card says who, fetch what, how many, deliver where. The card arrives, the action happens. The software industry took the cards and the swimlanes, and what it most often dropped was exactly this half. The action queue brings it back. Every row is a real kanban card.

The metrics tradition. Watch controllable inputs, not outputs on display. The controllable input metrics idea in *Working Backwards* splits metrics in two. Output metrics (revenue, total cycle time) are results and can only be watched. What today's action can change is the input metric (how early a missing document is found, chase response time). A big screen that shows only output metrics gives the action no handle, by definition.

What did AI change? One thing removed an old excuse, and one thing created a new necessity.

First, the cost of translating data into a suggested action collapsed. Stopping at display used to have a respectable reason. Translating "backlog is rising" into "chase these seven claims first" meant hard-coding rules for every kind of situation, too expensive for anyone to write. LLMs made that layer of translation cheap (the pattern selection in Chapter 10 does exactly this job). Stopping at display has had no excuse since.

Second, the decision trail went from virtue to necessity. Traditional systems keep logs for audit, written for the day someone might look. An AI system's trail has one more recipient, and it shows up every day. Each person's accept or override of each suggestion, plus the reason, is the only continuous right-or-wrong signal produced outside eval, and it flows back into rule iteration and golden cases (Chapter 11). An AI system without a trail is pouring out its most expensive training data on the spot.

## Framework One: The Six-Level Action Integration Ladder

> **The action integration ladder measures how deeply a deliverable bites into the workflow, six levels from "can be seen" to "gets smarter."** Judge level by level, and stop at the first level you cannot produce evidence for.

Read only the first two columns to place yourself. The last two are for a closer look on review.

| Level | Gloss | Test for Standing Here | What the Next Level Costs |
|------|----------|------------|------------------|
| **visibility** | It can be seen | Data is aggregated and displayed, and someone looks at it | (Starting point) Just data and charts |
| **prioritization** | It is ranked | The ranking logic matches the users' real trade-offs (chase ≠ risk, Chapter 0) | One value judgment, what matters more and who gets to say |
| **recommendation** | It suggests | Every row gives a next action, and the reason can be challenged | Tacit knowledge, the suggestion logic eats front-line judgment (Chapters 6, 11) |
| **task creation** | It becomes a task | The suggestion lands on a named person, in the work entry point he already uses, with a status and a due date | Organizational ownership, owner negotiation + workflow embedding |
| **decision capture** | The decision is kept | Accept / override is recorded along with the reason | The front line's trust, willingness to put a real name on a decision (Chapter 12) |
| **closed loop** | The loop closes | Someone reviews the trail data on a cadence, and it has actually changed a rule or an eval | Operating cadence, a review mechanism that stays alive long term (Chapter 18 takes it over) |

The queue at Anchor & Helm stands at level five during the pilot. The owner column, the Human Call column, and reason codes have been in Linda Marsh's team's work entry point since day one of the pilot. Level six has been cashed in only once, the review in the second half of this chapter that changed one line of a condition and added golden cases. One catch is not a cadence. Only once the review grows into a fixed mechanism does the queue qualify for level six, and that last cell of the table is handed to the next chapter.

Two rules for reading the table. First, most dashboards die at level one, and most "AI assistants" die at level three, with suggestions, no owner, no trail. Second, the higher you go, the less engineering and the more organization. The lower half can be reached by writing code. Every level of the upper half has to ask the organization for something.

This makes three ladders in the book. The outcome ladder measures how far a project has gotten (Chapter 1). The data fitness ladder measures whether a data source deserves to drive an action (Chapter 9). The action integration ladder measures how deeply a deliverable is embedded in the workflow. Each measures its own dimension. They do not swap and do not convert.

What the upper half asks of the organization, the internal reader can get, with a shortcut outsiders do not have. Level four stalls on owner negotiation because the person writing code has no authority to claim responsibility on someone else's behalf. You are inside the company, and you can push directly to change the SOP. Write "high-priority claims in the queue are handled by the on-duty team lead the same day" into the claims operations work standard, and level four drops from an organizational negotiation to a document revision, through the existing standards revision process, signed off by the business side's supervisor, not you. Institutional anchoring is the biggest lever in the internal reader's hands (Chapter 21).

On the same stretch of ladder, being internal also adds a scheduling dependency. Level four requires the suggestion to appear in the work entry point he already uses, and inside a company that entry point is often the corporate portal or the core system, and the people who change those are the platform team, not you. You need two things from them, a slot on the portal, and one release window of the core system that carries your module. Both come on the platform team's own iteration schedule, usually counted in quarters, so ask one iteration cycle before your launch date. Do not wait until the pilot is running to remember.

The level six review cadence is actually easier to keep alive long term from the inside. An external deliverer is gone by the exit date, and the review cadence leaves with him. You are still here. You can hang the action on a regular meeting the business side already holds, making it a line on the agenda rather than an extra step someone has to remember. Once it hangs there, the review's owner is whoever chairs that meeting.

## Framework Two: Queue Design Patterns

Turn the upper half of the ladder into a table and you have the action queue, the productionized version of the Chapter 0 two-hour prototype ([Template 0.3](../appendices/template-00-field-mvp-pack.md)), with every column able to state its origin.

**Column structure = the projection of the four layers of the decision rights boundary (Chapter 8).**

| Decision Rights Layer | Columns in the Queue | Who Is Responsible |
|----------|-----------|--------|
| Sense | Claim ID, reason stuck, missing item, days waiting, risk signal, status-in-doubt flag | AI summarizes facts |
| Advise | Suggested priority, suggested next action, reason | AI stops here |
| Act | Owner, Human Call | People take over here. Without confirmation the system takes no action |
| Decide | No columns on the table for this layer | The payout red line. The table has no columns for this layer, and the blank itself is the red line (Chapter 8) |

**Three columns = the final form of the three oversight questions (Chapter 12).** The three questions. Is there time to look? The ability to judge? The authority to stop it? They land on the queue as three things. The Human Call column. If she says no, does it count? It counts. That is authority. The reason column. The information for judging right or wrong is in the same row. That is ability. Risk ranking plus a daily volume cap, with the number of rows entering human view derived backward from the review time budget. That is time, and it lives in the suggested priority column, which keeps the daily count within budget. Oversight ends up as three columns on a table. The boxes on the flowchart are only its shadow.

**Trail schema = the answer to that question from Chapter 9.** "Do fields written back by AI count as truth?" No, and they must never get the chance to. The schema (the field structure of the trail table) cuts cleanly, with four rules.

- Suggestions and facts are stored in separate tables. The fact table (the merged view and source system fields) records only the world and what people did.
- The suggestion table is append-only, never updated. Not one word of AI output is written back to the source.
- Every suggestion gets one trail row, matching the six decision trail fields of Chapter 12 item for item. The six are input snapshot and rule/model version, suggestion and reason, Human Call with the decider's real name, and timestamp.
- On override, one more field, a reason code, a few enumerated values plus an optional note, chosen in two seconds. Anchor & Helm's version has six. Risk judgment differs, priority judgment differs, information outdated, already handled offline, suggested action not feasible, other. The reason code is the easiest to skip and the one that must not be skipped. It is the entrance to level six.

## At Anchor & Helm: The Big Screen, the Fourteen Steps, and the Decision Trail's First Catch

### The Big Screen, Translated Live

Replay the three questions from Friday of week 9.

"Kevin, the big screen is up. You see the auto exceptions backlog rising. Then what?"

"Have the team lead handle it."

"How does it get to the team lead? Do you call her, or is she watching the screen too?"

"The system could alert her."

"The alert arrives. How does she know which one to handle first?"

Kevin laughed. "You are describing that queue of yours."

Three questions in, the big screen ask took itself apart. For a backlog number to become an action, there has to be an owner (the team lead), a next step (which claim to move first), and a basis (the reason). The queue has all three, and they already live in Linda's team's work entry point. What the big screen wanted to do, the queue's first four levels have done. The three questions are a field variant of Chapter 6's three-layer probing method. There it chases expert judgment, here it chases the action chain behind an ask, the same craft.

The conversation did not end there. Kevin's ask had one real core left. He wants to know the system is being managed. To have the numbers in his head, and an answer when Grant asks. That need is entirely legitimate, and meeting it takes no big screen. Three things, all much cheaper, are enough.

1. **A rollup view**, a page of numbers summed by team, line of business, and aging, where every number clicks through to the queue itself. It is only ever an entrance to the queue, never a parallel screen (not the same thing as the merged view in Chapter 9's data layer, one faces up, the other faces down).
2. **Exception escalation rules**. Queue aging past a threshold, an unsafe interception event, a lengthening status-in-doubt list. Three kinds of signal escalate to Kevin automatically, and the rest of the time nothing bothers him.

3. **A weekly report**, one page watching the North Star and the process metrics (the metric tree in Chapter 18 gives it a formal skeleton).

Kevin listened and said, "Fine, better than a big screen. A big screen I have to watch myself. This one comes to me." He may not have realized the weight of that sentence. "It comes to me" is the whole difference between visibility and task creation.

### The Fourteen Steps Revisited, Which the Queue Eats and Which It Leaves

The fourteen real steps counted from a folding stool in Chapter 6 are now the map of the queue's embedding points. Before the pilot starts, you and Linda rule on every step again. Absorb, transform, or keep?

| Original Step (Chapter 6's Fourteen) | Where It Goes |
|--------------------------|------|
| 1 scan new claims / 2 enter into Excel / 3 sort today's order by color | **Absorbed**. Claims enter the queue automatically, risk ranking replaces the color codes |
| 5 search the inbox for documents | **Absorbed**. The inbox extraction signal prompts "documents arrived" |
| 13 Tuesday and Thursday filter of claims over seven days, chase in the group chat | **Absorbed**. Queue aging escalates automatically. Two manual filters a week become one automatic watch every day |
| 4 check the document list | **Transformed**. The system pre-generates the missing list, a person reviews it (errors and omissions are concern class, Chapter 11) |
| 6 attach to the system / 8 send chase email | **Transformed**. The system gives the lead and drafts the text. Attaching and sending are done by a person, and the red line of no automatic outbound messages still stands (Chapter 0) |
| 9 amount scan / 11 flag risk red | **Transformed**. Five rules + the long tail suggest a red flag and give a reason, and the final call goes through the Human Call column. The word or two only the team understood, written beside the risk column in step 11 of Chapter 6, became the ancestor of the reason code |
| 12 change status | **Transformed**. The Human Call is captured in the trail automatically. Writing back to the core system is still a ten-minute daily operating discipline (Chapter 9, owner Kevin) |
| 7 / 10 call the surveyor | **Kept**. Judgment and relationships, the system does not touch them |
| 14 back up Excel before leaving | **Kept**. Linda still backs up. The day she stops on her own is the true measure of trust (Chapter 21) |

Five steps absorbed, six transformed, three kept. Everything absorbed is information hauling. Everything kept is judgment and relationships. That is the workflow projection of Chapter 0's "AI does the grunt work. People make the calls." Excel is not retired. In the early pilot it is still the source of truth for claim status (Chapter 9). Only after the week 13 retest passes does the merged view stop deferring to it, and the three columns she added to Excel herself (actual status, chase count, risk mark, Chapter 6) move into the queue as the trail. The warning that "the system will kill its own source of truth with its own hands" is guarded during the pilot by the status-in-doubt list.

### Week 13, the Decision Trail's First Catch

At the end of pilot week 3 (Monday of project week 13), with the cost scare just put out (Chapter 16), you review three weeks of decision trail for the first time. Overall override rate, somewhere in the teens. Split by suggestion category, one thorn jumps out. High-priority suggestions triggered by "prior claim linkage" were overridden by Linda's team 78% of the time. Ten times the system said "risky, escalate for review," eight times it was pushed back.

The reason code distribution saved you half a day. Of the 78%, the great majority picked "risk judgment differs," and the notes kept repeating the same phrase, repair shop filing for the customer. Two hours of tracing back. Annotation guide section 4.2 (Chapter 11) had two layers. A repeated phone number counts as a linkage signal, but a repair shop filing on behalf of customers is an exception scenario, and the same number reporting for different customers is not high risk. In implementation the first layer made it into code, and the exception line was missed. So every repair shop that used its own number to file for customers was treated as a fraud ring.

Why did eval not catch it? Of the fifty golden cases, only one had this shape, and it happened to overlap with other risk signals, so "high priority" counted as correct. Eval was not wrong. The ruler was not bent. This material was never put on it.

> **Override data is the last net for the errors eval cannot catch.**

The fix is one line of a condition. Claims with the wrong shape go into the golden cases, and "incidents go onto the ruler" becomes a fixed process in Chapter 18. The mechanism deserves the record more than the fix. This error set off no alarm, drew no customer complaint, and showed on no monitoring chart. It was fished out by Linda's team's two-second reason codes. Victor Reyes read the page of analysis and replied with one line, "The trail caught something live for the first time. That week on constraint engineering paid for itself."

## Failure Modes

**1. Insight without action, delivering at level one.** The project closes with "the management cockpit is live," and three months later nobody opens it. The dashboard is a conspiracy of supply and demand. The reporting chain wants "presentable progress," the engineering side wants "a deliverable nobody is accountable for" (a display cannot be wrong, a suggestion can), and its success metric can always be made positive.

**2. Recommendation without owner, suggestions left hanging.** The system generates dozens of "worth attention" items a day, every one reasonable, nobody claims them. Assigning an owner is an organizational negotiation, not an engineering task. The person writing code has no authority to claim responsibility on someone else's behalf, so the owner column defaults to blank, and a blank is painless in a demo (the presenter is the temporary owner). A suggestion with no responsible person is a decorated insight, not a suggestion. The owner column's legitimacy comes from the SOP and job responsibilities, not from the system and not from you.

The next four are pits you fall into after the queue is up.

**3. Five tools stitched into one workflow.** Look in system A, act in system B, record in spreadsheet C, ask for the reason in group chat D. Each existing system has its own owner and its own cost of change, and "open a new interface" is always cheaper than "embed in the old entry point." The cost shifts from the project to the user, and every system switch drops usage by half. One test. How many systems does completing one suggestion touch? More than two and you are bleeding users.

**4. Alert fatigue, everything important equals nothing important.** Escalation rules keep getting added, the manager receives 40 "important alerts" a day, and from week 3 on he swipes them all away. Same structure as the scope creep of Chapter 8. Everyone has the power to add an entry to "important," nobody has the power to remove one. Adding one is free for the proposer, and the recipient pays the whole cost. The fix is a budget. First set how many the recipient is willing to look at per day (the time question of the three), then derive the escalation thresholds backward.

**5. Not recording the override reason, the loop breaks at the last link.** The trail table has accept/override and no why. For the front line, writing the reason is pure expense, and the benefit goes to the system. Without design, the default is nobody writes. A free-text box equals forcing the front line to give up writing. Without reason codes, 78% tells you only that the system is not trusted, not which rule is wrong.

**6. Stopping at level five, a trail nobody reviews.** Reason codes get filled in for months, and the trail table is never opened once. The front line paid the cost as designed, and nobody is at the receiving end. Review needs an owner and a cadence, neither of which writing code can produce, so it is the easiest thing to postpone indefinitely after launch. Anchor & Helm's first catch came from the act of reviewing, not from the trail table's existence. The test. Ask on what date the trail last changed a rule or the golden cases. No date, and the ladder stops at level five.

!!! note "Frontier Sketch: The Ladder Is Being Climbed"
    The act layer will not stay empty forever. A team building autonomous software engineering agents shared one test in 2026 (paraphrased). How long an agent can run unattended in a given step depends on the density of deterministic checks. The denser the loops that settle right or wrong on the spot, linters (code checkers), type checks, automated tests, the farther an agent goes without a human stepping in, and their internal processes with the clearest error shapes are already fully autonomous. This is the same principle as "put the LLM where its output can be checked" (Chapter 10). The upper half of the ladder is paved with verification loops, not with smarter models. The two forms of evidence for moving up are in Chapter 8, and Anchor & Helm's first move up is in Chapter 22.

## Next Monday

1. Put the last dashboard you delivered on the six-level ladder, and place it with one question. "Who changed an action last week because of it?" No name, and it is at level one.
2. Pick the metric you display most often and run the three-question translation. You see the change, then what? Who handles it? How does he know which to handle first? Write the answers as three items, owner, next action, reason. If you cannot fill all three, what you delivered is insight.
3. Check whether your system records override reasons. If not, add reason codes this week. No more than seven values, plus an optional note ([Template 17.2](../appendices/template-17-action-queue.md)).
4. If you already have a trail, split the override rate by suggestion category once, and pick the category with the highest override rate to trace back the rule implementation. Odds are an error eval never caught is waiting for you.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 17 Next Monday actions. First run python3 templates/action-queue/run_report.py
with the built-in sample to show me an override weekly report, then open schema.sql, reason-codes.json, and weekly-override-report.sql and explain each one.
Then I will name the metric displayed most often on the dashboard I delivered recently. You ask only the three questions, you see the change then what, who handles it,
how does he know which to handle first, and the three answers are mine to write. The reason code values are mine to define, no more than seven, and you check the count and mutual exclusivity.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The six-level action integration ladder (visibility → prioritization → recommendation → task creation → decision capture → closed loop; the higher you go, the less engineering and the more organization); queue design patterns (column structure = the projection of the four layers of the decision rights boundary; three columns = the final form of the three oversight questions; the six decision trail fields + reason code, suggestions and facts stored separately)
- **Templates.** [Template 17](../appendices/template-17-action-queue.md), Action Queue Design Patterns, Decision Trail Schema, Before/After Workflow Map
- **Key judgments**
  - "A system's value is not in what it knows. It is in whose next action it changes."
  - "A dashboard leaves the four organizational things to the viewer to solve on his own, so the viewer chooses not to solve them."
  - "Override data is the last net for the errors eval cannot catch."
  - "Everything absorbed is information hauling. Everything kept is judgment and relationships."
