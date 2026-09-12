# From a verbal "continue" to a signed page: the deployment charter

**Load this reference when:** the sponsor said "continue" and nothing is written; "we get along well, the paperwork would only put distance between us"; there are no signatures; an activity is written as the goal; three people describe three different projects (L0 → L1 authorization).

Source: chapter 4 (`docs/chapters/ch04-charter.md`); template 4 §4.1–4.2, 4.7 (`docs/appendices/template-04-deployment-charter.md`); `repo/templates/deployment-charter/charter.md`.

## Contents

Decisions: the definition · seven elements · four signatures · order and the three internal additions · resource reassessment and exit · charter vs approval form · change rule. Procedures: call the meeting · the 60 minutes · the sponsor's bigger number · a refused commitment · after the meeting. Detectors. Key judgments. Templates. Vendor seat.

## Decisions

**Write the charter when authorization is vague, because vague authorization is more dangerous than none.** A project with no authorization never starts and hurts nobody. "Continue", "get started", "I support this direction" hands every party the permission it wanted, each spends real money on a contradictory expectation, and sunk cost hardens the gap into a standoff. The charter's use is to make the expectation gap blow up at the cheapest moment.

**Definition: a one-page working agreement signed by both sides, setting out one measurable North Star outcome, named users and owners, boundaries and data, what each side puts in, and two-way exit conditions.** Three words carry the weight. One page: past one page nobody remembers it, so it constrains nobody. Signed by both sides: produced live in the contracting meeting; a document you wrote and carried over for a signature does not count. Exit conditions: they matter as much as the goal.

**Seven elements; none may be blank. The cell you leave blank is the cell that blows up ten weeks later.**

| # | Element | Standard in one sentence | What happens if blank |
|---|---|---|---|
| 1 | North Star outcome metric | One, measurable, an outcome and not an activity; with baseline, target and settlement point (when measured, over what window, who produces the number) | The project proves itself with activity metrics and the board does not buy it |
| 2 | actual user and owner, by name | The person who uses it and the person who owns it after launch, names not departments; the owner is not you | The day the system launches is the day an orphan is born |
| 3 | Scope and red lines | What gets built, what explicitly does not ("not this phase", by name), what is not touched at all | Scope swells at every meeting and red lines get stepped on in the excitement |
| 4 | Data boundary and access commitments | Which data, in what form, approved by whom (a name), delivered when (a date); de-identification standard and who sets it; the security review date | The death email, "it is going through the process" |
| 5 | Business-side commitment | People × time, by name, written into their calendar and not their wishes; second row, your team's commitment and protection conditions, by name, countersigned by your manager, stating whose weekly must clear it before anyone is pulled | A one-way delivery promise, the handoff certain to fail; your schedule pulled out from under you tomorrow |
| 6 | Acceptance method | Written as launch release conditions tied to the eval, golden cases plus thresholds; releasers are the business-side owner plus the risk owner, not you; sign the mechanism now, fill in the numbers later | Acceptance turns into "does the boss think it is fine" |
| 7 | Exit conditions | Two-way, which signal lets which side call a stop; three parties may trigger reassessment | Once the project is a zombie, nobody has the authority to shoot it |

**Four signatures: the sponsor, the business owner, you, your manager.** Drop the last one and your schedule can be pulled out from under you tomorrow. What your manager signs is not what gets built; it is that these people, for these weeks, belong to this project first. Walk him through the role charter and your team's commitment row before the meeting; he signs fourth.

