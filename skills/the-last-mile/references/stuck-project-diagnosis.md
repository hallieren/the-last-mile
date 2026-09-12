# Stuck and cannot tell where: gap, rung, missing mechanism

**Load this reference when:** a project is stuck and nobody can say where; "phase one successfully completed" has been written; nobody is accountable for the goal; you are still catching alerts a year after launch; the business side calls you "the AI expert", "here to take our requests", "the implementing party" or "another innovation type"; you are at kickoff and want to write the causes of death before they happen.

Source: chapters 1, 2 (`docs/chapters/ch01-last-mile.md`, `docs/chapters/ch02-inheritance.md`); templates 2, 4 §4.3–4.6 (`docs/appendices/template-02-role-charter.md`, `docs/appendices/template-04-deployment-charter.md`).

## Contents

Decisions: five gaps and the evidence test · grading the evidence · outcome ladder · four invisible mechanisms · three-line triangle · four molds · fit precondition. Procedures: diagnose · pre-mortem · role charter · correct the name. Detectors. Key judgments. Templates. Vendor seat.

## Decisions

**Score the five gaps before touching the technology.** Pushing harder (tune the prompt, raise accuracy, add a permissions module) cannot cross a structural gap. A demo is the five gaps papered over for an audience, so "the demo went well" is no evidence about production.

| Gap | Demo world | Production world | Evidence test (one line, already happened) |
|---|---|---|---|
| Data | Hand-picked clean data | Real systems lag, have holes, disagree on meaning | You checked the real system's fields once and can name which cannot be taken at face value |
| Workflow | Users adapt to the demo | The system embeds in what users already do | You sat beside a user and can say which step the system embeds in |
| Trust | The audience wants to be impressed | Users fear being held responsible | Real users scored outputs one by one, and someone owns the unsafe cases |
| Ownership | You present, you are responsible | After launch there must be an owner | The post-launch owner has a name, and the security reviewer has sat in a meeting |
| Value | "It works well" is enough | Must convert into a reportable business number | A business number was written before the demo, and someone claimed the consequences of it worsening |

**Grade each evidence line on the four grades; a gap with no writable line is a cause-of-death candidate.** Same scale as scoring an output, different object.

| Grade | What the evidence line looks like |
|---|---|
| pass | An event you can write down that already happened |
| concern | Half done, e.g. the fields were checked but the source of truth is not decided |
| useless | Written, not wrong, does not show the gap is closed, e.g. answer accuracy offered as value evidence |
| unsafe | Signs it will blow up at launch, e.g. a security review six weeks out (illustrative); this is your cause-of-death candidate |

**Locate the rung, then read the two rulers together.** The five gaps cut across and ask which are still open now; the ladder runs upward and asks which rung you have reached. Achievement settles only at L3/L4.

| Rung | Name | Reaching it means |
|---|---|---|
| L0 | demo | The demo succeeded, the applause is here |
| L1 | pilot | Real users, real data, in use inside a controlled scope |
| L2 | production | In production, with an owner, monitoring and rollback |
| L3 | adopted | Users' daily actions have changed; taking it away would hurt |
| L4 | self-sufficient | The business side runs, maintains and improves it on its own |

If the project is at L0 and the next planned step is "improve the results", be alarmed: you are running the second leg with the first leg's playbook. Most deaths happen between L2 and L3, where the team disbands and operations are "handed to IT"; launched and unused looks worse than never launched.

**Read the four invisible mechanisms backwards to name the missing one.** A vendor has four things that force out expectations, filtering, decisions and handoff. Inside a company none of the four exists and none of the functions can be dropped.

| Vendor mechanism | What it forces out | Where it hides inside | What rebuilds it |
|---|---|---|---|
| Contract and acceptance clauses | Expectations in writing, acceptance at a fixed moment | The project approval form, an executive's one sentence, the OKR wording your predecessor left | The four charter signatures; launch release conditions (`charter.md`, `eval-as-spec.md`) |
| Price tag and quote | Asks get filtered, "let us wait and see" carries a cost | Attention and schedule; your service carries no price | The five-question elimination; the intake gate and its non-monetary price (`saying-not-now.md`, `closeout-and-platform.md`) |
| Payment milestones and the right to pause | Not deciding has a price, unmet commitments give you leverage | Budget cycles, renewed funding points, the PMO register | The three resource gates; the three tiers of resource reassessment (`stage-changes.md`, `charter.md`) |
| Exit date | Handoff has a deadline | Next year's headcount, your OKRs, the transfer ledger | The three mandatory handoff mechanisms and the responsibility transfer agreement (`launch-adopt-handoff.md`) |

