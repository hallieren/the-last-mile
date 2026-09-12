# Launch, adoption, handoff: the climb from L2 to L4

**Load this reference when:** the system is live and an error has reached a person, the sponsor wants the gain proved, the same few people are the only users, someone calls it a surveillance tool in a meeting or a team goes silent, or you hear "it doesn't run without you" and have to rule on whether you may step out of the daily.

Source: chapters 18, 20, 21, 22 (`docs/chapters/ch18-launch-and-metrics.md`, `ch20-resistance-as-signal.md`, `ch21-adoption-engineering.md`, `ch22-handoff.md`); templates 18, 20, 21, 22 (`docs/appendices/template-18-metric-tree.md`, `template-20-resistance-decoder.md`, `template-21-adoption-plan.md`, `template-22-handoff.md`); `repo/templates/metric-tree/metric-tree.md`, `repo/templates/handoff/checklist.yaml`.

The climb has three settlements and none of them is a date. L2 settles when the North Star shows a special cause signal and the first incident was handled by process. L3 settles when taking it away would hurt; between L2 and L3 lies nothing but organizational engineering. L4 settles when all five Show Me tests pass and the response window closes in writing. Your achievement is counted only at L3/L4.

## Contents

- Decisions: L2 launch and measure; L2 → L3 resistance; L2 → L3 adoption; L3 → L4 handoff
- Procedures: before launch; an error reaches a person; challenged in public; decoding silence; a usage curve drops; may I step out of the daily
- Detectors, Key judgments, Templates, Vendor seat

## Decisions

### L2, launch and measure: prove the gain, not the trend

Build the metric tree before launch. Three layers, every metric with an owner and an action; "a metric with no owner and no action is only scenery."

| Layer | Question it answers | Typical metrics | Action on deviation, examples |
|---|---|---|---|
| North Star (outcome) | Did the improvement happen | The charter North Star, weekly median on a run chart | Two consecutive points back above the baseline median → go through the process layer for the cause |
| Process (mechanism) | Why it happened, where the lever is | Queue aging; detection lead time; override rate split by suggestion category, no overall average; status-in-doubt list length | Over the line → claimed and cleared the same day; a sudden change in one category → trace that category's rule implementation and list version; continuous growth → re-check the daily cleanup discipline |
| Balancing (cost) | Did the improvement shift the cost | Complaint rate; reviewer overtime hours | Rising → check chase scripts and frequency; rising → check the queue's daily volume setting |

- Three rules. One North Star, from the charter, no better-looking one set up after launch. Every metric has an owner and an action, or delete the row. Balancing metrics on the same page as the outcome; "the victims of a shifted cost are usually not in the reporting meeting. Only the metric speaks for them." A balancing metric on a separate page is always "next time."
- Metric row columns: Layer | Metric | Definition and Measurement | Data Source | Baseline | Owner (a named person, not a department) | Owner's Reporting Line | Action on Deviation (who does what). Two to four process metrics, at least two balancing metrics (rule).
- If the owner does not report to you, put the whole tree on the business department's own weekly agenda and write the claiming actions into their team SOP. "An action written into the SOP is their job at review time. An action sitting in your email is only your request." Hang the run chart on the business line's existing review, not a meeting of your own.
- If you cannot write a balancing metric, ask "whom is this improvement most likely to shift its cost onto?"
- Baseline discipline. Built before launch from 8 weeks of history (rule), corrected claim by claim through reconciliation; pull it from the warehouse yourself, a median line is up the same day. Run chart kept continuously, every point on it, the median as the one reference line. Improvement claimed only on a special cause signal, six consecutive points on the same side of the median (rule). Common cause is the random rise and fall built into the system; special cause is a structural change. "A line drawn between two points gives you no trend, only an illusion of slope." Five points on one side is one short; say so.
- Not live yet → start collecting the baseline today. Live with no baseline → record from today and say so in the next report; an honest "no baseline" beats a fabricated comparison.
- Fairness spot check on the monitoring surface: override distribution by customer segment every quarter (rule), first check at the end of the first quarter after launch.
- When a resource commitment is offered on the spot, ask which kind it is: moving people is honored now, adding headcount queues for the annual review.

Write the incident runbook before the incident, like the kill criteria. Levels govern response speed; the four grades govern severity, a separate numbering.

