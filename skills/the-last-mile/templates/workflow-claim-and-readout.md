# Workflow claim and readout

Source: `docs/appendices/template-00-field-mvp-pack.md` §0.1, 0.4, 0.5, 0.6 (and `repo/templates/field-mvp/workflow-claim.md`, `scoring-table.md`, `readout-memo.md`; the repo wins on conflict).

| Field | Value |
|---|---|
| Project / ask | <one-line ask as voiced> |
| Clock start | <date the ask was voiced, or the date of the email that manufactured the start> REQUIRED |
| Readout date | <clock start + 48 hours> REQUIRED |
| Requester / your manager (cc) | <name> / <name> |
| Scorer (a real user whose daily work changes after launch, not their boss) | <role and name> REQUIRED |
| Red lines confirmed by (risk owner or compliance, in writing; silence is not consent) | <name>, <date> REQUIRED |

**0.1 Workflow claim** (one sentence, two blanks)

> This system will change **<who: role and name>**'s **<which next action>**.

Self-check: "who" is a specific person you can book for 40 minutes, not a department; "action" is something he already had to do today, not something new added to him; cannot write it → go back and find the "who", do not go further.

**0.4 Scoring sheet** (the real user marks each line; read the four grades aloud first)

| Case ID | Grade (pass / concern / unsafe / useless) | Reason (user's own words) | Follow-up |
|---|---|---|---|
| <case id> | | | |

pass: follow this suggestion and nothing goes wrong. concern: right direction, but a detail makes me hesitate (write down what). unsafe: following it causes harm (top-priority signal, ask "what would happen"). useless: not wrong, but no use to me (value signal, ask "what do you actually need"; reserved for real users; when engineers read traces the fourth grade is `unclear`; do not mix them).

**0.5 Readout memo** (one page, five sections, answer first)

```
Conclusion: <continue | narrow | redirect | get more data | stop> (one sentence + one numeric piece of evidence)
1. What was validated: whether the workflow claim holds; <x> pass / <y> concern / <z> unsafe / <w> useless
2. Key finding: the 1–2 sentences of judgment worth showing an executive
3. Risks exposed: data risk <…> / trust risk <…> / boundary risk <…>
4. Unvalidated hypotheses: what this MVP did not cover (synthetic data → data feasibility unvalidated, mandatory)
5. Recommended next step: scope <…>; people needed <…>; data access needed <…>; time box <…>;
   whose schedule gives way <name>; how many people at how many hours a week <n × h>; reassessed by <date>
```

**0.6 Red line declaration** (set before 0:00, recorded in the memo's notes)

- [ ] No real production data / no identifiable customer information
- [ ] No messages sent outside automatically
- [ ] Do not touch <this scenario's core decision red line>
- [ ] This MVP promises no launch date. Its deliverables are a basis for judgment, not version 0.1

**Rules**
- The scorer must be someone "whose daily work changes after the system launches," not that person's boss.
- No 1–5 scores. Numbers let people politely give a 3. Four grades force a position.
- Record the user's own words. They are the most expensive raw material of the discovery stage.
- "Stop" is a legitimate conclusion, and a high-return one. You spent two hours saving the company three months. Inside a company, stopping cannot live only in the readout. It goes into the kill register with revival conditions attached.
- Every conclusion comes with evidence (score numbers, the user's own words). Never write "overall feedback was positive."

**What a wrong filling looks like**
- Claim: "Let the department use AI to improve exception handling efficiency." No who, no action; nobody can be booked for 40 minutes and "improve efficiency" is nobody's next action today.
- Case table: all synthetic, all typical. Data feasibility entirely unvalidated, no edge cases; the scoring only sat the ten easiest questions.
- Scorer: the director. 9 pass / 1 concern, and not a single unsafe could be drawn out; the person who should be at the table is the one whose daily work changes.
- Readout: "Overall feedback positive, direction validated, recommend continuing." No numbers, no quotes, continue as the default. Ask "what will the user do differently next Monday because of it"; no answer, and on the four-grade scale the deliverable is itself useless.

Filled in → goes to: the deployment charter (the three commitments behind "continue" become element 5 and the reassessment date) and the pre-mortem; a stop goes to the kill register.
