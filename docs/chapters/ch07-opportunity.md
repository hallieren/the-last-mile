# 7 · The Opportunity Screen: Five Questions That Kill Most Ideas

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-07-five-questions.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The business side and your boss have a dozen AI ideas stacked up, and every one of them sounds workable. Which one, and on what grounds? The harder half is telling the sponsor to his face that the idea he forwarded you should not be built.
>
> **What You Will Be Able to Do.** Score any AI use case on the five questions (Pain / Data / Decision / Risk / ROI). Screen out the unqualified opportunities in one afternoon with the elimination table. Report the results to an executive on one page, including the elimination of the one he forwarded himself.

---

## Turning the Clock Back to Before the Charter Meeting

The readout (the memo that states the conclusion at the end of the Field MVP) has just been delivered. You have "the direction works." You do not have "what to build." Inside a week there are three candidates on your desk.

The first comes from the top. Thursday evening Grant Whitmore forwards a board email. Inside it is a piece of industry news, a peer has launched an "intelligent service bot," with a board member's own words attached. "Can our service line get one of these too?" Grant added four words. "Evaluate this for me." The second comes from the corridor. Kevin Doyle stops you. "Keep pushing on the exceptions thing. Separately, our monthly operations report takes two or three days of stitching data together by hand. Can AI generate it? That one pays off fast."

The third is the one the Field MVP itself pointed to, an action queue for exception claims (the queue that lines up the next action for every claim), carrying ten scored cases and three unsafe marks (output a real user judged should never have appeared). Turn the clock back and this is exactly the two weeks before the charter meeting in Chapter 4.

All three "can be built." With today's model capability there is almost no proposal that "cannot be built," and that is precisely the problem. There are already enough ideas. What you need is a discipline for eliminating them.

## Why This Is Hard: Ideas Became Free, Validation Did Not

Chapter 1 covered demo inflation. Demos got so cheap that being impressive no longer proves anything. The same inflation has an earlier form inside an organization, idea inflation. Proposing a software requirement used to mean the proposer had at least worked out the workflow and the fields, so the proposal itself carried a cost. Today anyone who finishes reading one news item can produce an AI use case that sounds like it holds up. The cost of producing an idea has fallen close to zero.

The cost of validating one has not dropped a cent. Validating a use case means a pilot (real users, real use, inside a controlled scope). Three months, a team, a hard-won stretch of data access, and the most expensive item of all, the organization's patience for "this AI thing." When the first AI project fails, what burns is AI's name at this company, and the next project breaks ground on the rubble.

An open funnel mouth, an expensive funnel bottom, and no gate in between. That is the assembly line enterprises use to mass-produce zombie AI projects. Worse, the bill for picking the wrong use case arrives three months later, and by then nobody records the cause of death as "we picked the wrong use case." They record "the model is not good enough," "the data is garbage," "the users would not cooperate."

So this judgment is worth writing as one sentence. Picking the use case is the deliverer's single highest-leverage decision, higher than any architecture decision. Get the architecture wrong and you refactor. Get the prompt wrong and you edit it. Get the use case wrong and three months go to zero, with trust overdrawn.

## Where the Right to Screen Comes From Inside a Company

Answer a prior question first. On what grounds do you decide that a business unit's idea is not to be built? A team from outside can say "I took on this one thing, not every idea you have." You cannot say that sentence. Claims' asks belong to Claims. You are not their superior and you are not their review committee. Veto a department's proposal on your personal professional judgment and it works the first time. The second time they go around you. The third time they go straight to Grant Whitmore. The right to screen has two sources, and neither one is granted by you to yourself.

**One, the intake gate.** Every AI idea comes in through the same entrance, the same five-question sheet, the same elimination rule, hung on the company's existing project approval review or requirements review. The gate's force does not come from your judgment. It comes from which meeting it hangs on, who backs it, and whether it is written into policy. Behind the gate you are only the person who fills the sheet in. What gets eliminated is the idea that does not pass the sheet, not the idea you dislike. Chapter 25 turns all of this into organization-level intake discipline. This chapter is its hand-built version.

**Two, the resource pool the sponsor (the executive who funds it and makes the call) authorized.** What Grant gave you was never "you may veto other people." It was "what this team works on first this quarter is set by this sheet." You hold no veto power. You hold scheduling rights. Say "we are not doing this" and you have no standing. Say "this team is not doing this this quarter, on these three pieces of evidence" and you have standing.