| Level | Definition | Response |
|---|---|---|
| P1 | An unsafe-class error enters human view; being caught by a person does not downgrade it, what caught it was already the last line of defense | Same-day notice drafted within two hours (rule); retrospective within 48 hours (rule); incident case into the golden cases within 24 hours (rule) |
| P2 | Concern-class errors over threshold or in batches | Retrospective the same week (rule); trace rules and data sources |
| P3 | A rising trend in useless-class errors | Folded into the monthly retrospective |

- The same-day notice has three parts and the order cannot change: (1) the defense held, the interception mechanism worked as designed, then the error; (2) scope of impact, verified facts only, anything unverified is written as "being checked"; (3) root cause under investigation with a retrospective deadline. Drafted by you within two hours, issued the same day by the business owner, distribution drawn by how far the rumor can reach, wider inside a company. No individual named as responsible. The owner may edit; the one line you hold is the order. Move scope ahead of the defense and fact becomes spin. "The notice itself is a reliability deposit"; the promised deadline must be met.
- The four retrospective questions run in one order, model → rule → interaction → data; each layer is eliminated before the next, and the three eliminations are the evidence for the attribution. Repairs do not transfer.

| Layer | Question | Repair |
|---|---|---|
| Model | Input signal sufficient and the model still judged wrong (long tail)? | Switch pattern, add a review gate, or lower the decision rights layer |
| Rule | A rule missing, or the implementation drifted from the annotation guide? | Change the rule, release a new dated version of the annotation guide |
| Interaction | A person saw it but had no time, no basis, or no authority to stop it? | Change the queue design |
| Data | Input, list, or fields wrong (a repair shop list that drifts)? | Fix the data and add operating discipline: an owner and an update cadence |

- Flow-back lands on names: who rules on the category at the retrospective, who adds the golden case and countersigns the incident record. Either name missing, the loop is not closed. Kill criteria are checked by the book and the check recorded even when nothing triggers; "the value of checking is in the act of checking every time." After the repair goes live, replay the golden cases once and attach the result to close the record. A recurrence of the same shape responds one level up, and the runbook itself gets a retrospective.

### L2 → L3, resistance: decode it before you answer it

- The radius rule: the system's radius of visibility minus its radius of consultation is your resistance band. Whoever's work the system turned into data without a conversation owes you a constraint interview, and it arrives on its own in the ugliest form it can.
- Rule on the form with the decoder, then confirm the cause in an interview anchored on one instance.

| Form | Common real cause | First response |
|---|---|---|
| Delay, rescheduling, "too busy lately" | Interest, this is all cost to him | Go back and consult; find the fight he is already in and help him win once first |
| A barrage of detail, endless technical challenges | Fear disguised as professionalism (occasionally he really does know) | Name it, "I sense there is another worry behind the detail. Can you say more?", and go through the detail seriously |
| Sniping at a meeting, a challenge in public | Pride, turned into data, skipped over, compared | Do not defend, name the emotion first, book the conversation into the field, one on one |
| Data withheld, a process forever "in progress" | Information gap plus risk | Go back and consult, plus a governance pledge |
| Agreed in principle, nothing moves | Interest or fear, politeness is the disguise | Narrow it to one concrete action and one concrete date, watch where it sticks |
| Silence, no objection and no use | The deepest kind, the conversation was given up on or he was never invited | Go to them and shadow; force a check of the design-defect hypothesis |

- The four real causes: interest (what does he lose), fear (how will the data be used, what replaces him), pride (is he the last to know), information gap (does he know what you are up to). One piece of resistance often comes in layers.
- Three rules of use. Form and cause do not map one to one; the table gives candidates, the interview gives the diagnosis. Name first, decode second, redesign third; reverse the order and not one step works. Keep alive the hypothesis that he is right; some resistance points at a place you got wrong.
- In the room, do two things and no more. Name it: "That worry is fair. This system really can be used to appraise people. I am not going to pretend it cannot. Let us talk about how we make sure it is not used that way." Book the field: "I want to come sit half a day this week and go through your cases from the top." Never defend the intent; "defending intent does not work on a fear of capability."
- The decoding interview does not sample. Take the few cases with the longest waiting time, "the mechanism hides in the extremes," and probe in three layers: replay what he did first on that case, compare it against a similar case that did not go overdue, ask under what conditions he can afford to wait. Test for having dug to the bottom: the answer lands on a piece of design you can change (a "waiting on external" status, attribution to the step not the person). "Their attitude is the problem" means you have not got there.
- Scripts are functions, not lines. Admit the capability, do not defend the intent; name it then shut up; hand back the pride ("you know this step better than I do, where is it wrong?"); anchor on an instance ("was there a specific case last week that made this number feel unfair?"); separate visibility from other causes ("if these numbers were pulled tomorrow, would your worry go away? What would be left?"); turn fear into a scenario ("in the worst case, who uses this data, and how?"); get the acceptance condition stated ("under what conditions would this feel like it is helping you rather than watching you?"); close with a date and a way out, "if we recorded it in the wrong place, we change the system, not the wording"; make him a co-author ("which pledge do you think is missing?"). Banned: "The system does not mean it that way." / "The data does not lie." / "This is a company-level decision." / "Do not get emotional." Every one defends intent and dodges capability.
- Answer the fear of capability with a written governance pledge, never a verbal one; a verbal pledge expires when its author changes post.

