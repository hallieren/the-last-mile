# Building and running at L2: co-build, the running budget, the action queue

**Load this reference when:** your team writes all the code and the receiving side watches; the bill arrived and someone asks "is this number normal"; P95 is over the line, there is no fallback, the LLM went down and the queue went blank; the owner says "I still want a big screen" or a dashboard nobody opens is called the deliverable (L2, production).

Source: chapters 15, 16, 17 (`docs/chapters/ch15-cobuild.md`, `docs/chapters/ch16-production-engineering.md`, `docs/chapters/ch17-dashboard-to-queue.md`); templates 15, 16, 17 (`docs/appendices/template-15-cobuild.md`, `docs/appendices/template-16-production-readiness.md`, `docs/appendices/template-17-action-queue.md`); `repo/templates/cobuild/*.md`, `repo/templates/action-queue/schema.sql`, `repo/templates/action-queue/reason-codes.json`.

## Contents

Decisions, in three parts. Co-build: identity not skill · the four clauses · the explain-it questions · three shapes of receiving side · signing, cost, permissions, enforcement · rotating release and health numbers. Running budget: the four ledgers · one owner per ledger · minimum observability set · degradation · cost and retry moves · readiness rules. Action queue: the four organizational things · the six-level ladder · columns from the decision rights layers · trail schema · reason codes and override rate · translating the big screen · absorb / transform / keep. Procedures: sign the co-build agreement · run a rotating release · stand up the running budget · run a degradation drill · design the queue · weekly override review. Detectors. Key judgments. Templates. Vendor seat.

## Decisions

### Co-build

**Treat silence from the co-build engineers as identity, not skill, and design their place to win.** Assigned tasks done and not one step further is the rational strategy of someone whose appraisal sits on the business line while the project sits under your name, and who fears he is training his own replacement. Three things must be designed, none happens on its own: code ownership (an asset in their name), skill growth (capability they take with them), internal visibility (their supervisor sees their names). What gets replaced is writing code to a spec; what cannot be replaced is the person who knows why the code is written this way and where to start when it breaks at midnight, so put their place to win on the latter.

**Owner says no one can be spared → offer the backward-staffing trade, not an exemption.** Agents now do the scaffolding, boilerplate and test cases, so "no capacity" no longer buys your team the whole build. Put the receiving side's weekly hours in writing and name the day-job reshuffle (whose existing work gives up the hours, in which week); no written answer, do not sign the co-build agreement. What co-build transfers is the ability to understand and evolve code; the code keeps getting cheaper, the people who can evolve it more expensive.

**Sign the four clauses on one page, both sides, in force before the pilot starts.**

| # | Clause | Rule | What it prevents |
|---|---|---|---|
| 1 | Code ownership goes to the receiving side | From day one all code sits in modules under the receiving side's name. Ownership counts only when it lands in three places, CODEOWNERS, merge rights, the oncall rotation. CI and release run on their existing process, no second one built. You commit as a collaborator | The "your project" story; changing the owner only on handoff day |
| 2 | Backward staffing | Split work by "whoever maintains it after handoff leads the writing now", not "who is faster now". Leading the writing is not writing alone: the lead writer is accountable, can explain it and decides merges; the other side pairs and reviews | All core work to your team, the receiving side left with chores |
| 3 | If you cannot say it, do not merge it | AI-generated code is reviewed by the maintaining side and explained by the submitter face to face through the three explain-it questions. Binds both sides: code you generated with an agent is explained to them too | Black boxes that run and nobody can change |
| 4 | Biweekly rotating release | Every two weeks (rule), 30–45 minutes (rule), a receiving-side engineer, not you, demonstrates progress to the receiving-side owner; first one inside the pilot's second week (rule) | Co-build engineers invisible inside the organization |

Red line under clause one: the day the AI team holds gatekeeping rights for the long run is the day permanent ops begins. There is no option of "develop on our side first and migrate at handoff".

**Test the explanation, not the code.** A rejection does not mean the code failed, it means the explanation failed. Before resubmitting, the submitter must have had his hands on it (rewriting, simplifying, adding tests all count); "memorize it and say it again" is not accepted. Run the three questions on your own next PR first.

