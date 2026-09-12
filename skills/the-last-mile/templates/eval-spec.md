# Eval spec and annotation disagreement log

Source: `docs/appendices/template-11-eval-spec.md` §11.1, §11.3, §11.4 (and `repo/templates/eval-spec/eval-spec-template.md`; the repo wins on conflict).

One eval spec evaluates one task. Finished before the architecture decision meeting; signed by the business owner and the risk owner, not by the people who built it.

| Header field | Fill in |
|---|---|
| Project name | <project> |
| Version and date | <version>, <date> REQUIRED |
| Co-builders (actual users, by name) | <user name>, <user name> REQUIRED |
| Trigger condition for the next retest | <event, e.g. a list-type rule changes, monthly flow-back lands> REQUIRED |

**1. Task definition (workflow-claim level)**

| Item | Fill in |
|---|---|
| One-sentence task | For every <case type> entering <queue>, give <next action, owner, risk flag> for <user group>, to follow or override with a stated reason REQUIRED |
| Input / Output | <data sources and fields, cite `templates/data-fitness-and-source-of-truth.md`> / <field list; suggestion + reason + Human Call column are mandatory> |
| Users / Red line | <named down to the team> / <what this task does not do, e.g. no suggested amounts, cite `templates/scope-decision-log.md`> REQUIRED |

**2. Golden cases, 50–200 (rule)**

| Case ID | Source type (typical / edge / historical incident / annotation disagreement) | Input summary | Correct answer | Basis for answer (reconciliation evidence / confirmed by the person involved) | Annotator | Date |
|---|---|---|---|---|---|---|

**3. Error taxonomy**

| Error category | Definition | Business consequence | Grade (unsafe / concern / useless) | Tolerance |
|---|---|---|---|---|
| <category the user cannot accept even once> | <definition> | <consequence> | unsafe | Zero tolerance, 0 cases REQUIRED |

**4. Per-category thresholds and acceptance lines**

| Error category | Threshold (on golden cases) | Acceptance line | Retest cadence |
|---|---|---|---|
| <unsafe category> | 0 cases | 0 cases | Rerun on every update to the set |
| <concern category> | ≤<N>% | ≤<N>% and the trend does not rise over three consecutive replays (rule) | <monthly> |

**5. Human review path**

| Item | Fill in |
|---|---|
| Trigger condition | <hits a risk rule with low confidence / suspected unsafe-class output> REQUIRED |
| Destination and owner | <the queue's Human Call column>, <reviewer name> REQUIRED |
| Time limit | <review within N hours>, daily volume worked back from the review time budget |
| Flow-back mechanism and owner | Review conclusions added to the golden cases monthly; suspected unsafe reviewed weekly; owner <person name> REQUIRED |
| Reminder mechanism | <a meeting that owner already holds, e.g. the monthly QA review> |

**Annotation disagreement log**

| Disagreement ID | Case ID | Annotator A mark + reason | Annotator B mark + reason | Root cause (different standards / different information / different reading of the task) | Type (within-department / cross-department / compliance-related) | Ruled by | Ruling | Settled into a rule (guide entry) | Date |
|---|---|---|---|---|---|---|---|---|---|

**Rules**
- Every fact a "correct answer" cites must stand at validated or above on the data fitness ladder. Candidate cases that do not reconcile go through the three-way reconciliation first, and those that cannot be ruled on are dropped. The annotation basis cites an entry in the annotation guide, and the guide carries a dated version. Check the makeup against the mix lines: typical under half, edge ≥30%, historical incident ≥10% (rule).
- The unsafe class must come from asking the actual user "which kind of error can you not accept even once." Each category states a consequence, not a technical cause. The taxonomy is layered by cost, not by bug type.
- No overall score. Any "overall accuracy X%" is the shortest path to burying the unsafe class. Thresholds and launch release conditions cite each other.
- Trace the root cause before talking about a ruling: different standards need a business decision; different information means fill in the information and annotate again; different reading means go back and fix the task definition.
- Route by type and never let one hang. Within-department, the workflow owner rules on the spot and it goes into the guide. Cross-department, pause annotation, half a page with both definitions and consequences to the common superior or the sponsor weekly, ruled within two weeks (rule). Compliance-related, the risk owner.
- The person ruling holds business decision rights, not a vote or a compromise between the two annotators. Every ruling is settled into one executable line of the guide, or the same disagreement comes back. Disagreement cases go into the golden cases. Report the disagreement rate and the number ruled on.

**What a wrong filling looks like**
- Task: "Comprehensively evaluate the quality of AI output in the <domain> scenario." No action, no user, no red line, so every section after it has no target.
- Golden cases: 50 randomly exported from the test database, answers filled in by the security reviewer against the system fields, one annotator. Easiest database, unreconciled answers, not the actual user, no disagreements possible.
- Taxonomy: one category, "output error"; tolerance "as few as possible." No business consequence, not layered by cost.
- Threshold: "overall accuracy ≥ 90% passes acceptance." 2 missed risks out of 50 still score 96% (illustrative); unsafe buried in the average.
- Human review: "handled by human intervention when necessary." No trigger, owner, time limit or flow-back; the eval is one-shot.

Filled in → goes to: the charter's release conditions (`templates/deployment-charter.md` element 6), gate one in `templates/escalation-gates.md`, and the error ledger (`docs/appendices/template-16-production-readiness.md` §16.2), all reading this table as is.