| Pledge | Landing mechanism | What a violation looks like |
|---|---|---|
| 1. Data improves the process, never appraises individuals | The appraisal metric list may not cite any individual number the system produces; entered into the policy document | Someone's waiting time or override records show up in a performance review conversation |
| 2. The team concerned sees its own data first | Any material with a team's numbers goes to that team's lead N working days (rule) before the meeting | A team sees numbers about itself for the first time in a meeting room |
| 3. Aggregate display before individual detail | The upward-facing view goes no finer than the step and the team; individual detail lives only in the team's own view | A table ranking individuals circulates outside the team |
| Technical guardrails, the hard means | Splitting a table by person disabled at the warehouse layer; the individual dimension de-identified in the shared layer; a pull needing individual detail goes through approval and leaves a trail (who, which day, why, what) | Someone goes around approval and one query ranks the data by person |

- Issuer discipline: "a governance pledge can only be issued by the person with the power to violate it. Your signature does not count." Issuing elements, missing any one voids it: issuer (the business owner, not the project team); how it takes effect (in writing, to every team covered, entered into policy, reissued when the system extends to a new team); issuer change (the successor reissues within 30 days (rule), no reissue → flagged red on the transfer ledger and walked through at the quarterly business review); appeal path (the issuer or an independent third party, union representative or HR, written reply within N working days (rule), appeals do not go through the project team).
- If the owner will not sign, that is an answer, not a communication failure. Ask which of the three he is stuck on; stuck on the first usually means he is himself appraised on these numbers. Land pledges 2 and 3, tell the front line honestly which one you did not get, and make no promise on his behalf.
- Give the pledge a recheck action: every later request for numbers split by person goes back to it. "A policy pledge with no recheck is only the written version of a verbal one."
- If the challenge names your department's track record ("the last system was yours too"), decode the history along with it. Take the old debt on first, not by apologizing but with a difference that can be checked: which of the five capabilities belongs to whom, whose annual goals name this system, which escalation tree gets walked. Refuse the debt and every later promise is discounted automatically.

### L2 → L3, adoption: from usable to missed when it is gone

- Rule with the social model, not the product model. Training settles whether they know how; adoption is settled by who is using it (peer environment), whether the users are doing well (visible winners), and whether not using it costs anything (institutions). "Organizations do not adopt tools. Habits adopt tools."
- Fill the four mechanisms in this order before launch: network first, cadence fixed, wins amplified, institutions last.

| # | Mechanism | What it is | What it prevents |
|---|---|---|---|
| 1 | Super-user network | A front-line seed user with influence, given privileges and identity. Pick by influence, not by title | Adoption resting on the project side's pitch; nobody to carry the feeding period |
| 2 | Operating cadence | A 30-minute queue retrospective every week (rule): reason code distribution, aging rows, one improvement. Embed it in a ritual that already exists | A new ritual cannot win a calendar slot and dies in three weeks |
| 3 | Short-term win announcement | One win worth telling inside the first month (rule), in business language, announced by the business owner. The winner is the business team | The improvement goes unnoticed, or the credit goes to "AI" |
| 4 | Institutional anchoring | Onboarding material covers queue operation; the SOP references the system. Lock the habit in with the cost of leaving it | Held up by enthusiasm; the curve goes to zero when the person leaves |

