# 11 · Eval as Spec: Write the Eval Before the Architecture

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-11-eval-spec.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The business side asks "what accuracy can this reach," and you cannot give a number. "Accurate" has never been defined. Most internal projects have no acceptance meeting, but on launch day someone still has to release it, and any number you report now turns into an argument on that day.
>
> **What You Will Be Able to Do.** Write the five parts of an eval spec before drawing the architecture. Co-build golden cases with the actual user and treat annotation disagreements as requirements discovery. Use that spec to rule on architecture upgrades and launch release, and use the co-build to get business rules that were never aligned across departments written down for the first time.

---

## Week 7, Thursday, a Question Nobody Could Answer

The pattern discussion wrapped up yesterday (Chapter 10). Kevin Doyle calls you into his office and asks a question he has been holding for a while. "This system, what accuracy can it reach?"

Behind the question is real pressure. The acceptance line in the charter reads "tie it to the eval, golden cases plus thresholds, sign the mechanism now and fill in the numbers later" (Chapter 4). Golden cases are real cases with the correct answer settled in advance. The old ticket's "Q&A accuracy ≥90%" was voided and filed at the project approval change review, and now the moment to "fill in the numbers later" has come. Kevin answers to Grant Whitmore. He needs a number.

You do not give one. You ask back. "Last week a claim with a questionable amount in Linda Marsh's team went through as a routine claim. Whose error is that? Is it an error at all?"

The room goes quiet for a few seconds. By the core system, that claim showed nothing abnormal. The status moved normally, no deadline was missed. By Linda's instinct, it should have been flagged red. By the customer service log, the customer even praised the speed. Same claim, three answers.

"If I tell you '95%' right now," you say, "on release day we will fight over every single claim, because we never agreed on what counts as an error. Give me a week and a half and I will give you a table you can sign. It is worth more than a number. The signatures are yours and Victor's. You are the business-side owner, Victor Reyes is the risk owner, and whether this system goes live was never supposed to be decided by the people who built it. There is an annotation session in week 8. Come sit in for twenty minutes, and you will watch the denominator of that number being made."

Where there is no definition of error, there is no accuracy, and no release either. This chapter is about how to make that definition.

## Why This Is Hard: An AI System's Spec Cannot Be Written as "Input X, Output Y"

A traditional software spec describes behavior. Input X, output Y must follow. It can be enumerated, walked through, and ticked off on an acceptance sheet. An AI system cannot do that. The same input can produce different outputs, and the input space is never exhausted. So many teams skip the spec, paper over it with "it works well," and postpone defining error to the moment disagreement costs most, the last week before launch.

The way out is a different form of spec. Writing the behavior spec in finer detail will not save it. An AI system's spec does not describe behavior. It describes the acceptable distribution of errors. The system will err, but what it gets wrong, how much, and where a wrong output goes can be agreed in black and white. The thing that carries that agreement is the eval. Golden cases define what the system "should be." The error taxonomy and thresholds define "how good is good enough." What these three look like, the "At Anchor & Helm" section shows with concrete cases. The eval set is the requirements spec itself. Being a testing tool is its part-time job.

That also explains the words "before the architecture." Chapter 10's governing principle is "Start with the dumbest thing, and let the evidence force the upgrade," and the evidence can only come from the eval. Without an eval written first, a pattern upgrade has no criterion, architecture trade-offs decay into contests of taste, and acceptance decays into the political question of "does the boss think it is fine." This is the core discipline added in the AI era, and one of this book's two technical anchors. The other is the action queue of Chapter 17 (the queue that lines up the next action for every claim).

## Prior Art, and What AI Changed

Write "what counts as right" first, then write the implementation. That order has two mature ancestors.

**The engineering tradition, TDD's "tests as spec."** Kent Beck's test-first discipline is at its core about writing the test first so that you are forced to think the requirement through before writing code. The test is an executable spec, and how many tests there are is secondary. Eval as spec is its closest relative. Golden cases are the AI system's "tests written first."

**The consulting tradition, aligning the picture of success before the work starts.** Peter Block's contracting discipline in *Flawless Consulting*. What the client will see on the day the project succeeds must be aligned in concrete language before the work starts, or delivery day is disappointment day. The eval spec turns that "picture of success" from adjectives into fifty concrete cases plus a threshold table.