| Question | Passing answer | Failing signal |
|---|---|---|
| Why is it written this way? | He states the alternatives and why he did not pick them | "That is how it came out" / "It runs" / "That is how the agent wrote it" |
| Where can it go wrong, and how would you find out? | He points to the specific failure path and the matching log, alert or backstop | "It should not go wrong" / "The tests all passed" |
| If it has to change, where do you start? | He states the change point and how far it reaches | A long scroll through the code hunting for the entry point |

**Name the shape of the receiving side before signing; the clauses change with it.**

| Receiving side | Who the counterpart is | How the four clauses change |
|---|---|---|
| One team, your team keeps the system | The business side's operations staff | Clauses one and two spin free. Three and four apply to the operations staff, and what gets explained is rules, thresholds and exception handling, not code |
| A platform team | They keep general capability, not your business modules | Clause two's "whoever owns it later" is answered "not us". Settle before signing which modules go to the platform and which stay on the business line. Cannot settle it, do not sign |
| The business line's own IT | Appraised on the business line | All four as written |

**Time the signing, the graduation date, the cost and the permissions.**

| Predicate | Ruling | Action |
|---|---|---|
| The pilot has been called and has not started | The only signing window. Later, the do-it-all habit has formed; earlier, the staffing sheet has no factual basis | Sign this week |
| Signing day | Nobody inside a company sets the handoff date for you | Write the expected graduation date on the agreement, the week all five self-sufficiency tests (Show Me) pass. Without it the apprenticeship degrades into pairing forever |
| "Whose account does their time come out of?" | A project has no ledger inside a company; the answer must land in two things | The owner commits weekly hours in writing as their supervisor, a commitment clause of the same rank as the user commitment, chargeback where it exists; plus one line in each engineer's quarterly objectives, lead writing and gatekeeping on these modules |
| "Who carries their own day job?" | Booking the time settles the account, not the work; evenings are not an answer | The owner reshuffles in writing: their schedule gives up the matching hours, who takes them and in which week goes into the same agreement. The rotating release lets him see every two weeks what the reshuffle buys, so it does not slide back |
| Repo write access will not clear the security gate | What gives way is never ownership | Fallback ladder: read-only on the whole repo, write access only on the modules named in the agreement, the merge pressed by someone from the receiving side. If restricted write is still refused, commit on a restricted branch inside the same repo; CODEOWNERS and CI stay on the receiving side, so handoff day still has no "changing the owner" |
| The first rejection under clause three has happened | Hand over enforcement, not just work | From that week merges on that module are gatekept by the receiving side's senior engineer; you are no longer its gatekeeper |
| No account to revoke, no exit date (internal) | Headcount and the ledger do what account revocation does outside | Two substitutes, used from signing day, not handoff day: next year's staffing budget reserves no ops headcount for this system; the PMO transfer ledger's owner column for these modules carries a real name from the receiving side |

**Use the three internal shortcuts as actions.** Open a PR against the company-wide PR template adding a field for the AI-generated share and the name of the person who explained it (change it once, every project benefits). Put both engineers on the internal tech talk series as the rotating release stage. Ask the owner to write the rotating release demo into a line of their quarterly appraisal, so visibility walks out of the meeting room into the appraisal form.

**Fill the backward staffing sheet in the rule's order.** Columns: Module / Maintainer After Handoff / Where the Maintainer Is Appraised / Lead Writer / Pairing-Review Side / Current Gatekeeping Rights and Transfer Condition. Fill the second column first, then work backward to the lead writer. A row where maintainer and appraisal disagree is a hidden accountability vacuum and needs a written convergence plan. A module beyond the receiving side today still reads "maintainer, the receiving side (longer term)"; the pairing on that row is the convergence path. Every row states its transfer condition, e.g. "handed over after two consecutive reviews of that module with no rejection" (rule); before handoff day gatekeeping on every row sits with the receiving side.

