# 12 · Trust Constraints: Turn Your Reviewers into Designers

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-12-trust-matrix.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** Security, compliance and privacy reviews always block the project at the last minute. The reviewer's first sight of the design is the final gate, and saying "no" is his safest move.
>
> **What You Will Be Able to Do.** Run one constraint interview with the risk owner in week 2 of the opening, fill six classes of trust constraint into the trust constraint matrix, and let the design grow with the constraints attached. Test whether oversight is real or nominal with the three oversight questions. Run the security review as a confirmation meeting.

---

## Week 8, Forty Minutes into the Review

In the room sit Victor Reyes, two colleagues from compliance, and the head of the IT data team. Item five on the agenda is "review of data write-back and change permissions on source systems," usually the most tangled part of the whole review. Victor turns to that page and says, "Skip this one. The merged view is purely derived and purely read-only. It writes back to no source system, and I signed the source of truth decision log." Nobody objects. The meeting was set for two hours. That one sentence saved thirty minutes.

A few minutes later, one of the compliance colleagues asks the question. "When the AI's suggestion is wrong, whose responsibility is it?"

Before you can open your mouth, Victor answers. "Every suggestion stops at being a suggestion. Without confirmation from the named person in the 'Human Call' column, the system produces no action at all. Suggestions carry a trail the whole way, and if something goes wrong the full chain can be pulled up. We settled this design together in week 2."

Now think back to the parallel universe of Chapter 1. The you who went straight to a chatbot met the same risk owner, Victor, at the week 10 security review, and was stopped cold by the same three questions. Does customer data leave the boundary? Who audits the model's output? Who is responsible when it is wrong? The review was scheduled six weeks out, and the project died of comfort. In the real universe, you pulled Victor into the design meetings in week 2. Same man, same three questions, two endings, and the only difference is timing.

Week 8 goes smoothly because it stopped being a review long ago. It is a confirmation meeting. The real review happened inside every design decision from week 2 to week 7. This chapter is about how.

## Why This Is Hard: The Reviewer's Rational Move Is to Say No

An engineer's default model of review is an exam. Cram the material beforehand and bet the reviewer will not ask about the weak spot. That model is wrong because it never looks at where the reviewer sits.

Look at Victor's seat. He is the last person on the project to see the design. He is not in the design discussions, not there when the design takes shape, and the review meeting is the first time he sees the whole of it. Yet if there is a data incident, his is the first name on the accountability email (in the Chapter 5 stakeholder map, the risk owner cell and the blocker cell carry the same name). Least information, heaviest responsibility. Inside that structure of timing, saying "no" or "send me more material" is rational, and has nothing to do with a taste for caution. Releasing a system he did not help build and cannot see through, he carries all of the downside and shares none of the upside.

> **The reviewer sees the design last and is held responsible first. Saying no is his rational choice.**

So the root cause of review blocking a project is not the reviewer. It is when the information reaches him. Treat constraints as a launch gate and review is left with two values, pass or fail, and fail is always safer for him. Treat constraints as design inputs and every constraint becomes a design parameter, open to discussion about how to satisfy it, open to weighing its cost, and usable as currency to buy space. The earlier constraints come in, the larger the design space. The later they come in, the less is left but "pass or fail."

## Prior Art, and What AI Changed

Manufacturing paid this tuition fifty years ago. The core proposition of the quality movement (the Deming and Toyota traditions) is that quality is built in, not inspected in. A defect caught at inspection costs an order of magnitude more than one prevented at design, and the stricter the inspection, the slower the delivery, with no gain in quality. The fix is to move quality standards forward into design. More inspection cannot save a final check. The security review is software delivery's final check, and the same law applies unchanged.

Peter Block supplies the other half in *Flawless Consulting*. The person with the most resistance often has the most information. A blocker is a requirements owner nobody interviewed, Victor's three questions are a requirements spec written as questions, and the word "obstructive" does not attach to him. You already used the first half of this principle in Chapter 5, the pre-mortem hand-delivered to his desk. This chapter is the second half, taking his requirements formally into the design.

What did the AI era change? Reviewers have no vocabulary for reviewing AI. Traditional review has a mature checklist, permissions, encryption, logging, change management, and Victor can run through it with his eyes closed. But the constraints an AI system adds are on no checklist. Model output is not reproducible, so how do you define "the same test passed"? Where is the boundary of training data and context? For a system that extracts information from email, does maliciously constructed email content count as an injection attack (prompt injection)? How far does "why did the model suggest that" have to be explained before it counts as auditable? The reviewer is learning too. That brings two consequences.

