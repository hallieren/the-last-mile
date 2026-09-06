# Template 11 · Eval Spec, Golden Case Collection List, Annotation Disagreement Log

> Companion chapter(s): Chapter 11. The three tools are in order of use. Set up the spec skeleton first (11.1), then collect cases by the list to fill it (11.2), and record every disagreement during annotation in 11.3, rule on it, and settle it into a rule.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 11.1 Eval Spec Template (Five Parts, Fill Section by Section)

One eval spec evaluates one task. Fill the document header with: project name / version and date / co-builders (actual users by name) / trigger condition for the next retest.

### 11.1.1 Task Definition

| Item | Fill In |
|----|------|
| One-sentence task (workflow claim level) | e.g., for every auto exception claim entering the queue, give the next action, the owner, and a risk flag, for the reviewer to follow or override with a stated reason |
| Input | Data sources and fields (cite the source of truth decision log, Template 9.4) |
| Output | Field list (suggestion + reason + Human Call column are mandatory) |
| Users | Named down to the team |
| Red line (what this task does not do) | e.g., no suggested payout amounts (cite the scope decision log, Template 8) |

### 11.1.2 Golden Cases List

Size 50–200 cases. Register each one:

| Case ID | Source Type (typical / edge / historical incident / annotation disagreement) | Input Summary | Correct Answer | Basis for Answer (reconciliation evidence / confirmed by the person involved) | Annotator | Date |
|---------|------|----------|----------|----------|--------|------|

**Rules**:
- [ ] Every fact a "correct answer" cites must stand at validated or above on the data fitness ladder. Candidate claims that do not reconcile go through the three-way reconciliation first (Template 9.3), and those that cannot be ruled on are dropped.
- [ ] The annotation basis cites an entry in the annotation guide (e.g., "rule of thumb 4: prior claim linkage"), and the guide carries a dated version.
- [ ] Check the makeup of the set against the mix lines in 11.2.

### 11.1.3 Error Taxonomy

| Error Category | Definition | Business Consequence | Error Severity Vocabulary (unsafe / concern / useless) | Tolerance |
|----------|------|----------|-----------------------------------|--------|
| e.g., missed risk | A high-risk claim judged routine | Grows into a major case, regulatory complaint | unsafe | Zero tolerance |

**Rules**: the unsafe class must come from asking the actual user "which kind of error can you not accept even once." Each category states a "consequence," not a "technical cause." The taxonomy is layered by cost, not by bug type.

### 11.1.4 Per-Category Thresholds and Acceptance Lines

| Error Category | Threshold (on golden cases) | Acceptance Line | Retest Cadence |
|----------|------------------------|--------|----------|
| e.g., missed risk | 0 cases | 0 cases | Rerun on every update to the set |
| e.g., material error | ≤10% | ≤10% and the trend does not rise over three consecutive replays | Monthly |

**Rules**: **no overall score**. Any "overall accuracy X%" is the shortest path to burying the unsafe class. Thresholds and launch release conditions cite each other (Chapter 4).

### 11.1.5 Human Review Path

| Item | Fill In |
|----|------|
| Trigger condition | e.g., hits a risk rule with low confidence / suspected unsafe-class output |
| Destination and owner | e.g., the queue's "pending human" column, the review team lead |
| Time limit | Review must happen within how long |
| Flow-back mechanism | Review conclusions are added to the golden cases monthly; suspected unsafe-class errors are reviewed weekly |
| Flow-back owner | Who is responsible for adding review conclusions to the golden cases on cadence and bumping the guide version with them, named to a person |
| Reminder mechanism | Hang it on a meeting that owner already holds (e.g., the monthly QA review), no new reminder, do not rely on anyone remembering |

---

## 11.2 Golden Case Collection List

### Four Source Types and Where to Find Them

| Type | Definition | Where to Find | Mix Line |
|------|------|----------|--------|
| **Typical cases** | High frequency, answer undisputed | Random sample from the source of truth | **Under half** |
| **Edge cases** | Cases right at a rule's threshold | Aged claims, claims at the amount threshold, claims where rules conflict | ≥30% |
| **Historical incident cases** | Cases that once went wrong or were misjudged | Complaint log, retrospective notes, internal audit reports, regulatory inspections, veterans' "the one I got wrong" stories | ≥10% |
| **Annotation disagreement cases** | Cases the two annotators marked differently (entered after ruling in 11.3) | The annotation session itself | Added continuously |

Edge cases and historical incident cases are the soul of the eval. That is where the system's value and its risk both live.

### Collection Steps

