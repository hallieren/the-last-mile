# Template 22 · Handoff Plan, Five Self-Sufficiency Tests, Handoff Cadence Sheet

> Companion chapter(s): Chapter 22. The three tools are in order of use. Fill in the plan template (22.1) when the handoff starts, because until the owners are named, the two sheets after it have no subject. Run the test sheet (22.2) item by item in stage three. Lay out the cadence sheet (22.3) from handoff start to the closing of the response window. It picks up from the "handoff checklist" at the last beat of Template 15's cadence sheet.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 22.1 Handoff Plan Template

### 22.1.0 Plan Header

| Item | Fill In |
|----|------|
| Project / system | |
| Handoff start date / target exit date | |
| Response window (length and scope, terms in 22.3) | |
| Signatures (four owners + the delivering team's lead) | |
| Transfer ledger entry number (PMO AI system transfer ledger) | |

### 22.1.1 Owner Placement Sheet

Rules: one real name per row. One person may hold several rows, but each row holds only one name. "The team is responsible" means nobody is responsible.

**Blank template**:

| Role | Responsibility | Real Name |
|------|------|------|
| System owner | Budget and priorities, the four-ledger running budget (Chapter 16), request scheduling, first signature on whether to stop | |
| Maintenance owner | Code and production, gatekeeping rights over every module, releases, first-line incident response | |
| Eval guardian | Approving new golden cases, the weekly review, annotation guide version control | |
| AI dependency owner | Model and platform changes, evaluating and signing off on provider model version upgrades, dependency library changes, and platform migrations | |

**Anchor & Helm example**:

| Role | Anchor & Helm Placement |
|------|----------|
| System owner | Kevin Doyle (from the week 22 budget cycle) |
| Maintenance owner | The two claims-ops IT engineers hold gatekeeping rights by module (one person per module; every module on the business line side from week 24) |
| Eval guardian | Linda Marsh (from week 23) |
| AI dependency owner | The younger engineer runs the replay, Linda Marsh (quality) and Kevin Doyle (cost) sign |

### 22.1.2 Three AI Handoff Items Owner Sheet

The vocabulary of a traditional IT handoff does not have these three. They are the easiest to miss and the most fatal. Name an owner for each, no blank rows allowed:

**Blank template**:

| Item | Question to Answer | Receiver Type (Business / Ops / Platform) | Real Name |
|----|--------------|------------------------------|------|
| Continuous eval updating | Who adds golden cases, who approves them? Who guards the per-category thresholds? | [business / ops / platform] | |
| Re-verification on model and dependency changes | On a model version switch or dependency upgrade, who runs the golden cases replay? Who signs "safe to switch"? | [business / ops / platform] | |
| Decision trail review | Who chairs the override review? Who analyzes the reason code distribution? Who runs the fairness spot check? | [business / ops / platform] | |

**Anchor & Helm example**:

| Item | Anchor & Helm Owner | Receiver Type |
|----|----------|------------|
| Continuous eval updating | Adding: review flow-back + the review team; approving: Linda Marsh | Business |
| Re-verification on model and dependency changes | Runs the replay: the younger engineer; signs: Linda Marsh (quality) + Kevin Doyle (cost) | Business |
| Decision trail review | Chairs: Linda Marsh; analyzes: the older engineer; the quarterly fairness spot check likewise (Chapters 12/18) | Business |

---

## 22.2 Five Self-Sufficiency Tests Sheet

Rules: the test method is always **Show Me**, you are in the room and do not step in; inject the scenario into the real system wherever possible; any failure sends the item back for rework, and what gets added is a drill, not a document; only when all five pass does stage four of the cadence sheet begin.

| Capability | Show Me Scenario | Pass Standard | Rework Action on Failure |
|------|----------------|----------|--------------|
| Run | Cut one AI dependency point without warning | The business side degrades, notifies by the template, and recovers on its own, with no instruction from the deliverer the whole way | Rerun the degradation drill (Template 16.3), add an incident notice drill |
| Configure | One real configuration change (list / threshold / rule parameter) | The full change, test, release cycle runs on the business side's gatekeeping rights, and the change passes the eval replay | Walk it again as a pair, check configuration item permissions and documents |
| Exceptions | Inject a class of situation the system has never seen | The first reaction is the escalation path, not the deliverer; the ruling gets settled somewhere (into the golden cases or a rule) | Draw the escalation tree together + two injection drills, then retest |
| Evolve | One small request end to end + one model version upgrade | From scheduling to rotating release with no commit from the deliverer; the upgrade passes the golden cases replay and gets both signatures | Back to co-build pairing (Chapter 15), shrink the request and retest |
| Teach | The business side onboards one newcomer | The newcomer handles the queue independently within two weeks; the training material is maintained by the business side itself | Have the newcomer recount where they got stuck. Fix the mentoring path, not the manual |

**Anchor & Helm example (the "exceptions" failure, as it happened)**: Week 25, the rainstorm batch (dozens of interrelated auto damage claims entering the queue at once, identical missing documents, tangled risk signals), and the claims operations team's first reaction is to call you → recorded as **failed**. Two weeks of rework: escalation tree (check the decision trail and drift signals first → Linda Marsh judges → beyond scope, escalate to Kevin Doyle, with that class of claims paused and routed to manual handling if needed) + two injection drills. Retest in week 27 passes. The ruling routes to manual, the incident case goes into the golden cases the same day, the phone does not ring. Note that the failure is not an incident. It is the test doing its job. The value of a test is not in passing. It is in exposing.

---

## 22.3 Handoff Cadence Sheet

| Stage | Who Chairs the Retrospective | Who Touches Production | Who Answers Outside Questions | Condition for the Next Stage |
|------|--------------|----------|--------------|--------------------|
| 1 Your team leads (business side observes) | Your team | Your team | Your team | Co-build agreement in force, gatekeeping rights of the first module handed over (Chapter 15) |
| 2 Shared lead | Business side chairs, your team adds | Both, gatekeeping rights handed over module by module | Business side answers, your team backstops | Gatekeeping rights of every module on the business line side, four consecutive retrospectives chaired by the business side |
| 3 Business side leads (your team advises) | Business side | Business side (your team no longer commits) | Business side | All five self-sufficiency tests passed (22.2) |
| 4 Stepping out of the daily | Business side | Business side | Business side | Response window closed with written confirmation, write access reduced to read-only, no open rework items |

**Response window terms** (written into the responsibility transfer agreement):

- Length: 3 months recommended, the period when the new team's confidence is most fragile.
- Scope: only two kinds are taken, P1 incidents (an unsafe reaching human eyes, scale in Template 18.2.1) and exceptions the escalation tree ran to the end and did not catch. Daily ops and routine requests are outside the window. Taking one means falling back to stage three.
- Record: log every request for help inside the window; review once before the window closes, which capability each request pointed to, and whether to add one targeted drill.
- On expiry: write access drops to read-only, removal from the oncall rotation and the retrospective's standing attendee list (the design of co-build clause one is honored here, Chapter 15).
- Closing the window: needs written confirmation from the business owner and the ops owner. No confirmation means extension by default, and extension by default means permanent ops.

---

## 22.4 Counterexample: A Tidy-Looking Wrong Answer

An excerpt from a handoff completion report, and it looks fine at the retrospective:

```
Handoff deliverables: ops manual (52 pages), architecture diagram, code repository and account transfer form,
  2 training sessions (sign-in photos on file), 8 screen recordings of operations.
Owner placement: system owner: Kevin Doyle; maintenance owner: the business line engineering team;
  eval guardian: to be decided by the business side after handoff.
Five self-sufficiency tests: covered by documentation, training, and Q&A, deemed passed.
Response window: we are right here in the company, come find us anytime.
```

Line by line:

1. The deliverables list is all nouns (manual, accounts, code, recordings) and not one verb (can respond, can judge, can evolve). Chapter 22's test is exactly this ratio. Documents are the shadow of capability, and a shadow cannot hold the system up.
2. "The business line engineering team" breaks the placement sheet's first rule. Each row holds only one name, and team responsible equals nobody responsible.
3. Eval guardian "to be decided after handoff" = a blank row on the three AI handoff items owner sheet. The easiest to miss and most fatal item really was missed. Nobody approves golden cases, and the eval starts rotting from handoff day.
4. "Training deemed passed" swaps out 22.2's test method. All five capabilities are Show Me, cut a dependency, inject an exception, run a real change end to end. Having heard the lesson and being able to catch it are two different things, and Anchor & Helm's rainstorm batch in week 25 is the evidence.
5. "We are right here in the company, come find us anytime" looks considerate and is in fact never exiting. The internal team was always in the company, and nobody comes to revoke your access. The response window must state a length (3 months recommended), a scope (only P1 and exceptions the escalation tree did not catch), and written confirmation of closing. Missing any one is extension by default, and extension by default is permanent ops.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/handoff/checklist.yaml`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/handoff/checklist.yaml): sample machine-readable handoff checklist, validates the named-owner fields for the four owners and the three AI items (a blank name raises an alert)
- [`templates/handoff/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/handoff/): five self-sufficiency tests state machine (pending / failed / passed, failed must carry a rework action and a retest date)
- [`templates/handoff/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/handoff/): response window countdown and help request log template
