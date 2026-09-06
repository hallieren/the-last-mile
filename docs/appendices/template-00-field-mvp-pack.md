# Template 0 · Field MVP Pack

> Companion chapter(s): Chapter 0. The five templates (0.1–0.5) follow the order of the two-hour process and can be copied and modified directly. 0.6, the red line declaration, is an input set before the clock starts and is not counted among the five.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 0.1 Workflow Claim

One sentence, two blanks:

> This system will change **[who: role and name]**'s **[which next action]**.

**Self-Check**:
- "Who" is a specific person you can book for 40 minutes, not a department.
- "Action" is something he already had to do today, not something new added to him.
- Cannot write it → go back and find the "who". Do not go further.

**Wrong → Right** (the first right example is from this book's Anchor & Helm case):
| Wrong (not a claim) | Right |
|---|---|
| Use AI to improve claims efficiency | Let claims reviewer Linda Marsh, on opening an exception claim, see directly what material is missing and whom to chase first |
| Build a knowledge base assistant | Let a newly hired customer service rep, on taking a refund dispute call, get a citable handling position within 30 seconds |

---

## 0.2 Case Table

10 representative cases. Adjust the fields to the scenario. The skeleton:

| # | Case ID | Current Status | Reason Stuck | Time Waiting | Key Context Fields (add or drop per scenario) | Source (real, de-identified / synthetic) |
|---|---------|----------|----------|----------|------------------------------|--------------------------|
| 1 | | | | | | |
| … | | | | | | |

**Case Selection Rules**:
- 6–7 typical claims + 2–3 edge cases + 1 case "even the front line finds hard."
- Mark the source of every case. **All synthetic data = the data feasibility hypothesis is entirely unvalidated**, and that must go into the Readout.
- Red line: no real, identifiable customer information. If de-identified data cannot be had, use AI to generate realistic synthetic cases.

---

## 0.3 Action Queue Prototype

One table is enough (Excel / any spreadsheet tool / a one-screen web page, do not spend more than 25 minutes on the interface):

| Case ID | Reason Stuck | Missing Item | Suggested Priority | Suggested Next Action | Owner | Reason | **Human Call** |
|---------|----------|--------|------------|------------|--------|------|--------------|

**Design Rules**:
- The "Reason" column is mandatory. Every AI suggestion must give a reason that can be challenged. That is the target of the scoring step.
- The "Human Call" column is the soul. It declares the system's position, **advising people, not deciding for them**.
- Every row must have an owner. A suggestion with no owner is a dashboard, not an action queue.

---

## 0.4 Scoring Sheet (Real User Marks Each Line)

| Case ID | Grade | Reason (User's Own Words) | Follow-up |
|---------|------|------------------|------|
| | pass / concern / unsafe / useless | | |

**The four grades defined** (read to the user before scoring):
- **pass.** Follow this suggestion and nothing goes wrong.
- **concern.** Right direction, but a detail makes me hesitate (write down what).
- **unsafe.** Following it causes harm (top-priority signal, ask "what would happen").
- **useless.** Not wrong, but no use to me (value signal, ask "what do you actually need"; this grade is reserved for real users taking a position. When engineers read traces to judge evidence, the fourth grade is unclear. Do not mix them).

**Facilitation Rules**:
- The scorer must be someone "whose daily work changes after the system launches," not that person's boss.
- No 1–5 scores. Numbers let people politely give a 3. Four grades force a position.
- Record the user's own words. They are the most expensive raw material of the discovery stage.

---

## 0.5 MVP Readout Memo

One page, five sections, answer first:

```
Conclusion: [continue / narrow / redirect / get more data / stop] (one sentence + one numeric piece of evidence)

1. What was validated: whether the workflow claim holds; the score distribution (x pass / y concern / z unsafe / w useless)
2. Key finding: the 1–2 sentences of judgment worth showing an executive (e.g., "chase priority ≠ risk priority")
3. Risks exposed: data risk / trust risk / boundary risk, one line each
4. Unvalidated hypotheses: what this MVP did not cover (synthetic data → data feasibility unvalidated, mandatory)
5. Recommended next step: scope, people needed, data access needed, time box; inside a company add three more, whose schedule gives way, how many people at how many hours a week, and by when it gets reassessed (the Chapter 4 charter locks them in)
```

**Rules**:
- "Stop" is a legitimate conclusion, and a high-return one. You spent two hours saving the company three months. Inside a company, stopping cannot live only in the readout. It goes into the kill register with revival conditions attached (Chapter 25). You will see the person who made the ask tomorrow.
- Every conclusion comes with evidence (score numbers, the user's own words). Never write "overall feedback was positive."

---

## 0.6 Red Line Declaration (Set Before 0:00, Not at 1:59)

Confirm in writing with the business side and the risk owner before the clock starts, and record it in the memo's notes. Silence is not consent:

- [ ] No real production data / no identifiable customer information
- [ ] No messages sent outside automatically
- [ ] Do not touch [this scenario's core decision red line, e.g., the payout amount decision]
- [ ] This MVP promises no launch date. Its deliverables are a basis for judgment, not version 0.1

---

## 0.7 Counterexample: A Tidy-Looking Wrong Answer

Every cell in the Pack excerpt below is filled in, and it would not be sent back if submitted. That is exactly what makes it dangerous.

```
Workflow Claim: Let the claims department use AI to improve exception handling efficiency.
Case Table: 10 cases, all AI-synthesized, all typical "missing material" claims.
Scoring Sheet: scorer Kevin Doyle (Director of Claims Operations); result 9 pass / 1 concern.
Readout: Overall feedback positive, direction validated, recommend continuing.
```

Line by line:

1. **The claim has no "who" and no "action".** "The claims department" cannot be booked for 40 minutes, and "improve efficiency" is nobody's next action today. Rewrite against the 0.1 right example: let Linda, on opening an exception claim, see directly what material is missing and whom to chase first.
2. **All synthetic + all typical.** The data feasibility hypothesis is entirely unvalidated (0.2 requires this to go into the readout), and there are no edge cases. The scoring only sat the ten easiest questions.
3. **The scorer is the boss.** Kevin judges "whether it looks respectable in a report," not "what happens when it is really used tomorrow" (Chapter 0, failure mode 2). Nine pass from a director's hand, and not a single unsafe could be drawn out. The person who should be at the table is Linda.
4. **The readout has no numbers and no quotes.** "Overall feedback positive" is exactly the phrase 0.5 bans by name. Treating "continue" as the default conclusion is Chapter 0's failure mode 4.

The overall test. Take this Pack and ask "what will Linda do differently next Monday because of it," and there is no answer. On the four-grade scale, this deliverable is itself useless.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/field-mvp/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/field-mvp/): the table scaffolding and AI prompt scripts for this Pack