**Run the rotating release to its agenda, and read three health numbers every beat.** 0:00–0:05 reconcile last beat's commitments with reasons for anything unfinished; 0:05–0:20 demonstration on real data, "what it can do" and "what a wrong one looks like and how it gets caught", a release that shows only successes does not pass; 0:20–0:30 owner Q&A, your team adds only when named and never answers for them; 0:30–0:40 the presenter states the goal for the next two weeks; 0:40–0:45 cadence sheet update. Every beat marks one transfer action (gatekeeping rights of a module handed over; a production issue handled alone; lead-writer rights rotated; the receiving side leads the technical retrospective); progress is read from items of power handed over, not training sessions held. Health numbers: the receiving side's share of commits (must rise); modules where your team holds gatekeeping rights (must fall); questions at the release your team answers for them (must trend to zero). Any one running the wrong way two beats running (rule) sends you to Detectors.

### Running budget

**Design the running budget like a feature, before launch.** Traditional "launch it, then hand it to ops" rests on three premises an AI system breaks: cost grows linearly with calls and no marginal cost trends to zero (a stuffed context pays in latency and diluted attention even with provider caching); the latency distribution has a long tail that lands on the business rhythm, P50 looks good and P95 kills you; quality drifts silently with no exception stack and no alert, the first to notice is a front-line hunch. Uptime, error codes and resource usage are blind to all three. The budget holds a place in the architecture, the schedule and a vote at the launch gate.

**Stand up four ledgers, one budget line, one action on breach, one named owner each.**

| Ledger | Records | Budget line | Action on breach |
|---|---|---|---|
| Cost | Cap on cost per item, plus the monthly total | Worked back from business value: what the labor hours one item saves are worth, system cost allowed only a fraction of it. Never from last month's bill | Cost review the same day, not at month end |
| Latency | The P95 cap, not the average, with the peak window on its own line | Worked back from the user's rhythm: from opening the queue to being able to work, how many seconds can they wait | Degrade, or extend precomputation |
| Error | Per-category error rate caps | The eval spec threshold table carried over as is, build nothing new: unsafe 0 (rule), concern ≤ 10% (rule), useless ≤ 20% with the trend not rising (rule), measured by online sampling | Rework; a kill criteria trigger means pause |
| Degradation | A fallback for every AI dependency point | "The drill passed": really pull the dependency and the core process still runs | A dependency point with no fallback does not launch |

**Name exactly one first-line owner per ledger.** The test is whose budget or whose daily actions a breach hits directly; everyone else related is a countersignature. The owner need not be the fixer, but the breach alert lands in one inbox. Two names is the same as no name. Bind each ledger to a fixed moment when its numbers are read; anyone may read them is the same as nobody reads them.

**Make the account separable before opening the cost ledger.** Calls mixed into a shared gateway or one cloud account show nothing at month end. FinOps tagging or a showback line for this system is the precondition, not a bonus. Split usage by system first, then talk about moving it.

**Hand the budget to the business side, or accept permanent ops.** The business side is a real owner only once it takes the budget; whoever holds the budget holds the priorities. If the money stays on your project funds, your cost center feeds it forever and the team that feeds it becomes its ops team. The running budget sheet becomes the budget account at handoff, renamed row by row.

**Build the minimum observability set, three pieces; missing one, a ledger cannot be kept.**

| Piece | What it is | Rule |
|---|---|---|
| End-to-end trace | Any single suggestion replayable: input snapshot, what was retrieved, prompt and model version, which rules hit, final display | A trace is not the decision trail. The six trail fields are an audit commitment, "who decided what"; the trace is engineering replay, "why does this suggestion look this way". One chain, two readings; build both |
| Online eval sampling | Golden cases replayed on a cadence, plus a share of production output spot-checked by human review, booked by the eval spec categories | When people cannot keep up a model screens first, but its verdicts count only once calibrated on a human-annotated sample with disagreement read per category. On the unsafe class the model may only report, never release |
| Drift signals | Sudden-change alerts on the input distribution (mix, amounts, types) and on the override rate | When the override rate moves, the input or the model moved first |

Online eval sampling and drift alerts launch at the same rank as uptime monitoring, not in phase two.