- Super-user pick test: "a hard case comes in, who does everyone get up and go ask?" Write three names; if all three are team leads, pick again. Agreement, one page, walked through with the business owner in the room. Selection, all must hold: influence test; actual user, not his supervisor; dares to say unsafe ("someone who only says nice things cannot feed a good system"); voluntary ("an appointed champion is not a champion"). Privileges: first use, new features and rule versions two weeks (rule) before everyone else and his view can veto the release cadence; direct channel to the development board skipping tickets, every suggestion answered inside two weeks (rule), a fixed response capacity block reserved in your schedule before you say it, "a bad check can be written only once"; chairing the queue retrospective. Identity: a formal name granted by the business owner in front of everyone, naming rights sit with the business side; contributions credited by name in public, "promoting the system = promoting your own work"; the super-user takes the training instructor role. Obligations: the feeding-period commitment, keep using it at its dumbest and fill reason codes seriously; the hours go into his workload, his supervisor confirms in writing how many hours a week or it goes into his quarterly OKRs, no free rides. Exit, written in advance: voluntary any time, ask once to stay, no pressure; four straight weeks (rule) of not using or not attending voids the status automatically; red line, using data visibility to appraise or pressure colleagues means immediate removal.
- The feeding period runs on design and reward, not goodwill. Seed users keep using the system at its dumbest and keep feeding it real judgment, and "the reward is paid before the system gets smart": their name on the rules the reason column cites, so the more it is used the more it looks like their work.
- Operating cadence sheet, one row per tier: weekly queue retrospective (30 min) chaired by the super-user, in the tail of the business owner's existing weekly; biweekly rotating release chaired by the co-build engineers; monthly metrics and win announcement chaired by the business owner, in the one-page slot of the monthly business review. Columns: Frequency | Ritual | Agenda (time-boxed) | Chair | Embedded in an Existing Meeting. Creating a new ritual takes a written explanation of why no existing ritual can hold it. Two red lines: the retrospective crowded out twice in a row is an adoption warning, handled like a drop in daily actives; the subject of the monthly announcement is the business team, the project side has no name on this page. Handoff marker: the day all three tiers are chaired by the business side, the cadence handoff is complete.
- Measures. Daily actives = the share of users who took a Human Call action that day. Depth of use = override rate, reason code fill rate, share of "other" codes.
- "An order changes login behavior, not decision behavior." The front line invents the cheapest compliance, accepts everything, picks "other" without looking, and the trail poisons the golden cases. High daily actives with override rate near zero and the "other" share shooting up means nobody is judging; do not read it as a perfect system.
- Announcement rule: the subject is the business team (the department that uses the system, not your platform or data team), the measure a business number, the system's name in the last paragraph or nowhere. Confirm the business owner will say it in his own voice.
- Adoption plan, one row per mechanism, columns Mechanism | Goal (verifiable) | Action | Owner | When; no row blank, "a mechanism with no owner is not a mechanism, it is a wish." Three checks: your own team appears among the four owners more than once → adoption is still growing on you and the handoff will go wrong; no mechanism yet has a hook in the business side's existing institutions → do not launch yet; the first thing you check when daily actives drop is the unsafe trail, then the manager's attendance, then features.
- Institutional anchoring is the one lever that needs nobody to remember it. Write the change as revision text (add a queue operation section to onboarding; every "check the core system" in the SOP becomes "check the queue") and hand it to the process owner with the wording; file the SOP revision yourself where the process system lets you, and budget the review gate it adds.

### L3 → L4, handoff: transfer capability, not files

- "Praise is a diagnosis." "It doesn't run without you" announces that you are the system's single point of failure. Inside a company nobody revokes your access, so stepping out of the daily is an event of responsibility, not a physical event: the five capabilities move off your team.
- Five daily capabilities, and documents cannot carry them: run (someone responds when it fails), configure (someone dares to touch a rule), exceptions (someone judges a situation never seen), evolve (someone keeps feeding the eval), teach (someone trains the next newcomer). "Documents record 'why we decided this back then.' What the system needs every day is 'how to judge this now.'"
- Test each with Show Me, never a signature.

| Capability | Show Me scenario | Pass standard | Rework on failure |
|---|---|---|---|
| Run | Cut one LLM dependency without warning | The receiving side degrades, notifies by the template, recovers, no instruction from you | Rerun the degradation drill, add an incident notice drill |
| Configure | One real change (list, threshold, rule parameter) | The full change, test, release cycle on the business side's gatekeeping rights; the change passes the eval replay | Walk it again as a pair, check permissions and config items |
| Exceptions | Inject a class of situation never seen | The first reaction is the escalation path, not a call to you; the ruling settles into the golden cases or a rule | Draw the escalation tree together, two injection drills, retest |
| Evolve | One small request end to end, plus one minor model version upgrade | Scheduling to rotating release with no commit from you; the upgrade passes the golden cases replay with both signatures | Back to co-build pairing, shrink the request, retest |
| Teach | The business side's own mentor onboards one newcomer | The newcomer handles the queue independently within two weeks (rule); material maintained by the business side | Have the newcomer recount where they got stuck; fix the mentoring path, not the manual |

