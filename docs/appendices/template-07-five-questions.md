# Template 7 · Five-Question Opportunity Rubric

> Companion chapter(s): Chapter 7. The three pieces are ordered by use. Score question by question first (7.1), then summarize and eliminate (7.2), then report (7.3).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 7.1 Five-Question Scorecard

One card per candidate use case. Score each question 1–5. **Any score with a blank evidence column is treated as a 2.** Numbers, users' own words, and data samples count. Adjectives do not.

**Blank scorecard** (the card header carries the candidate use case name / scorer / date):

| Question | Score (1–5) | Evidence (numbers / users' own words / data samples) |
|---|---|---|
| Pain | | |
| Data | | |
| Decision | | |
| Risk | | |
| ROI | | |

### Question 1 · Pain

**Test question.** Whose action is bleeding? Is the bleed rate (loss per unit of time, hours, complaints, fines, churn) measurable? The implication follow-up. If it goes unfixed for three months, what happens? Who suffers?

| Score | Anchor |
|----|------|
| 5 | A specific person + a specific action + a measured bleed rate; leave it and someone keeps taking blame or paying out |
| 3 | The pain is real, but the bleed rate has not been measured. Measure it first, then come back and score |
| 1 | Cannot name the person or the action; or after the follow-up "what happens if it is not fixed," the answer is "not much" |

**What the evidence column requires.** Users' own words / ticket volume / waiting time / complaint records. "Everyone feels that way" is not allowed.
**Note.** A candidate whose pain vanishes under the follow-up (for example, "nobody reads the monthly report closely") is not a regrettable low score. It is this card's most valuable output.

### Question 2 · Data

**Test question.** What data does this action need? Does it exist? Can you get it? Can you trust it? (A pre-check here. The full grading method is the data fitness ladder in Chapter 9.)

| Score | Anchor |
|----|------|
| 5 | Data exists, the business owner is named, samples are in hand, spot checks hold up |
| 3 | It exists and is reachable, but trustworthiness is unverified. A conditional pass, with the reconciliation or validation action and its deadline written down |
| 1 | The key data does not exist, or there is no realistic path at all to getting it |

**What the evidence column requires.** Data samples / field spot-check results / the name of the data's business owner. "The business unit says it is all there" does not count as evidence, and neither does "we assumed it was all there" (Chapter 9 will tell you what that sentence is worth).

### Question 3 · Decision

**Test question.** Which decision point in the real workflow does AI enter? How many times may it be wrong at that step? Who backstops it, and how fast does the error surface?

| Score | Anchor |
|----|------|
| 5 | It enters at the advise layer; the backstop is named; errors are visible on the spot and can be overridden |
| 3 | There is a backstop, but discovery of the error is delayed, or the backstop has not yet confirmed |
| 1 | Real-time and outward-facing with nobody backstopping; or a decision with near-zero error tolerance (money, compliance, safety) executed directly by AI |

**What the evidence column requires.** Where the decision point sits in the real workflow (the output of the field archaeology in Chapter 6, not its position on the official flowchart) + the backstop's name.

### Question 4 · Risk

**Test question.** What does the worst single output look like? Does it reach only inside, or customers, regulators, money? Can the loss be closed out (found, corrected, made good)?

| Score | Anchor |
|----|------|
| 5 | The worst output's loss stays inside and can be closed out, and it sits outside the agreed red lines |
| 3 | There is a path outward, but a gate sits on it (human review, delayed sending, an amount cap) |
| 1 | One bad output can reach a customer, a regulator, or money, and it cannot be taken back |

**What the evidence column requires.** Write out the imagined text of that "worst output" word for word (for example, "Your loss assessment payment is expected within three business days"). If you cannot write it, you have not thought about it seriously.

### Question 5 · ROI

**Test question.** What is the North Star outcome metric? What is the arithmetic that turns the improvement into money? Who owns that bill?

| Score | Anchor |
|----|------|
| 5 | An outcome metric + the conversion arithmetic + a person willing to carry that number in his own reporting |
| 3 | The metric is measurable, but the conversion is rough or the person owning the bill has not confirmed |
| 1 | Only activity metrics ("it launched," "92% accuracy"). Chapter 1 covered why they do not survive the boardroom |

**What the evidence column requires.** The arithmetic itself, and the name of the person who owns the bill.

---

## 7.2 Elimination Table

All candidates summarized on one table:

| Candidate | Proposed By | Proposer's Rank / Does He Control Your Budget | Pain | Data | Decision | Risk | ROI | Lowest Score (Which Question) | Conclusion | Referral Route (Fill In When the Conclusion Is Elimination) | Condition / Re-evaluation Condition (Who Rechecks It, at Which Standing Meeting) |
|------|--------|--------------------------------|------|------|----------|------|-----|------------------|------|------------------------------|----------------------------------------|
| | | | | | | | | | Winner (conditional) / Eliminated / Needs more evidence | Refer to a standard tool / Refer to self-serve / Refer to an outside purchase (with ops ownership) | |

**Seven hard rules:**

1. **Any question scoring ≤2 is eliminated outright.** No weighting, no averaging, no "considering it in the round." The five questions stand in a multiplying relationship. One factor close to zero makes the product zero whatever it multiplies. Wherever you see a "weighted total" row, delete it.
2. **A 3 = a conditional pass.** The condition (what evidence to add, what validation to run) goes into the table with a deadline. Not met by the deadline, it drops to 2.
3. **Elimination ≠ never.** Every eliminated candidate gets one line of re-evaluation condition, what evidence, if it appears, makes it worth running the five questions again. The re-evaluation condition also needs a recheck owner and a place to be rechecked. Writing it down is not the same as being remembered, and a re-evaluation condition nobody rechecks is a politely worded permanent refusal. The default is to hang the elimination table on the team's quarterly ask review and read it out each quarter. "Not now" needs an exit before elimination can be enforced at all.
4. **The evidence column is all that counts.** In 7.1, any score with a blank evidence column is treated as a 2. Imagined scores are this table's most common forgery.
5. **Eliminating everything is a legitimate result.** Write the conclusion as "back to discovery to find an opportunity," not "loosen the standard and screen again."
6. **Do not mix the scales.** This table's 1–5 screens opportunities (you are the scorer, the logic is finding the weakest link). The Field MVP's pass / concern / unsafe / useless is for real users testing a single output. The two scales are not interchangeable.
7. **Elimination needs an exit.** Every row concluding in elimination also gets a referral route, refer it to a standard tool, refer it to self-serve, or refer it to an outside purchase with ops ownership written down. Leave it blank and the one who feeds it from then on is you.

**Worked example** (the three Anchor & Helm candidates, the full working is in Chapter 7):

| Candidate | Proposed By | Proposer's Rank / Does He Control Your Budget | Pain | Data | Decision | Risk | ROI | Lowest Score (Which Question) | Conclusion | Referral Route | Condition / Re-evaluation Condition |
|------|--------|--------------------------------|------|------|----------|------|-----|------------------|------|----------|------------------|
| Service chatbot | The board (forwarded by Grant Whitmore) | Top level, does not directly control your team's schedule | 3 | 1 | 2 | 1 | 3 | 1 (Data / Risk) | Eliminated | / (none of the three ready-made routes applies, gather evidence first) | Re-measure the call mix after exception handling is cured; the standard-answer library gets built (recheck owner, you; where, the team's quarterly ask review) |
| Automated monthly reports | Kevin Doyle | Business unit head, does not control your team's budget | 1 | 3 | 4 | 4 | 2 | 1 (Pain) | Eliminated | Refer to self-serve (turned into a favor done in passing, forty minutes' worth) | No project approval (recheck owner, you; where, the team's quarterly ask review) |
| Exceptions action queue | The Field MVP readout | Not applicable (produced inside the team, not an individual's proposal) | 5 | 3 | 4 | 4 | 4 | 3 (Data, conditional) | Winner | / | Finish the core system × Excel data reconciliation during discovery (recheck owner, you; where, a precondition for pilot launch) |

---

## 7.3 Reporting One-Page Format

For reporting the screening result to the sponsor. One page, answer first:

```
Conclusion. [winning candidate] moves into charter negotiation / discovery.
      One-sentence reason + one number (example, "about six tenths of the waiting time is 'waiting on documents with nobody chasing,' and the queue can eat half of it").

Candidates and results. The full elimination table (with scores and which question the lowest score sits on).

For each eliminated candidate, three lines.
  Cause of death. Question X, N points.
  Evidence. The single hardest piece of evidence (a number / a quote / a sample), not an opinion.
  Re-evaluation condition. What evidence, if it appears, triggers a re-evaluation.

Next step. The winning candidate's time box, the data access and staffing it needs
        (this column is the input to the charter negotiation, see Chapter 4).

Opportunity cost, the other things this team is not doing because of it (the candidates ranked behind, which row each is stuck on, which quarter each waits for, written for the sponsor and for the department that ranked behind).
```

**Facilitation rules:**

- **Language.** Do not say "I do not recommend it." Say "the evidence says not yet." A position gets haggled over, and evidence can only be rebutted by better evidence.
- **When eliminating an executive's proposal.** Let the table speak and read only the evidence column, and give him one sentence he can repeat upward (example, "treat the source of the calls first, and the foundation for service automation gets laid along the way"). What he needs is not to be persuaded. It is a reason he can pass on.
- **Say it in person. Do not fire the table off by email.** Eliminating someone's idea is a trust event, not an information transfer (Chapter 5).
- **One page, no more**, and the most an attachment may be is the 7.1 scorecard itself.
- File the elimination table after the report. An internal elimination table has to live for years, not three months, so when the subject comes back up, what you open is the evidence and the re-evaluation condition from the time, not your memory.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/five-questions/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/five-questions/): the scoring tables for this rubric and the script that generates the reporting one-pager