**Degrade by cutting intelligence to protect the process.** Traditional degradation cuts features to protect the core. The dumbest thing that works, the rules layer, is the floor in normal times and the fallback when supply is cut; it is an asset, not scaffolding, and needs an owner, tests and updates as business rules change. "System under maintenance, please try again later" is not a fallback; a fallback runs the core process. "Expensive" is a failure shape alongside down and slow; write the cost-breach degradation (route to a smaller model, lower the sampling frequency, narrow the scope) in advance.

**Take the four cost moves in this order; they do not contribute equally.**

| Order | Move | What it cuts | Magnitude |
|---|---|---|---|
| 1 | Full recomputation to incremental (only items with a new event recomputed) | The number of calls | Largest |
| 2 | Static blocks (the manual, whole rule texts, piles of examples) out of the prompt into retrieval, two or three passages per call | The length of each call | Largest; changing the call path also has to clear the eval, discipline not ceremony |
| 3 | Cache extraction results for stable inputs; anything passing schema validation goes into the cache | Paying twice for the same input | Behind the first two |
| 4 | Long-tail items routed to a smaller model; the eval decides where the split goes | Price per call | Smallest, under a tenth of total savings (illustrative); gateway-style routing saves 10–20% of inference cost (illustrative) |

Combined, cost per item fell to 1/6 (illustrative). Set retry discipline by call cost: pulls keep three attempts with doubling intervals (rule); LLM calls get backoff plus a retry budget of at most two attempts per item (rule), over the limit the row goes to the "pending human" column. Latency moves: precompute the queue before the morning peak; make the refresh asynchronous, show the latest result at once with its timestamp, update in the background.

**Pass the readiness gate out loud.** Any "no" on the checklist is either fixed or accepted out loud at the escalation decision meeting with the accepting person written down; passing in silence is not passing. The cost instrument produces numbers daily, split by step; the month-end bill is a confirmation, never news. The degradation trigger is automatic, not somebody switching by hand at night. An alert that has never fired needs one firing manufactured for it; an alarm that does not sound is more dangerous than no alarm. Ownership items: budget account accepted in writing by the business owner; cost booking standard settled (chargeback / showback / not booked); one cross-department first-line owner per ledger; reconciliation cadence set as who, which day of the week, which page.

**Keep the sheets to their rules.** Running budget sheet columns: Ledger / Metric / Budget Line / Alert Line (ahead of the budget line, at 80% (rule)) / Current Value / Action on Breach / Ledger Owner. Not one error ledger row is newly invented; it and the eval spec threshold table reference each other. Current value is updated at each weekly reconciliation; two consecutive weeks blank (rule) means the observability set has a hole. The owner column takes a person, not a department; this sheet is the working ledger of the operating handoff. Degradation register columns: AI Dependency Point / Failure Shape (down / slow / expensive) / Fallback / What the User Sees / Trigger and How / Date Last Drilled / Owner.

### Action queue

**Clear four organizational gates or you delivered "knowing".** Owner (whose information is this), next action (what to do right now), reason (why trust it), capture (where is done or not done recorded, where does the next person pick up). All four are organizational, not informational; a dashboard leaves all four to the viewer, so the viewer chooses not to solve them. The people who look have no power to act, the people who act are not looking. A display cannot be wrong, a suggestion can, which is why dashboards get delivered.

**Place the deliverable on the six-level action integration ladder; stop at the first level with no evidence.**

| Level | Test for standing here | What the next level costs |
|---|---|---|
| 1 visibility | Data aggregated and displayed, someone looks | Just data and charts |
| 2 prioritization | Ranking logic matches users' real trade-offs (chase ≠ risk) | One value judgment: what matters more, who gets to say |
| 3 recommendation | Every row gives a next action and the reason can be challenged | Tacit knowledge; suggestion logic eats front-line judgment |
| 4 task creation | The suggestion lands on a named person, in the work entry point he already uses, with a status and a due date | Organizational ownership: owner negotiation plus workflow embedding |
| 5 decision capture | Accept / override recorded with the reason | The front line's trust, a real name on a decision |
| 6 closed loop | Someone reviews the trail on a cadence and it has actually changed a rule or an eval | An operating cadence that stays alive |

