# Template 16 · Production Readiness Checklist and Running Budget Sheet

> Companion chapter(s): Chapter 16. The three tools are in order of use. Before launch (prototype up to pilot, pilot to production) run the gate item by item with 16.1. Fill in 16.2's four-ledger running budget sheet before launch and reconcile it weekly after. Register the fallback for every AI dependency point in 16.3, and only a drill that passes counts as "having a degradation path."
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 16.1 Production Readiness Checklist

Tick item by item. Any "no" is either fixed, or accepted out loud at the escalation decision meeting with the accepting person written down. Passing in silence is not passing.

### Cost Ledger

- [ ] Is the cap on cost per claim set? Worked back from business value (what the labor hours one claim saves are worth, with system cost allowed only a fraction of it), not worked back from last month's bill.
- [ ] Does the cost instrument produce numbers daily, split by step (extraction / priority / other call points)? The month-end bill should only ever be a confirmation, never news.
- [ ] Do retries have a budget and a backoff (a per-claim cap on attempts, and where it goes over the limit, such as the "pending human" column)?
- [ ] Is recomputation incremental, or does every refresh run the whole thing again?
- [ ] Have the static blocks in the prompt (the manual, whole rule texts, piles of examples) been checked? Has everything that can move into retrieval or a cache been moved?
- [ ] Are the results for stable inputs cached (the same email is not paid for twice)?
- [ ] Are calls tiered? Are claims that do not need the big model using the big model? Is there eval evidence for where the split goes?

### Latency Ledger

- [ ] Is the P95 cap set? Worked back from the user's working rhythm. Averages do not count.
- [ ] Has the peak window (the morning peak, say) been measured on its own (with real concurrency, not one person clicking once)?
- [ ] Is everything that can be precomputed computed before the user arrives?
- [ ] Is the refresh asynchronous (show the most recent result with its timestamp marked first, update in the background)?

### Error Ledger

- [ ] Do the per-category error rate caps carry the eval spec threshold table over as is (Template 11.1.4)? Build nothing new, set no overall score.
- [ ] Is the online sampling cadence set (the golden case replay period, the spot-check proportion of production output, who reviews)?
- [ ] Are spot-check results booked by category, with the action on breach written down (rework / kill criteria, Template 14)?

### Degradation Ledger

- [ ] Does every AI dependency point have its fallback registered in 16.3?
- [ ] Has the degradation path been drilled (the kind where the dependency is really cut and real users are present)?
- [ ] Is the degradation trigger automatic (a failure rate or latency breach switches it over), or does it count on somebody switching by hand in the middle of the night?
- [ ] Is the rules layer still alive (an owner, tests, updated as business rules change)? Before deleting it, answer this. On the day supply is cut, what do you rely on?

### Observability

- [ ] Can any single suggestion be replayed from the trace (input snapshot, what was retrieved, prompt and model version, which rules hit, final display)?
- [ ] Are the trace and the audit decision trail kept apart? The trail answers "who decided what" (an audit commitment, Chapter 12), the trace answers "why does this suggestion look the way it does" (engineering replay). You need both.
- [ ] Are drift alerts configured (a sudden change in the input distribution, a sudden change in the override rate)?
- [ ] Have the alerts been verified? An alert that has never fired needs one firing manufactured for it. An alarm that does not sound is more dangerous than no alarm.

### Operating Ownership

- [ ] Does each of the four ledgers have a named owner (is the last column of 16.2 filled in)? A ledger you cannot put a name to will not be managed.
- [ ] Is the budget account for running cost settled? Has the business owner accepted that account in writing? After the handoff (Chapter 22), whose budget does this money come from?
- [ ] Is the cost booking standard settled (chargeback / showback / not booked)? Without a standard, calls only ever mix into one department total, and what this system spent cannot be split out.
- [ ] Is the cross-department first-line owner settled for each of the four ledgers? The test is whose budget or whose daily actions a breach hits directly. Everyone else related is written in as a countersignature.
- [ ] Is the reconciliation cadence set (who, which day of the week, which page)?

---

## 16.2 Running Budget Sheet (Four-Ledger Template)