The first is bad news. Where uncertainty is highest, review rulings are most conservative, and "if I cannot understand it, better not launch it" is killing a great many otherwise healthy projects. The second is a rare opening. The reviewer lacks the vocabulary, and you are the only person on the floor able to help him build a framework for reviewing AI. This is the spillover of AI uncertainty management, the one skill of its own (Chapter 2). In the language of Chapter 5's Trust Equation, with a risk owner the fastest way to open a position in credibility (to bank your first deposit of standing) is to hand him a framework he can use to judge safety himself. Proving your own system safe is the slower move. Teaching the reviewer to review you is the highest form of being trusted.

## The Framework: The Trust Constraint Matrix

The trust constraint matrix is one table that moves trust constraints forward into design inputs. Six classes of constraint as rows, three columns, filled from week 2 through to the review meeting.

Six classes of constraint, covering everything an enterprise means by "why should I trust you."

| Constraint | The Question It Answers |
|------|-----------|
| **Privacy** | Whose information, and what information, moves inside which boundaries? |
| **Security** | Who can access what, and change what? Where is the attack surface? |
| **Audit** | When something goes wrong, can you reconstruct who did what, when, and on what basis? |
| **Human oversight** | At which step is a person present, and in what way is that presence real? |
| **Fairness** | Will the system systematically treat one class of subject worse? |
| **Maintainability** | After you are reassigned, leave, or the system enters its third year with nobody watching, who can safely change it? |

Three columns, each with its own discipline.

- **The specific requirement for this project**, and it has to be specific to this project. "Complies with the company data security standard" does not count as filled in. "Customer-identifiable information may not leave the claims domain" does. What goes in this column comes from the constraint interview, not from your imagination.
- **How the design satisfies it**, a mechanism, not a promise. "We will be careful about de-identification" does not count. "Name, ID number and plate number are replaced with placeholders at the extraction layer, and no plaintext appears at any step after that" does. Write the cost at the end of every cell, who spends how much extra time under this way of satisfying it, and what capability is given up (the antidote to "over-compliance" in the failure modes below).
- **Who signs off**, by name. This column is the device that turns the reviewer into a designer. The day his name goes on, he stops being the judge and becomes a co-author, and what he defends at the review is a design he took part in.

What six rows by three columns looks like, two rows from the Anchor & Helm review version.

| Constraint | The Specific Requirement for This Project | How the Design Satisfies It | Who Signs Off |
|------|------------------|--------------|-----------|
| Audit | Every suggestion is fully traceable | The six end-to-end decision trail fields (the six are listed below under At Anchor & Helm); the merged view is purely derived, purely read-only, no write-back. Cost, log storage and the hours for the quarterly spot check | Victor Reyes |
| Human oversight | No action without human confirmation | Risk ranking with a daily volume cap (time); suggestions carry their reason (ability); the Human Call column names a person (authority). Cost, a cap on daily throughput, with the backlog going through the old manual process | Kevin Doyle |

The three steps of the review front-loading process that go with it.

1. **Week 2, the constraint interview.** Go with questions, not with a design (there is no design to bring, which is exactly why this is the best moment, everything can still be changed). Ask three things. What has gone wrong with systems like this before? What are you afraid of? What evidence do you want to see when it comes to the review? Note that these are the three questions you ask him, and they are not the three he will ask you at the review. The answers go into the matrix's first column.
2. **Carry the matrix through the whole design.** Run every major design decision past the second column. Which row does this choice make easier to satisfy, and which harder? The matrix is a living document, and blank rows are legitimate. Mark a row you cannot fill as an open question. It is the blank row you hid that blows up at the review.
3. **Run the review as a confirmation meeting.** Send the review packet ([Template 12](../appendices/template-12-trust-matrix.md)) a week ahead, organized around the answers the reviewer wants. The packet (the bundle of review materials) is the matrix's snapshot at review time, assembled from five things, the de-identification boundary on the data flow diagram, the permission inheritance table (which records how queue permissions inherit core system roles, and has nothing to do with Chapter 2's inheritance matrix), the audit log schema, the rollback path, and the open questions list. Confirm the matrix row by row at the meeting, and rule only on open questions.

Of the six rows the easiest to fake is human oversight. "We have set up a human review step" will always tick the box in a review document. The test against that formality is the three oversight questions.

> **Is there time to look? The ability to judge? The authority to stop it?**