Two reading rules: most dashboards die at level one, most "AI assistants" at level three (suggestions, no owner, no trail); the lower half is reached by writing code, every level of the upper half asks the organization for something. One catch is not a cadence; the queue qualifies for level six only once the review is a fixed mechanism. The three ladders (outcome, data fitness, action integration) never convert.

**Derive the columns from the decision rights layers; the decide layer gets no column.** Sense (item ID, reason stuck, missing item, days waiting, risk signal, status-in-doubt flag): AI summarizes facts. Advise (suggested priority, suggested next action, reason): AI stops here. Act (owner, Human Call): people take over; without confirmation the system takes no action. Decide: no columns; the blank itself is the red line, a "suggested payout" column must not exist. Design points: risk signals trace to a source rule or model version; aging counted in business days, not calendar days; the status-in-doubt flag lights when the source system and the source of truth disagree; the suggested next action starts with a verb and is executable, outbound sending actions produce a draft only; the owner is a named person with the basis for assignment written down, one of SOP clause / job responsibility / supervisor assignment, and a blank owner is a decorated insight, not a suggestion.

**Read three columns as the three oversight questions.** Human Call = authority (if she says no, it counts). Reason = ability (the information for judging right or wrong is in the same row). Risk ranking plus a daily volume cap, rows entering human view derived backward from the review time budget = time. Oversight ends up as three columns on a table; the boxes on the flowchart are only its shadow.

