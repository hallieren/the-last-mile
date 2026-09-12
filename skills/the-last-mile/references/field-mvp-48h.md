# The opening 48 hours: a vague ask into a table a real user has scored

**Load this reference when:** a vague AI ask has landed ("we want an AI assistant", "make the department more efficient", "ideally with a dashboard"), an executive's idea arrives with a deadline, kickoff is Monday, and nothing has been scored yet (below L0).

Source: chapter 0 (`docs/chapters/ch00-field-mvp.md`); template 0 (`docs/appendices/template-00-field-mvp-pack.md`); `repo/templates/field-mvp/*.md`.

## Contents

Decisions: three roads · four inputs and their fallbacks · the workflow claim · the four grades · the five conclusions · three boundaries. Procedures: manufacture the start · the two hours minute by minute · readout · buy the user's 40 minutes · a stop. Detectors. Key judgments. Templates. Vendor seat.

## Decisions

**Take road three.** Road one, a scoping study of 4–6 weeks (illustrative) of interviews and a requirements document, spends half the sponsor's horizon and leaves the business side wondering whether you can code. Road two, straight to a demo, dies the moment the demo succeeds. Road three, the Field MVP: inside the opening 48 hours (rule), spend two hours (rule) building a minimal workflow prototype with a real user, ten rows and one table, real enough that a front-line reviewer can point at each row and say this one helps, this one is dangerous. Let the disagreement blow up at hour 48, not on day 90. Agreement to an abstract description is cheap; ten concrete rows cannot be agreed to cheaply.

**Get four inputs; each has a fallback, and the friction of getting them is the first batch of findings.** Whichever input is hardest to get is where the organization's first real boundary lies.

