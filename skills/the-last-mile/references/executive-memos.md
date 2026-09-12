# Writing the one page an executive can call

**Load this reference when:** the VP wants one page, a decision meeting is on the calendar, an impact report has to carry a number that missed target, or the last five-paragraph email to an executive drew no reply.

Source: chapters 13, 19 (`docs/chapters/ch13-tradeoff-narrative.md`, `docs/chapters/ch19-executive-memos.md`); template 19 (`docs/appendices/template-19-memo-suite.md`); `repo/templates/memo-suite/prompt-memo-scaffold.md`.

## Contents

Decisions (reading order, SCQA, the ADR memo, the four things, "it will make mistakes," where the material comes from, the internal center of gravity, landing actions, two signing points, sponsor pressure, the three memos, four shared rules, expectation slots, the loop, four internal recalibrations, the honest gap, options, run chart citation, send timing) · Procedures (write a decision memo; write an impact memo; between memos) · Detectors · Key judgments · Templates · Vendor seat

## Decisions

**Write in the reader's decision order, not your derivation order.** Forty pages against ten minutes is not a volume problem, it is an order problem. You wrote in the order you reached the conclusion (current state, reconciliation, selection, review, conclusion); he reads in the order he calls it (conclusion, cost, risk, what he has to do). Write one more page in the reversed order; the forty pages need not get thinner. The one page is the interest on the forty, not its summary.

**Align four things inside ten minutes: the conclusion, the cost, the risk, what he has to do.** Miss one and his rational choice is to commit to nothing. He is not rejecting you; he cannot answer for it yet.

**Open with SCQA in three lines.** S, a fact both sides already agree on (only what he already knows and accepts; new information in S loses the anchor). C, the single hardest piece of evidence that threatens it (one scoring run, one distortion rate; do not pile them up). Q, the question that rises in his mind, his question ("should we invest now, and how much"), not yours ("which architecture"). A, your conclusion. On the page they land as "background," "but," "so the question to answer."

**The ADR memo, six sections, one page of body text.**

| Section | What goes in it | Rule |
|---|---|---|
| SCQA opening | Three lines | Q must be his question |
| The conclusion in one sentence | The call to be made, bold, carrying scope, duration and the validating metric; the key number's source in one parenthesis | The pyramid apex test: if you cannot say it in one sentence, do not start writing |
| Three pillars | Three reasons, one line of evidence each | MECE; evidence is nouns (records reconciled, a co-signature, a scoring result), not adjectives; if it will not fit on one line the evidence is not hard enough yet |
| The trade-off said out loud | What was given up, what it bought, where the thing given up now sits (a revival condition per item) | The soul of the memo, the only section that works against you and so the one that makes the rest credible; the cost is written by you, never left for the reader to discover |
| Risk and backstop | Error categories → per-category threshold and tolerance (zero-tolerance classes listed separately) → the backstop path → the resource reassessment conditions | A commitment, not an apology; every sentence has a subject and a mechanism, no "we will try," no "in principle" |
| The three things I need from you | Three at most, each his action, each dated to the day | Without it the memo is a report; a clear ask can be refused, a vague report is always safe |

**Quote the decision rights ladder inside the trade-off section, four layers top down.** Decide, pay or not, how much, a red line never touched. Act, send notices, assign, change status, humans take over here. Advise, priority, next step, reason, AI stops here this phase. Sense, gather documents, dwell time, risk signals, AI does this. Each layer up needs that layer's evidence, the advise layer's acceptance record accumulates from the pilot, and each layer is decided on its own, by him. What he sees on the ladder is a boundary, not the AI in the media.

**Present "this system will make mistakes" with the backstop, never with an apology.** "We do not promise 'no mistakes,' we promise 'when it is wrong, it can be found and it can be caught.'" Say it in error categories, per-category thresholds and the human review path; a single unsafe in the pilot degrades that whole class to human review. Panic comes from "nobody handles it when it goes wrong," and "it will make mistakes" frightens nobody on its own.

**Write nothing new; take the hardest line out of each artifact.** C ← the Field MVP scoring data. Pillar evidence ← the reconciliation report and the eval baseline. The trade-off section ← a transcription of the scope log. The risk section ← the error taxonomy plus the human oversight design.

**Lead the last section with people, priority and owner, not budget.** An internal executive rarely calls "do we approve this money"; the money already has a line. He calls whether you get people, where you rank, and who owns it after launch. Confirm the post-launch owner by name inside item 1; a department name does not count. Leave that half-sentence off this page and there is no second occasion to write it, and a year later the midnight alert rings on your phone by default.