**Cut the trail schema by four rules.** Suggestions and facts in separate tables; the fact table records only the world and what people did. The suggestion table is append-only, never updated; not one word of AI output is written back to a source field. Every suggestion gets one trail row matching the six decision trail fields (input snapshot, rule/model version, suggestion, reason, Human Call with the decider's real name, timestamp). On override, one more field, a reason code, enumerated values plus an optional note, chosen in two seconds; it is the entrance to level six.

**Enumerate reason codes, ≤ 7 plus other (rule), in the front line's own language.** Sample set and what each feeds: risk judgment differs (the word repeating in the notes is the name of the next rule); priority judgment differs (the ranking logic); information outdated (data lag, feeds the fitness retest); already handled offline (a workflow escape signal, the action happened outside the system); suggested action not feasible (the action set); other (note required; other above 30% (rule) means the values need revision). A free-text box equals forcing the front line to give up writing.

**Use the override rate as the instrument the eval cannot be.** Override data is the last net for errors the eval never saw. Split it by suggestion category, never read the overall figure; an overall rate in the teens hid one category at 78% (illustrative), and the reason code distribution located a missed exception line in a rule's implementation in two hours (illustrative). The golden cases held one case of that shape; the ruler was not bent, this material was never put on it. Claims with the wrong shape go into the golden cases.

**Translate a big-screen ask with three questions, then meet the real need with three cheaper things.** "You see the number rise. Then what?" / "How does it get to the person who acts?" / "The alert arrives. How does he know which one to handle first?" The ask takes itself apart into owner, next step, basis, which the queue already has. The real need is to know the system is being managed and to have an answer when the sponsor asks. Give: a rollup view (numbers by team, line and aging, every number clicks through to the queue, an entrance to the queue, never a parallel screen); exception escalation rules (≤ 3 signal categories (rule), e.g. aging past a threshold, an unsafe interception, a lengthening status-in-doubt list, thresholds derived backward from how many the recipient will look at per day); a weekly one-pager on the North Star and process metrics. The tell that it worked: "a big screen I have to watch myself; this one comes to me." "It comes to me" is the whole difference between visibility and task creation. A wish left hanging becomes a second screen competing with the queue for the right to explain.

**Rule on every real workflow step as absorbed, transformed or kept before designing the embedding.** Absorbed = pure information hauling (find, copy, move, watch). Transformed = hauling plus human confirmation; the system does the first half, the person the second. Kept = judgment and relationships (persuade, coordinate, decide). Three checks: a judgment absorbed means the decision rights boundary is drawn wrong; the person's second half of every transformed step lands on a queue column (Human Call / review), not in another system; the kept steps are written down explicitly, "what the system does not touch" is the boundary promise to the front line.

**Pull the internal levers on the upper half.** Level four's owner negotiation collapses into a document revision: write "high-priority rows in the queue are handled by the on-duty team lead the same day" into the work standard through the existing standards revision process, signed off by the business side's supervisor, not you; institutional anchoring is the biggest lever in your hands. Level four also adds a scheduling dependency: the work entry point is the portal or the core system owned by the platform team, so ask for the portal slot and the release window one iteration cycle before your launch date (rule). Level six's review hangs on a regular meeting the business side already holds; its owner is whoever chairs that meeting.

## Procedures

**Sign the co-build agreement (the days after the pilot is called, before it starts).**
1. Name the shape of the receiving side; for a platform team, settle which modules go where first or do not sign.
2. Fill the backward staffing sheet, "maintainer after handoff" first; write a convergence plan on every row where maintainer, appraisal or lead writer disagree.
3. Fill clause one's checklist: CODEOWNERS, merge rights, oncall, CI and release on their existing process, collaborator accounts for your team, an exception list item by item with reasons.
4. Get the owner's two cost answers in writing, weekly hours with the accounting method (booked to the project / chargeback / quarterly objectives, pick one) and the reshuffle of their day job.
5. Write the expected graduation date, the week all five Show Me tests pass.
6. Book the first rotating release inside the pilot's second week and put the release demo into the engineers' quarterly appraisal line.
7. Change CODEOWNERS this week if it all sits with you; the later, the more expensive.

**Run a rotating release (every two weeks (rule)).**
1. Presenter is a receiving-side engineer in rotation; standing audience is the receiving-side owner (required) plus all co-build members.
2. Follow the five-segment agenda; a demonstration with no wrong output shown does not pass.
3. Sit in the audience; add only when named; never answer for them.
4. Record this beat's transfer action on the cadence sheet and update the three health numbers.
5. At the last beat, the receiving side demonstrates the whole system to the owner and the handoff checklist has no new items.

**Stand up the running budget (before the launch gate).**
1. Make the account separable, FinOps tag or showback line, and work out cost per item once (last month's bill ÷ items handled); take it to the system owner and ask "do you know this number".
2. Set the four budget lines from value and rhythm, the error rows copied from the eval spec threshold table, the alert line at 80% (rule).
3. Name one first-line owner per ledger by the breach test; write countersignatures separately; set the reading moment (who, which day, which page).
4. Build the trace, the online eval sampling cadence and the drift alerts; manufacture one firing for every alert.
5. Open the largest prompt, move static blocks into retrieval or a cache, make recomputation incremental, set retry budgets by call cost, precompute before the peak; re-clear the eval after any call path change.
6. Walk the readiness checklist at the escalation decision meeting; every "no" is fixed or accepted out loud with a name.
7. Write into the sheet's footer that at handoff this page becomes the business line's budget account.

**Run a degradation drill (before launch, every 90 days (rule), and after any model swap or call path change (rule)).**
1. Register the dependency point with its failure shape, fallback, what the user sees, trigger and owner.
2. Really cut the dependency, on production data, with real users present; hang it on the company's annual disaster recovery or business continuity drill by adding one line (which dependency, what it falls back to, who watches).
3. Pass condition one: review carried on through the half hour. Pass condition two: asked afterward "did you notice", most say no.
4. A failed drill blocks changes to that dependency point until the drill is made up; record the date.

**Design the queue (before the pilot starts).**
1. Lay the columns by layer, sense / advise / act, and leave decide with no column.
2. Divide daily rows by review minutes in front of the reviewer; set the daily volume cap and derive escalation thresholds backward.
3. Build the trail as two tables, fact and suggestion, append-only; enumerate reason codes with the front line, ≤ 7 plus other.
4. Rule on every real step absorbed / transformed / kept with the actual user; run the three checks.
5. Write the owner rule into the SOP through the standards process; request the portal slot and release window one iteration cycle early.
6. Answer the big-screen ask with the rollup view, ≤ 3 escalation signals and the weekly one-pager.

**Run the weekly override review (level six, hung on an existing business-side meeting).**
1. Split the override rate by suggestion category; read the reason code distribution and the share of other.
2. Trace back the rule implementation for the highest category.
3. Add rows with the wrong shape to the golden cases; record the date the trail changed a rule or a case.
4. Other above 30% (rule) → revise the code values with the front line.

## Detectors

- If the co-build engineers' share of commits has been zero two weeks running (rule), you are already doing it all; on handoff day the code is complete and the capability is zero.
- If the core modules are "too critical, we take those first" and they get documents, test data and page styles, you are using them as cheap labor and confirming their deepest fear.
- If "tests passed, merge it" is the bar, black boxes are accumulating; CI verifies running, not understanding; the first change request after handoff freezes the system.
- If three months in you are still the merge gatekeeper on every module and you answer the owner's questions at the rotating release, co-build has turned into custody.
- "The code isn't wrong, why not merge it?": the code passes, the explanation does not; when it breaks at midnight the person woken is him, not the agent.
- If the modules' CODEOWNERS, oncall and merge rights all sit with you, every week you wait raises the price of changing them.
- Pull the LLM dependency in test for ten minutes; if the core process is not left, you have no degradation path and the rules layer was deleted as scaffolding.
- If the monitoring list is uptime, error codes and resource usage, an all-green dashboard is the most dangerous thing you own.
- If the month-end bill is the only cost monitoring, the feedback is thirty days late by nature and cost per item is on no engineer's panel.
- Ask any ledger owner "did it break a line last week"; no answer means that ledger is not running. A title in the owner column means nobody reads it.
- Whichever ledger you cannot put a name to is the address of your next incident.
- Ask "who changed an action last week because of it?"; no name and the deliverable is at level one.
- If the three-question translation cannot fill owner, next action and reason, what you delivered is insight.
- If completing one suggestion touches more than two systems, you are bleeding users; every switch halves usage.
- If the manager gets forty "important alerts" a day (illustrative) and swipes them away, nobody set the recipient's daily budget; add-entry rights are free to the proposer and the recipient pays.
- If override reasons go into a free-text box, the front line has been told to stop writing; an override rate of 78% (illustrative) then says only "not trusted", not which rule is wrong.
- Ask on what date the trail last changed a rule or the golden cases; no date and the ladder stops at level five.

## Key judgments

- "What stops co-build is identity, not skill. Give the co-build engineers a place where they can win."
- "If you cannot say it, do not merge it."
- "The test for staffing is 'whoever owns it later,' not 'whoever is faster now.'"
- "The running budget has to be designed like a feature."
- "Do not delete the dumbest thing that works. It is your degradation path."
- "A system 100% online does not mean it is still saying the right things."
- "A system's value is not in what it knows. It is in whose next action it changes."
- "Override data is the last net for the errors eval cannot catch."

## Templates

- `templates/queue-columns-and-trail.md` (main chain): column structure by layer, trail schema, reason code rules, before/after workflow map.
- Co-build agreement header, clause one checklist, backward staffing sheet, explain-it checks, rotating release agenda, cadence sheet: `docs/appendices/template-15-cobuild.md` §15.1–15.2; drop-in files in `repo/templates/cobuild/` (ownership checklist, PR template with the AI-share and explainer fields, collaborator access sample).
- Production readiness checklist, running budget sheet, degradation path register: `docs/appendices/template-16-production-readiness.md` §16.1–16.3.
- The error ledger copies the threshold table of `templates/eval-spec.md` (`docs/appendices/template-11-eval-spec.md`) §11.1.4; a breach pauses through `docs/appendices/template-14-stage-gates.md` kill criteria.
- `scripts/override_report.py` splits overrides by category and alarms on the other share; `repo/templates/action-queue/schema.sql` and `reason-codes.json` are the trail DDL and the sample enumeration.

## Vendor seat

Clause one is physical on the vendor side: code in the client's repo, an external collaborator account revoked on the exit date, so headcount and the transfer ledger inside do what account revocation does outside. The running budget and the action queue apply as is. A line in a contract is not a working mechanism.