- Three rules. You are in the room with your hands behind your back. One failure sends the item back for rework, and what gets added is a drill with a retest date, not a document. Only when all five pass does stage four begin, counted from that week, not from the week the North Star was reached. "The value of a test is not in passing. It is in exposing." If it fails during the test period, congratulations.
- Four-stage cadence; each stage answers who chairs the retrospective, who touches production, who answers outside questions, and carries one gate.

| Stage | Chairs the retrospective | Touches production | Answers outside questions | Gate to the next stage |
|---|---|---|---|---|
| 1 Your team leads, business side observes | Your team | Your team | Your team | Co-build agreement in force; gatekeeping rights of the first module handed over |
| 2 Shared lead | Business side chairs, you add | Both, gatekeeping handed over module by module | Business side answers, you backstop | Every module's gatekeeping on the business line side; four consecutive retrospectives (rule) chaired by the business side |
| 3 Business side leads, you advise | Business side | Business side, your team no longer commits | Business side | All five Show Me tests passed |
| 4 Stepping out of the daily | Business side | Business side | Business side | Response window closed in writing; write access read-only; no open rework items |

- "The handoff began on day one of co-build." The repo in the business line, backward staffing, the rotating release and "if you cannot say it, do not merge it" are stage one. What needs scheduling is the three transfers of stage three and the date of stage four.
- Three AI handoff items, absent from every traditional IT checklist: keep the eval updated (who adds golden cases, who approves, who guards per-category thresholds, who versions the annotation guide; "an eval frozen on handoff day means drift goes undetected from then on"); re-verify on model and dependency changes (who runs the golden cases replay, who signs "safe to switch"; "the first model retirement notice is the system's death sentence" otherwise); review decision trail data (who chairs the override review, who analyzes reason codes, who runs the fairness spot check). Platform-level route, once per company: one eval platform, one change re-verification process, one trail review template. First step, hand the replay process to the platform team to maintain and keep only the right to set the questions.
- Three mandatory mechanisms, each drawing force from somewhere other than your willpower; missing any one slides you into permanent ops: next year's staffing budget reserves no ops headcount for this system (Finance's line, headcount cut per capability that passes); the date all five tests pass is a line in your quarterly OKRs (your manager's review of you); the PMO's transfer ledger, one line per live system, five capabilities × owner, blanks flagged red, walked through at the quarterly business review. No PMO → hang the ledger on the standing agenda of the sponsor weekly.
- The receiving side is three parties. The business side takes configure, exceptions, teach; ops takes first-line incident response and degradation notices inside run; evolve plus the three AI items land on the business line's own engineers. No engineers there → the three AI items get their own ledger lines with real names; where no real name can be written, the platform team executes and the business side's eval guardian signs. "Writing 'ops' and moving on is not allowed."
- Owner placement sheet, one real name per row; one person may hold several rows, each row holds one name; "the team is responsible" means nobody is. System owner (budget, priorities, first signature on stop or not), maintenance owner (code, production, gatekeeping, first-line response), eval guardian (approves golden cases, weekly review, annotation guide versions), AI dependency owner (evaluates and signs model and dependency changes). A row you cannot fill is a cause-of-death candidate; start the ledger's first line with it, blanks red.
- Where the budget sits decides the owner. Move running cost from project funds to the business department's budget line; from then on the owner asks his people "is it worth it" instead of asking you "can you," and you stop sitting in on cost reviews. Money on your project funds means the system is still yours.
- Response window terms, in the responsibility transfer agreement: length 3 months (rule), the period when the new team's confidence is most fragile; scope, only two kinds, P1 incidents and exceptions the escalation tree ran to the end and did not catch; a routine request taken means falling back to stage three; every help request logged and reviewed before closing (which capability it pointed to, whether to add one drill); on expiry, write access read-only, removed from the oncall rotation and the retrospective's standing attendee list; closing needs written confirmation from the business owner and the ops owner, no confirmation means extension by default, and extension by default means permanent ops.
- Capacity debt: every day you stand duty on this system is a day your team cannot give another department next year, and "the week you are on vacation is the system's risk exposure." Make the "only I can do this" list; every line is a handoff debt.

## Procedures

**Before launch (L1 → L2 week).**
1. Draw the metric tree: one North Star from the charter, 2–4 process metrics, ≥ 2 balancing metrics (rule), owner and action on every row. Put it on the business weekly; write the claiming actions into their SOP.
2. Confirm the 8-week reconciled baseline (rule) and the median line. None → start today and say so.
3. Write the one-page incident runbook: what counts as P1, who the notice goes to, the four questions in order, how the case enters the golden cases, who rules and who countersigns.
4. Drill the same-day notice with one historical wrong output and a stopwatch; lock down whatever runs past two hours (rule).
5. Fill the adoption plan's four rows; count your own team among the owners (> 1 = not ready); find the existing ritual that holds the retrospective (none = do not launch yet).
6. If any number the system produces can appraise an individual, get the governance pledge issued by the business owner this week, with the technical guardrails filed on the data platform.

**An error reaches a person.**
1. Grade it on the four grades, then set the level: unsafe seen = P1 even when caught; concern over threshold or in batches = P2; useless rising = P3.
2. Stand in the front line's work area for ten minutes; you hear the rumor half a day before your reporting line does.
3. Draft the three parts in fixed order within two hours (rule); the business owner issues the same day, no individual named, unverified facts written as "being checked."
4. Retrospective within 48 hours (rule) for P1, the same week for P2: model → rule → interaction → data, each layer eliminated in writing before the next; repair on the layer found; where the memo promised a downgrade on a missed-risk case, execute it the same week.
5. The case into the golden cases within 24 hours (rule), kept permanently; kill criteria checked and the check recorded even when not triggered.
6. After the repair goes live, replay the golden cases and attach the result to close the record. Same shape recurs → one level up, and the runbook gets its own retrospective.

**Challenged in public.**
1. Name it. Admit the capability, never defend the intent, then stop talking.
2. Book the field: half a day this week, one on one, from the top of a real case. Nothing more in the room.
3. Interview on the extremes with three-layer probing until the answer lands on a design you can change. Ship the design change first.
4. Draft the pledge, the business owner issues it in writing to every team covered, appeal path at the bottom. Not signed → ask which pledge he is stuck on, land 2 and 3, tell the front line which one you did not get.
5. Verify: the person concerned comes to the retrospective with his own numbers. A former opponent is the most convincing spokesman; name him the next super-user.

**Decoding silence.**
1. Find a count that can be falsified: daily actives, decision trail, override records. Any one at zero over a long stretch turns an impression into a diagnosis.
2. Go to them and ask "walk me through one of your recent cases from the top," never "why are you not using it." Watch which step he routes around the queue at.
3. Keep the design-defect check alive; the silence may mean the thing has no use in his workflow.

**A usage curve drops.**
1. Pull that team's scores and override records for the two weeks the curve turned. An unsafe that landed or concern over threshold → the problem is the system and the incident story; run the incident procedure.
2. Count the team manager's attendance at the last four retrospectives (rule). Zero → the fix sits with the owner, not the system; attendance goes into the team lead's job description.
3. Only then look at features: reason code distribution, aging rows.
4. When the fix belongs to a manager on another reporting line: let the number walk into the owner's view on its own (per-team daily actives and attendance in that department's own monthly operating data); failing that, the super-user raises it at the retrospective as a peer; only then lay the two sheets side by side, data only, no conclusion.
5. Test institutional anchoring: ask a recent joiner how a case of this kind is handled; the old SOP recited = the fourth mechanism is still owed.

