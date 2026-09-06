# 18 · Launch and Measure: Prove the Gain, Not the Trend

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-18-metric-tree.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The system is live and the numbers are moving. How do you get everyone to believe the system deserves the credit? An incident happens. How do you keep one error from eating months of banked trust?
>
> **What You Will Be Able to Do.** Use the three layers of a metric tree to turn "the system is improving things" into defensible evidence. Use an eight-week baseline plus a run chart to tell fluctuation from change. Write the AI incident runbook before the incident happens, so the first incident is handled by process, not by mood.

---

## Pilot Week 5, Two Pieces of News in the Same Week

It is pilot week 5, project week 14. On Monday the weekly numbers come out. First-touch handling time for auto exceptions is down 18% against the pre-launch baseline. The monthly report to Grant Whitmore is booked for Friday, and that number was going to be the star.

The launch itself went smoothly. The pilot started on Monday of week 10. Before it started, the security review packet from Chapter 12 was updated to a launch version and served a second time, the same document used once more, with monitoring definitions and a rollback path (rehearsed once) added, signed by Victor Reyes, and filed as launch gate material.

On Wednesday at 10:40 in the morning, something else happened. The queue suggested one claim as routine. Linda Marsh glanced at it, overrode it in the Human Call column, picked the reason code "risk judgment differs," and wrote two words in the note. Repair shop. At the system level this is one override. At the organizational level it is a bomb. By eleven, the claims department was passing around "the AI waved a fraudulent claim through as routine." By lunch the version had evolved into "the AI got it wrong," and the rumor had dropped the half sentence "and Linda caught it."

So you are carrying two things into Friday's meeting room. A proof problem for the good news. On what grounds do you say the -18% is the system's doing? A trust problem for the bad news. How do you keep one error, one that was caught, from defining this system's reputation? These two things are the whole of the work in the launch period.

## Why This Is Hard: Numbers Fluctuate, and Memory Is Asymmetric

Proving is hard because operating numbers fluctuate by nature. The mix of claims shifts, people rotate, seasons move, and first-touch handling time rises and falls every week. Between "it went down after launch" and "it went down because of the launch" lies the whole of statistics. If you do not deal with that, sooner or later someone will deal with it for you. The week the number bounces back, someone will say, "See, it never had anything to do with the system."

Trust is hard because organizations have an asymmetric memory for AI incidents. An 18% improvement is remembered for three days, one incident for a year. The reason is structural. An incident is a story. It has a claim number, characters, and a "that was close" plot, and it can be retold in full over lunch. An improvement is a statistic, a curve drifting slowly downward, with no plot, and nobody retells it. People spread stories. They do not spread distributions.

So the real work of the launch period is two things. Turn the improvement into defensible evidence, and turn the incident into a recoverable process. The first relies on measurement discipline, the second on a runbook written in advance (the procedure manual for handling incidents, unfolded in framework two). The common enemy of both is improvisation.

## Prior Art, and What AI Changed

**The discipline of measuring improvement comes from healthcare quality improvement.** The tool first. A run chart is a chart of points plotted in time order with the baseline median as a reference line (you saw one in Chapter 14). *The Health Care Data Guide* (Provost and Murray, paraphrased here) faces a problem with exactly your shape. Clinical metrics fluctuate by nature, and "this improvement saved lives" has to be defensible. Their method uses two tools. The run chart is one. The other is a pair of distinctions, common cause variation (the random rise and fall built into the system) and special cause change (the signal of a structural change, for example six consecutive points on the same side of the median). The discipline is one sentence. Build the baseline first, and claim improvement only when a special cause signal appears. A line drawn between two points gives you no trend, only an illusion of slope.

**The discipline of incident handling comes from SRE (site reliability engineering, an operations discipline).** Tiered response, notice within a time limit, blameless retrospectives. An incident is a learning asset, and shame does not help, provided the incident is caught by a process rather than by emotions.

