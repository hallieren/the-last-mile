# 16 · Production Engineering: Set the Running Budget Before You Launch

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-16-production-readiness.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** Everything was fine in the pilot, so how does real traffic bring an exploding bill, latency over the line, and something acting up every few days?
>
> **What You Will Be Able to Do.** Stand up the four ledgers of the running budget for an AI system (cost / latency / error / degradation), build the minimum observability set, and turn "how much a month, how much per claim" into one page an owner can manage against.

---

## Monday of Week 12, One Bill

The pilot starts on Monday of project week 10 and runs eight weeks. The first two weeks are calm. The eight people on Linda Marsh's team use it every day, the eval spot checks turn up no unsafe, and Kevin Doyle's weekly report carries the phrase "chasing early" for the first time.

The pilot enters week 3, project week 12. On Monday Finance forwards the monthly bill to Kevin, Kevin forwards it to you with one line attached. "Is this number normal?" The LLM call spend is 4 times the estimate you gave him before the pilot started.

There is a second thing the same week. Tuesday at the morning peak, a queue refresh goes from 3 seconds to 40. On Wednesday Linda puts it to you politely. "The queue takes forty seconds to turn over. We cannot wait that long, so we have gone back to working out of the inbox. The inbox does not make you wait." The usage curve drops on cue. Two days of investigation turn up three causes.

1. **Full recomputation.** Every refresh by every person recomputes the whole team's several hundred claims from scratch, while fewer than two in ten claims actually have a new event on a given day.
2. **A retry storm.** An extraction call that fails is retried at once, with no cap on attempts, and a failed claim comes around again on the next full recomputation. Rate limiting, retries, more rate limiting, feeding each other.
3. **The whole operations manual stuffed into the prompt.** To lift the accuracy of the document checklist during the prototype, the entire manual was pasted into every call. Claim volume was small then, and nobody was watching tokens.