**May I step out of the daily (L3 → L4).**
1. Name the four owners, one real name per row; ask the PMO for the transfer ledger, or start its first line.
2. Fill the three AI items with real names; "ops" is a blank. None present → you are using a traditional IT handoff template.
3. Lay out the cadence sheet and find the stage you are in from the evidence: who chaired the last four retrospectives, which modules' gatekeeping sits on the business side.
4. Build the three mandatory mechanisms: the headcount line, your OKR line, the ledger line. Move the running cost onto the business budget.
5. Book the Show Me you are least sure of this week, scenario and room settled, hands behind your back. Fail → drill plus retest date, never a document.
6. All five passed → stage four counts from that week. Sign the one-page responsibility transfer agreement with the response window terms; write access read-only, off the oncall and attendee lists.
7. Log every request in the window; a routine one taken means back to stage three. Close only on written confirmation from the business owner and the ops owner.

## Detectors

- If the report shows the best-looking week and not the bounce-backs, you are screenshot reporting; put every point on the run chart, or you will be accused of picking.
- If the plan is "let's get to the bottom of it before we say anything," you are in incident silence; rumor runs ten times faster and always picks the worst version.
- If the celebration has no complaint rate and no overtime hours on the same page, the cost was shifted and comes back with interest in three months.
- If the last incident's repair was a model swap or a prompt change, write the action down and check it against the layer the retrospective ruled on; a data-layer fault repaired at the model layer fixes nothing.
- If you proved the numbers right line by line, you won the argument and lost the system.
- If you asked the sponsor to lean on people, power changed behavior and not willingness; the resistance has gone underground into silence, and the person you leaned on is next project's dependency.
- If the weekly report says "feedback from all teams is good" and nobody objected, read the daily actives; the deepest resistance says nothing.
- If your answer to every challenge is one more training, force "if he is right, which piece of the design is wrong?"
- If you sign the pledge yourself, it binds nobody. If it has no recheck, it is the written version of a verbal one.
- If adoption is judged by the training sign-in sheet, look at daily actives in weeks two and three after the training instead.
- If daily actives are high, override rate near zero and "other" codes climbing, nobody is judging; the system is eating poisoned fuel.
- If every super-user is a team lead, you picked by title and insulted the real opinion leader for free.
- If the announcement's subject is the system, the credit was stolen and the network is about to fall apart.
- If a recent joiner recites the old SOP, the first three mechanisms will walk out with the people.
- If your handoff checklist is nouns (manual, accounts, code) and not verbs (can respond, can judge, can evolve), you are sending documents.
- If a test item has a signature and no injected scenario and drill date, Show Me has decayed into a sign-off.
- If the step-out date appears in no plan, or the ledger line has blanks, you are already permanent ops.
- If the first gatekeeping rights are scheduled for the week you get pulled onto the next project, or that line is blank, the handoff started too late and can only hand over a legacy.
- If the transfer agreement lacks any of window length, the two scopes, or who confirms closing in writing, it is the clean break or its internal mirror, the break that never comes.
- Counterexample cells. A deliverables list of manual, accounts, code and recordings is all nouns. "Maintenance owner: the engineering team" is a blank row. "Eval guardian: to be decided after handoff" means the eval starts rotting on handoff day. "Five tests covered by documentation, training and Q&A, deemed passed" swapped out Show Me. "We are right here, come find us anytime" is never exiting.