Diagnosis by row: nobody accountable for the goal → row one was never rebuilt. Asks arrive without end and you can push none back → row two. A pilot still "continuously optimizing" in its fourth month → row three. Still catching alerts at midnight a year after launch → row four. The carrier can change (a one-pager at the sponsor's standing meeting instead of a PMO register, quarterly goals agreed in writing instead of OKRs); the source of enforcement cannot go missing. It has to be someone else's budget, someone else's performance review, or an action that fires automatically when the date comes due.

**Draw the three-line triangle, one name per line; a line you cannot name is the project's largest exposed surface right now.** Your manager holds schedule and performance review. The business side gives people and data. The sponsor gives the mandate. If two lines are the same person, you have one line fewer. Your calendar is torn in half: half at the business side's desk, half in your own department's meetings.

**Identify which mold you are being pressed into and correct it on the spot, in one sentence.** How the business side names you is how it will use you. Listen to the words used when they introduce you to someone else.

| What they call you | The expectation behind it | How the project dies | On-the-spot correction |
|---|---|---|---|
| "The AI expert the Group brought in" | Perform something impressive, then step aside | Settles forever at L0 | "A demo is fine, but the people who should be seeing it this week are the front-line team. Their scores are what move the project." |
| "Here to take our requests" | Execute, do not ask why | On-time delivery of the wrong ask, no gap checked | "Every ask must answer a workflow claim." Enforce it from the first ticket |
| "The implementing party" | Launch is the finish line, ops belongs to someone else | Dies between L2 and L3 | "I am accountable through L3. Launch is not my finish line." |
| "Another innovation type" | Ships a mess, gets reassigned | The predecessor's debt lands on your account | Find the last project's real cause of death and say it out loud in front of the front line |

Do not argue, do not escalate it into a principle. Watch the reaction: the reaction itself is stakeholder information.

**Two internal assets, two internal traps.** Assets: depth (you only do the increment of field archaeology) and presence (you can walk to the desk any time). Traps: permanent ops (you cannot leave, so handoff is deferred forever) and ask inflation (your service carries no price, so ideas pour in at triple speed; the intake gate is the first lifeline).

**Check the fit precondition before assigning this investment.** This method belongs to one quadrant only: a complex system needing deep customization, handed to a user organization without the capability to absorb it on its own. A simple configurable product needs only standard tooling. A user organization made of engineers needs only good documentation plus technical support. If what the business side wants is off-the-shelf software, sending you in is a mismatch.

## Procedures

**Diagnose a stuck project.**
1. Write one line of current evidence per gap using the test column above. An intention, a plan, a survey, a demo is not evidence.
2. Grade each line pass / concern / useless / unsafe. Any gap with no writable line, or graded unsafe, is a cause-of-death candidate.
3. Mark the rung on L0–L4 by what has happened (real users on real data = L1; owner, monitoring, rollback = L2; taking it away would hurt = L3; business side runs it alone = L4).
4. Read the four mechanisms table backwards and name the row that was never rebuilt.
5. Draw the three-line triangle; the line without a name is where the project is exposed.
6. Run the 15-minute (rule) pre-mortem below and send it to the sponsor.

**Run a pre-mortem.**
1. Assume the project is dead six months (rule) from now. Work backward to how it died.
2. Write the three (rule, 15-minute version) to five (rule, full pre-mortem at charter signing) most likely causes of death. Each maps to one of the five gaps, carries a defense you can start this week, and names an owner and a start-by date.
3. Make each cause concrete enough to picture the meeting on that day. "Low user adoption" is banned. Check against the reference library: data (the source of truth is one team's private spreadsheet; the status field lags; the join keys are unstable; the data owner will not grant production access); workflow (the user is asked to open an N+1th system; suggestions have no owner; exceptions have no exit; the time saved gets eaten by new review work); trust (one unsafe incident in the first month decides everything; suggestions cannot be questioned because they carry no reason; the front line feels watched instead of helped); ownership (the security or compliance review starts too late; no owner after launch; the system goes dark when you change roles or take leave; the business-line engineers never co-built it; you never step out of the daily); value (the metric is an activity; nobody claims the North Star; success criteria get discussed the week before the demo; ROI can only be expressed as accuracy).
4. Cover at least four of the five gaps (rule). If every cause lands in one gap, you have not seen the others.
5. Send it to the sponsor. Watch who it draws in to talk to you. That person is a stakeholder you had not mapped; put the name on the map and send him what he fears on page one.
6. Review it monthly (rule). Add new ways to die as the pilot finds them. Draft it the night before the charter is signed; its causes of death are the raw material for the charter's exit conditions.

**Write the role charter in week 1 (rule), before the deployment charter.**
1. Write what you are accountable for and to which level: take the ask to a verifiable production outcome, accountable through L3, L4 reached through handoff; full coverage from discovery through design trade-offs, eval, prototype to production, adoption and handoff. If you cannot write "to which level", you have not talked to your sponsor about the definition of the outcome; do that first.
2. Write what you do not promise: not to settle the outcome on "the demo went well"; not to promise a schedule that bypasses security or compliance review; not to force a launch when the data or the eval does not support it; not to touch the project's red line.
3. Write whom you do not replace, one row each, and read it aloud row by row: the POC demo squad (your settlement point is a production outcome; executive showcases stay with the business side), outsourced development (every ask must answer a workflow claim; high-volume bounded feature work can still be outsourced), internal consulting (your advice is delivered as a running system; strategic advisory still needs advisors), ops ticket support (accountable through L3, not for closing tickets; day-to-day tickets stay with ops), the platform team (accountable for one business side's field outcome; the platform roadmap stays with them).
4. Fill the two-sided expectations table. From you: a one-page sync every week, answer first, bad news the moment it appears; every AI suggestion carries a reason, can be challenged and overridden; presence at production incidents; you teach their people to run it; you say stop when it is time; committed input in the charter with the fulfillment rate reported monthly (rule); the handoff arrangement stated well before launch. From them: one sponsor who can make the call, 15 minutes a week (rule); real users' time; de-identified data access and a clear data boundary; security and compliance reviewers on the project team from week 2 (rule); one consistent introduction line; named business-side commitments and schedule protection; ops ownership and on-duty arrangements after launch, by name.
5. Walk your manager through it before the sponsor; he signs fourth on the deployment charter and needs to know first what you are accountable for. Then 15 minutes (rule) with the sponsor, line by line; record every disagreement there, leave nothing to assumed agreement.
6. Give the sponsor one repeatable introduction line: "They are accountable for taking this project from an idea to launched and used, working alongside our people the whole way."
7. Attach it ahead of the charter negotiation. Review it three times (rule): when the charter is signed, before launch, at the ops handoff.

**The inheritance matrix: this method is five older disciplines plus one.** Problem discipline (hypothesis first, facts rule), trade-off thinking (choose under constraints, teach the other side to decide), discovery skill (question discipline, qualification), landing discipline (contracting, resistance as a signal), production responsibility (monitoring, rollback, iterate until someone uses it). The one skill added on top is AI uncertainty management: eval, human oversight, drift. On a cross-department project you own alone, at least one of the five must let you hold your own with an expert; for the rest, know when to ask.

## Detectors

- If the demo got a party, an all-hands email and a roadmap, then you have treated L0 as the midpoint. Move the celebration to the first time a real user depends on it to get work done.
- If "demo feedback was very positive" appears in the requirements document, then you have validated only that the concept can be understood. Audiences consume amazement, users consume reliability.
- If the team disbands at L2 and operations are "handed to IT", then you are in the stretch where most deaths happen. Ask who owns the system next quarter, by name.
- If the report reads "trained the model, connected the data, ran the training sessions, 92% accuracy" (illustrative), then activity metrics have replaced the outcome. Ask: when the North Star gets worse, does anyone hurt? A metric nobody hurts over cannot be the North Star.
- If the archive note reads "phase one successfully completed" and no business number moved, then the project died of comfort. Nobody called a stop because no meeting failed.
- If your output is filling with recommendations, proposals and assessments and you touch production less each week, then you are in the one mold you impose on yourself, internal consulting. Weekly self-check: did one production outcome move up a rung this week because of me? Two weeks running (rule) with no answer, and you are already internal consulting.
- If you took the first ticket without a follow-up question, then your right to discovery is gone.
- If you introduce yourself as "full stack" and last three rounds under an architect's or a consultant's questions, then "full stack" is covering "good at none of it". Self-score the matrix.
- If one line of the triangle has no name, then that line is the project's largest exposed surface.
- If the pre-mortem drew nobody in, then it was not concrete enough to make anyone recognize their own fear on page one.
- If the mechanism that keeps the project honest is your own willpower, then it is not a mechanism.

## Key judgments

- "Enterprise AI projects are rarely shot. They die of comfort."
- "A demo is, by definition, the five gaps papered over for an audience."
- "The deliverer's unit of value is the production outcome, not the demo; achievement is settled only at L3/L4."
- "The three lines are not held by one person. That is the basic shape of internal delivery."
- "Whether that boundary is a company wall or a department wall changes how visible the mechanisms are, not the mechanisms themselves."
- "This method invented nothing. It is a reorganization of old wisdom under new constraints."
- "How the business side names you is how it will use you. Get the name wrong and correct it on the spot."
- "Every column of the matrix has someone stronger than you. At least one column must let you sit across from an expert. The rest, know when to ask for help."

## Templates

- `templates/pre-mortem.md`: the five-cause memo to the sponsor, with owner and start-by per defense.
- `docs/appendices/template-02-role-charter.md`: the one-page role charter (accountable to which level, whom I do not replace, two-sided expectations).
- `docs/appendices/template-04-deployment-charter.md` §4.6: the reference library of common ways to die by gap.

## Vendor seat

On the vendor side the four mechanisms sit on the table in plain view: contract and acceptance clauses, the quote, payment milestones tied to thresholds, the contract end date. Learn the mechanism here, then land it in the document you hold, and remember that a line in a contract is not a working mechanism.
