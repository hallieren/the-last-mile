# Template 18 · Metric Tree, AI Incident Runbook, Same-Day Notice

> Companion chapter(s): Chapter 18. The three tools are in launch order. Before launch, build the metric tree and baseline (18.1), write the incident runbook (18.2), and have the same-day notice template ready (18.3). All three must be done before the first incident happens.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 18.1 Metric Tree Template

### 18.1.1 Three-Layer Structure (Fillable)

One row per metric. **The owner and "action on deviation" columns may not be left blank.** Delete any metric you cannot write an action for. It is only scenery.

| Layer | Metric | Definition and Measurement | Data Source | Baseline | Owner | Owner's Reporting Line | Action on Deviation (Who Does What) |
|----|------|-----------|----------|------|-------|-----------------|----------------------|
| North Star (outcome) | | From the charter, the only one | | ≥8 weeks before launch | | | |
| Process (mechanism) | | Can be changed directly by an action | | | | | |
| Process (mechanism) | | | | | | | |
| Balancing (cost) | | The cost the improvement may shift onto someone | | | | | |
| Balancing (cost) | | | | | | | |

### 18.1.2 Anchor & Helm Example

| Layer | Metric | Definition and Measurement | Owner | Owner's Reporting Line | Action on Deviation |
|----|------|-----------|-------|-----------------|----------|
| North Star | First-touch handling time | From an auto exception claim entering exception status to first handling complete, weekly median, shown on a run chart | You + Kevin Doyle | Dual owner, inside your team + business side | Two consecutive points back above the baseline median → go through the process layer for the cause |
| Process | Queue aging | Count of overdue claims in the queue not moved | Linda Marsh (team lead) | Business side, does not report to you | Over the line → claimed and cleared the same day |
| Process | Missing-document detection lead time | Time from a claim entering exception status to the missing document being identified and a chase sent, against baseline | Your team's engineer (renamed line by line at handoff) | Inside your team | Lead time shrinks → check the extraction pipeline |
| Process | Override rate | Split by suggestion category (per-category measurement, no overall average) | You | Inside your team | A sudden change in one category → trace back that category's rule implementation and list version |
| Process | Status-in-doubt list length | Count of claims the queue flags as status in doubt (Chapter 9's operating item) | Kevin Doyle | Business side, does not report to you | Continuous growth → re-check the review team's ten-minutes-a-day status cleanup discipline |
| Balancing | Complaint rate | Complaints related to exception claims, shown on the same page as the outcome | Kevin Doyle | Business side, does not report to you | Rising → check chase scripts and frequency |
| Balancing | Reviewer overtime hours | Weekly overtime for Linda's team | Kevin Doyle | Business side, does not report to you | Rising → check the queue's daily volume setting |
| Monitoring surface (fairness) | Override distribution spot check by segment | Override distribution by customer segment, once a quarter (Chapter 12's fairness row) | You + Victor Reyes | Inside your team + risk owner | Significant skew → trigger a fairness review |

### 18.1.3 Checklist

- [ ] One North Star, word for word the charter North Star; no new metric set up after launch.
- [ ] **Every metric has an owner and an action on deviation**; the owner is a named person, not a department.
- [ ] For metrics whose owner does not report to you, the action on deviation is written into their team SOP or weekly meeting agenda, not left hanging on your reminders; an action written into the SOP is their job at review time.
- [ ] Balancing metrics ≥2, shown on the same page as the outcome metrics; a balancing metric on a separate page is always "next time."
- [ ] Baseline: ≥8 weeks of data before launch, cleared through the data check claim by claim (whatever does not reconcile is corrected first, Chapter 9).
- [ ] The run chart shows every point, no picking weeks; improvement is claimed only when a special cause signal appears (such as "six points on one side": six consecutive points on the same side of the baseline median, paraphrased from *The Health Care Data Guide*).
- [ ] The monitoring surface (override alert thresholds, error category distribution, golden cases replay cadence) is maintained in the same table as the metric tree, with definitions citing the eval spec (Template 11).

---

## 18.2 AI Incident Runbook

### 18.2.1 Level Table

| Level | Definition | Response | Anchor & Helm Example |
|------|------|------|----------|
| **P1** | An unsafe-class error enters human view; **being caught by a person does not downgrade it** (what caught it was already the last line of defense) | Draft the same-day notice within two hours; retrospective within 48 hours; incident case into the golden cases within 24 hours | A risk claim suggested as routine |
| **P2** | Concern-class errors over threshold or appearing in batches | Retrospective the same week; trace back rules and data sources | Missing-document lists wrong in batches |
| **P3** | A rising trend in useless-class errors | Folded into the monthly retrospective | Share of empty suggestions rising two weeks running |

### 18.2.2 The Four Retrospective Questions

Go layer by layer. Wherever the fault is located, that is where the repair goes. **Attribution decides the repair path. Attribute it to the wrong layer and the repair fixes the wrong place.**

| Layer | Test Question | Typical Repair Path |
|----|----------|--------------|
| **Model layer** | The input signal was sufficient and the model still judged wrong? | Switch pattern / add a human review gate / lower the decision rights layer |
| **Data layer** | The input itself was wrong (list not updated, fields distorted, source drift)? | Fix the data + add operating discipline (give the data asset an owner and an update cadence) |
| **Rule layer** | A rule missing, or the implementation inconsistent with the annotation guide? | Change the rule, release a new dated version of the annotation guide |
| **Interaction layer** | A person saw it but had no time / no basis / no authority to stop it? | Change the queue design (fix the three oversight questions item by item, Chapter 12) |

Note: the table is in definition order of the four layers. For the order of investigation see Chapter 18's four retrospective questions (model → rule → interaction → data).

The attribution walkthrough for Anchor & Helm's misclassification incident: model layer (no usable signal in the input, not a model capability problem); rule layer (implementation consistent with the guide); interaction layer (all three questions pass, the catch succeeded); **data layer hit** (the repair shop list did not cover a newly registered entity). Repair: the list promoted to an operating asset with an owner (monthly update, dated version, config item changeable), not a model swap.

### 18.2.3 Incident Case Flow-Back into Eval

- [ ] 1. The incident case goes into the golden cases within 24 hours (historical incident category, Template 11.2), kept permanently.
- [ ] 2. The kill criteria are checked by the book and recorded, **whether or not they trigger**; the check record is attached inside the incident record (Chapter 14).
- [ ] 3. The retrospective conclusion is settled in writing. Rule layer changes go into a dated version of the annotation guide; data layer changes state the new owner and update cadence.
- [ ] 4. After the repair goes live, the golden cases (including the new incident case) are retested once, and the result is attached to close the incident record.
- [ ] 5. If an error of the same shape recurs, respond at the next level up. The runbook itself gets a retrospective too.

---

## 18.3 Same-Day Notice Template

Three parts, and the order cannot change: the defense first, then the scope, and root cause last. **Drafted within two hours, sent the same day**; the distribution is drawn by "how far the rumor can reach," and no individual is named as responsible.

> **[Notice] On today's [error category] by [system name]**
>
> Issued by [business-side owner; you are the drafter]
>
> ① [The defense held] Today at [time], the system suggested a claim that should have been [X] as [Y]. [Review role] caught it in the Human Call column and overrode it. **That step exists to catch exactly this kind of error. The defense worked as designed, and the full trail is on record.**
> ② [Scope of impact] No real action was taken on the claim; all suggestions from [today / the same period] have been checked, [no error of the same shape / N more claims handled together].
> ③ [Root cause under investigation] Preliminary direction [one-sentence direction], retrospective conclusion and improvement measures within [deadline].

Anchor & Helm example (pilot week 5):

> Issued by Kevin Doyle. This morning the queue suggested a high-risk claim as routine. The review team lead caught it in the Human Call column and overrode it to high risk. That column exists to catch exactly this kind of error. The defense worked as designed, and the full trail is on record. Scope of impact: no real action was taken on the claim; today's queue has been checked, and there is no error of the same shape. Root cause under investigation, preliminary direction the repair shop list not covering a newly registered entity, retrospective conclusion within 48 hours.

**Rules**:

- [ ] Part one always states the interception mechanism first, then the error. This is the correct order of the facts, not spin. The system's design premise is that AI will make mistakes and people backstop them.
- [ ] You hold the drafting right, the business-side owner holds the issuing right; only when the person with the power to violate this defense issues it does the notice avoid being read as the technical team defending itself.
- [ ] The scope of impact states only verified facts; what is not verified is written as "being checked," never a guess.
- [ ] The promised retrospective deadline must be met. The notice itself is a reliability deposit (Chapter 5).
- [ ] Before any incident, drill once with a historical wrong output and time it; lock down in advance any step that runs past two hours.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/metric-tree/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/metric-tree/): run chart generation script (baseline median and special cause signal marked automatically) and sample override alert threshold config