Does the review volume match the human reviewer's time budget? Does he have the information he needs to judge right from wrong at hand? Does his "no" count? Miss one of the three and oversight is nominal. Nominal oversight is more dangerous than none. It manufactures the illusion that somebody is watching the gate, and every other defense slackens with it.

## At Anchor & Helm: Three Questions Become Parameters, the Judge Becomes an Author

**Week 2, the constraint interview.** Item four of the pre-mortem drew Victor in (Chapter 1), and in week 1 you answered his 11-question questionnaire line by line (Chapter 2). So you and Victor had already been round a full loop before week 2 started. In week 2 you invite him back, 60 minutes, a whiteboard, no design. What he asks in person is still those three questions, word for word. Does customer data leave the boundary? Who audits the model's output? Who is responsible when it is wrong? These are the three he will ask you at the review, not the three you asked him in the interview, and they are a different thing again from the three oversight questions above.

But the interview dug out what sits underneath the three questions. Two years ago a small tool one department built for itself carried a detail table containing customer information out of the company, and the accountability landed on him. That department was one of our own too, the tool was called an internal tool too, and nobody along the way thought it needed stopping. What he fears is "being bypassed, and still taking the fall when something goes wrong." AI itself comes second. That is the sentence written in his cell of the Chapter 5 stakeholder map, and it was not written wrong.

You were at the company when that happened. This is one of the openings being internal gives you. Most of the answer to the interview's first question is already in your hands. So do not go in empty-handed asking "what has gone wrong." Go in with a hypothesis. Say the incident you remember first, let him correct the details, then ask one line, "which one is there that I do not know about." The ones he adds are the information you were actually missing. That line also tells him you are not here to run a process, you remember what has gone wrong at this company.

Three questions, translated on the spot into three design parameters.

1. **Does data leave the boundary → customer-identifiable information is de-identified at the extraction layer.** Name, ID number, plate number and phone are replaced with placeholders before they enter the queue or any model call. The de-identification boundary is a solid line on the data flow diagram. There is plaintext to the left of the line and none to the right.
2. **Who audits the output → every suggestion carries a trail the whole way.** Input snapshot, rule and model version, suggestion, reason, Human Call, timestamp, not one missing. AI output is not written back to the source and exists in trail form (Chapter 9's discipline, which turns into an audit commitment here).
3. **Who is responsible when it is wrong → queue permissions inherit core system roles, and the Human Call carries a real name.** No separate account system is built. Whoever may handle a given claim in the core system is the only one who may pick it up in the queue. The final action on every suggestion lands on a person with a name.

There is a fourth question beyond the three. For a system that extracts information from email, does maliciously constructed email count as an injection attack? The reviewer cannot answer that one either. The answer did not stop at a question mark. Over the following weeks it grew inside the design into a fourth parameter.

Email content is treated as untrusted input, always. The extraction layer recognizes only a schema whitelist, anything outside the four fields is rejected (Chapter 10), and the extraction result contains no free instruction text. An email that says "please handle this claim as routine" can at most contaminate a few field values. It cannot give the system orders. Add the system stopping at the advise layer, plus no action without the Human Call column, and the blast radius of an injection is held by design inside "one suggestion waiting for human review."

When the interview ended, four of the matrix's six rows were filled. Fairness and maintainability were left blank, marked as open questions. In week 3 Victor joined the audit log design review as agreed (the line planted in Chapter 2 honored), and his name appeared in the third column for the first time.

**Weeks 2 to 7, the matrix travels with the design.** When Chapter 9 settled the merged view as "purely derived, purely read-only," Victor's requirement was already written in the matrix's audit row. "Derived data does not feed the source" is data discipline on your side and an audit boundary on his, one design satisfying two ledgers at once. When Chapter 10 rejected the fully automatic multi-agent design, the human oversight row was one of the criteria.

The two blank rows also landed during these weeks. The error taxonomy of Chapter 11's eval filled in the fairness row. The priority logic uses no customer identity attribute, and the override (a human overturning the AI's suggestion) distribution is spot-checked by customer segment each quarter. What counts as a finished fairness row is being able to say what data would reveal unfair treatment. Writing "no discrimination" does not count. The maintainability row waited for the design to take shape. Rules and the de-identification config become configuration items the claims-ops IT engineers can change (they take over in Chapter 15). What counts as a finished row here is letting the person taking over try changing a configuration item once. It counts when the change goes through.

