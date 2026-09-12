# Pilot kill criteria

Source: `docs/appendices/template-14-stage-gates.md` §14.3–14.4 (and `repo/templates/stage-gates/kill-criteria-weekly-report.md`; the repo wins on conflict).

Timing rule: written in the same meeting as the escalation resolution, signed the same day. Kill criteria are written during the excited period. They cannot be written during the disappointed one. A stop standard written only after entering the pilot is void.

| Header field | Fill in |
|---|---|
| Pilot name / start, end and duration | <pilot>, <start date>, <end date>, <N weeks> REQUIRED |
| Owner (first signatory on "stop or not") | <owner name> REQUIRED |
| Signatures | <delivery lead name>, <business owner name>, filed with <sponsor name>, dated <date> REQUIRED |
| Relationship to the charter's resource reassessment conditions | This sheet is a pilot-level operating trigger, executed by the action in its own row. Project-level shutdown is still ruled by the charter's resource reassessment conditions (element 7), and the power to shut down runs one way, to the sponsor / the project approval committee. Neither replaces the other |
| Resource renewal point | <the next round of people and compute, written as the three gates and the graduation criteria, no dates> |
| Reassessment date | <date, set with the pilot launch day>; if it comes due with no escalation resolution, settle on the graduation criteria and convert to formal project approval or shut down REQUIRED |

**Item table** (every row a hard number, no "assess as the situation warrants")

| # | Trigger (the data appears, it stops) | Data source | Action on trigger | Recovery condition | Recheck cadence |
|---|---|---|---|---|---|
| 1 unsafe | Unsafe-class errors ≥<N> in a single week (one occurrence once the step sits at the act layer) | Weekly retrospective record of suspected unsafe cases | Pilot pauses for rework, that whole class of suggestion degraded to human review, root cause retrospective | Golden case replay passes after the fix, the owner signs the restart | Every <Friday> |
| 2 North Star | Weekly median of <metric> above the 8-week pre-pilot baseline (rule), two consecutive weeks (rule) | Weekly points on the run chart | Pause the expansion, check the data source (fitness retest) before the system | Two consecutive weeks back below the baseline | Every <Friday> |
| 3 Cost | System cost per <case> above <fraction> of the value of the labor hours it saves, two consecutive weeks (rule) | The cost ledger page, not the month-end bill | Pause the expansion, cost review | Back under the value line and held two weeks | Every <Friday> |
| 4 Acceptance | Target user group's weekly usage rate below <agreed line>, two consecutive weeks (rule) | Usage logs | Pause the expansion, go back to users to locate the reason | Reason closed out and usage recovers for a week | Weekly |
| 5 Business-side input (required) | Committed data access or people unmet two consecutive weeks (rule) | Scheduling records | Triggers the charter's resource reassessment conditions, handled at the matching tier | Input resumes | Weekly |

**Weekly report** (one per recheck): pilot name; week and dates; recorded by; unsafe count this week against the red line, not triggered / triggered → execute now; one row per suspected or confirmed unsafe event (date, case ID, description, verdict, disposition, counts toward red line); every other row rechecked with this week's data, triggered / not triggered, status of the post-trigger action; sign-off by the owner (first signatory), the delivery lead, the sponsor on file.

**Rules**
- A trigger means executing the action in its row, with no meeting reopening the standard itself. The time to argue the standard has passed.
- A trigger is not a failure, it is the defense holding. The first sentence of the outward notice says the mechanism held, then the root cause investigation.
- After entering the pilot, adding items is allowed, loosening existing ones is not.
- Record every recheck (triggered / not triggered), and archive the whole sheet when the pilot ends. This sheet gets checked line by line again in the incident retrospective after launch.
- A case that has triggered goes into the golden cases permanently (historical incident cases).
- The data does the stopping. People only sign the restart.

**What a wrong filling looks like**
- "Kill criteria: assess flexibly as the pilot runs." The exact phrase forbidden; no row, no number, no action, so nothing fires without a meeting.
- A row written after the pilot data looked bad. By then every proposed line is a position, and the final standard is a mark of power.
- An owner column reading "<department> will arrange a dedicated person later." No first signatory on "stop or not," and no one to sign a restart.
- A trigger written as "the owner decides whether to pause." A person's decision, not an automatic action; whoever says stop first owns the conclusion.

Filled in → goes to: the weekly report every recheck day (`repo/templates/stage-gates/kill-criteria-weekly-report.md`); the impact memo's defense record ("zero triggers" written as zero triggers, `templates/memo-impact.md`); the post-launch incident retrospective.
