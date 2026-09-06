# Template 25 · Intake Rubric, Red Line List, Saying No Scripts, Kill Register

> Companion chapter(s): Chapter 25. The four tools are in order of use. A candidate project clears the red lines first (25.2, any one vetoes), then gets scored (25.1). When the ruling is no, use the conversation script (25.3). Once it is said, it lands in the register (25.4) for a retrospective a year later.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

## 25.1 Organization-Level Intake Rubric (Five-Dimension Scoring Table)

**Relation to the Chapter 7 five-question sheet.** The five questions assess "is this use case any good" (the deliverer's personal tool in the field), and the intake rubric assesses "can this organization carry it, is it worth carrying" (the gate at the team's door). The five questions' Risk column is promoted here into a red line (25.2) and no longer gets scored.

**Scoring rules.** 1–5, weakest-link logic (same as the Chapter 7 elimination table). Any dimension ≤2 does not enter the schedule, and a re-evaluation condition gets written. A 3 is a conditional pass, with the condition and the deadline written into the sheet. No weighting, no averaging. The evidence column takes only numbers, users' own words, and samples.

**Where the gate's force comes from** (fill this in first, or the rubric is only talking to itself; pick one of the three and name the carrier it hangs on)

- Hang it on the company's existing project approval review / architecture review / quarterly ask review (name the meeting)
- Endorsed once by the CIO or the responsible head
- Written into the company's AI governance policy

| Dimension | Test Question | What a 1 Looks Like | What a 5 Looks Like |
|------|----------|-----------|-----------|
| Strategic value | Win it, and what does the organization get? One department's thanks, or agenda power and standard-setting power over a class of problem? | A single department's goodwill, with no organization-level benefit you can state | It opens a repeatable class of problem, and the ROI arithmetic has a business owner who stands behind it |
| Data readiness | How far do the key data exist, how reachable are they, how far can they be trusted? Have they been reconciled? | The key data do not exist, or there is no realistic path to getting them | Samples in hand, a reconciliation conclusion, a named data owner |
| Owner in place | Is there someone on the business side who signs for the outcome? Who backstops the errors, who maintains it after launch? | "Once it launches someone will look after it" | A named owner has been through the meeting and has claimed actions |
| Production path | Do review, oversight, and change discipline get through? Or can only the demo live? | No path through security or compliance review, no oversight headcount in existence | The review path is agreed, and the oversight role and its hours are committed |
| Reuse potential | What gets banked into the pattern library (Chapter 23)? How much cheaper is the second delivery? | Pure custom work, the judgment structure does not transfer | The skeleton transfers, and halving the cost of the second delivery has a basis |

**Note on owner in place.** No written agreement can force the business side to produce a signer, so forcing out a named owner runs on a resource trade. You want our people and our time, so first give us the person who signs for the outcome after launch, name into the project approval resolution. No name, and this dimension scores 1, and by weakest-link logic it does not enter the schedule.

**Scorecard** (one per candidate; a 3 row must fill the "Condition / Deadline" column, same convention as Template 7.2):