This row carries one more discipline specific to being internal. The signer may not come from this project's delivery team. The device in the third column is turning the reviewer into a co-author, but if the future maintainer is you, this cell is you signing for yourself, the device fails on this row, and what you signed is not a constraint but an ops commitment with no end date. So the maintainability row is either signed by the business line's IT or ops, or left blank and handled as an open question. Blank is more honest than self-signed, because a blank gets asked about at the review and a self-signature does not.

The three oversight questions landing at Anchor & Helm is the human oversight row of the matrix above, unpacked. The queue is ranked by risk with a daily volume cap, and the number of rows entering human view each day is worked back from the review time budget, better to leave some out of the ranking than to have them glanced at and not read. That is time. Every suggestion carries its reason, so the information for judging right or wrong is in front of her and she does not have to check three systems. That is ability. In Linda's team's "Human Call" column, does her "no" count? It does, and without that column the system produces no action. That is authority. These three designs land as actual columns of the queue in Chapter 17.

**Week 8, the confirmation meeting.** The packet goes to Victor and compliance a week ahead. One red line on the data flow diagram for the de-identification boundary, one page for the permission inheritance table, one page for the audit log schema, half a page for the rollback path, two open questions. That produces the scene this chapter opened with. The whole write-back review is skipped, and Chapter 9's "purely read-only" decision is cashed in on the spot for thirty minutes. Compliance asks where responsibility lands and Victor answers for you. Notice the language he answers in. Every sentence is from the matrix's second column. He is answering for a design he signed, and there is nothing of covering for you about it.

The cover of the packet carries two lines in the byline block, solution design by you, constraint design by Victor. That is not a layout detail. It is a ritual you have to build on purpose, and inside a company it has ready-made vehicles. The review conclusion memo goes out from you and Victor jointly, and recipients see two senders. The design document's author line carries two names side by side. At the meeting he presents the constraints section, not you.

Take care not to downgrade this into an approver's signature. An approver's signature is a process action, and after signing he is still the judge. Joint authorship is a change of identity, and after signing he defends his own design.

From blocker to co-signer, this line took eight weeks, and every step has a record. The pre-mortem hand-delivered, the questionnaire answered line by line, the constraint interview, the audit log reviewed together, the matrix signed. In the Trust Equation this is a run of consecutive deposits, and not one of them was luck.

Record the cost honestly. Pulling Victor into the design was not free. The de-identification layer, the audit log and permission inheritance came to roughly one extra week of engineering. Worth it? The cost of the other road was posted back in Chapter 1, a six-week review queue plus one rejection at the final gate. Constraints that come early have costs that are visible and plannable. Constraints that come late have costs that are hidden and fatal. This packet's life does not stop at eight weeks either. Chapter 18's launch gate updates and reuses it.

That extra week is harder to defend inside a company, because it has no budget line of its own. "Launch first, security later" wins at every scheduling meeting. The way to defend it is not to argue technical necessity. It is to change whose request it is. The day the de-identification layer, the audit log and permission inheritance were written into the matrix's second column, they stopped being your technical preference and became specific requirements written down by the risk owner. Whoever wants to cut that week is cutting Victor's requirements, and needs his nod. His requirement is the budget justification for that week, and that is the second use of putting real names in the third column.

Beyond the review it was built for and the reuse in Chapter 18, this packet has a third use, in a place you would not expect. The annual internal audit, a regulatory inspection, a Group compliance spot check, all ask the same set of questions. Who can access it, how do you reconstruct what happened, at which step is a person really present. At that point you are still at this company, and you are the one called in to answer. So the constraint matrix is not a project artifact for you. It is a permanent ledger, and it gets updated for as long as the system lives. After each spot check, add the newly asked questions into the first column, and answer one fewer next time. This also explains why the maintainability row cannot be left blank overnight. A spot check does not look at how beautifully you delivered. It looks at who is responsible now.

Look one layer further out. You and Victor are not a one-off project relationship. You are long-term colleagues, and there can be an account between you. This time's six-row matrix, the way the de-identification boundary was drawn, the six trail fields, the permission inheritance principle, all of it most likely holds unchanged for the next AI system. Save this packet as an "AI system constraint baseline" the two of you share, and the second project's constraint interview starts from "which rows are different this time" instead of from "what has gone wrong before." A formal 60-minute interview becomes one confirmation in a corridor. The baseline is his asset too. He does not have to reinvent his criteria for every AI system. This is compounding that only exists inside a company, and the real cost of the first packet has to be amortized across every project that follows.

## Failure Modes

