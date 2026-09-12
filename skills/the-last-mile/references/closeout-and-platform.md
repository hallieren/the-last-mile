# Closing out: what the next project keeps, what crosses to the platform

**Load this reference when:** the project has stepped out of the daily and someone asks "what do we keep"; the next department's ask looks like the last one with the nouns swapped and the schedule was set as starting from zero; the platform team wants your requests or you want theirs; "rewrite it for the next department"; the custom code and a dozen platform judgments are rotting in the business line's repo and in your head.

Source: chapters 23, 24 (`docs/chapters/ch23-pattern-library.md`, `docs/chapters/ch24-field-to-product.md`); templates 23, 24 (`docs/appendices/template-23-pattern-extraction.md`, `docs/appendices/template-24-f2p-memo.md`); `repo/templates/pattern-library/*.md`, `repo/templates/f2p-memo/f2p-memo-template.md`, `repo/templates/asset-recovery/recovery-checklist.md`.

## Contents

Decisions: definitions · the flywheel and where it breaks · four asset classes · three admission criteria and two internal rules · agents as the fifth carrier · carried over vs reset to zero · the register and its upkeep · the f2p memo and the three filters · four classes × three exits · recovery triggers · the platform's field day · dual-track cells · the quarterly line. Procedures: capture at closeout · asset recovery · send a memo · start the next project from the shelf. Detectors. Key judgments. Templates. Vendor seat.

## Decisions

**Use the three words exactly.** A pattern is a reusable practice that still holds once the field context is stripped off a specific project. The pattern library is an organization-level store that accumulates patterns under one admission standard. A playbook is a full set of patterns for one class of project, from discovery through handoff. What is reusable is the judgment structure (find the private source of truth → three-way reconciliation → action queue → decision trail → adoption mechanisms), not the code; code moved to another line dies on the field names on day one.

**Turn the flywheel, and name an owner at every step.** Deploy → capture (the closeout retrospective produces candidate patterns) → generalize (strip the field context, write where it applies and where it does not) → reuse (field-test it on the next project) → feed back and revise → deploy. It breaks at two points: capture has no owner (the retrospective ends and everyone leaves) and reuse has no feedback (it works badly, nobody fixes it, the asset stays at 1.0 forever). Inside a company it breaks at a third: the capture moment never arrives, because there is no closeout event. Manufacture it, hung on one of two hooks: the first week after the responsibility transfer agreement is signed, or a retrospective a fixed number of weeks after launch written into the project approval resolution so the meeting happens when the date comes due.

**Sort every asset into one of four classes; the reuse profile differs and mixing them makes the library unusable.**

| Class | What it holds | Reuse profile |
|---|---|---|
| Template | Documents and process (the charter template, the three-layer probing script, the four adoption mechanisms) | Easiest, usable across industries as is |
| Component | Code and schema (the queue skeleton, the decision trail schema, the extraction pipeline interface) | Medium, needs adapting to the data source |
| Judgment rule | Transferable judgments ("chase priority ≠ risk priority", "if you cannot say it, do not merge it") | Carried away in one sentence, with the boundary attached |
| Metric model | The structure of a metric definition (the three tiers of the metric tree, the error severity vocabulary) | Swap the North Star, keep the structure |

**Admit on three criteria, all three or it stays off the shelf.** (1) At least one field validation: running in a demo does not count, surviving on the business side's floor counts. (2) A written boundary: where it does not apply is worth more than where it does. (3) A named owner: an asset with no owner rots in six months (rule), and the danger of rot is that the asset keeps being cited after it stops working.