The sharpest part is that not one of these three decisions was wrong during the prototype. Full recomputation was the simplest, unlimited retries the least trouble, stuffing in the manual the fastest to show results. The prototype optimizes for learning speed, and all three moves were right for it. They just were not put on trial again when the stage changed (this is Chapter 14's changing stage without changing the rules, and this time the bill is what dragged it out).

## Why This Is Hard: An AI System's Running Characteristics Are Not the Same Shape

Traditional software's assumption of "launch it, then hand it to ops" rests on three premises. An AI system satisfies none of them.

Cost grows linearly with calls, and there is no marginal cost trending to zero. Double the users of traditional software and server cost barely moves. Every LLM call is close to full price. Even with the model provider's own caching, a stuffed context still pays a bill in latency and diluted attention, and the more irrelevant content it holds, the more easily the model misses the few lines that matter. Double the claim volume and the bill doubles, and wasted calls are billed to the last cent. Cost has become, for the first time, a running variable that occurs claim by claim, not a fixed investment bought once and never charged per transaction again.

The latency distribution has a long tail, and the tail lands exactly on the rhythm of the business. Average latency means nothing. P50 looks good and P95 kills you. Line up a period's requests by how long they took. The one standing in the middle is P50. The one at the 95% mark, with only a small share slower than it, is P95, and only 5% of requests are slower. Peak requests also cluster naturally into one window (reviewers all open the queue in the morning). Those 40 seconds were the long tail colliding with the morning peak, and an "average" cannot see it at all.

Quality drifts silently. The code has not changed and the system reports no error, but the input distribution has moved. Claim mix, fraud methods and the repair shop list are all in motion, and model behavior moves with them. No exception stack, no alert. The first to notice is usually a front-line hunch or a customer complaint.

The traditional trio of ops monitoring (uptime, error codes, resource usage) is blind to all three. So there is only one conclusion. The running budget has to be designed like a feature, holding a place in the architecture and the schedule and a vote at the launch gate, rather than written up as an ops manual after launch.

## Prior Art, and What AI Changed

The ledger our predecessors left is called the error budget. The core idea of the Google SRE school (paraphrased here). Reliability is a budget, not a wish. 100% availability is the wrong target. The right move is to set a reliability target, and the gap between it and 100% is the budget, which the team spends freely inside (releases, risks), freezing changes once the budget burns through. It turned "do not err" from a moral expectation into a manageable account. Its companion is observability discipline. A system has to be able to answer "what is it doing right now, and why."

What did the AI era change? The budget goes from one ledger to four. Beyond the error budget come the token cost ledger (cost became a running variable, claim by claim), the latency ledger (the long tail colliding with the business rhythm) and the quality ledger (the error ledger in the framework below). The per-category threshold table of Chapter 11 turns from an acceptance document into a running instrument, and the eval goes online (Chapter 18 puts it as the threshold table becoming the monitoring definitions as is, meaning which table monitoring reads from here on, the same thing).

And "degradation" gained a new meaning. Traditional degradation cuts features to protect the core. An AI system's degradation cuts intelligence to protect the process. The LLM goes down, gets slow, gets expensive, and the question is whether you can fall back to rules mode and keep the core process running.

Chapter 10's "start with the dumbest thing" pays out its second value here. Do not delete the dumbest thing that works. It is your degradation path.

## The Framework: The Four Ledgers and the Minimum Observability Set

**The four ledgers of the running budget.** One budget line, one action on breach and one named owner each. Read the first four columns first. The last column holds Anchor & Helm's actual numbers, looking back across the whole pilot, at a point later than this chapter's story, so take your time matching it up.

| Ledger | What It Records | How the Budget Line Is Set | Action on Breach | Anchor & Helm Magnitude |
|------|--------|--------------|----------|----------|
| **Cost** | Cap on cost per claim, plus the monthly total | Worked back from business value. What the labor hours one exception claim saves are worth, with system cost allowed only a fraction of it. Do not work back from last month's bill | Trigger a cost review, instead of finding out at month end | 4 times the estimate when it was out of control, cost per claim back to 1/6 after the four moves |
| **Latency** | The P95 cap (not the average), with the peak window on its own line | Worked back from the user's working rhythm. From opening the queue to being able to work, how many seconds can they wait | Degrade, or extend precomputation | Morning peak refresh back from 40 seconds to under 3 |
| **Error** | Per-category error rate caps | Carry over the Chapter 11 threshold table as is, build nothing new. unsafe zero tolerance, concern ≤10%, useless ≤20% with the trend not rising, measured by online sampling | Rework. A kill criteria trigger means pause (Chapter 14) | One suspected unsafe case across the whole pilot, caught by Linda in week 14 (Chapter 18), short of the two-in-one-week trigger line. concern under half the threshold, useless around one in ten, and it stopped surfacing after that batch of repair shop mislabels was fixed in week 13 |
| **Degradation** | A fallback for every AI dependency point | The budget line is "the drill passed." Really pull the dependency and the core process still runs | A dependency point with no fallback does not launch | The LLM dependency cut for half an hour, the queue fell back to rules mode and review carried on |

The cost ledger has a precondition inside a company. The account has to be separable in the first place. Your calls are most likely mixed into the Digital Center's shared gateway or the company's single cloud account, and what comes out at month end is one department total that shows nothing about which system spent what. Tagging this system's calls with FinOps (the practice of splitting cloud spend by system), or hanging them on a showback report (showback only shows the bill and deducts no budget), is the precondition for standing up a cost ledger, not a bonus. Without the split you do not even have the month-late reminder that is the month-end bill, and the first time anyone notices the cost will be at next year's budget meeting.

The owner column holds one more pitfall specific to the inside. The owners of the four ledgers are often not in the same department. Cost follows the budget account, and the action on breach needs the business side to make the call. Latency and errors live in your system, and the actions are done by your people. Degradation's fallback needs the business side to accept that half hour of no supply. So each ledger names exactly one first-line owner, and the test is whose budget or whose daily actions a breach hits directly. Everyone else related is written in as a countersignature (confirming together but not carrying the main responsibility). The first-line owner does not have to be the person who fixes it, but the breach alert can land in only one inbox. Two names is the same as no name.

**The minimum observability set.** Three pieces, and missing one means a ledger cannot be kept.

1. **End-to-end trace**, any single suggestion replayable. A trace is the complete record of one suggestion from input to display, the input snapshot, what was retrieved, the prompt and model version, which rules hit, the final display. It is not the same thing as Chapter 12's six decision trail fields. The six fields are an audit commitment, answering "who decided what," and they are for Victor Reyes and compliance. A trace is engineering replay, answering "why does this suggestion look the way it does," and it is for whoever is debugging. One chain, two readings. Do not conflate them, and do not build only one.
2. **Online eval sampling**, golden cases replayed on a cadence, plus a proportion of production output spot-checked by human review, booked by the Chapter 11 categories. The number of rows spot-checked decides how fine a ratio you can read, and the sample size follows Chapter 11's passage on how to read a ratio line. When people cannot keep up, let a model screen first, but the model's verdicts count only once they have been calibrated on a human-annotated sample, with the disagreement rate read separately by error category. On the unsafe class the model may only report, never release.
3. **Drift signals**, sudden-change alerts on the input distribution (claim mix, amount distribution, policy type composition) and on the override rate. The override rate is the share of system suggestions the reviewers push back, and when that share moves, usually the input or the model moved first.

The last two do not serve this chapter alone. They are ready-made components of Chapter 18's launch monitoring surface.

## At Anchor & Helm: One Week of Repairs, One Page

The repairs take you and the two claims-ops IT engineers (the headcount set in Chapter 15) one week. Four moves on cost.

**Full recomputation becomes incremental.** Only claims with a new event get recomputed, a new email, a status change, a timeout. Call volume drops by a large chunk right away.

**Cache the extraction results for stable fields.** The extraction result for one email does not change on its own, so extract once and store it, and anything that passes schema validation (all fields present, types matching) goes into the cache. Until then every round of full recomputation was paying again and again for the same email.

**The manual moves out of the prompt and into retrieval.** Each call now carries only the two or three passages tied to the current claim's document type, and token length collapses. Accuracy did not drop, confirmed by two weeks of spot checks (changing the call path also has to clear the eval. That is discipline, not ceremony).

**Long-tail claims routed to a smaller model.** The rules layer already absorbs most claims (Chapter 10's step two, the part where rules are the floor), so cut once more inside the long tail that needs the LLM. Claims whose signals are simple and merely uncovered by the rules go to a smaller model. Only the genuinely hard ones use the big one. The eval decides where the split goes, and if the smaller model clears the threshold on that subset, the subset is its.

With all four moves in, cost per claim falls to 1/6 of what it was, and the monthly total is back inside the estimate line.

The retry storm gets treated on its own. The source is the LLM call in the extraction step, while the email pull that was rewritten back then turns out to be fine, because that stretch has carried a cap and a backoff (wait a while before retrying after a failure, with the wait lengthening each time) all along. The fix for the extraction stretch is backoff plus a retry budget, at most two attempts per claim, and over the limit it goes to the "pending human" column. The email pull keeps the three attempts with doubling intervals set in Chapter 15, which is the standard for pulling. The new ledger for LLM calls tightens to two, because one call costs far more than one pull.

The person doing the work is exactly the engineer who rewrote that retry logic back under "If you cannot say it, do not merge it." (Chapter 15). Last time he learned to make one stretch of retries explainable. This time he opened a ledger for retries across the whole chain.

Latency gets two moves of its own. Precompute the queue, working the whole team's queue out before the morning peak. Make the refresh asynchronous, so opening it shows the most recent result at once (the interface marks the data's timestamp) while the background updates incrementally. The morning peak refresh comes back under 3 seconds, and usage climbs back to where it was a week later.

The degradation drill is set for Friday afternoon. You do something that surprises Linda's team, cutting the LLM dependency on purpose for half an hour. The queue falls back to rules mode, the five rules of thumb rank claims as usual, the reason column says as usual which rules matched, and the missing documents column grays out to "extraction paused, open the claim to read the original email." Review carried on through that half hour, and some people never noticed. The drill counts as passed on two conditions, that review carried on through that half hour with real users present, and that when asked afterward "did you notice," most say no. The cadence goes into the register, every dependency point drilled at least once more within 90 days, with a rerun mandatory after a model swap or a change to the call path ([Template 16.3](../appendices/template-16-production-readiness.md)). This is the second identity of the rules layer Chapter 10 left behind. In normal times it is the floor. When supply is cut it is the fallback.

You do not have to invent an occasion for the drill. The company most likely already has an annual disaster recovery drill or a business continuity drill on the books, so hang the pull-the-plug drill for AI dependency points onto that one. The schedule, the notification templates and the acceptance records are all there already, and it comes with a date somebody else keeps for you. All you have to do is add one line to that drill list, saying which dependency gets pulled, what it falls back to, and who is present to watch.

At the next weekly you bring no repair report. You bring one page, the four ledgers. Kevin looks at it and says, "When I signed off on that bill last month I felt hollow. I did not know whether that number counted as normal." Now he knows. This system has a cap on monthly running cost (back to the estimate line), a cap on cost per claim (1/6 of what it was before it ran away), a morning peak P95 of three seconds, error thresholds that are exactly the table he ruled on in Chapter 11, two degradation switches with their triggers, and one named owner per ledger.

"This page stays with me," he says. It is the first time Kevin can manage this system against numbers instead of against feeling. You add a line of small print in the footer while you are at it. At the handoff when the pilot ends, this page becomes a budget account, and running cost moves from project funds into claims operations' department budget (Chapter 22's setup starts on this page).