One page, posted where the owner can see it. Set the alert line ahead of the budget line (at 80%, say), and write the action on breach hard in advance, rather than inventing it in front of the bill.

| Ledger | Metric | Budget Line | Alert Line | Current Value | Action on Breach | Ledger Owner |
|------|------|--------|--------|--------|----------|-----------|
| Cost | Cost per claim | | 80% of the budget line | | Cost review the same day | |
| Cost | Monthly call total | | 80% of the budget line | | Cost review the same day | |
| Latency | P95 on the core operation | | | | Degrade / extend precomputation | |
| Latency | P95 in the peak window | | | | Same as above, peak on its own line | |
| Error | unsafe class | 0 | Highest level on the first one | | kill criteria (Template 14) | |
| Error | concern class | Carry over the Template 11.1.4 threshold table (e.g., ≤10%) | | | Rework retrospective | |
| Error | useless class | Carry over the Template 11.1.4 threshold table (e.g., ≤20% with the trend not rising) | | | Rules and prompt retrospective | |
| Degradation | Drill status of each dependency point | Passed, and no more than 90 days ago | | | No change allowed until the drill is made up | |

**Anchor & Helm example rows (the pilot week 4 version, numbers stated relatively, your sheet needs absolute numbers)**:

| Ledger | Metric | Budget Line | Current Value | Ledger Owner |
|------|------|--------|--------|-----------|
| Cost | Cost per claim | ≤ the post-repair level × 1.5 (post-repair = 1/6 of what it was before it ran away) | Inside the budget line | The claims-ops IT engineer (the instrument) → follows the budget account to Kevin Doyle after the handoff |
| Cost | Monthly call total | The estimate line from the pilot approval | Back inside the line | Same as above |
| Latency | Morning peak queue refresh P95 | ≤3 seconds | Met | The claims-ops IT engineer |
| Error | The three category thresholds | The Chapter 11 threshold table as is | Spot checks met | Linda Marsh's team (spot checks) + you (booking) → the maintaining side after the handoff |
| Degradation | Two points, extraction and long-tail priority | Drilled (Friday of pilot week 3) | Passed | The claims-ops IT engineer |

**Rules**:

- [ ] Not one row of the error ledger is newly invented. It and Template 11.1.4 reference each other, and changing that side means changing this side.
- [ ] "Current value" is updated at each weekly reconciliation. Two consecutive weeks blank means the minimum observability set has a hole.
- [ ] The owner column takes a person's name, not a department's. At the handoff (Chapter 22) rename it row by row. This sheet is the working ledger of the operating handoff.

---

## 16.3 Degradation Path Register

One row per AI dependency point. A fallback has to be able to run the core process. "System under maintenance, please try again later" is not a fallback.

| AI Dependency Point | Failure Shape (Down / Slow / Expensive) | Fallback | What the User Sees | Trigger and How | Date Last Drilled | Owner |
|-----------|--------------------------|------|--------------|----------------|--------------|-------|
| e.g., missing document extraction | Down / slow | Pause extraction, rules rank as usual | The missing documents column grays out to "extraction paused, open the claim to read the original email" | Failure rate or latency breaches the line, switched automatically | | |
| e.g., long-tail priority suggestion | Down / slow / expensive | Everything goes through the rules layer, the reason column still says which rules matched | Long-tail claims marked "ranked by rules only" | Same as above. On a cost breach, route to the smaller model first, then degrade fully | | |

**Rules**:

- [ ] "Expensive" is a failure shape too. Write the degradation action for a cost breach (route to a smaller model, lower the sampling frequency, narrow the scope) in advance.
- [ ] The three elements of a drill, really cut the dependency, production data, real users present. Ask users afterward "did you notice." The best degradation is the one users did not notice.
- [ ] Every dependency point is drilled at least once every 90 days, and a change to a dependency point (a model swap, a change to the call path) makes a rerun mandatory.
- [ ] Chapter 10's line is honored on this sheet. Do not delete the dumbest thing that works. It is your degradation path. The rules layer needs an owner, tests, and updates as business rules change, or the fallback itself has already collapsed.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/production-readiness/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/production-readiness/): the cost per claim instrument script, the drift alert rule sample, and the trace field scaffold