| Dimension | Score (1–5) | Evidence (numbers / users' own words / samples) | Condition / Deadline (a 3 is a conditional pass, required) |
|------|-----------|---------------------------|----------------------------------------|
| Strategic value | | | |
| Data readiness | | | |
| Owner in place | | | |
| Production path | | | |
| Reuse potential | | | |

**Anchor & Helm example, full automation (loss assessment and payout approval), week 28**

| Dimension | Score | Evidence | Condition / Deadline |
|------|-----|------|-------------|
| Strategic value | 5 | The only path to another notch off claims cost; a board agenda item | / |
| Data readiness | 2 | Loss assessment data (repair hours / parts prices / image reading) not reconciled; what the queue reconciled is only process status data | / (≤2 does not enter the schedule, write a re-evaluation condition) |
| Owner in place | 2 | "Who signs for a loss the AI set" went unclaimed | / (same) |
| Production path | 1 | The regulator's line is not out, and Victor Reyes (Head of IT Security and Architecture) is clear that the review does not pass | / (same) |
| Reuse potential | 4 | The estimate assist component reuses across lines of business | / |

> Note. This example never really gets as far as scoring. Red lines 1 and 3 are already triggered (see 25.2), and the veto comes first. Scoring it anyway has exactly one use, seeing which dimensions the alternative path has to rebuild (data readiness → reconcile the loss assessment data; owner → land a payout signer; production path → wait for the regulator's line, build the oversight capacity). The steps get built up from the low-scoring dimensions.

## 25.2 Red Line List

| # | Red Line | Test Question (One Line) | Anchor & Helm Instance |
|---|------|------------------|----------|
| 1 | Automated decisions at an irreversible-harm step | Can the harm from the single worst output be taken back? | "Never touch payout decisions" (Chapter 8) is this one's instance. A payout decision is irreversible the moment it takes effect |
| 2 | A move of decision rights with no human oversight capacity behind it | After the move, is there still someone with the time to look, the ability to judge, and the authority to stop it? (the three oversight questions, Chapter 12) | With the payout approval team having no spare capacity to review every AI loss estimate, raising "assist" to "automatic" crosses the line |
| 3 | Outward-facing output in a regulatory grey zone | When that output causes a dispute, what do you answer the regulator with? | An insurer's outward statements are regulated. Nothing goes outward before the line on AI payout approval is clear |

**The three rules of "red lines do not enter the scoring sheet"**:

1. Any one vetoes. Not scored, not weighted, not compensated by any high score. The meaning of a scoring sheet is trade-off. The meaning of a red line is boundary.
2. Adding or removing a red line is not the project team's vote. It is re-argued only as the external source changes (the regulator gets clear, the oversight capacity gets built, a reversal mechanism appears), and the re-argument leaves a trail.
3. Keep the red lines few (three or so). Every extra fake red line that could have been scored dilutes the veto force of the real ones.

## 25.3 Saying No Scripts

> **A script is a crutch, not a line to recite.** Use your own words, but keep the function of every sentence (same convention as Template 20.2).

**Step one, affirm the goal** (declare that what you refuse is the path, not the intention)

- "The half sentence before the conclusion. You have not got the direction wrong, and this is the road we have been laying all along." (Function, catch the goal, so the refusal earns the right to begin)
- "We get to this goal sooner or later. What we are settling today is which road and when." (Function, switch the question from whether to do it to how to go)

**Step two, state the evidence** (the rubric goes on the table, read the evidence item by item)

- "This is the sheet we use for intake. Going through it, the evidence on [dimension] is [numbers / users' own words / samples]." (Function, let the sheet talk, you only read it out)
- How to put Risk. "The single worst output is [concrete scenario]. That account, [regulatory / brand / customer, whichever the other side cares about most], you know better than I do." (Function, put risk in the other side's ledger, not in model probabilities)
- The banned lines. "The model will make mistakes." "AI is not mature enough." Both demote a judgment question into a technical one, which invites the other side to rebut you with "then get a stronger model."

**Step three, offer a path** (a step plus conditions; an unconditional "no" is a refusal, a conditional "no" is a roadmap)

- "What I recommend is not dropping it, it is rebuilding the steps. First do [the assist form one layer down], with the condition nailed down. [Measurable threshold] met, [which class of decision] moves up one layer, each layer decided on its own." (Function, turn the "no" into a "yes" with milestones)
- "I am putting this into the register, and the revival condition is [an event, not a date] (how to write it, Template 8). When the day comes you will not have to raise it, I will." (Function, turn the promise into a trail anyone can check)

**Banned throughout**. "The schedule is full" (delay is not refusal) / "This cannot be done" (an unconditional "no") / a "policy does not allow it" that cannot name which policy (it outsources the judgment to the institution, and the other side goes looking for whoever can change the policy). Borrowing external hardness for a red line is fine. If you can name the regulation number or the policy clause, name it. A "policy does not allow it" that cannot say which clause is a shield, not a red line.

## 25.4 Kill Register

| Project | Proposer | Kill Reason | Revival Condition (events, not dates) | Retrospective Conclusion a Year Later |
|------|--------|-----------|---------------------------|----------------|
| Full automation (loss assessment and payout approval) | Grant Whitmore | Red lines 1 and 3 triggered; data readiness 2 | Estimate assist override rate <10% and the regulator's line clear, re-argued layer by layer | (to fill) |
| Service chatbot | The board (forwarded by Grant Whitmore) | Eliminated in Chapter 7, Data 1 / Risk 1 | Re-measure the call mix after exception handling is cured; the standard-answer library gets built | (to fill) |

**Retrospective discipline** (once a year, two questions per row):

1. Did it get built later, here or somewhere else? How did it go?
2. Did the revival condition come true? Once it did, did anyone re-score it?

**The fifth column's three conclusions**. The kill was right (built elsewhere, and it died of the cause predicted back then) / the kill was wrong (the condition came true long ago with nobody re-scoring, or the predicted cause of death never happened) / the evidence has changed (back through the rubric).

**The rubric's own eval** (the spirit of Chapter 11, the judgment that judges intake also has to be judged). Whichever dimension the wrong kills cluster on is the dimension whose test question you fix. A register that stays empty for a long time is also a signal. Not that every judgment was right, but that the gate is not working.

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/intake/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/intake/): table samples for the five-dimension scorecard and the red line checklist; kill register sample
- [`templates/intake/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/intake/): lightweight script sample for revival condition due reminders (register scan plus event-triggered prompts)