The hard part is not the accounting move. Moving this money into claims operations' budget account is half an hour of work for Finance. The hard part is whether claims operations will own that line in its own department budget next year. Owning it puts one more number on their cost sheet, and that number will get asked about at the quarterly business review. Which is why the money has to be separable before it can move. Kevin will not accept a total mixed into the Digital Center's shared gateway account, because he cannot read what makes it up and you cannot prove the money belongs to this one system. Split usage by system first, then talk about moving it.

The business side is a real owner only once it takes the budget. Whoever holds the budget holds the priorities (week 22 in Chapter 22). From the first month Kevin pays for it, what he asks when he schedules is whether his own people are worth it, not whether you can. If he does not take it, the money stays on the Digital Center's project funds, your cost center feeds it forever, and the team that feeds it ends up being its ops team. That is the financial source of permanent ops.

The four moves did not contribute equally. All the field left behind is a qualitative account. Full recomputation to incremental cut the number of calls, the manual moving into retrieval cut the length of each call, and those two are the largest in magnitude. The cache removed the part where the same email was paid for again and again, ranking behind them. How much the long-tail routing to a smaller model saved was not recorded at the time, and the calculation was done once before the handoff. About six in ten of the long-tail claims went to the smaller model. That move accounts for less than a tenth of what the four saved in total, the smallest of the four. This matches industry experience. Gateway-style routing usually saves only ten to twenty percent of inference cost, so do not expect it to carry the load. Take the moves in this order.