The AI era changed two things. First, monitoring gained a layer specific to AI, the monitoring surface. Most of it is what earlier chapters already settled, carried over as it is. The override rate and its sudden-change alerts. The error category distribution taken online (the threshold table of Chapter 11 becomes the monitoring definitions as is). Golden cases replayed on a cadence. Drift signals (the signs of the system's results quietly degrading over time, the minimum observability set of Chapter 16). The fuel all comes from the decision trail of Chapter 17.

Second, the incident retrospective gained a question that did not exist before. Was the error in the model, the data, the rules, or the interaction? The four layers have completely different repair actions. Attribute it to the wrong layer and the repair fixes the wrong place.

Together, these two are the same defense in a different state. AI uncertainty management, the one skill this method adds of its own (the single new skill Chapter 2 named), was delivered by Chapter 11 in its design state, the defense drawn on the blueprint and in the eval, with nobody yet watching it every day. This chapter delivers its operating state, the same defense standing watch in production through the monitoring surface and the runbook.

## Framework One, the Metric Tree Plus Baseline Discipline

A metric tree splits "is the system improving things" into three layers, with every metric carrying an owner and an action. The table below runs through the three layers, North Star, process, and balancing. The process layer has the most mechanisms and involves the most people, so that row is the longest.

| Layer | Question It Answers | Anchor & Helm Instance | Owner | Action on Deviation |
|----|-----------|----------|-------|----------|
| **North Star (outcome)** | Did the improvement happen | First-touch handling time (the charter North Star, Chapter 4), shown on a run chart | You + Kevin Doyle | Two consecutive points back above the baseline median → go through the process layer for the cause |
| **Process (mechanism)** | Why the improvement happened, where the lever is | Queue aging (count of overdue claims not moved), missing-document detection lead time, override rate (split by suggestion category), status-in-doubt list length (Chapter 9's operating item, owner Kevin) | Linda Marsh (team lead), your team's engineer (renamed line by line at handoff), you, Kevin, in the same order as the left column | Over the line → claimed and cleared the same day; lead time shrinks → check the extraction pipeline; a sudden change in one category → trace back that category's rule implementation and list version; continuous growth → re-check the review team's ten-minutes-a-day status cleanup discipline |
| **Balancing (cost)** | Did the improvement shift the cost | Complaint rate, reviewer overtime hours | Kevin | Rising → check chase scripts and frequency; rising → check the queue's daily volume setting |

Three rules. **First, there is one North Star, and it comes from the charter.** No setting up a better-looking one after launch. **Second, every metric must have an owner and an action.** Who does what when the metric moves is written next to the metric. A metric with no owner and no action is only scenery. **Third, balancing metrics are shown on the same page as outcome metrics.** The balancing layer guards against pressing the problem down here and having it pop up over there. If handling time fell because every reviewer worked an extra hour a day, or because chasing drove customers up the wall, that is shifting the cost, and it does not count as improvement. The victims of a shifted cost are usually not in the reporting meeting. Only the metric speaks for them.

The second rule has a hurdle inside a company. Most process layer owners do not report to you. Queue aging belongs to Linda, the status-in-doubt list and both balancing metrics belong to Kevin, and their schedules are set by Claims Operations, not by you. So actions like "claimed the same day when over the line" cannot hang on your reminders. Get the whole metric tree onto the business department's own weekly meeting agenda, and get the claiming actions written into their team SOP. An action written into the SOP is their job at review time. An action sitting in your email is only your request.

The override rate in the process layer deserves its own mention. It is the last net for the errors eval cannot catch. Chapter 17 already showed it, when the 78% override rate on "prior claim linkage" suggestions exposed a condition the implementation had missed.

One more item hangs on the monitoring surface, the fairness spot check pre-planted in Chapter 12, the sentence written into the fairness row of the trust constraint matrix. The override distribution is spot-checked by customer segment every quarter, with the first check scheduled for the end of the first quarter after launch. It guards against the system systematically treating one class of customers worse with nobody noticing.

**Baseline discipline** in three sentences. The baseline is built before launch. Anchor & Helm used eight weeks of history, corrected claim by claim through reconciliation (Chapter 9's reconciliation paying off a second time, which is to say it gets used once more; without the correction, the baseline itself stands on distorted status fields). The run chart is kept up continuously, with the median as one reference line. Improvement is claimed only when a special cause signal appears.

In the launch period, the internal deliverer has three advantages to take, and they only count once written down as actions. The baseline does not have to wait for the business side to export data for you. Pull the eight weeks of history from the data warehouse yourself, and a median line is up the same day, so "nobody knows how slow it used to be" finds no excuse inside a company. You can hear the rumor first. On the day of the incident, standing in the claims department's work area for ten minutes gets you there half a day before it reaches your reporting line. The notice has to be drafted within two hours, and the calm of those two hours is bought with that half day. The run chart does not need a meeting of your own. Hang it on the claims line's existing business review as a fixed agenda item. That works better than chasing people to look at a chart every month.

## Framework Two, the AI Incident Runbook

The AI incident runbook is the handling process written before the incident happens. Levels, notice, retrospective, flow-back. The word "before" is the whole point, for the same reason as the kill criteria of Chapter 14. The process is written while calm. It cannot be written on the day of the incident.

**Levels.** P1 to P3 are response levels. They set how soon there must be action and who must be alerted, and they govern how fast someone takes charge. They are a separate numbering from unsafe / concern / useless, which governs how severe the error is. An unsafe-class error entering human view is P1, and it runs the full course of same-day notice plus a time-limited retrospective. Being caught does not downgrade it, because what caught it was already the last line of defense. Concern-class errors over threshold or appearing in batches are P2, retrospective the same week. A rising trend in useless-class errors is P3, folded into the monthly retrospective.

**The same-day notice** has three parts, and the order cannot change. Part one, the defense held. State first that the interception mechanism worked as designed, then the error itself. Part two, the scope of impact. How many claims, and whether there were real consequences. Part three, root cause under investigation, with a deadline for the retrospective. Drafted within two hours, sent the same day, with the distribution drawn by "how far the rumor can reach." Inside a company that line has to be drawn wider. You lack the buffer an outsider has. The person sending the notice is the person being talked about, and if you do not send it, someone sends it for you. Putting the defense first is the correct order of the facts, and has nothing to do with PR spin. This system's design premise is that AI will make mistakes and the Human Call column backstops them (Chapter 12's three oversight questions, Chapter 17's queue design). The incident is precisely the moment the design is validated.

Who issues the notice is a separate question inside a company. You hold the drafting right. The business-side owner holds the issuing right, and at Anchor & Helm this notice was signed by Kevin Doyle. The reason is the same as for the governance pledge of Chapter 20 (that chapter goes into detail). Only the person with the power to violate it can issue it. Your signature does not count. Send it out alone and the three parts read as the technical team defending itself. With Kevin's name at the bottom, the sentence in part one, that the defense worked as designed, becomes the claims line's own judgment. The price is that he has the right to edit the draft. The one thing you hold the line on is that the order cannot change. Move the scope of impact ahead of the defense, and this notice turns from fact into spin.

**The four retrospective questions.** The investigation runs in a fixed order. Was the model layer wrong (long-tail judgment falling short)? Was the rule layer wrong (a rule missing, or the implementation drifted)? Was the interaction layer wrong (a person saw it but had no time, no basis, or no authority to stop it)? Was the data layer wrong (input, list, or fields incorrect)? The first three questions are all elimination. Only when you have asked your way down and none of the three layers was wrong does the data layer come up, and by then the three eliminated layers are the evidence for the attribution. Wherever the fault is located, that is where the repair goes. Model layer, switch pattern or add review. Rule layer, change the rule and release a new version. Interaction layer, change the queue design. Data layer, fix the data and add operating discipline.

**Flow-back.** The incident case goes into the golden cases permanently within 24 hours (the historical incident category of Chapter 11, where the flow-back mechanism of the human review path left the interface ready long ago). Incidents go onto the ruler, meaning that once in the eval they become a lasting test standard, and from here on that is a fixed process. The kill criteria are checked by the book and recorded, whether or not they trigger.

Flow-back has to land on names. The easiest slip inside a company is for it to stall at "incident handling belongs to operations, eval belongs to development." The incident record closes on the claims line, and not one golden case gets added on your side. Anchor & Helm wrote this item with real names. Linda rules at the retrospective on which category the incident case goes into, you add it to the golden cases the same day and countersign in the incident record, and if either name is missing the loop is not closed. After you step out of the daily, this item is handed over under the three AI items going platform-level (Chapter 22 goes into how), and what receives it is the platform's eval capability, not "someone will always look after it."

## At Anchor & Helm: Forty-Eight Hours of One Incident, and One Honest Run Chart

**Wednesday, 12:10, the notice goes out**, less than two hours after Linda's override, to the whole claims department, Kevin, Grant Whitmore, and Victor Reyes.

> This morning the queue suggested a high-risk claim as routine. The review team lead caught it in the Human Call column and overrode it to high risk. That column exists to catch exactly this kind of error. The defense worked as designed, and the full trail is on record. Scope of impact. No real action was taken on the claim. Today's queue has been checked, and there is no error of the same shape. Root cause under investigation, retrospective conclusion within 48 hours.

In the afternoon the rumor changed versions. "The AI got it wrong" became "the AI got it wrong, but Linda caught it, and that is how the system was designed." Which version of an incident the organization remembers is set in the first two hours. Let the notice run a day behind the rumor and you spend a quarter correcting that version.

**Thursday, the retrospective.** You, Linda, Kevin, and the claims-ops IT engineer go through the four questions. The model layer? The long-tail judgment really was wrong, but the amount sat right at the top of the usual range, the claim was reported the same day, the photos were complete, and there was no prior claim linkage. The input held no usable signal, and a stronger model would still be guessing. The rule layer? The implementation of the five rules was checked line by line against the annotation guide. No drift. The interaction layer? Linda had the time, the reason column, and the authority. All three questions pass, and the successful catch is itself the evidence. The data layer? Hit. That repair shop registered only last month. Linda said at the meeting, "The address is right next door to the one I crossed off. The owner changed the name. How is my list supposed to keep up with that?"

In Chapter 6 she already said it, "it is not a fixed list. I crossed one off just last month." Chapter 11's annotation guide got its dated version because of that sentence. Back then it was a maintenance cost. Now it is the prophecy of an incident's root cause. The list drifts, a fact this system knew from day one and had not yet scheduled into operations.

Attribution decides the repair path. The retrospective locates the data layer, and the repair action follows. The list is promoted from Linda's rolling mental list to an operating asset with an owner. Her team updates it monthly, it goes into the annotation guide's dated version, and it becomes a config item the claims-ops IT engineer can change (the maintainability row of Chapter 15). The queue adds a weak-signal prompt for newly registered repair shops not on the list. Not high risk, only a prompt, "new entity, not on the list."

One more thing lands without waiting for the repair. The ADR memo to Grant Whitmore promised in black and white (Chapter 13) that if a single missed-risk case appears during the pilot, the whole category of suggestions is downgraded to human review. That week it is executed by the book. All risk-class suggestions go to human review until the repair passes a golden cases replay.

The incident case goes into the golden cases that day, kept permanently. Then, in front of everyone at the retrospective, you do something some people think unnecessary. You pull out the kill criteria written in Chapter 14. Two or more unsafe-class errors in a single week means pause and rework. This week, one. Not triggered, keep running, and the check goes into the incident record. "Why check if it did not trigger?" Check even when it does not trigger. The value of checking is in the act of checking every time. Each time the stop clause is executed in earnest is the only proof that it has teeth.

**Friday, the report.** The one page for Grant Whitmore is a run chart. An eight-week baseline, the median as one line, and all five pilot weekly points below the median, an average drop of 18%. On the chart the baseline points scatter above and below the reference line, and the pilot points are all below it, still one point short of a signal.

```
First-touch handling time, weekly median, all points

Baseline, eight weeks       Pilot, five weeks
  ·     ·      ·     ·             baseline points, above the median
─────────────────────────────      baseline median, the reference line
 ·   ·     ·      ·                baseline points, below the median
                   ·  ·  ·  ·  ·   pilot weekly points, all five below the line
                                  ○ next week's sixth point, a signal only on the same side
```

You told him three things honestly. First, by the rules of improvement measurement, five consecutive points are one short of a shift signal. Only if next week's sixth point is still below the line does this 18% stand. Second, there is still a gap to the charter's -30%, and the next step on the gap is chasing missing documents earlier. The process layer's detection lead time still has visible room, and that is next month's main push. Third, one unsafe-class incident occurred this week. Caught, reviewed, added to the golden cases, kill criteria checked and not triggered.

Grant looked at the chart for a long time and said, "The last person who told me 'one point short does not count' was Audit. Keep running. Tell me the day the sixth point comes in." Then he added two operations staff on the chase side for Kevin. More trust, not blame. Those two people did not appear out of nowhere. What Grant could settle on the spot was only a move within Claims Operations, shifting people from another team to the chase side with total headcount unchanged. Adding two actual heads waits for the annual headcount review, a round of request and approval, slower than you would think. Resource commitments inside a company come in these two kinds. The one honored on the spot is moving people. The one that queues is adding headcount. When you hear a commitment, ask which kind it is first.

This is not luck. This is compound interest. The reliability term in the Trust Equation's numerator is built up one "said it, did it" at a time (Chapter 5). The harder backing comes from the charter. Nobody suspects you of dressing things up, because the clause that takes the resources back has been on the table all along, the charter's resource reassessment conditions (Chapter 4), and like the kill criteria checked by the book on Wednesday, it was gone through by the book this week and did not trigger. The thirty seconds of awkward silence when the exit conditions were written in Chapter 4 paid off all their interest at this moment.

This run chart and this retrospective record will not be used only once. They are ready-made raw material for the impact memo of Chapter 19 (that chapter goes into detail). The evidence you need at closeout is already banked this week.

## Failure Modes

Four, matching the four links of reporting, incident handling, balancing metrics, and attribution.

**1. Screenshot reporting.** Pick the week with the best-looking number, make it a slide, and leave out the weeks it bounced back. The reporting chain favors single-point good news at every level, and every retelling deletes some uncertainty. But trust is indivisible. Get caught once and every number loses credibility with it, including the true ones. The run chart is the antidote. Every point is on the chart, so you have no way to pick, and no way to be accused of picking.

**2. Incident silence.** Something goes wrong and it is digested internally first, "let's get to the bottom of it before we say anything," then a passive response three days later. The cost of the notice is immediate and concrete, and the risk of silence is delayed and probabilistic, the same time-discounting trap as Chapter 12's "our own tool" escape (quietly going live to dodge review). A small certain cost now outweighs a large probabilistic cost later. But rumor runs ten times faster than fact, and rumor always picks the worst version. Every day you stay silent is a day campaigning for the "AI is unreliable" narrative.

**3. Reporting outcomes only, ignoring balancing metrics.** Handling time fell and there is a big celebration, and the complaint rate and overtime hours are not in the monitoring at all. Balancing metrics measure the cost someone else pays for you, and the victims, the customers chased up the wall, the reviewers working overtime, are not in the reporting meeting. A shifted cost is invisible on every individual report. Three months later the complaints pile up into an event, and the improvement is given back with interest.

**4. Attributing to the wrong layer.** Something goes wrong and the model is suspected first, and a data layer problem gets repaired as a model layer problem. Attribute it to "the model is not good enough" and the next three weeks go to switching models, tuning prompts, and adding review gates, none of which fixes the point. The model layer is the easiest to think of and the easiest to touch, and one line of config lets you announce "we are fixing it." A data layer repair means finding an owner, setting an update cadence, and changing operating discipline. Slow, and it does not look like technical work. The four layers' repair actions do not transfer, and misjudge the layer and every hour is lost. The test. Write down the repair action from the last incident, see which layer it falls in, and check whether that is the same layer the retrospective record ruled on.

## Next Monday

1. Draw a metric tree for the system you have now. One North Star (from the charter), two to four process metrics, at least two balancing metrics, each with an owner and an action on deviation. If you cannot write a balancing metric, ask one question. Whom is this improvement most likely to shift its cost onto?
2. Check the baseline. If you are not live yet, start collecting baseline data today. If you are live with no baseline, start recording from today and say so honestly in the next report. An honest "no baseline" beats a fabricated comparison.
3. Use [Template 18](../appendices/template-18-metric-tree.md) to write a one-page AI incident runbook. What counts as P1, who the notice goes to, the four retrospective questions, how the incident case gets into the golden cases. Write it before the incident, like the kill criteria. It can be written while calm, and cannot be written on the day of the incident.
4. Run a drill. Take one wrong output from history, walk through the same-day notice template, and time it. The parts that run over are the parts to lock down in advance.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 18 Next Monday actions. First run python3 templates/metric-tree/run_chart.py
with the built-in sample to show me a run chart with the special cause marked. Then copy metric-tree.md to the working directory I name.
I will read you the North Star from the charter. The process and balancing metrics are mine to propose. You ask only for each one's owner and action on deviation, and mark what is missing [TBD].
If I cannot come up with a balancing metric, ask one question, whom is this improvement most likely to shift its cost onto. The P1 definition in the runbook is mine to write.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The three-layer metric tree (North Star outcome → process mechanism → balancing cost, every metric with an owner and an action); baseline discipline (eight-week baseline + run chart + claim improvement only on special cause); the AI incident runbook (unsafe is P1 / the three-part same-day notice / the four retrospective questions / the incident case goes into the golden cases permanently)
- **Templates.** [Template 18](../appendices/template-18-metric-tree.md), Metric Tree, AI Incident Runbook, Same-Day Notice
- **Key judgments**
  - "Organizations have an asymmetric memory for AI incidents. An improvement is remembered for three days, an incident for a year."
  - "The launch period has two jobs. Turn the improvement into evidence, and turn the incident into a process."
  - "The first sentence of the incident story is that the defense held."
  - "A metric with no owner and no action is only scenery."
  - "Attribution decides the repair path. The retrospective asks which layer failed first, and how to fix it second."