**Follow every approved item with a verifiable landing action.** Who, by which day, writes it into which sheet, and copies whom. The 2 hours written into the schedule sheet are the real 2 hours; the 2 hours nodded at in a meeting are not. The copy line turns "not done" from a private matter into something the sponsor sees; inside a company visibility is where enforcement starts.

**Two signing points (people from one department, capacity from another)** → one page, the first five sections shared, the last section in two columns, each signed, each dated. Not two pages; each would assume the other is covering it. Side effect, whoever fails to deliver fails in front of the other one.

**Sponsor pressure in the name of support (a live board demo on the prototype)** → neither refuse nor take it whole; give him something he can call, written the way the page is written, conclusion (a three-minute recording plus the scoring sheet and the ladder drawing), cost (it does not hit as hard as live), what it buys (zero risk of blowing up, a harder story). The pressure is translated into a trade-off he can call responsibly.

**Three moments, three memos, one shared rule.** Name the moment before you write; if you cannot, check the calendar, phase boundaries are objective.

| Moment | Memo | His question | Middle section |
|---|---|---|---|
| Authorization at the open | Kickoff memo | What are you promising, what do you want me to commit, how will it die | The outcome promised (the charter's metric plus one early win dated inside the first month) + investment needed in two columns + pre-mortem summary (three ways to die, a defense each) |
| A decision at the midpoint | Decision memo (the ADR memo) | What am I calling, what does it cost, what happens when it goes wrong | Three pillars + the trade-off said out loud + the decision rights ladder + risk and backstop |
| Renewed funding at the close | Impact memo | Was it worth it, how far short, which next step | Run chart evidence + the honest gap + next-step options |

The kickoff puts commitments on record, the decision memo asks for a call, the impact memo delivers the evidence. The opening and the ending are identical across all three; only the middles differ.

**Four shared rules.** One page of body text, attachments unlimited. Lead with the conclusion (the pyramid apex test). The ending always carries "what I need from you," even if only "hold ten minutes on your calendar." Delivered 48 hours before the meeting (rule), so the meeting runs around the document.

**Keep one expectation-management slot per memo.** The executive's AI expectations were pre-calibrated by the media into a diode, conducting or not. Kickoff → the pre-mortem summary. Decision memo → the decision rights ladder. Impact memo → the honest gap, the missed number written exactly as it is, never "close to target." Calibrating once per memo beats one reconciliation on acceptance day.

**Close the loop.** The moment the impact memo's recommended option is approved is the S of the next kickoff. As many phases as the project has, that many turns.

**Recalibrate four things inside a company.**
1. The cost of reporting bad news. Your sponsor sits on or one layer from your review chain; write the gap honestly anyway. What it buys is his default belief in every number you give him afterward, and that deposit is not for sale anywhere else.
2. The ask splits into two columns. Who sends the people (real names, hours per week, a precedent cited). Who gives the word (whose mouth the sentence must come out of, the sponsor or the other side's manager). Every item in the second column is a political act; work out whose standing you are spending before you write it.
3. Timing is set by the fiscal year, not the project. The impact memo's date is worked back from the day budget preparation starts; a week late and your numbers make next year's pot. The kickoff is planted a quarter ahead of the headcount table freezing. A year after launch, when no bill reminds anyone the system is alive, send the impact form again to the same recipient, unasked.
4. The copy line. Sponsor as primary; three fixed copies, your manager, the business-side owner, the PMO. The copy line is the paperwork that turns going over a head into not going over one.

**Write the honest gap in three parts.** Number against number ("-22% against -30%, 8 percentage points short," illustrative, never "close to target"). Attributed to verifiable events (when the people arrived, when the fix took effect), never "we need more time." Carrying its own void condition ("if the metric stops improving inside N weeks, this judgment is void and we go back to option N"). If you cannot write the third, the first two are a justification, not an attribution. Written as "expected to hit target soon," what gets approved is hold and watch.

**Give 2–4 options, each with content, investment and when to choose it.** Revival-list items are stated by their revival condition (ripe or not, how far short), not by mood. Hold and watch always sits last, with a ceiling on the watching period and its cost; when it comes due with no new evidence, "another month of watching" goes through project approval again. Mark the recommendation "we recommend N."

**Cite the run chart by the rules.** Every point on the chart, the baseline median as the reference line, the special-cause rule named (six points on one side, rule), no cropped stretches, no trend drawn between two points. Write the defense record whether it looks good or bad, incidents caught, the layer the retrospective attributed them to, flow-back into the golden cases, the kill criteria check result. Zero triggers still gets written as "zero triggers"; it is the evidence that the stop clause has teeth.

**Send by the table, then write back within 24 hours (rule).**

| Memo | When to send | Meeting shape |
|---|---|---|
| Kickoff | Monday of the week the phase starts, inside one week of the approval meeting | Usually no meeting; for the record plus one calendar request |
| Decision | 48–72 hours (rule) before the meeting where it gets called | A 10-minute meeting, silent reading first, then the pillars |
| Impact | 48 hours (rule) before the retrospective or the annual budget and headcount review | The meeting works the options around the document; the approval comes as it breaks up |

Document before meeting. Within 24 hours of the meeting, write the approval outcome back into the project record; that is the S of the next memo.

## Procedures

**Write a decision memo.**
1. Pyramid apex test: who you want and what you want him to call, in one sentence. Cannot → stop; what you want may be understanding, not a decision.
2. Borrow a shell: pull up project approval memos this company has already approved; write to their section names, length and copy line.
3. Fill the six sections from existing artifacts. The trade-off section names at least two things given up with a revival condition each, and pastes the ladder in as it stands.
4. Pre-read: the executive's assistant or a past counterpart reads it for four minutes (rule), then answers "what is the decision, what is the cost, what happens when it goes wrong." Any question he cannot answer → rewrite that section.
5. Place the apex yourself: land the conclusion on what this executive was pressed on the last time he called a decision (the payment cycle, not accuracy). AI lays the body of the pyramid; the apex is yours.
6. Run the self-check (S has no new information; C is one hardest fact; every pillar a noun; no "significant," "solid," "basically"; every ask his action with a date; body inside one page). Deliver 48–72 hours ahead.

**Write an impact memo with a missed number.**
1. Put the hardest number straight into C, hit or missed.
2. Conclusion in one sentence, bold, whether the validation holds and which option is recommended.
3. Evidence: run chart by the citation rules, the mechanism explained, the defense's field record.
4. The honest gap, three parts. Test the void condition first; if it cannot be written, go back to the attribution.
5. Options, hold and watch last with a ceiling. Ask with a date and an occasion.
6. The day before, hand it to the executive's assistant; ask what question has chased him this week; rewrite the subject line and reorder the first evidence on that answer. Pull two words from the company strategy document into the conclusion and one comparable number from a neighboring department's system into the evidence.

**Between memos, honor promises with no ask attached.** "You said to tell you the day the sixth point comes in. It came in today, still below the median. Six points on one side, a structural shift, not fluctuation. Chart attached." No request, no next step. Three weeks later (illustrative) that deposit is what a missed number trades on.

## Detectors

- If the last thing you sent an executive drew no reply, it was sorted, not rejected; his inbox sorts by "what do I have to do," and information with nothing to do drops into white noise.
- If the trade-off section contains no sentence that hurt to write, you are selling, not reporting; once a hidden cost is exposed you permanently lose the right to lead with the conclusion.
- If the memo has no "what I need from you" with a date, it asks for understanding; the nod is for you, not for the project.
- If the body runs over one page, you have not found the apex; going over is a diagnostic signal, not a sign of thoroughness.
- If the memo starts from "project background" and the conclusion sits on the last page, it copies the order of the work, not the order of the reader.
- If the opening memo is all architecture or the closing memo all war stories, the form followed your state of mind, not his decision moment.
- If the memo carries only numbers and requests and never calibrates what AI can do, the missed number will be read as "so much for AI."
- If every item in the communication record carries a request, you are the person who wants resources, not a partner.
- If the memo's "owner after launch" is a department, the midnight alert already has your number.

## Key judgments

- "Executives are not short of information. They are short of a structure they can decide on."
- "The point of a 40-page plan is to let one page dare to be that short."
- "A memo with no 'what I need from you' changes nothing once it is read."
- "Once a hidden cost is exposed, you permanently lose the right to lead with the conclusion."
- "Executives do not reply to information. They reply to decision requests."
- "Three moments, three forms. Mix them and they stop working."
- "The evidence of communication is the other person's changed behavior, not your sent folder."
- "The first email was not rejected. It was sorted."

## Templates

- Decision memo with the SCQA self-check and the four-minute test: `templates/memo-decision.md`.
- Impact memo with the honest gap and options: `templates/memo-impact.md`.
- Kickoff memo and the shared rules list: `docs/appendices/template-19-memo-suite.md` §19.1, §19.4; `repo/templates/memo-suite/prompt-memo-scaffold.md` drafts the body and leaves the apex blank.
- The trade-off section transcribes `templates/scope-decision-log.md`; the risk section reads `templates/eval-spec.md` and the charter's three tiers in `templates/deployment-charter.md`.
- `scripts/run_chart.py` produces the median, the six-on-one-side signal and the short notice.

## Vendor seat

The annual budget and headcount review is the renewal meeting, and the kickoff's "who gives the word" column is the client decision-maker's signature. Renewal is a contract event outside, so the year-after memo has a date; the honest gap is still what the number trades on. A renewal clause is one line, and a line in a contract is not a working mechanism.