Here is something an outside team cannot do and you can, going to look at the account directly. The cloud platform console and the FinOps reports sit inside the company, so you do not have to wait for someone to forward you the monthly bill. You can pull it by day and by step yourself. The more valuable half is the denominator, the baseline number you can compare against. Go ask the department next door about the comparable system it launched a year ago, what its cost per claim is, and benchmark once sideways. An outside team can only get the summary sheet the other side is willing to give. You can get the detail, and you can get other people's numbers.

## Failure Modes

**1. No degradation path.** The LLM service twitches and the whole system is paralyzed, with reviewers staring at a spinning page. The cause has two layers. A degradation path is a "negative feature," invisible in normal times and unimpressive in a demo, so it always loses the schedule to new features. The other layer is the capability ceiling criterion coming back (the criterion named in Chapter 10, engineers look at what a model can do, enterprises look at what an error looks like when it is wrong), "we have an LLM now, what do we need rules for," and the rules layer gets deleted as transitional scaffolding. But the rules layer is an asset, not scaffolding (Chapter 10). The discipline. Every AI dependency point registers its fallback and really drills it before launch.

**2. Monitoring that looks only at uptime, that is, availability.** Availability is 100% month after month while suggestion quality has been drifting for three weeks, and the first to notice is Linda's hunch. The monitoring list is inherited from traditional software, uptime, error codes, resource usage. That system has no place for "quality drifting silently," because traditional software's behavior does not change while the code stays the same. When the quality ledger is missing, an all-green dashboard is precisely the most dangerous thing. A system 100% online does not mean it is still saying the right things. The discipline. Online eval sampling and drift alerts launch at the same rank as uptime monitoring, not in phase two.