- [ ] 1. Finish the 11.1.1 task definition first. Without a task, there is no way to judge whether a case is representative.
- [ ] 2. Draw candidates from the source of truth (not the easiest database to reach), preparing 1.5 times the target count.
- [ ] 3. **Clear the data check case by case**: where the three sources agree, in; where they disagree, rule by three-way reconciliation; where no ruling is possible, drop (Chapter 9's baseline: skip this step and nearly half the answers may be wrong).
- [ ] 4. AI pre-fills fields and drafts answers (AI does the grunt work); the actual user rules on the final answer (people make the calls).
- [ ] 5. Double independent annotation, disagreements go through 11.3.
- [ ] 6. Enter with version and date; bump the annotation guide version in step.
- [ ] 7. Set the rolling update cadence: cases flowing back from review are added monthly; drift in business rules (e.g., a change to a list-type rule) triggers an immediate update.

---

## 11.3 Annotation Disagreement Log

An annotation disagreement is not noise. It is a business rule that was never aligned, surfacing. One row per disagreement, and the loop closes only when it is "settled into a rule":

| Disagreement ID | Case ID | Annotator A Mark + Reason | Annotator B Mark + Reason | Root Cause (different standards / different information / different reading of the task) | Type (within-department / cross-department / compliance-related) | Ruled By | Ruling | Settled into a Rule (which entry of the annotation guide) | Date |
|---------|---------|----------------|----------------|--------------------------------|--------------------------------|--------|----------|----------------------------------|------|
| e.g., D-01 | 37 | High risk: phone number appearing for the third time in six months | Routine: shop-filed claims are common, count only plate + filer | Different standards, whether "prior claim linkage" counts the phone number | Within-department | Kevin Doyle (Director of Claims Operations) | Phone number counts toward the signal; on its own it only triggers human review | New exception scenario added to guide section 4.2 | / |

**Rules**:

- [ ] Trace the root cause before talking about a ruling: **different standards** need a business decision; **different information** means fill in the information and annotate again; **different reading** means go back and fix the 11.1.1 task definition.
- [ ] Route disagreements one of three ways by type, and never let one hang. **Within-department disagreement**, find the owner of this workflow, rule on the spot, and write the ruling into the annotation guide. **Cross-department disagreement**, pause annotation, write both definitions and their business consequences on half a page, and send it to the two sides' common superior or put it on the sponsor weekly as an agenda item. **Compliance-related disagreement**, cross-department or not, goes to the risk owner (Chapter 11).
- [ ] The person ruling must hold business decision rights (the workflow owner or above), not a vote or a compromise between the two annotators.
- [ ] Every ruling must be settled into one executable line of text in the annotation guide, or the same disagreement comes back on another claim.
- [ ] Disagreement cases themselves go into the golden cases (the fourth type in 11.2). They are the cases with the highest information density in the set.
- [ ] Report the disagreement rate and the number ruled on. The disagreement rate is not poor annotation quality, it is the number of missing pages in the requirements document. Every ruling is one more business rule the organization has aligned.

---

## 11.4 Counterexample: A Tidy-Looking Wrong Answer

An excerpt of the five parts. Every section has content, and it looks like a spec:

```
Task definition: Comprehensively evaluate the quality of AI output in the claims scenario.
Golden cases: 50, randomly exported from the test database; answers filled in by Victor Reyes (security reviewer) against the system fields.
Error taxonomy: one category, "output error"; tolerance: as few as possible.
Threshold: overall accuracy ≥ 90% passes acceptance.
Human review: handled by human intervention when necessary.
```

Line by line:

1. The task definition is not at workflow claim level. "Comprehensively evaluate output quality" has no action, no user, and no red line, so every section after it has no target.
2. The golden cases break three rules: drawn from the easiest database to reach, not the source of truth; answers taken from the system fields, which by Chapter 9's baseline means nearly half may be wrong without reconciliation, and the rule requires standing at validated or above; Victor annotating alone, so with no double annotation there are no 11.3 disagreements to record, and disagreements are where business rules surface, and he is not the actual user.
3. The taxonomy has one category and no business consequence. The taxonomy is layered by cost; the unsafe class must come from asking Linda "which kind of error can you not accept even once."
4. "Overall accuracy 90%" is exactly the overall score 11.1.4 forbids: 2 missed risks out of 50 still scores 96%, and unsafe is buried in the average.
5. "Human intervention when necessary" is missing four things: no trigger condition, no owner, no time limit, no flow-back. Review conclusions cannot get back to the golden cases, so this eval is one-shot.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/eval-spec/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/eval-spec/): this appendix's eval run scaffolding and per-category threshold report script
