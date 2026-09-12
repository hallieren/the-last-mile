# Bringing the reviewer into the design before the security review

**Load this reference when:** a security, compliance or privacy review is two weeks out and the reviewer has not seen the design, someone says "it's just an internal tool," or "there's human review anyway" is standing where an oversight design should be.

Source: chapter 12 (`docs/chapters/ch12-trust-constraints.md`); template 12 (`docs/appendices/template-12-trust-matrix.md`).

## Contents

Decisions (timing, the matrix, the three columns, anti-formality checks, the three oversight questions, the six trail fields, prompt injection, the maintainability row, blank rows, cost, the extra week, joint authorship, the baseline) · Procedures (front-loading in three steps; the reviewer's three questions as parameters; the review packet) · Detectors · Key judgments · Templates · Vendor seat

## Decisions

**Constraints enter as design inputs in week two of the opening, never as a launch gate.** The root cause of review blocking a project is when the information reaches the reviewer, not the reviewer. He sees the design last and is held responsible first, so saying no is his rational choice. Treat constraints as a gate and review has two values, pass or fail, and fail is safer for him. Treat them as design inputs and each becomes a parameter with a cost that can be traded. The earlier they come in, the larger the design space.

**Fill the trust constraint matrix, six rows × three columns, from week two through the review.**

| Row | The question it answers | Anti-formality check |
|---|---|---|
| Privacy | Whose information, and what information, moves inside which boundaries? | Spot-check whether de-identified data can re-identify a person; whether the right side of the line really has no plaintext |
| Security | Who can access what, and change what? Where is the attack surface? | Whether the new system's permissions exceed what the same person has in the source system |
| Audit | When something goes wrong, can you reconstruct who did what, when, and on what basis? | Take one historical suggestion and actually rehearse a trace |
| Human oversight | At which step is a person present, and in what way is that presence real? | Daily volume × review time per row, do the division in front of the reviewer |
| Fairness | Will the system systematically treat one class of subject worse? | It counts as a mechanism only if you can say "what data would reveal unfair treatment." Writing "no discrimination" does not count |
| Maintainability | After you are reassigned, leave, or the system enters its third year with nobody watching, who can safely change it? | Have the future maintainer try one change. It counts when the change goes through |

| Column | Discipline | Does not count | Counts |
|---|---|---|---|
| The specific requirement for this project | From the constraint interview, not from your imagination | "Complies with the company data security standard" | "Customer-identifiable information may not leave the claims domain" |
| How the design satisfies it | A mechanism, not a promise, and the cost on the last line of every cell, who spends how much extra time, what information or capability is given up | "We will be careful about de-identification" | "Name, ID number and plate are replaced with placeholders at the extraction layer, no plaintext at any later step. Cost, same-name customers across cases checked by hand, about 1 extra minute per case (illustrative)" |
| Who signs off | A real name. The day it goes on he stops being the judge and becomes a co-author, and what he defends at the review is a design he took part in | A department, a title | One person per row; blank = no owner yet, an open question |

**Run the three oversight questions on every human step.** Is there time to look? The ability to judge? The authority to stop it? Miss one and oversight is nominal. Nominal oversight is more dangerous than none, it manufactures the illusion that somebody is watching the gate, and every other defense slackens with it. The design that answers them: risk ranking with a daily volume cap worked back from the review time budget (time); every suggestion carries its reason (ability); the Human Call column names a person and without it the system produces no action (authority). Any one unanswered → change the design this week, cap the volume, add the reason, or give a real authority to stop it.

**Carry the six decision trail fields end to end, not one missing.** Input snapshot, rule and model version, suggestion, reason, Human Call, timestamp. AI output is written back to no source field; derived views are purely read-only. This is the audit commitment (who decided what); the engineering trace (why the suggestion looks this way) is a separate reading of the same chain.

**Treat prompt injection as a design parameter, not an open question.** Externally writable content (email, attachments) is untrusted input, always, handled as data and never as instructions. The extraction layer recognizes only a schema whitelist, anything outside the fixed fields is rejected, and the result contains no free instruction text. With the system stopped at the advise layer and no action without the Human Call, the blast radius is held by design inside "one suggestion waiting for human review."

**Never self-sign the maintainability row.** The signer may not come from this project's delivery team. If the future maintainer is you, the cell is you signing for yourself, the device fails on this row, and what you signed is an ops commitment with no end date. Sign it from the business line's IT or ops, or leave it blank as an open question. Blank is more honest than self-signed, a blank gets asked about at the review and a self-signature does not. A spot check a year later asks who is responsible now, so the blank cannot stay blank forever.

**Keep blank rows on the table as open questions.** Never delete them. It is the blank row you hid that blows up at the review; an open question you list yourself is a deposit into credibility.

**Write the cost of every mechanism, or constraints accumulate one way.** Whoever proposes a constraint does not bear the cost of using it; one more requirement costs the reviewer nothing and lands on the front line's time. The cost line lets each constraint trade like any design parameter. Over-compliance and no compliance die different deaths on the same date.

**Defend the extra week of engineering (about one week, illustrative, for de-identification, the audit log, permission inheritance) by changing whose request it is.** Not by arguing technical necessity. The day those items entered column two they stopped being your preference and became the risk owner's written requirements. Whoever wants to cut that week is cutting his requirements and needs his nod.

**Build joint authorship, not an approver's signature.** The review conclusion memo goes out from you and the risk owner jointly, recipients see two senders. The design document's author line carries two names side by side. He presents the constraints section at the meeting, not you. An approver's signature is a process action, and after signing he is still the judge. Joint authorship is a change of identity, and after signing he defends his own design.

**Save the packet as a shared "AI system constraint baseline."** The second project's interview starts from "which rows are different this time," and a 60-minute interview becomes a corridor confirmation. After every audit, inspection or spot check, add the newly asked questions to column one and answer one fewer next time. The matrix is a permanent ledger for as long as the system lives.

## Procedures

**Front-load the review, three steps.**
1. Week 2 of the opening (rule), the constraint interview, 60 minutes (rule), with the risk owner named in the stakeholder map. Bring questions, not a design; there is no design yet, which is why everything can still be changed. Three must-asks: What has gone wrong with systems like this before? What are you afraid of? What evidence do you want to see when it comes to the review? These are not the three he asks you at the review, and not the three oversight questions. Internal variant, go in with a hypothesis: name the incident you remember, let him correct the details, then ask "which one is there that I do not know about." Output, a first draft of column one plus an open questions list.
2. Carry the matrix through the whole design. Run every major decision past column two, which row does this make easier to satisfy, which harder. Fill the rows as the design lands: fairness from the error taxonomy (no identity attribute in the ranking logic, override distribution spot-checked by customer segment each quarter); maintainability from the co-build (rules, de-identification config and thresholds as configuration items, changes through the existing release process, a model upgrade runs the regression eval).
3. Run the review as a confirmation meeting. Send the packet a week ahead (rule), organized around the answers he wants. Confirm the matrix row by row; rule only on open questions. Whole agenda items get skipped on one sentence when the row is signed ("purely derived, purely read-only, no write-back").

**Translate the reviewer's three review questions into design parameters.**
1. "Does customer data leave the boundary?" → de-identification at the extraction layer; the boundary is one solid line on the data flow diagram, plaintext to the left, none to the right; minimum-fields principle.
2. "Who audits the model's output?" → the six trail fields, every suggestion; no write-back to the source.
3. "Who is responsible when it is wrong?" → queue permissions inherit the source system's roles, no separate account system; the final action on every suggestion lands on a named person in the Human Call.

**Assemble the review packet, §0–§9. The packet writes nothing new.** Every section rearranges material already in the matrix and the design documents. A section you cannot write means the design has a hole; fix it at the design layer, not the document layer.

| § | Section | Must contain |
|---|---|---|
| 0 | Cover | The system in one sentence at workflow-claim level; the review scope, including what is explicitly not under review; a two-line byline, solution design (you) / constraint design (the risk owner and every column-three signer); the maintainability-signer rule; the nature of the meeting, confirmation (every row signed) or ruling (open questions listed) |
| 1 | Answers-first page | The reviewer's top questions × a one-line answer × the section with the detail; his third interview answer decides this page |
| 2 | Data flow diagram | The de-identification boundary as one solid line; the read-only / writable attribute of every arrow; external call points; where data does not flow, drawn explicitly |
| 3 | Permission model | Role / what they can do in the queue / inherits from (source system role) / exceptions and why; the new system enlarges nobody's existing permissions |
| 4 | Trail notes | Audit log schema (the six fields plus suggestion ID and decider), retention, query permissions, spot-check cadence; the declaration that AI output is written back to no source field |
| 5 | De-identification boundary | Field / treatment / where it happens / reason for keeping; a re-identification test on N records with the result |
| 6 | Human oversight design | One line each, question × mechanism × evidence (the division, a sample of the reason column, a demonstration of the stop path) |
| 7 | Rollback path | Trigger / action and duration / which old process runs after / owner / rehearsal record, one real rehearsal before launch |
| 8 | Open questions | Unsettled item × suggested handling × what this meeting has to rule on; never hidden |
| 9 | Attachments | The full matrix plus the signature page |

**The review is less than two weeks from launch and the reviewer has not seen the design** → put the constraint interview into this week's calendar today.

## Detectors

- If the reviewer's name first appears on the schedule rather than on a design meeting's sign-in sheet, you are already in compliance-as-the-last-gate.
- If you are in the middle of explaining to yourself why this system does not need to go through review ("internal helper script," "pilot tool"), you are already inside the "our own tool" escape. It is the failure an internal team commits most, because no door physically stops you. One escape and the cell turns red permanently, and you work with him for years.
- If "there is human review anyway" has not been divided, write the daily volume and the review time budget on the same line and divide, in front of the reviewer; 500 rows a day at three seconds each (illustrative) is a box ticked, and on the day it goes wrong the reviewer takes the whole fall and the front line stops signing the Human Call.
- If column two has no cost line, constraints are accumulating in one direction; the pilot data will be dismal and the project dies of "no value" on the same date it would have died of "risk."
- If the fairness row says "no discrimination" and cannot name what data would reveal unfair treatment, it is not a mechanism.
- If the maintainability signer is on your delivery team, the row is an ops commitment with no end date; blank it and list it as an open question.
- If the reviewer answers a compliance question in your place using column-two sentences, the row is his; if he looks at you, it is still yours.

## Key judgments

- "The reviewer sees the design last and is held responsible first. Saying no is his rational choice."
- "The earlier constraints come in, the larger the design space. The later they come in, the less is left but 'pass or fail.'"
- "Is there time to look? The ability to judge? The authority to stop it?"
- "Nominal oversight is more dangerous than none."
- "Teaching the reviewer to review you is the highest form of being trusted."
- "Over-compliance and no compliance die different deaths on the same date."
- "Blank is more honest than self-signed."

## Templates

- Constraint interview, matrix, filling guide, review packet: `docs/appendices/template-12-trust-matrix.md` §12.1–12.2.
- The human review path that feeds the oversight row: `templates/eval-spec.md`.
- The six trail fields as queue columns: `templates/queue-columns-and-trail.md`; `docs/appendices/template-17-action-queue.md`.
- Stakeholder map for the risk owner's name: `docs/appendices/template-05-stakeholder-map.md`.

## Vendor seat

The crosswalk applies this as is; the client's risk owner is still the last to see the design until you book the interview. Your neutral seat ("that is not mine to decide") makes joint authorship cheaper for you than for an insider. A security clause in the contract is one line; the row is filled when the reviewer's name is on it and the mechanism has been rehearsed. A line in a contract is not a working mechanism.