**3. Cost noticed only after the fact.** The month-end bill is the only cost monitoring. A bill settles monthly, so the feedback is thirty days late by nature. The more structural layer is ownership. In an organization the bill belongs to Finance and the code belongs to engineering, so "cost per claim" is on no engineer's instrument panel, and a number nobody owns does not get managed. The discipline. The cost instrument produces numbers daily, split by step, and breaching the budget line triggers a review the same day. The month-end bill is a cost autopsy. It cannot serve as cost monitoring.

**4. A budget set that nobody reads.** The four ledgers are standing, the one page has been handed over, and three months later nobody has opened it. The budget lines are set on paper, nobody gets woken when one breaks, and the owner column holds a job title instead of a name. The launch gate is passed once, the running accounts need someone reading them every day, and the two get treated as one thing. Deeper down, reading the numbers has no moment. Anyone may read them, which is the same as nobody reading them. The discipline. Bind every ledger to a named owner and a fixed moment for reading its numbers, with a breach landing in his inbox automatically. The test. Pick any ledger and ask its owner "did it break a line last week." No answer means that ledger is not running.

## Next Monday

1. Work out cost per claim for your system once, last month's call bill divided by the number of claims handled. Take the number to the system owner and ask "do you know this number." If he does not, the cost ledger has no owner yet.
2. Open your largest prompt and find the static blocks inside it (the manual, whole rule texts, piles of examples). Ask one question. Can these move into retrieval or a cache?
3. Pull the LLM dependency in the test environment for ten minutes and see what is left of the system. If the core process is not left, you have no degradation path. Go back to Chapter 10 and get back the dumbest thing that works, the one you deleted.
4. Run the launch gate once with the checklist in [Template 16](../appendices/template-16-production-readiness.md), and fill in the owner column of the four-ledger table. Whichever ledger you cannot put a name to is the address of your next incident.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 16 Next Monday actions. First run python3 templates/production-readiness/cost_dashboard.py
with the built-in sample to show me the four-ledger instrument, then open drift-alerts.json and trace-schema.json and explain every field. Then I give you
last month's call bill and the number of claims handled, and you only work out cost per claim. Whom I take the number to is mine to decide. Build Template 16's checklist as a table, with the four ledgers' owner column
filled in by me with real names, leaving what I cannot fill blank and flagged red. You may find the static blocks in my largest prompt. Whether they move is mine to decide.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The four ledgers of the running budget (cost / latency / error / degradation, each with one budget line, one action on breach and one named owner); the minimum observability set (end-to-end trace / online eval sampling / drift signals)
- **Templates.** [Template 16](../appendices/template-16-production-readiness.md), Production Readiness Checklist and Running Budget Sheet, the item-by-item launch gate, the four-ledger template (with the Anchor & Helm example rows), the degradation path register
- **Key judgments**
  - "The running budget has to be designed like a feature."
  - "Do not delete the dumbest thing that works. It is your degradation path."
  - "A system 100% online does not mean it is still saying the right things."
  - "The month-end bill is a cost autopsy. It cannot serve as cost monitoring."