Before the gate exists, the substitute is repetition. The same sheet, the same rule, the same reporting format. By the third time, the rule starts to exist ahead of the individual case, and that is the smallest form of an institution.

## Prior Art, and What AI Changed

On the question of which opportunities are worth the investment, sales thought it through forty years before engineering did.

**SPIN's four-question structure.** The large-sale questioning method Neil Rackham set out in *SPIN Selling* (its thinking paraphrased here) has four layers, situation, problem, implication, need-payoff. The most valuable one is implication, pushing "this is pretty annoying" into "what happens if it is not fixed? How much do you bleed a month? Who takes the blame for it?" Most proposals die on that question. The pain is real, but not fixing it kills nobody.

**Solution Selling's qualification discipline.** Qualification is screening an opportunity for fitness before work starts, and not chasing what does not qualify. The Michael Bosworth line of sales methods has one counterintuitive iron rule (paraphrased). The most expensive mistake in sales is chasing the wrong deal, and losing a deal ranks behind it. Burning three months on an opportunity that does not qualify costs ten times what being turned down on the spot costs. So the fitness standard goes up front, and unqualified opportunities are dropped on purpose.

Move that iron rule inside a company and both ends need converting. There is no "losing a deal" here. What corresponds to it is turning down an executive's idea to his face, and the cost is one person's goodwill, payable immediately, repairable with one report and one re-evaluation condition. What corresponds to "chasing the wrong deal" is taking on an unqualified idea, and the cost is three months of the team's capacity plus AI's name at this company, payable in three months, unrepairable, and the next project is still yours to run. Set the two bills side by side and qualification's arithmetic is more lopsided inside than outside. Yet it is harder to enforce inside, because the goodwill bill is the one you pay today and the other one the whole company pays next year.

Both traditions ask whether it is worth doing, and both assume that whether it can be built is not in question. Traditional software behaves deterministically. Install it and it runs. An AI use case gets no such default, which adds two hard gates traditional qualification never had.

- **Data readiness**, because data does not become ready just because the idea is appealing. The idea is free. The raw material is not.
- **Error tolerance**, because a probabilistic system will be wrong. The question shifts from "is it any good" to "how many times may AI be wrong at this step? Who backstops it when it is?" The same model is an assistant where someone backstops it and an incident where nobody does.

Turn the two gates into questions and you get three. Data readiness maps to Data, which asks whether the raw material is there. Error tolerance does not fit into one question and splits into two. How many errors are allowed and who backstops them is Decision. How far an error travels afterward and whether it can be pulled back is Risk.

The implication SPIN pushes for is the Pain here. The "is it worth doing" both traditions ask is the ROI here. Pain and ROI are inherited from the prior art. Data, Decision, and Risk are the homework the AI era added. Together, five questions.

## The Five-Question Framework and the Elimination Table

The five-question framework, five test questions for judging an AI use case, each scored 1 to 5. Read the table by looking first at the third column, the test question, and the fifth column, what a low score looks like. Leave the fourth column for when you come back to score.

| # | Question | Test Question | What a 5 Looks Like | What ≤2 Typically Looks Like |
|---|-----|----------|----------|----------------|
| 1 | **Pain** | Whose action is bleeding? Is the bleed rate (loss per unit of time, hours, complaints, fines, churn) measurable? | A specific person + a specific action + a measured bleed rate; leave it and someone keeps taking blame or paying out | Cannot name the person or the action; or after the follow-up "what happens if it is not fixed," the answer is "not much" |
| 2 | **Data** | Does the data this action needs exist? Can you get it? Can you trust it? (A pre-check. The full grading is the data fitness ladder in Chapter 9, the grading of whether data is fit enough, and that ladder and the outcome ladder in Chapter 1 are two different ladders) | Data exists, the business owner is named, samples are in hand, spot checks hold up | The key data does not exist, or there is no realistic path to getting it |
| 3 | **Decision** | Which decision point does AI enter? How many times may it be wrong there? Who backstops it, and how fast does the error surface? | It enters at the advise layer; the backstop is named; errors are visible on the spot and can be overridden | Real-time and outward-facing with nobody backstopping; or a decision with near-zero tolerance handed to AI to execute directly |
| 4 | **Risk** | What does the worst single output cause? Does it reach only inside, or customers, regulators, money? Can the loss be closed out? | The worst output's loss stays inside and can be closed out, and it sits outside the agreed red lines | One bad output reaches a customer or a regulator, and it cannot be taken back |
| 5 | **ROI** | What is the arithmetic that turns the outcome metric's improvement into money? Who owns that bill? | An outcome metric + the conversion arithmetic + a person willing to carry that number in his own reporting | Only activity metrics ("it launched," "92% accuracy," numbers that say only what was done). Chapter 1 covered why they do not survive the boardroom |