**1. Compliance as the last gate.** On the schedule, "security review" is the last box before launch, and the reviewer's first sight of the design is the final gate. Project templates naturally draw review at the end of the flow, and engineers treat review as a cost center to be put off as long as possible. So the reviewer gets the least information, latest, saying no is his most rational move, and both sides push the project toward death from inside their own rationality. One test. If the reviewer's name first appears on the schedule rather than on a design meeting's sign-in sheet, you are already in this failure mode.

**2. The "our own tool" escape.** To dodge review, the system is positioned as an "internal helper script" or a "pilot tool" and goes live quietly, outside the formal process. The pain of review is immediate and concrete, the risk of being traced is delayed and probabilistic, the standard time-discounting trap. By the time the tracing arrives the system has real users, and the political cost of taking it down is enormous. Worse, you have detonated with your own hands the thing the risk owner fears most, being bypassed. One escape and this cell turns red permanently, and you still have to work with him for years, where permanent means what it says. Of the four in this chapter, this is the one an internal team is most likely to commit, because you are inside the firewall already, you have the permissions already, what you build is called an internal system already, and no door physically stops you. Other people are happy to wave you through, a tool built by one of our own can just start getting used. One test. If you are in the middle of explaining to yourself why this system does not need to go through review, you are already inside it.

**3. Nominal human oversight.** The review step exists, the human reviewer gets 500 rows a day, three seconds each. The "time" of the three questions fails. Review checks only the boolean "is there human review," and nobody does the arithmetic of daily volume times seconds per row. Both the system side and the review side have an incentive to see that box ticked, the former to pass, the latter to be off the hook. On the day something goes wrong the human reviewer takes the whole fall, the front line refuses from then on to sign anything in a "Human Call" column, and the trust gap collapses. The test is simple. Write the daily volume and the review time budget on the same line and divide.

**4. Over-compliance.** All six constraints turned to maximum, double review on everything, even the amount ranges the claims reviewers need for judgment de-identified away, three levels of approval on every action. The system is impeccably safe, and safely unusable. The pilot data is dismal and the project dies of "no value" rather than "risk." The root is that whoever proposes a constraint does not bear the cost of using it. One more requirement costs the reviewer nothing, and the cost lands entirely on the front line's operating time and the system's usability. A matrix that does not write costs down lets constraints accumulate in one direction only. The fix is in the second column's discipline, write the cost of every constraint's satisfying mechanism, and let it take part in the trade-off like any other design parameter. Remember, over-compliance and no compliance die different deaths on the same date.

## Next Monday

1. Pull out your stakeholder map (Chapter 5), find the name in the risk owner cell, and book one 60-minute constraint interview. Bring questions, not a design. What has gone wrong before? What are you afraid of? What evidence do you want to see at the review?
2. Fill in a first version of the trust constraint matrix with [Template 12](../appendices/template-12-trust-matrix.md). Mark rows you cannot fill as open questions, keep them on the table, and do not delete them.
3. Run the three questions on your system's human oversight step. If any one of them has no answer, change the design this week. Cap the volume, add the reason, or give a real authority to stop it.
4. Look at the schedule. If the security review is less than two weeks from launch and the reviewer has not seen the design, put the constraint interview into this week's calendar today.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 12 Next Monday actions. First run python3 templates/trust-constraints/redact.py
on the built-in sample to demonstrate field-level de-identification, then open audit-log-schema.sql and show me what the audit log looks like. Those two are the mechanism samples
for the matrix's "privacy" and "audit" rows. Then build an empty trust constraint matrix from Template 12. The answers from the risk owner constraint interview are mine to fill in
row by row when I get back, and rows I cannot fill get marked as open questions and stay on the table, not deleted. The three oversight questions are mine to answer, you only record them.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The trust constraint matrix (six rows, privacy / security / audit / human oversight / fairness / maintainability, by three columns, the specific requirement / how the design satisfies it, cost included / who signs off) + the review front-loading process (week 2 constraint interview → the design carries the matrix → the review becomes a confirmation meeting); the three oversight questions
- **Templates.** [Template 12](../appendices/template-12-trust-matrix.md), Trust Constraint Matrix and Security Review Packet, organized around the answers the reviewer wants, sent a week ahead
- **Key judgments**
  - "The reviewer sees the design last and is held responsible first. Saying no is his rational choice."
  - "The earlier constraints come in, the larger the design space. The later they come in, the less is left but 'pass or fail.'"
  - "The three oversight questions. Is there time to look? The ability to judge? The authority to stop it?"
  - "Teaching the reviewer to review you is the highest form of being trusted."