| Input | Standard | If it cannot be had |
|---|---|---|
| One vague ask | Whatever sentence was said | None needed |
| 3–10 historical cases (rule) | Structure and details, not necessarily a data file | Stand at the data owner's screen and hand-copy field names, status transitions and de-identified summaries; take no data with you (compliance blocks copying, looking usually gets through). Only failing that, AI-generated synthetic cases, and the readout must say so. If the block is unclear ownership rather than a refusal, skip the process: find the real owner of the table in the system, write the fields and the purpose in one sentence, ask him to nod |
| One real user, by name | Someone whose daily work the system will change after launch; "the department" does not count | Lay out the scorer definition, ask for 40 minutes (rule), let the boss sit in and not score on her behalf. Still refused, write "no access to real users" into the readout; that line speaks louder than any score |
| One red line | Confirmed by the risk owner or compliance, not by the requester; silence is not consent | Draft the three most conservative yourself (no real production or identifiable customer data; no automatic outbound messages; the scenario's core decision untouched) and send them to the risk owner for confirmation before the clock starts |

**Write the workflow claim; if you cannot, stop and find the who.** `This system will change <role and name>'s <next action they already take today>.` The who is bookable for 40 minutes; the action is something he already had to do today, not something new added to him. "Build an AI assistant" and "improve efficiency" do not qualify. Cannot write it = you do not know whose work you are changing, and whatever you build is decoration.

**Score on the four grades, never 1–5.** Numeric scores make users give a polite 3; four grades force a position, and unsafe and useless are counted separately.

| Grade | Definition read to the scorer | Signal |
|---|---|---|
| pass | Follow this suggestion and nothing goes wrong | Usable as is |
| concern | Right direction, but a detail makes me hesitate (write down what) | Uneasy, not dangerous |
| unsafe | Following it causes harm; ask "what would happen" | Risk signal, top priority |
| useless | Not wrong, but no use to me; ask "what do you actually need" | Value signal, just as fatal, different in kind |

Three unsafe carry far more information than seven pass. The fourth grade follows the scorer: a real user taking a position on outputs marks useless (value); an engineer reading system traces marks `unclear` (this one's outcome cannot be verified yet). The first three grades mean the same in both sets. Never mix the two fourth grades in one table.

**Settle one of five conclusions from the scoring distribution plus the red-line and data facts.** Continue / narrow / redirect / get more data / stop. "Stop" is legitimate and high-return: two hours that save three months (illustrative) and a team. "Continue" is not the default.

**Declare three boundaries before the clock starts.** It is not a system (no real production data, no sensitive information, no launch date promised; it is a probe, a long way from version 0.1). Synthetic data cannot validate data feasibility (synthetic cases test only the shape of the workflow and user trust; the readout must say the data hypothesis is unvalidated). One MVP does not replace discovery (it gives direction and the authorization to enter discovery; tacit knowledge it exposes still has to be captured by field archaeology).

## Procedures

**Manufacture the start.** The clock starts at the meeting where the ask is voiced. If the ask arrived as a chat message, a ticket or a line in the annual plan, no clock is running. Send one email naming the four inputs you need and the readout date 48 hours (rule) out, copying the person who made the ask and your manager. The moment it goes out, the 48 hours are running.

**Run the two hours (rule). AI does the grunt work, you make the calls.**
1. 0–15 min, rewrite the ask into one workflow claim. AI drafts candidate wordings; you pick and self-check. Deliverable: Workflow Claim.
2. 15–35 min, prepare 10 cases (rule). AI extracts fields from the hand-copied material or generates synthetic cases; you pick 6–7 typical, 2–3 edge, 1 that even the front line finds hard (rule), and mark the source of every case (real de-identified / synthetic). Deliverable: Case Table. Fields: case ID, current status, reason stuck, time waiting, key context fields, source.
3. 35–60 min, design the queue. AI suggests a column structure; you decide columns, statuses, owners, risk flags. Columns: case ID, reason stuck, missing item, suggested priority, suggested next action, owner, reason, Human Call. The reason column is mandatory and challengeable; the Human Call column is the soul, declaring the system advises people and does not decide for them; every row has an owner, or it is a dashboard. No more than 25 minutes (rule) on the interface. Deliverable: Action Queue prototype.
4. 60–85 min, generate the first output for the 10 cases: priority, next action, missing information, risk flag, reason. You review for obvious errors. Deliverable: filled queue.
5. 85–105 min, the real user scores each row pass / concern / unsafe / useless with the reason in her own words. Read the four definitions aloud first. If the first rows come back "fine, okay" with the boss in the room, change the question: point at a row and ask "if this were handled this afternoon exactly as written, what would happen?" Deliverable: Scoring results.
6. 105–120 min, write the readout. AI drafts; you settle the conclusion. Deliverable: MVP Readout Memo.

**Write the readout, one page, answer first.**
1. Header: `Conclusion: <continue | narrow | redirect | get more data | stop>. <one sentence>. <one number>.`
2. What was validated: whether the workflow claim holds; the distribution x pass / y concern / z unsafe / w useless.
3. Key finding: the one or two sentences worth showing an executive (e.g. chase priority ≠ risk priority).
4. Risks exposed: data / trust / boundary, one line each.
5. Unvalidated hypotheses: what the MVP did not cover; synthetic data ⇒ data feasibility unvalidated, mandatory.
6. Recommended next step: scope, people, data access, time box. Every conclusion carries evidence (score numbers, the user's own words). "Overall feedback was positive" is banned.
7. If the sponsor says "continue", translate it in the room into three verifiable things: whose schedule gives way, how many people at how many hours a week, by when it gets reassessed. Inside a company a verbal continue carries no resources of its own; whichever of the three you cannot get an answer to is the first to collapse in the next two weeks. The three go into the charter.
8. If the data is still stuck, say what you do until it clears (reconciliation design, tacit-rule interviews) and promise that if it is still stuck at the reassessment date, the readout opens with that fact.

**Buy the real user's 40 minutes when her manager stands in the way.** Lay out the scorer definition and ask him to sit in, not to score for her. You hold no paperwork, so the only card is exchange. Three chips: one action that saves her effort on the spot; the readout's conclusion copied to her supervisor; her name on the scoring sheet. The third is the cheapest and weighs the most.

**When the conclusion is stop.**
1. Write it in the readout with the numbers that support it, including the conclusion you are afraid to write.
2. Enter it in the kill register: project / requester / reason for stopping / revival conditions. Revival conditions written as events turn "not doing it" into "not doing it now"; the requester gets an exit and you need not hide the judgment. You will see him on the same floor tomorrow.

**Next Monday, in order, each the input to the next.** Write one workflow claim for the vaguest ask on your desk. Confirm the scorer is a real user, not her boss, and get the red line confirmed by the risk owner before the clock starts. Find 5–10 (rule) de-identified real cases and run the two hours. Write the readout whatever the result.

## Detectors

- If an hour and 45 minutes (illustrative) went to prompt tuning and the interface is beautiful, then the Field MVP became a mini demo. One spreadsheet with handwritten annotations beats a polished interface nobody has scored.
- If the scorer is the user's boss and the sheet came back with no unsafe, then you picked the wrong scorer. A manager judges whether it looks respectable in a report; the front line judges what happens when it is used tomorrow.
- If real customer data was used or the AI suggested payout amounts to make the MVP look good, then you started without a red line. One data violation or one dangerous suggestion destroys in a minute what takes weeks to build.
- If the scores are bad and the readout still says "overall direction validated", then you have treated continue as the only legitimate conclusion because stopping feels like your own failure.
- If the clock ran out and there is no table a real user marked line by line, then it was a paper discussion, however lively the meeting.
- If the claim has no who and no action (e.g. "let the department use AI to improve exception handling efficiency"), then it is not a claim: nobody can be booked for 40 minutes and "improve efficiency" is nobody's next action today.
- If the case table is all synthetic and all typical, then data feasibility is entirely unvalidated and the scoring only sat the ten easiest questions.
- If the scorer is the director and the result is 9 pass / 1 concern (illustrative), then not a single unsafe could be drawn out; the person who should be at the table is the one whose daily work changes.
- If the readout has no numbers and no quotes, then it is the banned sentence in another form. Ask "what will the user do differently next Monday because of it"; no answer means the deliverable is itself useless.
- If "continue" left the room without whose schedule, how many hours, and a reassessment date, then it was encouragement, not a resource.

## Key judgments

- "Let the disagreement blow up at hour 48, not on day 90."
- "AI does the grunt work. People make the calls."
- "If you cannot write the workflow claim, you are building decoration."
- "Three unsafe carry far more information than seven pass."

## Templates

- `templates/workflow-claim-and-readout.md`: the claim form with self-check, the scoring sheet, the readout memo, the red line declaration.
- `docs/appendices/template-00-field-mvp-pack.md` §0.2, §0.3 (and `repo/templates/field-mvp/case-table.md`, `action-queue.md`): the case table and the action queue prototype.
- `docs/appendices/template-04-deployment-charter.md` §4.1: where the three verifiable things behind "continue" get locked in.

## Vendor seat

The opening 48 hours hold on the vendor side; only the clock starts the day you arrive. The four inputs, the scorer definition and the red line confirmed by the client's risk owner apply as is. A line in a contract is not a working mechanism.