The elimination table is the summary of the five-question scores, plus one non-negotiable rule.

> **Any question scoring ≤2 is eliminated outright. No weighting, no averaging, no "considering it in the round."**

This is weakest-link logic, not sum logic, because the relationship among the five questions is multiplication. A use case scoring 1 on Data cannot be built however much Pain there is, the raw material will not feed in. A use case scoring 1 on Risk will not be allowed to launch once built. The only function of a weighted average is to translate "not feasible" into "ranked low," and a project ranked low still gets started in a year with budget to spare. A weighted average is the excuse you reach for when you do not want to eliminate anything.

A 3 is a conditional pass. The evidence is not hard enough yet, so write the validation action that closes the gap into the sheet, with a deadline. Not met by the deadline, it drops to 2. Elimination is not a death sentence either. Every eliminated candidate gets one line of re-evaluation condition, what evidence, if it appears, makes it worth running the five questions again. "Not now" needs an exit before elimination can be enforced at all.

Scoring takes evidence only, numbers, users' own words, data samples. The five questions burn evidence, not cleverness, and the evidence is all the stock you built up in the earlier chapters, the MVP scoring sheet, the friction log, the informal annotation that started in week 2.

> **Any score with a blank evidence column is treated as a 2.**

The **pass / concern / unsafe / useless** scale from Chapter 0 is for a real user to react to a single output. The five questions' 1 to 5 is for you to find an opportunity's weakest link. Two scales, two uses. Do not mix them.

The internal reader holds two things a person taking projects from outside cannot get. Both have to be written as actions, not as consolation.

One, ask the implication before the proposal takes shape. Run into the proposer in the corridor and ask in passing, "if this is not fixed, what does it look like three months from now, and who suffers?" Half the ideas fall apart in the other person's own answer, never entering the sheet, never entering a report, without offending anyone. The cheapest moment to eliminate an idea is before it has become a forwarded email.

Two, a record of past rejections is the hardest local evidence there is. Which department proposed the same thing two years ago, which question it died on then, and where that money went instead, only someone who has been at this company can look up. Put it in the evidence column and it beats any industry news, because the proposer remembers that episode too. The precondition is that the sheet from back then can still be found, see the section "Elimination Needs an Exit, and Re-evaluation Conditions Need a Recheck Owner" below.

## At Anchor & Helm: Three In, One Out

Three candidates, one at a time through the sheet. The full scorecard is in [Template 7](../appendices/template-07-five-questions.md). Here are the decisive rounds.