What did AI change? This is a new discipline, with three things the old traditions did not have. First, an error taxonomy replaces a single accuracy figure. In traditional software a bug is an anomaly. In an AI system errors are the normal state and come as a distribution, and the kinds of errors and their consequences matter far more than the total. Second, tacit knowledge has a systematic home for the first time. The five rules of thumb dug out of Linda in Chapter 6 could only be passed on verbally before. Now they have a place to be written down. Third, Chapter 2 concluded that this method adds exactly one skill of its own, AI uncertainty management, meaning eval, human oversight, and drift (the system's results quietly degrading over time). That sentence starts getting paid off in this chapter. The eval is the first load-bearing wall of that skill. Human oversight (Chapter 12) and drift monitoring (Chapter 18) are both built on top of it.

## The Framework: The Five-Part Eval Spec

| # | Part | Question It Answers | Discipline |
|---|------|-----------|------|
| 1 | **Task definition** | What is being evaluated | One sentence at the level of the workflow claim (Chapter 0). What input the system takes, what output it gives, for whom, and where the red line is. One eval evaluates one task |
| 2 | **Golden cases** | What counts as right | 50 to 200 real cases + correct answers. The count is set by coverage of error categories, every category must have cases that can detect it, never padded to a total. Answers clear the data check first. Edge cases and historical incident cases must carry real weight |
| 3 | **Error taxonomy** | What kinds of error there are | Each category states its definition, business consequence, and tolerance. Reuse the pass / concern / unsafe / useless error severity vocabulary (this book sets no separate sev-1/2/3 numbering; an error category's consequence tier borrows three of the four grades directly, so the scoring words and the severity words are one set). The unsafe class is zero tolerance |
| 4 | **Per-category thresholds and acceptance lines** | How good is good enough | One line per error category. No overall score. An overall score is the shortest path to burying unsafe |
| 5 | **Human review path** | Where outputs that fail go | Trigger condition, destination, who looks, how fast. Review results flow back into the golden cases |

Three rules of use. **First, golden cases must be co-built with the actual user.** The correct answer is in Linda's head, not in your reasoning. And the by-product of co-building, annotation disagreement, is itself requirements discovery (the field section demonstrates it). **Second, reconcile the answers first.** Every fact a golden case's "correct answer" cites must stand at validated or above on the data fitness ladder. Why, the next section will lay out Chapter 9's reconciliation numbers and do the arithmetic. **Third, set thresholds per error category.** The costs of different errors differ by orders of magnitude. One averaged line guarantees nothing.

## At Anchor & Helm: How Fifty Golden Cases Grew

In weeks 7 and 8, you and Linda's team did this. The time was not ready-made. The charter line "Linda's team, 2 hours a week, for case annotation and rule confirmation" (the business-side commitment line, Chapter 4) is one line of text, and nothing turns it into Linda's team's calendar on its own. You did three things. First, no new meeting. The annotation session was attached to the review team's existing weekly, run straight after it, so Linda did not have to fight for a new slot on your behalf. Second, state the exchange plainly. Your twenty years of rules get written down for the first time, and once written, the guide belongs to the review team, not to the system. Third, the fulfillment rate is reported monthly at Grant's weekly (Chapter 4). Two hours this month or zero, both sides can see it.

The division of labor follows Chapter 0's principle. AI does the grunt work (screening candidate claims and pre-filling fields, drafting first-pass answers), people make the calls (the final ruling on every answer can only come from a reviewer). The first line of work is the task definition, lifted straight from the sentence the Five Ones of Chapter 8 lock into. For every auto exception claim in the merged view, give the next action (whom to chase, what is missing, who takes it), for Linda's auto claims review team, and never touch the payout decision. All fifty cases are drawn against that sentence.

The answers themselves clear the data check first. You pulled eighty candidate claims from the merged view, and step one was reconciliation, with annotation after it. Chapter 9 did the arithmetic. 87 of 200, that is 44% of the fields, cannot be taken at face value, and here that becomes a discipline. Take the core system's fields directly as "correct answers" and nearly half your answers are wrong, which is accepting the system with a bent ruler. So every candidate claim is checked first. Where the system fields, the Excel tracker, and the inbox agree, it goes in. Where they disagree, run the three-way reconciliation ([Template 9.3](../appendices/template-09-data-fitness.md)) to rule on the truth, and drop what cannot be ruled on. Eighty screened down to fifty-nine, take fifty. The first mile of the eval is reconciliation, and annotation comes after it.

The error taxonomy grew out of three unsafe marks. On Field MVP day in Chapter 0, Linda marked 3 as unsafe, and the four-grade scale you used then was pass / concern / unsafe / useless. Looking back, that scale was the seed of the error taxonomy. It was already layering errors by consequence, it just had not grown categories yet. The first formal category grew precisely out of those three unsafe marks. All three pointed at the same thing, a risky claim queued as a routine one, and so it got a name.

| Error Category | Definition | Consequence | Severity (error severity vocabulary) | Tolerance |
|----------|------|------|------|--------|
| **Missed risk** | A high-risk claim judged routine | Grows into a major case, regulatory complaint | unsafe | **Zero tolerance, 0 of 50** |
| **Line-crossing suggestion** | A suggestion touches the payout decision red line (Chapter 8) | Responsibility has nowhere to land | unsafe | **Zero tolerance** |
| **Material error** | Missing-material list wrong or incomplete | A wasted round of chasing, the customer waits days longer | concern | ≤10%, and the error must be obvious to a reviewer at a glance |
| **Wrong action** | Next action or owner given wrong | One idle round | concern | ≤10% |
| **Empty suggestion** | The suggestion is not wrong but carries no information | The queue slowly goes unread | useless | ≤20%, negotiable, trend must not rise |

The two zero-tolerance rows come with an ugly statistical truth first. 0 of 50 is an entry ticket, not a proof of safety, because fifty cases cannot detect every surprise in real operation. The real defense for a zero-tolerance category is every decision trail entry after launch (Chapter 18).

The three ratio rows have an ugly truth too. Zero tolerance is counted in cases and does not depend on sample size. Ratio lines like ≤10% and ≤20% on fifty cases mean one case is two percentage points, and the ratio read from a single replay swings by a dozen points or more on its own. It gives direction, not a scale. So ratio thresholds are read as a trend across several replays, and that is what "three consecutive replays" at Chapter 14's gate one is about. To read the line finer, add cases, not just confidence.

The annotation guide, five rules of thumb on duty. How do you annotate missed risk? The answer is the five rules the three-layer probing of Chapter 6 dug out, amount deviation, report delay, survey photo count, prior claim linkage, repair shop list, with the judgments written into the guide exactly as Chapter 6's five lines have them. They go from verbal tradition to annotation guide, and "missed risk" splits accordingly into five testable ways to fail. Which signal the system missed is visible at a glance. Chapter 6's promise (tacit knowledge turns from interview color into a system asset) is paid off here.

One gets special handling, the repair shop list. Linda said outright "it is not a fixed list," so that section of the guide carries a dated version and rolls with the list. That is the first reason the eval must stay alive (failure mode 4 settles the account).

The makeup of the fifty is deliberately uneven. Typical claims are under half. A dozen or so edge cases (amounts right at the top of the usual range, reports filed exactly two days late, no more, no less). Ten historical incident cases, including the out-of-pocket repair claim Linda herself described misjudging in Chapter 6. That is where the system's value and its risk both live.

At the annotation session on Tuesday of week 8, Kevin came to sit in, as promised. He was not there to supervise. At next quarter's operations meeting he has to present this project, and when he does he has to report a number, and the denominator of that number is being made in this room. You arranged double independent annotation. Every claim is annotated by Linda and by another senior reviewer on her team (second only to her in seniority), each on her own. Forty-six of fifty agree. Of the four disagreements, three closed on the spot, each with a different root.

- One was different information. The other reviewer only looked at the photo count recorded in the core system and never opened the inbox attachments. Once filled in, the annotation changed to agree.
- One was different standards. A claim reported two days late straddled a weekend, and whether that counts as "beyond the ordinary" split them. Kevin ruled that report delay is counted in working days, and it went into the guide.
- One was a different reading of the task. The other reviewer had annotated missing materials as missed risk too. The task definition gained a sentence. Missed risk covers the five signals only. Missing materials belong to material error.

All three went into the disagreement log.

Item 37 blew up. A claim ending in 2093. The plate was new, but the filer's phone number was appearing for the third time in six months. Linda marked "high risk." The other reviewer marked "routine."

Both froze, each thinking the other was joking. You took the judgment apart the three-layer probing way. Linda's "prior claim linkage" counts three things, plate, filer, phone number, and a phone number appearing a third time is, to her, a strong signal of an intermediary filing on the customer's behalf. The other reviewer counts only plate and filer, and her reason was solid too. "Repair shops file for customers all the time. Flag them all and you hit a crowd of innocent ones." Two standards, each in use for over a decade, each working. Same team, same rule, two standards. Twenty years of verbal tradition never aligned them, because there was never an occasion that required them to write the answer on paper and then look at each other's. The eval is that occasion.

Linda turned to the observer's seat. "Kevin, your call." Kevin heard both sides and ruled on the spot. A repeated phone number counts toward the linkage signal, but on its own it does not make a claim high risk, it only triggers human review. The exception scenario for shop-filed claims goes into guide section 4.2. On the Annotation Disagreement Log ([Template 11.3](../appendices/template-11-eval-spec.md)) you wrote the first line. The disagreement, both sides' reasons, who ruled, the rule that came out.

On the way out Kevin said at the door, "Last week you asked me 'whose error is that.' Now I see why you would not give a number." The conclusion is worth a memo. Annotation disagreements are business rules that were never aligned, surfacing, and treating them as noise is a huge loss. The eval had not yet evaluated a single system output, and it had already made this company write a twenty-year verbal rule down for the first time.

On Friday of week 8, you handed over the per-category threshold table above plus one human review path, far more substantial than a number. The review path is written to the four items of the fifth part. Trigger condition, claims that hit a risk rule with low confidence, plus anything that looks like an unsafe-class error. Destination, the queue's Human Call column, and without that column the system takes no action. Who looks, the reviewer who picked up the claim, by name, and every suggestion carries its reason, so judging it right or wrong does not mean checking three systems. How fast, the number of claims entering human view each day is worked back from the review team's review time budget, and it is better to route too few than to have them glanced at and not read. The answers to Chapter 12's three oversight questions are already written here. Suspected unsafe-class cases are reviewed weekly, and review conclusions flow back into the golden cases. The golden cases are the requirements document, and the thresholds are the acceptance clauses. From here on this table serves several purposes at once.

- Where Chapter 10's upgrade criterion lands. Only when "structured extraction + rules" fails the missed-risk line does a heavier pattern earn a hearing.
- The charter's "fill in the numbers later" is formally paid off here. The old ticket's wording was voided and filed at the project approval change review (Chapter 4), the vacated slot is filled by this table, and the thresholds go straight into the project resolution as the launch release conditions.
- Raw material for the prototype-to-pilot gate (Chapter 14).
- After launch it becomes the live monitoring definitions as is (Chapter 18).

## When Nobody in the Room Can Rule

Kevin's on-the-spot ruling was lucky. The disagreement fell inside his own department's rules, he had the authority, and he was willing to spend it right there. Cross-department disagreements do not look like that. Imagine an annotator borrowed from customer service also sitting at the session. On one claim she marks "answered the filer, waiting for a reply," and the claims-side annotator marks "still on my desk." The same "in progress," used by two departments for ten years (the nine semantic-divergence fields of Chapter 9). Nobody in the room has the authority to change the other side's definition, and the session stalls there.

When it stalls, do not put it to a vote, and do not split the difference. That blends two clear rules into one rule nobody owns. What you do is classify the disagreement on the spot, write it into the disagreement log, and route it one of three ways by type.

- **Within-department disagreement.** Find the owner of this workflow, rule on the spot, and write the ruling into the annotation guide.
- **Cross-department disagreement.** Pause annotation. Write both definitions and their business consequences on half a page, send it to the two sides' common superior, or put it on the sponsor weekly as an agenda item. You cannot rule this one for anyone, but you can make sure someone rules within two weeks.
- **Compliance-related disagreement.** Cross-department or not, it goes to the risk owner, at Anchor & Helm that is Victor Reyes. A compliance definition is not an efficiency question and cannot be settled by whoever is loudest.

All three routes want the same thing. A disagreement is not allowed to hang. A hanging disagreement becomes a golden case each side annotates its own way, and that one case strips the whole table of its standing as arbiter.

## Co-building the Eval Is Standalone Value You Can Give the Business Side

Back to what Kevin said at the door. The real output of that annotation session was not fifty cases. It was this company writing a twenty-year verbal rule down for the first time, and the review team owning it. That annotation guide stays alive without your system. New-hire training uses it, cross-review uses it, and it is not voided when the core system is replaced next year. It is an organizational asset, not a project artifact.

That is also the best reason to ask for those 2 hours a week. Once the rules are written down, someone has to use them day to day, and the people who will use them are in your company, so this is something you can get done. You are not here to borrow labor to test a system. You are here to help the review team turn what lives only in Linda's head into something everyone on the team has in hand. That sentence can be said out loud at their weekly. "Help us with an evaluation" cannot.

Three more things only someone inside can move. The ten historical incident cases, you can pull straight from the complaint files and retrospective notes, without waiting for a veteran to volunteer a "the one I got wrong" story. The second annotator can be borrowed from another department. Ask a senior reviewer from customer service to annotate the same batch, and cross-department semantic divergence surfaces at the annotation session instead of in the queue after launch. Once the annotation guide is written, push to promote it to the review team's formal operating procedure, filed under a department document number, not left in your project folder.

After promotion someone has to run it. The guide belongs to the review team. Linda is the owner who maintains it, review flow-back and monitoring-triggered retests (Chapter 18) land on her monthly, and the reminder hangs on the review team's existing monthly QA review, not on anyone remembering. Inside a company no invoice reminds anyone that the eval is due for an update, so the reminder has to be written into a meeting people already hold. The two numbers of failure mode 4 are reported by that owner at that meeting. When she cannot answer, the rot has already started.

## Failure Modes

**1. Build first, evaluate later.** The architecture is set, the pipeline runs, and a week before launch someone remembers "we should do an evaluation." The eval got filed as "testing," and in engineering instinct testing comes after implementation. But an AI system's eval is the requirement. Written after the implementation it is no longer a requirement, it is a justification. The team will, without noticing, tune the thresholds until the architecture already built just passes. The upgrade criterion goes missing with it, and Chapter 10's "let the evidence force the upgrade" hangs in the air. One discipline. The eval spec is finished before the architecture decision meeting. That is the operational meaning of "before the architecture."

**2. A single accuracy metric.** "Overall accuracy 92%" makes it into the report. Organizations naturally favor a single number. Easy to remember, easy to compare, fits on a slide. But averages were invented for scenarios with symmetric costs, and here one missed risk costs ten thousand times one empty suggestion. 92% can mean "3 unsafe out of 50" at the same time, and the better the number looks, the deeper it buries them. When the old ticket's "≥90%" was voided at the project approval change review, the objection was that it was an overall score. Whether the number was high or low did not matter.

**3. An eval set of nothing but typical cases.** Every golden case is smooth, and the system sails through the first round with a high score. Typical cases are cheap to collect. Within reach, answers undisputed, annotation effortless. Edge cases mean digging through aged claims, and historical incident cases mean someone has to admit "I got one wrong." Both are expensive. But accepting on typical cases is issuing a diploma after examining only the easiest part of the system. One test. How many cases in your eval set have someone disagreeing with the answer? None means the disagreement was avoided, and disagreement is the substance of the spec.

**4. One-shot eval.** After acceptance the golden cases are never updated again. The eval was treated as a project artifact (finished and filed) when it is an operating asset (depreciating continuously). The repair shop list drifts, fraud methods evolve. Chapter 9 said fitness is a state, not a property, and the same holds for the eval. A one-shot eval means drift cannot be detected. The system quietly degrades and your ruler keeps proving it has not. The way out. Cases flowing back from review are added to the golden cases monthly, and monitoring anomalies trigger a retest (Chapter 18 takes over this line). How much updating is enough, look at two numbers. The number of cases that flowed back into the golden cases last month is not zero, and the annotation guide's version number moved this quarter. If neither can be answered, the eval is one-shot, however seriously it was co-built at the start.

## Next Monday

1. Ask one question about the AI system on your desk. "Which kind of error can the user not accept even once?" Write it down. That is the first row of your error taxonomy, the unsafe class. If you cannot write it, you have not yet talked to the actual user about consequences.
2. Use the collection list in [Template 11.2](../appendices/template-11-eval-spec.md) to gather 20 golden cases to start. Typical cases under half, at least 3 historical incident cases, dug from the complaint log and retrospective notes, or ask a veteran for a "the one I got wrong" story. Answers clear the data check first.
3. Ask two actual users to annotate the same batch **independently** and count the disagreements. Record each one in 11.3, find someone with decision rights to rule, and write it up as a written rule. The disagreement rate is the number of missing pages in your requirements document.
4. Dig out your project's acceptance clause. If it is an overall score, draft a per-category replacement. Now, not the week before acceptance.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 11 Next Monday actions. First run python3 templates/eval-spec/run_eval.py,
then run python3 templates/eval-spec/threshold_report.py, and show me the replay report and the per-category threshold table on the built-in sample. Then copy
eval-spec-template.md into the working directory I name. The unsafe row is mine to write. If I cannot write it, remind me to go talk to the actual user about consequences first,
do not make it up for me. The 20 golden cases are mine to dig out by the collection list. You only build the table and count disagreements. Rulings on the two annotators' disagreements and the written rules are
written by someone with decision rights, not you. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The five-part eval spec (task definition → golden cases → error taxonomy → per-category thresholds and acceptance lines → human review path); the three co-build rules (annotate with the actual user / reconcile the answers first / thresholds per category, no overall score)
- **Templates.** [Template 11](../appendices/template-11-eval-spec.md), Eval Spec, Golden Case Collection List, Annotation Disagreement Log
- **Key judgments**
  - "An AI system's spec does not describe behavior. It describes the acceptable distribution of errors."
  - "The golden cases are the requirements document, and the thresholds are the acceptance clauses."
  - "Annotation disagreements are business rules that were never aligned, surfacing. They are not noise."
  - "The first mile of an eval is reconciliation, not annotation."