## Key judgments

- "A metric with no owner and no action is only scenery."
- "The first sentence of the incident story is that the defense held."
- "Resistance is data. Suppress the resistance and you delete the data."
- "You win the argument and lose the system."
- "The deepest resistance says nothing, it just does not use the thing."
- "An adoption problem is mostly a problem of the manager's attention. The fix sits with the owner, not with the system."
- "Documents are the shadow of capability, not the capability."
- "The handoff began on day one of co-build."

## Templates

- `templates/handoff-plan.md` (main chain): plan header, owner placement sheet, three AI items, five Show Me tests with rework column, response window terms.
- `docs/appendices/template-18-metric-tree.md`: metric tree with the owner's reporting line column, incident level table, four questions, same-day notice; fill-in at `repo/templates/metric-tree/metric-tree.md`; `scripts/run_chart.py` marks the median and six on one side.
- `docs/appendices/template-20-resistance-decoder.md`: decoder with a worked row, hard conversation scripts by function, governance pledge with issuing elements.
- `docs/appendices/template-21-adoption-plan.md`: adoption plan, super-user agreement, operating cadence sheet; `repo/templates/adoption/` computes daily actives and depth of use.
- `docs/appendices/template-22-handoff.md` §22.2 and §22.3: five tests sheet, cadence sheet; `repo/templates/handoff/checklist.yaml` validates the owner fields and the test state machine.

## Vendor seat

The three mandatory handoff mechanisms are the contract end date, and the responsibility transfer agreement is the exit agreement with the account revocation date; the response window is not a given there and must be written into that agreement. Adoption engineering, the metric tree and the pledge apply as is, and the client owner issuing the pledge comes naturally from the neutral seat. A line in a contract is not a working mechanism.