**Candidate one, the service chatbot (the board's suggestion).**

Pain. Give it its due first, the service line's pain is real and call volume is climbing. Push one layer and it changes shape. Customer complaints cluster on "nobody tells me where it is stuck," and the bulk of the calls is a downstream symptom of the exceptions backlog, with inquiries only a small share. Fit a more patient answering machine to the symptom and the source bleeds exactly as fast. Pain 3, the pain is real, the leverage is upstream.

Data, 1. The chatbot would have to answer two kinds of question. For "where is my claim," the answer lives in the core system, the inbox, and Linda Marsh's tracker, and at minute 35 of the MVP you found that the status field lies (the first line in the Chapter 0 friction log). Using a lying field to answer customers in real time transfers the internal data debt straight to the customer. For wording questions, the library of standard approved answers it would need does not exist at all.

Decision and Risk, both at the floor. The entry point is real-time customer-facing replies, error tolerance is close to zero, and nobody backstops it, because bypassing people is the whole point of a service chatbot. What does the worst single output look like? You wrote it out. "Your loss assessment payment is expected within three business days." One wrong promise to a customer is one regulatory complaint. Decision 2, Risk 1.

ROI 3. Call cost can be computed, but the slice a chatbot would save cannot, because the bulk of the calls will fall on its own once the upstream is cured. The cause of death in one sentence. It would carry the conversation with the lowest error tolerance in the place where the data is worst.

**Candidate two, automated monthly reports (Kevin's proposal).**

This candidate dies faster than expected, and the murder weapon is SPIN's implication follow-up. You asked two more questions.

"Last month's report was three days late. What happened?" Kevin thought about it. "Nothing. I chased it once."

"After the report goes out, who replies or follows up?" He thought longer. "...Grant looks at two numbers. Everyone else files it."

The bleed rate is near zero. The pain is in the annoyance of producing it, not in any business consequence. Pain 1, and the conclusion is settled on that one question, with the other four filled in afterward for the file. That is how the elimination table saves time.

The monthly report's annoyance is not undeserving of help, but what it is worth is forty minutes of goodwill, not a three-month project. A few weeks later you automated, in passing, the reporting spreadsheet Kevin gets questioned about most, and Chapter 5 already showed you what those forty minutes bought. Eliminating a project is not the same as eliminating the other person's problem.

**Candidate three, the exceptions action queue.**

Pain 5. A specific person (Linda's team), a specific action (the next step on an exception claim), a measurable bleed rate, the first payment cycle running at 1.6 times the industry average. More precisely, about six tenths of the waiting time across the ten cases is "waiting on documents with nobody chasing, stuck with nobody claiming it." Chapter 4's -30% is computed from here.

Data 3, a conditional pass. The data exists, it has a business owner, ten de-identified samples came through. But the status field being untrustworthy is a confirmed fact, and only after the Excel is reconciled against the core system will you know which rung of the ladder this data actually stands on. Write the condition explicitly, the reconciliation gets finished during discovery (the stage of finding out how things actually are). Chapter 9 in its entirety is that condition being met.

Decision 4. AI enters at the advise layer, ranking, missing items, next action, with a Human Call column behind every suggestion, errors visible on the spot and overridable, the backstop named (Linda's team). The three unsafe marks remind you that tolerance has a boundary. Some error types (ranking a high-risk claim low) must not happen even once, and it takes an eval (the evaluation set) to fence them off (Chapter 11).

Risk 4. The worst single output is one wrong ranking suggestion being followed. The loss stays inside, and it can be found, corrected, and closed out. Not one word goes outside, and it sits outside the red line (no payout decisions).

ROI 4. First-touch handling time is the outcome metric and the conversion path is clear, reviewer hours, chase calls, complaint handling cost, customer churn. Kevin's operating budget owns that money, and Grant's board narrative ("catching up with the industry") can use it.

Three lines of summary.

| Candidate | Pain | Data | Decision | Risk | ROI | Lowest Score | Conclusion |
|------|------|------|----------|------|-----|-----------|------|
| Service chatbot | 3 | 1 | 2 | 1 | 3 | Data / Risk | Eliminated (re-evaluation condition, re-measure the call mix after exception handling is cured, and the standard-answer library gets built) |
| Automated monthly reports | 1 | 3 | 4 | 4 | 2 | Pain | Eliminated (turned into a favor done in passing, no project) |
| Exceptions action queue | 5 | 3 | 4 | 4 | 4 | Data (conditional) | Winner, conditional on data reconciliation during discovery |

## How to Tell Grant the Board's Suggestion Was Eliminated

The winner is easy to report. Eliminations are hard, especially when the eliminated one came from the board. Near the end of week 2 you book twenty minutes with Grant Whitmore. His first sentence is, "That service one. Did you look at it?"

You did not say "I do not think it fits," and you did not talk about technical difficulty. You put that one page of elimination table on the table and did one thing, point at the scores and read the evidence column. "The service line's pain is real, but the bulk of the complaints is 'where is my claim stuck,' and that is a symptom of the exceptions backlog. Cure exceptions and this share of the calls falls on its own." That is the Pain row. "It has to answer customers in real time about claim status, and the claim status field lies. The MVP hit that on day one." That is the Data row. "The worst single output is a wrong payout statement made to a customer. That is regulatory risk, and the chatbot has no human backstop." That is the Risk row.

Then the sentence you had ready. "So the conclusion is that the evidence says not yet, and my personal preference is not in it. The sheet carries the re-evaluation condition. After exception handling is cured, re-measure the call mix, and with the standard-answer library built, this candidate is worth running through the five questions again."

Grant studies the sheet for a while. He does not ask "why are we not doing it." He asks, "The board. How do I put it?" You give him a sentence he can repeat. "What the peer launched is a general-purpose service bot. We are treating the source of the calls first, exceptions. Once the metric moves, the foundation for service automation, the standard-answer library and trustworthy claim status, is laid along the way."

He puts the page in his bag. "I will take this. If the board asks, I will say it this way. On exceptions, let us set the metric at a meeting next week." That "meeting next week" is the charter meeting you saw in Chapter 4.

This scene is worth one line of retrospect. "I am not doing it" is a position, and positions get haggled over. "The evidence says not yet" is a judgment, and rebutting it takes better evidence, and nobody in the room has evidence harder than your ten cases. The re-evaluation condition then turns "no" into "not now." Elimination becomes a conclusion the future can overturn, not a taking of sides. Doing this inside your own company leaves less room to back out. The eliminated idea came from your own reporting line, the person who proposed it is still sitting across from you next week and still has to lend people to your project next quarter. So the internal exit cannot be the re-evaluation condition alone. The re-evaluation condition answers "why not this time." It does not answer "then what happens to my ask now," and it does not answer "who will still remember this sheet in six months." There are three exits.

- One, the gate. Before this report, it decides whether you have the standing to say what you just said.
- Two, the referral route. After the report, it decides where the eliminated ask went, and on whose books its ops cost lands later.
- Three, the recheck owner. Six months out, he decides whether this "not now" actually gets read again.

The next two sections cover the last two. Chapter 25 upgrades this whole move into organization-level intake discipline. Today's twenty minutes is its first rehearsal.

## Elimination Needs an Exit, and Re-evaluation Conditions Need a Recheck Owner

When a team from outside eliminates an idea, the idea disappears from view. Inside, it does not. Next quarter the proposer will have the ask you eliminated built by an outside firm, or he will buy a SaaS product, and when that thing starts erroring six months after launch, the tickets still route back to your team. What you eliminated was not the project, only your visibility into it. The ops liability arrives all the same.

So the internal version of elimination has one more move. Every "eliminated" row gets a referral route written behind it, one of three. Refer it to a standard tool, whatever the company's existing ticketing system, BI, or automation tools can do, and write down who configures it. Refer it to self-serve, a general capability the proposer can operate himself, and you give a template and one training session, not a project. Refer it to an outside purchase, and write down who selects, who accepts, and who owns ops after launch. Leave that last column blank and the name that fills in by default is yours. The monthly report row's "turned into a favor done in passing, no project" is the lightest of the three.

Re-evaluation conditions work the same way. Writing one down is not the same as being remembered. An outside team's elimination table gets archived with the project three months later. An internal elimination table has to live for years, and a lifespan with no end and a recheck count of zero is not "not now," it is a politely worded permanent refusal. So the re-evaluation condition gets two more columns, who rechecks it and at which standing meeting. The default is to hang the elimination table on your team's quarterly ask review, read the eliminated rows out each quarter, run the five questions again on the ones whose conditions have appeared, and formally close the ones whose conditions clearly never will, telling the proposer. This sheet is a team ledger, not a folder of yours. It has to still be there after you move on.

## Two Departments Both Passed the Five Questions. Which One First?

The five-question elimination table answers "is this worth doing." It does not answer "Claims and Underwriting both passed the sheet, which one first." A team taking projects from outside never meets the second question, serving one client at a time. The internal team is shared. In the same quarter, several business unit heads sit at the same level, any of them can go to Grant, and in their eyes "order" means "importance." So after the sheet there is a second sheet, three rows.

| Dimension | Question | How the Order Gets Set |
|---|---|---|
| Evidence maturity | Whose lowest score is a conditional 3, and can the condition be met this quarter? | Conditions that can be met this quarter go first, conditions six months out go behind |
| Commitment hardness | Whose business owner has already claimed people and weekly hours by name? | Claimed goes first, verbal support goes behind (the first of the three resource gates, Chapter 14) |
| Organizational timing | Whose outcome metric can make the next business review? | The one that can make it goes first, the one that cannot gets re-ranked next quarter |

All three tie, go back to Pain's bleed rate, and whoever bleeds fastest goes first.

One step after ranking. Put the opportunity cost on the same page. The report does not say "we picked the exceptions queue." It says "the other things this team is not doing because of it," listing the candidates behind it, which row each of them is stuck on, and which quarter each waits for. That column is written for the sponsor, and also for the department that ranked behind. In a shared resource pool, a trade-off that is not written out gets read as favoritism.

## Failure Modes

**1. Reasoning backward from technical capability to a scenario.** The project discussion starts from "our agent framework is mature," and the question is "where could the business side use it." The team's sunk investment in technology needs an outlet, and scoring quietly favors the scenarios that "can use our stuff." The order of the five questions, starting from Pain, is the antidote. For a candidate reasoned backward from technology, the Pain column usually holds nothing but "improve efficiency."

**2. Taking the wishlist.** The readout succeeds and you accept every "AI requirements list" the departments send, straight into the backlog (the list of what is queued to be scheduled), scheduled in the order received. The social cost of refusing is payable immediately, offending the proposer on the spot. The cost of accepting arrives three months later. But a wishlist is wishes sorted by rank, not opportunities sorted by evidence.

**3. Picking the one the executive is most excited about.** Grant's eyes light up at one idea and the project team automatically ranks it first. An executive's excitement is an approximate signal for resources and air cover (the senior cover that stands in front of you), so a team moving toward the light is being rational. But excitement measures how good an idea sounds when spoken. It is demo inflation's conference-room version, measuring narrative quality, not workflow leverage. On ROI settlement day, that applause does not discount to a cent.

## Next Monday

1. List every AI idea circulating in your organization, and first rewrite each one as a single "whose action" sentence (the workflow claim form from Chapter 0). Anything you cannot write is out in round one.
2. Pick three survivors and spend 30 minutes each scoring them on the [Template 7](../appendices/template-07-five-questions.md) scorecard. One rule only, the evidence column takes numbers, quotes, and samples, no adjectives.
3. Find the candidate you least dare to eliminate, usually the one proposed by the most senior person, and see which question its lowest score falls on. The evidence for that question is what you bring to your next report.
4. Use [Template 7](../appendices/template-07-five-questions.md)'s one-page format and deliver the result to the proposer face to face. Build the muscle memory for the sentence. "The evidence says not yet, and here is the re-evaluation condition."

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me do the Chapter 7 Next Monday actions. First run python3 templates/five-questions/onepager.py
with the built-in sample and show me a one-page elimination table. Then copy scorecard.csv into my own scorecard. I give the candidates
and the evidence for each question, you fill it in, the evidence column takes only numbers, quotes, and samples, and if I say an adjective, hand it back
for me to replace. I score, you do not. When filled in, rerun onepager.py pointed at my file, leave the one-pager for me to deliver in person, and add no conclusions of your own. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The five-question framework (Pain / Data / Decision / Risk / ROI, each with its test question) + the elimination table (1 to 5, weakest-link logic, any question ≤2 eliminated outright, no weighted average; a 3 is a conditional pass; every elimination must carry a re-evaluation condition); two scales with two jobs, pass / concern / unsafe / useless tests a single output, 1 to 5 screens opportunities; the three exits from elimination (the gate, the referral route, the recheck owner) + the three rows for cross-department ranking (evidence maturity / commitment hardness / organizational timing)
- **Templates.** [Template 7](../appendices/template-07-five-questions.md), the Five-Question Opportunity Rubric, the five-question scorecard (with 1/3/5 anchors and an evidence column) + the elimination table + the reporting one-page format
- **Key judgments**
  - "The cost of producing an AI idea has fallen close to zero, the cost of validating one is still expensive, and the mouth of the funnel must have discipline."
  - "Any question scoring ≤2 is eliminated outright. A weighted average is the excuse you reach for when you do not want to eliminate anything."
  - "Picking the use case is the deliverer's single highest-leverage decision, higher than any architecture decision."
  - "'I am not doing it' is a position. 'The evidence says not yet' is a judgment."