**Sign the charter after the Field MVP evidence, not before.** Contracting used to happen before any work, vision against vision, so agreements filled with "improve efficiency". Ten scored cases in two hours turn it into evidence against evidence: how big a target rests on how the waiting time breaks down across the cases; whether the front line puts hours in rests on the unsafe rows. Two clauses are new for a probabilistic system: the data boundary (an AI system has to eat the business side's data, so which data, de-identified how, in whose environment, approved by whom, delivered when is a clause, not logistics) and acceptance tied to the eval ("the demo passed" cannot accept an output that differs every run).

**Three inherited ideas hold.** The agreement is a 50/50 conversation about responsibility; a business side that only sets questions during contracting will not co-build later, and inside a company nobody manufactures the moment of forcing co-building for you, so you manufacture it in this meeting. The agreement has fixed elements, none left blank. "What you want" and "what you are willing to put in" are negotiated in the same room; a want that will not discuss what it costs is a wish, not an agreement.

**Three internal additions, all in the names-and-commitments segment.**
- Claiming the owner role needs something in return. "You built it, so you keep it running" is literally true inside a company, so the owner cell is a claim to be made, not a name to fill in. The owner claims it and gets, in return, that after launch the system's priorities and release schedule are his to set. A claim with nothing in return is politeness at signing and a blank at handoff.
- A committed input has no invoice, so substitute the fulfillment rate: hours promised versus hours delivered, one line of numbers, reported monthly (rule) at the sponsor weekly, and whoever came up short is visible in the meeting.
- Your team's commitment goes in with protection conditions, countersigned by your manager: pulling anyone goes through the sponsor's weekly first.

**Three tiers of resource reassessment when the business side's promised data access or staffing goes unmet two weeks running (rule).** Tier one: escalate to the sponsor weekly, where the sponsor decides between more input and less scope. Tier two: the project turns to "awaiting inputs" on the PMO register, with the reason column naming whose input is missing and what it is. Tier three: your team's people are released to other projects, with the release date and reason recorded openly in the weekly project report. None of the three tiers requires you to call a stop; missing inputs are the signal by themselves. Inside a company there is no pause card, salaries are paid either way, so element 7 says what triggers reassessment, never who may pause.

**Primary exit trigger: "When two consecutive evaluation cycles miss the threshold and no workable path to improvement exists, either side may propose termination."** Three parties may raise reassessment: the delivery side (inputs unmet two weeks running → the three tiers), the business side (a key risk event, a compliance change → sponsor weekly decides between cutting scope, going manual, adding input), the sponsor (a higher-priority project, a budget shift → re-place the project in the schedule and reconfirm the cadence). Written for the business side only it is a disclaimer; for the delivery side only, a one-sided contract. Exit conditions mean the person who calls a stop does not have to be the villain; without them, whoever says stop first owns the failure, so nobody says it.

**Charter ≠ project approval form; two documents, always.** The approval form governs budget and process compliance; the charter governs the work and the expectations and stays one page forever, in a state where somebody can still mark it up in red pen. If an old ticket carries conflicting acceptance wording (e.g. "Q&A accuracy ≥ 90%" (illustrative)), say so in the meeting, agree how to handle it, and file it through a project approval change review so it is voided and replaced by the eval release mechanism.

**"Sign the mechanism now, fill in the numbers later."** At signing the eval spec usually does not exist. Acceptable: "Release mechanism settled, thresholds per the attachment", naming who co-builds the eval spec and by when. Unacceptable: "Release criteria to be determined" or "to be agreed after launch". Release methods excluded by name: the demo passed, the boss is happy, trial feedback was good.

**Change rule: a change = a renegotiation.** Any side changing any element notifies all signatories, gets confirmation, and the version number goes up by one. A charter changed quietly is worse than no charter.

## Procedures

**Decide whether to call the meeting.**
1. Ask three key roles each to write one sentence on "what success looks like for this project". Three different sentences is all the reason you need.
2. Draft all seven elements yourself; mark the cells you expect to be contested. The cells you cannot fill (usually the business-side commitment and the exit conditions) are the project's largest exposed surface right now.
3. Before the meeting, walk to each party's desk, ask for their version of "continue", and bring only the differences into the room. Pull the original charters of this company's other projects; "the last project wrote it this way too" is a hard argument inside a company.

**Check the preconditions; missing any one, reschedule.** The decision-maker who can settle metrics and commitments on the spot has confirmed attendance. The role charter is aligned with the sponsor. The Field MVP evidence pack is in hand (original scoring results, readout memo, the data breakdown). The charter draft is pre-filled with contested cells marked. Extracts of acceptance and scope wording from any existing approval form or ticket are in hand.

**Run the 60-minute (rule) contracting meeting.**
1. 0–10 min, open with evidence. Retell the MVP scoring results and the readout conclusion; no vision deck. When anyone returns to the vision story, pull them back to the scoring sheet.
2. 10–25 min, the North Star. Metric definition → baseline (with the data risk stated; if the baseline is not clean, write "as set by discovery's reconciliation") → how the target was derived. Answer a disagreement over the target with a breakdown of the data, never with "I think". The hardest 15 minutes.
3. 25–35 min, names and commitments. actual user and owner by name; the business-side commitment settled row by row; get the person or their manager to confirm the hours in the room; the owner claim with its return; your team's row and protection conditions.
4. 35–45 min, scope, red lines, data boundary. The three lists, do / do not / do not touch; excluded requests onto "not this phase" by name; each dataset gets an approver and a date; the security review date goes into the schedule.
5. 45–55 min, acceptance and exit. Sign the acceptance mechanism first, then ride it into the exit conditions; that is the least awkward door. Warn them the silence is coming, then say: "We write these lines so that if it ever comes to that, the person who calls a stop does not have to be the villain."
6. 55–60 min, read back and commit. You read the seven elements aloud; the business side's corrections are the last round. Agree on write-up within 48 hours (rule) and signing within a week (rule).

**Two facilitation rules.** The decision-maker is in the room. You draft, you never finalize alone: every cell must be changed by the business side at least once during the meeting. A business side that leaves no fingerprints on it will never think of it as theirs.

**When the sponsor pushes for a bigger number.** Do not say yes and do not say no. Put the ten-case table on the screen and break the metric down by where the time goes: the portion the system can reach, the portion that is physical time or another system's routing. Show what half of the reachable portion yields. State what the bigger number would cost: a red line already agreed, or another project with another budget. Add the business framing (which story the smaller number tells at the board and holds) and the risk framing (the baseline is unverified; promising the bigger number signs a number on a foundation nobody has checked). Offer to come back after reconciliation and say whether the number was conservative or reckless.

**When the business side refuses the commitment row ("give you two new hires instead").** Go back to the scoring sheet, not to whose job it is. The unsafe rows came from the named team, the rule changes came from their annotations, new hires would not have caught them; without the hours the system learns the wrong priorities and the review time wasted after launch runs past the hours asked. Take their conditions into the charter (capped hours, booked in advance, not during peak). If you cannot agree, you do not sign.

**Within 48 hours (rule) of the meeting.** Write it up with every "changed in the meeting" spot marked so the business side sees its own fingerprints. Collect the edits; every edit is a cheap expectation gap blowing up, so welcome it. Sign within a week (rule). Draft the pre-mortem the same night; its causes of death are the raw material for element 7.

## Detectors

- If the charter has been filled into the ticket system's 27 fields (illustrative) and "the front-line team, 2 hours a week, not during the morning peak" became "business department cooperation, high", then it has been processed into a form; a signed form constrains nobody.
- If the North Star reads "complete development of the system and run the launch training", then it is an activity list. Read it aloud and ask, could this sentence fail to come true? A goal that cannot fail is not a goal.
- If the business-side commitment cell reads "will provide necessary support", then the charter is a one-sided love letter; the raw material (data, tacit knowledge, trial feedback) sits with them and an organization that never put anything in cannot take over operating it.
- If you hear "we get along well, all this red tape would only put distance between us", then the causation is backwards: a good relationship is the only window in which the unpleasant things can be said plainly. Agreements do not spend relationship capital; vagueness does.
- If the North Star cell reads "complete the launch and train everyone; also improve reviewer satisfaction", then it cannot fail and it smuggles in a second North Star; demote the second to an observation metric.
- If actual user reads "the relevant colleagues" and owner reads "the delivery team (holding it during the transition)", then there is no name and the handoff failure is written into the charter on day one.
- If "not this phase" is blank ("no requests currently need excluding"), then every request ever turned down can revive at the next meeting.
- If the data row reads "IT will give strong support and open the relevant access as soon as possible", then there is no approver and no date; that is the death email nobody answers.
- If the commitment row reads "the business department strongly supports this and agreed verbally at its weekly", then there is no name, no hours, nothing in anyone's calendar.
- If release reads "criteria to be agreed between the two sides after launch", then it is the wording declared unacceptable; the acceptable form is "release mechanism signed, thresholds to follow in the eval spec attachment".
- If exit reads "if the business side is not satisfied, it may terminate at any time", then it is one-way with no trigger, a disclaimer, not a mechanism.
- If the charter was carried over for a signature after the meeting rather than changed in it, then it was not signed by both sides in the sense that counts.

## Key judgments

- "Vague authorization is more dangerous than none."
- "A charter's use is to make the expectation gap blow up at the cheapest moment."
- "A charter with no business-side commitment in it is a one-sided love letter."
- "Exit conditions mean the person who calls a stop does not have to be the villain."
- "A goal that cannot fail is not a goal."
- "Agreements do not spend relationship capital. Vagueness does."
- "The awkwardness of writing exit conditions lasts thirty seconds. The cost of not writing them is counted in quarters."

## Templates

- `templates/deployment-charter.md`: the seven-element one-pager with the four signatures and the 60-minute agenda.
- `templates/pre-mortem.md`: drafted the night before signing; feeds element 7.
- `docs/appendices/template-02-role-charter.md`: aligned with the sponsor before the meeting; a precondition.

## Vendor seat

The four signatures become three (client decision-maker, client owner, you) with the commercial contract signed separately; the three tiers of resource reassessment become an exit clause ("if the client's committed input goes unmet two weeks running, we may propose a pause"); launch release conditions become acceptance clauses tied to the eval. Charter and contract must be two documents, and a line in a contract is not a working mechanism.
