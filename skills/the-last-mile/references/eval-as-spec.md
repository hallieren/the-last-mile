# Writing the eval before the architecture

**Load this reference when:** someone asks "what accuracy counts as passing," an acceptance clause carries one overall score, "we should do an evaluation" surfaces a week before launch, or a pattern upgrade is being argued on feeling.

Scope: this file covers what the eval is for, who signs it, and how a gate reads it. Computing intervals, validating judges and sizing samples belong to the ai-agent-evaluation skill.

Source: chapter 11 (`docs/chapters/ch11-eval-as-spec.md`); template 11 (`docs/appendices/template-11-eval-spec.md`); `repo/templates/eval-spec/eval-spec-template.md`.

## Contents

Decisions (the number question, the five parts, three rules of use, the taxonomy shape, two statistical cautions, mix lines, where the table is read, the human review path, the guide as an asset) · Procedures (the 2 hours; collecting cases; routing a disagreement; Monday's 20 cases) · Detectors · Key judgments · Templates · Vendor seat

## Decisions

**Asked "what accuracy can this reach"** → give no number. Ask back on one recent case, "whose error is that, is it an error at all," and watch the room give three answers → deliver, inside a week and a half (illustrative), a per-category threshold table the business owner and the risk owner sign. Where there is no definition of error there is no accuracy and no release. A number given before error is defined turns release day into a fight over every case.

**Write the spec as the acceptable distribution of errors, not as behavior.** Input X, output Y cannot be enumerated for an AI system. Golden cases define what the system should be; the error taxonomy and thresholds define how good is good enough. The eval set is the requirements document, and testing is its part-time job.

**Finish the eval spec before the architecture decision meeting.** Written after implementation it is a justification, not a requirement, and the thresholds get tuned until the architecture already built just passes. The upgrade criterion goes missing with it.

**The five parts.**

| # | Part | Question it answers | Discipline |
|---|---|---|---|
| 1 | Task definition | What is being evaluated | One sentence at workflow-claim level, what input, what output, for whom, where the red line is. One eval evaluates one task |
| 2 | Golden cases | What counts as right | 50–200 (rule) real cases + correct answers. The count is set by coverage of error categories, every category has cases that can detect it, never padded to a total. Answers clear the data check first. Edge and historical incident cases carry real weight |
| 3 | Error taxonomy | What kinds of error there are | Each category states definition, business consequence, tolerance. Severity borrows three of the four grades (unsafe / concern / useless), no separate sev numbering. The unsafe class is zero tolerance |
| 4 | Per-category thresholds and acceptance lines | How good is good enough | One line per category. No overall score, "an overall score is the shortest path to burying unsafe" |
| 5 | Human review path | Where outputs that fail go | Trigger condition, destination, who looks, how fast. Review results flow back into the golden cases |

**Keep the three rules of use.** Co-build golden cases with the actual user (the correct answer is in the reviewer's head, not in your reasoning, and disagreement is requirements discovery). Reconcile the answers first (every fact a correct answer cites stands at validated or above on the fitness ladder; take system fields as answers and nearly half may be wrong, 44% illustrative). Set thresholds per error category (costs differ by orders of magnitude; one averaged line guarantees nothing).

**Shape the taxonomy by cost, not by bug type.** The first row comes from asking the actual user "which kind of error can you not accept even once." The category grows out of the unsafe marks on the Field MVP scoring sheet.

| Category (worked shape) | Business consequence | Grade | Tolerance |
|---|---|---|---|
| Missed risk (a high-risk case judged routine) | Grows into a major case, regulatory complaint | unsafe | Zero tolerance, 0 of 50 (rule) |
| Line-crossing suggestion (touches the decide-layer red line) | Responsibility has nowhere to land | unsafe | Zero tolerance |
| Material error (the missing-item list wrong or incomplete) | A wasted round of chasing, the customer waits days longer | concern | ≤10% (illustrative), and the error must be obvious to a reviewer at a glance |
| Wrong action (next action or owner wrong) | One idle round | concern | ≤10% (illustrative) |
| Empty suggestion (not wrong, carries no information) | The queue slowly goes unread | useless | ≤20% (illustrative), negotiable, the trend must not rise |

**Hold the two statistical cautions.**
- 0 of 50 is an entry ticket, not a proof of safety. Fifty cases cannot detect every surprise in real operation. The real defense for a zero-tolerance category is every decision trail entry after launch.
- Zero tolerance is counted in cases and does not depend on sample size. Ratio lines like ≤10% and ≤20% on fifty cases mean one case is two percentage points, and the ratio read from a single replay swings by a dozen points on its own. It gives direction, not a scale. Read ratio thresholds as a trend across several replays; that is what three consecutive replays (rule) at gate one is for. To read the line finer, add cases, not just confidence.

**Compose the set unevenly.**

| Type | Where to find it | Mix line |
|---|---|---|
| Typical (high frequency, answer undisputed) | Random sample from the source of truth | Under half (rule) |
| Edge (right at a rule's threshold) | Aged cases, cases at the amount threshold, cases where rules conflict | ≥30% (rule) |
| Historical incident (once went wrong or was misjudged) | Complaint log, retrospective notes, internal audit reports, regulatory inspections, veterans' "the one I got wrong" stories | ≥10% (rule) |
| Annotation disagreement | The annotation session itself, entered after ruling | Added continuously |

Edge and historical incident cases are the soul of the eval; that is where the system's value and its risk both live. A list-type rule that drifts (a repair shop list, illustrative) carries a dated version in the guide and rolls with the list.

**Read the signed table in four places, and build nothing new at any of them.** The upgrade criterion (a heavier pattern earns a hearing only when the current one fails a line). The charter's "fill in the numbers later" slot (thresholds go into the project resolution as launch release conditions; the old overall-score wording is voided and filed). Gate one of prototype → pilot. The error ledger and the live monitoring definitions after launch, as is.

**Answer the human review path to four items.**

| Item | Answer |
|---|---|
| Trigger | Hits a risk rule with low confidence, plus anything that looks like an unsafe-class error |
| Destination | The queue's Human Call column; without that column the system takes no action |
| Who looks | The reviewer who picked up the case, by name; every suggestion carries its reason, so judging it does not mean checking three systems |
| How fast | The number of rows entering human view each day is worked back from the review team's review time budget. Better to route too few than to have them glanced at and not read |

Add a flow-back owner named to a person, and hang the reminder on a meeting that owner already holds (the monthly QA review), no new reminder. Suspected unsafe cases are reviewed weekly; review conclusions flow back into the golden cases monthly. The three oversight questions are already answered here.

**Treat the annotation guide as standalone organizational value.** It stays alive without your system, new-hire training uses it, cross-review uses it, and it is not voided when the core system is replaced. Push to promote it to the review team's formal operating procedure under a department document number, with a named owner who maintains it and reports the two one-shot numbers at that team's existing monthly review.

## Procedures

**Get the 2 hours a week (rule, the charter's business-side commitment line) without a new meeting.**
1. Attach the annotation session to the review team's existing weekly, run straight after it.
2. State the exchange plainly, "Your twenty years of rules get written down for the first time, and once written, the guide belongs to the review team, not to the system." "Help us with an evaluation" cannot be said at their weekly; this can.
3. Report the fulfillment rate monthly at the sponsor weekly. Two hours this month or zero, both sides see it.

**Collect the golden cases.**
1. Finish the task definition first. Without a task there is no way to judge whether a case is representative.
2. Draw candidates from the source of truth, not the easiest database to reach, 1.5× (rule) the target count.
3. Clear the data check case by case. Three sources agree → in. Disagree → rule by three-way reconciliation. No ruling possible → drop. The first mile of the eval is reconciliation.
4. AI pre-fills fields and drafts answers; the actual user rules on every final answer.
5. Double independent annotation, two actual users on the same batch. Borrow the second annotator from the neighboring department, so cross-department semantic divergence surfaces in the session instead of in the queue after launch.
6. Route every disagreement (below). Enter cases with version and date; bump the annotation guide version in step.
7. Set the rolling update cadence, review flow-back monthly, and a drift in a list-type rule triggers an immediate update. Pull the historical incident cases yourself from complaint files and retrospective notes; do not wait for a veteran to volunteer.

**Route an annotation disagreement. A disagreement is not allowed to hang.**
1. Root cause first. Different standards → needs a business decision. Different information → fill in the information and annotate again. Different reading of the task → go back and fix the task definition.
2. Then by type. Within-department → find the owner of this workflow, rule on the spot, write the ruling into the annotation guide. Cross-department → pause annotation, write both definitions and their business consequences on half a page, send it to the two sides' common superior or put it on the sponsor weekly; you cannot rule it for anyone, you make sure someone rules within two weeks (rule). Compliance-related → the risk owner, cross-department or not; a compliance definition cannot be settled by whoever is loudest.
3. Do not put it to a vote, and do not split the difference. That blends two clear rules into one rule nobody owns. The ruler holds business decision rights, the workflow owner or above.
4. Settle every ruling into one executable line of the annotation guide, or the same disagreement comes back on another case.
5. The disagreement case goes into the golden cases; report the disagreement rate and the number ruled on. The rate is the number of missing pages in the requirements document.

**Start on Monday with 20 cases (rule).**
1. Ask "which kind of error can the user not accept even once" and write it as the unsafe row. Cannot write it → you have not talked to the actual user about consequences yet.
2. Typical under half, at least 3 historical incident cases (rule). Answers clear the data check first.
3. Two actual users annotate the same batch independently; record each disagreement and find someone with decision rights to rule.
4. Dig out the acceptance clause. An overall score → draft the per-category replacement now, not the week before acceptance.

## Detectors

- If "what accuracy" has been answered with a number before error was defined, release day is a per-case fight already scheduled.
- If the eval is being written after the architecture is set, it is a justification, and the thresholds will settle wherever the build already passes.
- If the report carries one overall accuracy, unsafe is buried in it; 92% (illustrative) can mean 3 unsafe out of 50, and the better the number looks the deeper it buries them.
- If no case in the set has someone disagreeing with the answer, the disagreement was avoided, and disagreement is the substance of the spec.
- If the cases that flowed back into the golden cases last month number zero, or the annotation guide's version did not move this quarter, the eval is one-shot, however seriously it was co-built.
- If "it works well" or "the feedback is good" stands where a spec should, there is no acceptance and no release.
- Counterexample, task definition: "comprehensively evaluate output quality" has no action, no user, no red line, so every section after it has no target.
- Counterexample, golden cases: randomly exported from the test database (not the source of truth), answers from unreconciled system fields, one annotator who is the security reviewer and not the actual user, so no disagreement can ever be recorded.
- Counterexample, taxonomy: one category, "output error," with no business consequence; a taxonomy not layered by cost.
- Counterexample, threshold: "overall accuracy ≥ 90%" is the forbidden overall score; 2 missed risks out of 50 still score 96% (illustrative).
- Counterexample, human review: "handled by human intervention when necessary" has no trigger, no owner, no time limit and no flow-back, so the eval is one-shot from day one.

## Key judgments

- "An AI system's spec does not describe behavior. It describes the acceptable distribution of errors."
- "The golden cases are the requirements document, and the thresholds are the acceptance clauses."
- "Annotation disagreements are business rules that were never aligned, surfacing. They are not noise."
- "The first mile of an eval is reconciliation, not annotation."
- "0 of 50 is an entry ticket, not a proof of safety."
- "To read the line finer, add cases, not just confidence."

## Templates

- Eval spec skeleton and disagreement log: `templates/eval-spec.md`.
- Golden case collection list: `docs/appendices/template-11-eval-spec.md` §11.2.
- Gate one reads the table: `templates/escalation-gates.md`; the error ledger copies it: `docs/appendices/template-16-production-readiness.md` §16.2.
- `scripts/gate_check.py` replays a CSV against the per-category thresholds.

## Vendor seat

Launch release conditions are the contract's acceptance clauses tied to the eval; the crosswalk says eval as spec applies as is. An acceptance clause reading "accuracy ≥ 90%" is one line, and it buries unsafe exactly as the counterexample does. A line in a contract is not a working mechanism.