**Apply the two internal rules.** The owner column often needs a real name from another team and you have no authority to hand another team an owner role; two routes only, a shared manager settles it in one meeting, or push the library into a carrier that already exists (the company knowledge base, the platform team's component repo, the architecture review checklist) so an existing owner picks it up. And declare the force level on the front page, reference / recommended / mandatory; declare nothing and it is taken as mandatory by default, and every awkward use is on you.

**Treat agents as the fifth carrier, not a fifth class.** An agent carrying the queue skeleton, the trail schema and the reconciliation checklist is the executable form of the four classes (a reconciliation checklist grows into a reconciliation agent). Two rules do not move: the three admission criteria still apply and field provenance is waived for nothing; what an agent produces is always a draft, and the standard and the boundary are ruled on by a person. AI may draft, structure, rewrite the language and fill in formatting; AI may never supply "field provenance" or "validation record", those two fields are filled only by someone who was on site.

**Before the next project, split what carries over as is from what resets to zero.** Tacit knowledge does not transfer; the method for mining it transfers.

| Class | Carried over as is | Reset to zero |
|---|---|---|
| Template | The three-way reconciliation method, the four adoption mechanisms, the three-layer probing method | What goes into them; the super-user is picked again for the new field |
| Component | The queue skeleton, nouns swapped, not one column missing | Fields and data sources; moved over, they die on the field names on day one |
| Judgment rule | Sentences that hold across scenarios, boundary attached | The rules of thumb; the new field's combined feel overlaps the old list by not a word |
| Metric model | The metric tree structure, the error severity vocabulary | The golden cases; not one carries over |

**Keep the register to nine columns and its upkeep rules.** Class / name / one-line description / source project / validation count / owner / last updated / status (active, pending-reverify, retired) / force level. Validation count 1 is marked "awaiting a second field test" and down-weighted when a coding agent packs it. Every owner sweeps his assets once a quarter (rule); anything not updated in over six months (rule) is automatically demoted to pending-reverify. Retirement is not deletion; a retired entry keeps its text and states why, a dead pattern is teaching material too. The reuser does not have to be you; a third party's reuse counts as validation and is the highest-grade kind. Log the weeks saved on every reuse; the four weeks (illustrative) the second project saves land on capacity, an account only you keep, and that column is the number you write at the annual review.

**Write the f2p memo in four sections, one page, and send only if it clears three filters.** Obeys the one-page rules (lead with the conclusion, an ask at the end, delivered 48 hours (rule) before the meeting); only the reader changes, from a business executive to the platform lead.

| Section | Question | Rule |
|---|---|---|
| Phenomenon | Which field, at what frequency, on what evidence | Quote the actual words and the decision trail data, not impressions |
| The generalization case | Which other departments or scenes will hit this, and what n is | Write backward from the side with the need, never forward from what you built; n must be verifiable, with the name behind each n and whether the nth implementation needed industry adaptation |
| The product recommendation | What capability you are asking for | A capability, not a feature; rewrite it as "add a [button / page] for [one department]" and if it still holds it is a feature, rewrite it. Features belong to projects, capabilities to the platform |
| The cost of not doing it | What every project pays again, what is lost structurally | The small bill (engineering effort repeated per project) plus the big bill (consistency, aggregation analysis, response speed lost); say the most expensive one out loud |

Then one sentence "willing to give up for it" and "what I need from you" with a date (a scheduling review / 30 minutes (illustrative) in person / a written reply).

| Filter | Rule | Fails when |
|---|---|---|
| Report only at n ≥ 2 (rule) | n = 1 is custom work, n ≥ 2 is a signal; n counts departments | One department, however reasonable; it goes to the candidate register with a trigger condition, promoted the second time it appears |
| Describe the judgment structure, not the interface | "Waiting attributed across steps" crosses; "a Gantt chart" does not. An interface description turns the platform into an outsourcing shop, a structural description gives it design room | The memo names a widget |
| Attach what you are willing to give up | A recommendation with no trade-off is a wish list item. Four cards: your department goes first as pilot; your department retires its own custom implementation and switches to the platform version; your department supplies people to co-build; you file a PR straight into the platform repo and make the proposal a fact on the ground | Not one card produced, which means you want the platform doing your work, not providing a capability |

The candidate register has five fields: signal / source (department, proposer, date) / n / status / trigger or revival condition. A refused memo goes in with the reason for refusal and a revival condition written as an event, not a date. Go through it once a quarter (rule).

**Give every recovered item one of three exits; "leave it for now" is not allowed.** Four classes at the inventory (code, documents, judgment, metrics, the counting-side names for component, template, judgment rule, metric model). Exits: admit to the library (through the admission review, with an owner), send a memo (n ≥ 2 and platform capability level), leave it in the business line repo (business-line-specific, one line on why). The first two are not mutually exclusive; only "leave it" is exclusive, and a refused memo still stays in the library. Test per class: code, does it hold in another industry; documents, the framework transfers, the content does not; judgment, the method for mining it transfers, the rules of thumb do not; metrics, the structure is general, the vocabulary is business-line-specific. Field mapping to the register: class maps one to one; "general? = no" takes the leave-it exit and produces no register row; n = becomes validation count; owner is the same person, claimed at the count, confirmed at admission as knowing and agreeing; source project, last updated and status are filled at admission.

**Hang recovery on one of three triggers, or it never fires.** The fixed retrospective N weeks after launch; the moment before any team member moves posts; the quarterly asset inventory. Structure never declared is the same as structure that does not exist, even in the same git.

**Book the platform decision-maker's field day; you cannot look for him.** Make the on-site visit a standing institution, not a story: a morning behind real users, not a demo day, on a cycle. Any retelling distorts and the negative signals are lost first; "nobody asks the system anything" forms no requirement, and it is exactly what killed a conversational entry point and saved a quarter of development (illustrative). You are responsible for booking it, not for retelling it.

**When a memo is taken up, add three cells to the transfer ledger row.** The maintainer of the old implementation, the retirement condition (the day the platform version clears this project's golden cases), and who makes the call (the system owner). The dual-track period runs a quarter to a year (illustrative); leave any cell blank and you are feeding two systems at once.

**Put the channel into the quarterly report-out.** One fixed line: how many memos went out this quarter, what n each carried, how many the platform took; read by your manager, copied to the platform lead. What gets written into the report-out gets done; everything else is a favor done in passing.

## Procedures

**Capture at closeout (the manufactured moment, the team only).**
1. Ask one question and no other: "what here can the next project still use?" Not "how did it go".
2. Force out at least one entry in each of the four classes, in the business side's own words as they were said, not yet abstracted.
3. Strip the field context in three steps: swap the nouns (exception item → queue item, reviewer → handler, repair shop → outside party); drop the numbers (a result figure belongs in field provenance, not in the judgment); keep the structure, read it to a colleague who never worked the project and stop only when he can repeat back when to use it and when not.
4. Write "does not apply when" for every candidate; the one you cannot write is not admitted, because you do not understand it yet. At least one condition comes from a real failure or serious reasoning, not boilerplate.
5. Run the admission review in the same session, no separate meeting: the library owner plus one peer deliverer who did not work on the project. A pattern an outsider cannot read is a pattern whose stripping is not finished.
6. Run the AI pollution check, any one unanswered and it is refused: which project, which weeks, who was in the room; who can verify it (a proposer who was alone needs an endorsement); is there a failure record or a does-not-apply condition (only upsides = a promotional piece); does it carry an untraceable "industry best practice" line.
7. Register with owner (claimed by name, knowing and agreeing; he can state the next expected reuse scenario) and force level; on reuse, log the weeks saved and feed results back.

**Run asset recovery at the inventory (one of the three triggers).**
1. Put the module list on the screen and ask of every item "will the next project write this again?"; the share that says yes is your rot-in-the-field rate.
2. For every item in the four classes answer three questions: general? what is n? which exit?
3. Close with three checks: every item has a destination; every admitted item has an owner; every n = 1 candidate has its trigger condition written down.
4. Carry admitted items to the register through the field mapping, so two registration systems do not grow apart.

**Send an f2p memo.**
1. Run the three filters; fail any one and it does not go out (n = 1 → candidate register with a trigger).
2. Write the four sections, the give-up line and the dated ask; one page of body text.
3. Deliver 48 hours (rule) before the scheduling meeting.
4. Refused: record the memo with the reason and a revival event in the candidate register, and do not argue. Taken up: fill the three dual-track cells on the transfer ledger.
5. Sweep the register once a quarter; report the quarter's memos, n and uptake on the fixed line.

**Start the next project from the shelf.**
1. Take the carried-over column as is: the reconciliation method, the adoption mechanisms, the probing method, the queue skeleton with nouns swapped, the metric tree structure, the judgment rules with boundaries.
2. Reset to zero and do not skip discovery: golden cases, rules of thumb, fields and data sources, the super-user.
3. Feed one validated component with its boundary and validation record to a coding agent in a sandbox; the gap between its output and ready-to-start is the part of the asset you have not written down yet.
4. Have the apprentice lead the writing from the checklist while you gatekeep; reusable IP × the master-apprentice ladder is where capacity comes from.

## Detectors

- If the library has fewer words on "when this does not apply" than on code comments, what you left behind is a specimen, not an asset.
- Pull three assets at random; if the owner column or the project of the last revision cannot be answered, they are already in the graveyard, and someone burned once by a stale asset never comes back.
- If nothing on your reuse list is ruled "has to be redone", you are forcing a fit, not reusing, and the five gaps get stepped into again on the spot.
- Count the last retrospective's output; ways to die at zero means a victory record, not an asset.
- If the entry count grew faster than the project count, that stretch has no field provenance; trust in a library is indivisible and one fake pattern discredits all two hundred (illustrative).
- A wiki "best practice" untouched for six months with no owner and no field validation is re-claimed or deleted this week.
- Count last quarter's signals forwarded to the platform; none carrying an n and a give-up line means you were forwarding, not reporting, and the recipient will filter by not listening.
- If your platform counterpart's calendar holds no full day behind real users in a year, your shared knowledge of the field is entirely secondhand.
- If "asset recovery" is not an item on the last closeout agenda, recovery never happened; roughly 40% of general structure (illustrative) is rotting in the business line repo.
- A signal that lives only in your head is a bill the organization pays in full on the day you move posts.

## Key judgments

- "What is reusable is the judgment structure, not the code."
- "Tacit knowledge does not transfer. The method for mining it transfers."
- "An asset with no owner rots in six months."
- "The admission standard matters more than the library. A pattern with no field provenance is pollution."
- "Done well, your team is the platform's most expensive radar. Done badly, it is a source of noise on the roadmap."
- "n=1 is custom work. n≥2 is a signal."
- "A negative signal from the field is worth as much as a positive one."
- "A memo that was refused but recorded is still an asset."

## Templates

- Pattern extraction sheet (six fields, three stripping steps), asset register (nine columns), library admission checklist with the AI pollution check: `docs/appendices/template-23-pattern-extraction.md` §23.1–23.3; fillable versions in `repo/templates/pattern-library/` (`pattern-template.md`, `asset-register.md`, `downgrade_stale.py` for the six-month demotion, `packing-example/` for feeding an agent).
- f2p memo with the three-filter self-check and the candidate register: `docs/appendices/template-24-f2p-memo.md` §24.1; `repo/templates/f2p-memo/f2p-memo-template.md`, `candidates.csv`, `override-compare.sql` for cross-department reason code comparison.
- Closeout asset recovery checklist (four classes × three exits, field mapping to the register): `docs/appendices/template-24-f2p-memo.md` §24.2; `repo/templates/asset-recovery/recovery-checklist.md`.
- The dual-track cells go on the transfer ledger row of the handoff plan (main chain, `docs/appendices/template-22-handoff.md`).

## Vendor seat

The capacity ledger is day-rate pricing and margin on the vendor side, and the Group platform team is your own product team; the four weeks saved land on the quote there and on capacity here, and resetting to zero with every client prices the library higher. A line in a contract is not a working mechanism.
