# Handoff plan

Source: `docs/appendices/template-22-handoff.md` §22.1, §22.2, §22.3, §22.4 (and `repo/templates/handoff/checklist.yaml`; the repo wins on conflict). Fill the header and the owner sheets when the handoff starts; until the owners are named the two sheets after them have no subject. Run the tests sheet in stage three. The response window terms go into the responsibility transfer agreement.

| Item | Fill in |
|---|---|
| Project / system | <system name> REQUIRED |
| Handoff start date / target exit date | <date> / <date>, the exit date is the week all five tests pass, not a calendar pick |
| Response window (length and scope) | 3 months (rule); only P1 incidents and exceptions the escalation tree did not catch. REQUIRED |
| Signatures (four owners + the delivering team's lead) | <owner name> × 4, <your lead's name> REQUIRED |
| Transfer ledger entry number (PMO AI system transfer ledger) | <entry number>; no ledger → this sheet starts its first line, blanks flagged red |

**Owner placement sheet.** One real name per row.

| Role | Responsibility | Real name |
|---|---|---|
| System owner | Budget and priorities, the running budget, request scheduling, first signature on whether to stop | <owner name> REQUIRED |
| Maintenance owner | Code and production, gatekeeping rights over every module, releases, first-line incident response | <owner name> REQUIRED |
| Eval guardian | Approving new golden cases, the weekly review, annotation guide version control | <owner name> REQUIRED |
| AI dependency owner | Model and platform changes; evaluates and signs off on provider model version upgrades, dependency changes, platform migrations | <owner name> REQUIRED |

**Three AI handoff items.** Absent from every traditional IT handoff; no blank rows.

| Item | Question to answer | Receiver type (business / ops / platform) | Real name |
|---|---|---|---|
| Continuous eval updating | Who adds golden cases, who approves them, who guards the per-category thresholds | <type> | <owner name> REQUIRED |
| Re-verification on model and dependency changes | On a model version switch or dependency upgrade, who runs the golden cases replay, who signs "safe to switch" | <type> | <owner name> REQUIRED |
| Decision trail review | Who chairs the override review, who analyzes the reason code distribution, who runs the quarterly fairness spot check | <type> | <owner name> REQUIRED |

**Five self-sufficiency tests.** Test method is Show Me; status pending / failed / passed; a failed row carries a rework action and a retest date.

| Capability | Show Me scenario | Pass standard | Rework action on failure | Status / retest date |
|---|---|---|---|---|
| Run | Cut one AI dependency point without warning | The business side degrades, notifies by the template, recovers on its own, no instruction from the deliverer | Rerun the degradation drill, add an incident notice drill | <status> / <date> |
| Configure | One real configuration change (list / threshold / rule parameter) | The full change, test, release cycle runs on the business side's gatekeeping rights; the change passes the eval replay | Walk it again as a pair, check configuration item permissions and documents | <status> / <date> |
| Exceptions | Inject a class of situation the system has never seen | The first reaction is the escalation path, not the deliverer; the ruling settles into the golden cases or a rule | Draw the escalation tree together + two injection drills, then retest | <status> / <date> |
| Evolve | One small request end to end + one model version upgrade | Scheduling to rotating release with no commit from the deliverer; the upgrade passes the golden cases replay and gets both signatures | Back to co-build pairing, shrink the request and retest | <status> / <date> |
| Teach | The business side onboards one newcomer | The newcomer handles the queue independently within two weeks (rule); the training material is maintained by the business side | Have the newcomer recount where they got stuck; fix the mentoring path, not the manual | <status> / <date> |

**Response window terms** (into the responsibility transfer agreement): length 3 months (rule); scope, only P1 incidents (an unsafe reaching human eyes) and exceptions the escalation tree ran to the end and did not catch, daily ops and routine requests are outside the window and taking one means falling back to stage three; log every help request inside the window and review once before closing, which capability each pointed to and whether to add one targeted drill; on expiry, write access drops to read-only, removal from the oncall rotation and the retrospective's standing attendee list; closing needs written confirmation from the business owner and the ops owner.

Machine-readable keys in `checklist.yaml`: `system_owner`, `maintenance_owner`, `eval_guardian`, `ai_dependency_owner`, `ai_eval_update`, `ai_model_revalidation`, `ai_trace_review`, `cap_<run|config|exception|evolve|teach>_status` with `_rework` and `_retest` on a failed one, `window_end`, `window_scope`; an empty name raises an alert.

**Rules**
- One person may hold several rows, but each row holds only one name. "The team is responsible" means nobody is responsible.
- The vocabulary of a traditional IT handoff does not have these three. They are the easiest to miss and the most fatal. Name an owner for each, no blank rows allowed.
- The test method is always Show Me, you are in the room and do not step in; inject the scenario into the real system wherever possible; any failure sends the item back for rework, and what gets added is a drill, not a document; only when all five pass does stage four of the cadence sheet begin.
- Daily ops and routine requests are outside the window. Taking one means falling back to stage three.
- No confirmation means extension by default, and extension by default means permanent ops.

**What a wrong filling looks like**
- The deliverables list is all nouns (manual, accounts, code, recordings) and not one verb (can respond, can judge, can evolve). Documents are the shadow of capability, and a shadow cannot hold the system up.
- "Maintenance owner: the business line engineering team" breaks the placement sheet's first rule. Team responsible equals nobody responsible.
- "Eval guardian: to be decided by the business side after handoff" is a blank row on the three AI items sheet. Nobody approves golden cases, and the eval starts rotting from handoff day.
- "Five self-sufficiency tests: covered by documentation, training, and Q&A, deemed passed" swaps out the test method. Having heard the lesson and being able to catch it are two different things.
- "We are right here in the company, come find us anytime" looks considerate and is in fact never exiting. State a length, a scope, and written confirmation of closing; missing any one is extension by default.

Filled in → goes to: the PMO's AI system transfer ledger (one line per live system, five capabilities × owner, blanks red, walked through at the quarterly business review) and the one-page responsibility transfer agreement signed at stage four; then closeout, `references/closeout-and-platform.md`.
