# 0 · The Opening 48 Hours: Turn a Vague Ask into a Field MVP in Two Hours

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-00-field-mvp-pack.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The business side says "we want an AI assistant." You do not know what is behind that sentence, and neither, in fact, does the business side.
>
> **What You Will Be Able to Do.** Inside the opening 48 hours, spend two hours turning any vague AI ask into a minimal workflow prototype (a Field MVP) that real users can score line by line, and use it to decide whether to continue, narrow, redirect, or stop.

---

## Monday Morning, the Conference Room

You sit in the Group's Digital Center, and a request from claims operations at Anchor & Helm Insurance has landed on your desk. Monday morning at nine, COO Grant Whitmore gives you fifteen minutes.

> "We want an AI assistant to make the claims department more efficient. Our competitors are all doing AI, and the board keeps asking. In three months I want to see something."

Kevin Doyle, Director of Claims Operations, adds, "Ideally with a dashboard, so I can see the overall picture."

The meeting ends. Those two sentences are all the information you have.

*(Anchor & Helm Insurance is a fictional composite assembled from common enterprise scenarios and corresponds to no real company. Every company and character in this book is fictional.)*

Three roads lie in front of you now. The first two are familiar roads, and both are dead ends.

**Road one, a scoping study.** Spend four to six weeks on interviews, process maps, and a requirements document. This is the reflex of the IT requirements review process. File the request, get on the schedule, wait for the next iteration window. Six weeks later you have a handsome deck and a business side already wondering whether these people can code at all. Half of Grant's three months is gone.

**Road two, straight to a demo.** Pick the handiest large model and spend two weeks building a claims Q&A chatbot. Demo day is stunning, and Grant is pleased. Then it dies. The demo dies the moment the demo succeeds, the most common way enterprise AI dies (Chapter 1).

**Road three is what this book teaches, the Field MVP.** Inside the opening 48 hours, spend two hours building a minimal workflow prototype together with real users. Small enough to be ten rows of data and one table. Real enough that a front-line reviewer can point at each row and say this one helps, this one is dangerous.

Every method in this book grows out of these two hours. Win this round first, then talk method.

## Why This Is Hard: A "Vague Ask" Does Not Look Vague at All

The danger in an ask like "build an AI assistant" is that it does not look vague at all. It has a subject, an object, and a budget, and everyone feels they understand it. Everyone just understands something different.

- Grant wants something that proves to the board the company has not fallen behind.
- Kevin wants a dashboard that shows him the whole picture, and on the side, he would rather this project not disrupt his department.
- Linda Marsh wants nothing. She is the front-line team lead with twenty years in claims review. You have not met her yet, and nobody has asked her. And she is the one the system is ultimately for.

The traditional way to handle this divergence is alignment by meeting. More meetings, longer documents, until everyone signs. Alignment on paper has one fatal weakness. People's agreement to an abstract description is cheap. Everyone agrees to "use AI to improve claims efficiency," just as everyone agrees to world peace. The disagreement does not erupt until launch day, which is the most expensive moment for it to erupt.

The Field MVP flips the bet. Let the disagreement blow up at hour 48, not on day 90. Faced with one concrete table and ten concrete cases, people cannot keep agreeing cheaply. Within two hours Linda will point at row three and say, "Handle this one at the priority the system suggests, and the customer complaint goes straight up to the regulator."

## Prior Art, and What AI Changed

This approach is a cross of two mature traditions, not a new invention.

**The consulting tradition, contracting before diagnosis.** Open by settling the boundary of the engagement. Consulting calls this step contracting (agreeing on the terms of the engagement). Peter Block warns again and again in *Flawless Consulting* that the consultant's biggest mistake is to start work on a vague engagement, that is, to do diagnosis (finding the problem) before contracting. The first thing to do at the opening is to turn who wants what, where the boundary is, and what counts as success into an explicit contract. The Field MVP inherits that spirit and moves the contract negotiation from the meeting table to the front of a prototype. Ask the business side "what is your success criterion" and they cannot answer. Give them ten concrete rows of output and ask "does this count as success," and the answer comes out.

**The lean tradition, the smallest experiment for the biggest learning.** Eric Ries's MVP (minimum viable product) is at its core about validated learning. Identify the riskiest assumption and test it with the cheapest experiment. The Field MVP is the MVP's variant for the enterprise field. It tests three questions closer to the ground than "will users buy." Is the real pain the one we think it is, is the data enough to support action, and will front-line users trust it.

What did AI change? The cost of a prototype collapsed. In 2020, a scorable prototype in 48 hours was empty talk. Just learning the claims vocabulary took a week. Today every piece of grunt work in prototyping can go to AI. Pulling fields out of interview notes, generating realistic synthetic cases, drafting the queue's column structure, producing a first-pass judgment on ten cases. Contracting and prototyping (actually building the thing) used to be weeks apart. Now they are two hours apart. That is the technical reason this approach only became possible now. Once prototype cost collapsed, the order of "align first, then build" could be reversed.

Some things AI did not change. It cannot judge for you which boundary must not be touched, cannot say "this one is dangerous" in Linda's place, and cannot decide for Grant whether to keep investing. In the Field MVP's two hours, AI does the grunt work. People make the calls. That division of labor runs through the whole book.

## The Two-Hour Process

The Field MVP has fixed inputs, a fixed process, and fixed deliverables. The full picture first, then each part.

Four inputs, which you should be able to get inside the opening 48 hours. The clock starts at the meeting where the business side or an executive voices the ask. For the red line, do not go to the person making the ask. Go to the risk owner (the person accountable for this to the end) or to compliance for confirmation.

Most asks do not come with such a meeting. They arrive as a group chat message, a ticket, or one line broken out of the annual plan, and the clock never starts on its own. You have to manufacture the starting point and make it an event. Send an email naming the four inputs you need and the date of the readout 48 hours out (the memo that states the conclusion at the end of the process, see the last row of the table below), copying the person who made the ask and your manager. The moment that email goes out, the 48 hours are really running.

1. One vague ask. For example, "build an AI assistant for the claims department."
2. The structure and details of 3 to 10 historical cases. Note that this is not necessarily a data file. Data export goes through approval, measured in weeks, and rarely clears in 48 hours. Copying fields and case summaries by hand at the data owner's screen, or having AI generate realistic synthetic cases, both count as getting it. The order and the limits are below.
3. A profile of one real user, specific to the person. "The claims department" does not count. Linda does. Review team lead, clears the chase emails first thing every morning.
4. One red line that must not be crossed. For example, no automated payout decisions, no real customer data, no messages sent outside automatically.

Each of the four inputs has its own way of being unobtainable, and all are common. Each has a fallback.

- If the data does not clear, take the next best thing. First try to get in front of the data owner's screen and copy the structure and de-identified summaries by hand, taking no data with you. What compliance blocks is copying. Looking usually gets through. Only failing that, use AI-generated synthetic cases. They can test the shape of the workflow, not data feasibility, and the readout must say so. Inside a company, the way this input gets stuck is often not a rejected approval but unclear data ownership. Anyone could give it to you, nobody dares. Then skip the approval process. Find out first who the real owner of this table is in the system, write the fields you want to see and the purpose in one sentence, and ask him to nod.
- The real user cannot be booked, blocked by "just ask me if you have questions." That is the norm, not an accident. Lay out the definition of the scorer. Only someone whose daily work the system will change counts. Forty minutes is all you need, and the other person is welcome to sit in. Still no meeting, then write "no access to real users" itself into the readout. That line speaks louder than any score.
- Nobody will hand you a red line. Draft the three most conservative ones yourself and send them to the risk owner for confirmation. Silence is not consent.
- The friction of getting the inputs is itself the first batch of findings. Whichever input is hardest to get, that is where this organization's first real boundary lies.

Two things in the table need explaining before you look at it. The first is the workflow claim written in step one.

> **Workflow claim. One sentence that says whose next action this system will change, and which one.**

The second is the four-grade scale used in the scoring step. Not 1 to 5. Numeric scores make users give a polite 3. pass / concern / unsafe / useless forces a position, and unsafe and useless are counted separately. pass means it can be used as is. concern means something is uneasy but not to the point of danger. unsafe means following it causes harm, a risk signal, top priority. useless means not wrong but not useful, a value signal, just as fatal, different in kind. Three unsafe carry far more information than seven pass. The fourth grade follows the scorer. When a real user takes a position on outputs, the fourth grade is useless, and the question is value. When an engineer reads system traces to judge evidence, the fourth grade usually becomes unclear, meaning this one's outcome cannot be verified yet. The first three grades mean the same in both sets. Do not mix the two fourth grades in one table.

The two-hour process follows. Read the Time and What You Do columns first. For What AI Does and Deliverable, just skim the names. Case Table, Action Queue prototype and the rest are explained one by one in the Field MVP Pack section.

| Time | Step | What AI Does | What You Do | Deliverable |
|------|------|-----------|----------|------|
| 0 to 15 min | Rewrite the ask | Draft candidate wordings | Rewrite "build an AI assistant" into one workflow claim | Workflow Claim |
| 15 to 35 min | Prepare cases | Extract fields from raw material / generate synthetic cases | Pick 10 representative ones | Case Table |
| 35 to 60 min | Design the queue | Suggest a column structure | Decide columns, statuses, owners, risk flags | Action Queue prototype |
| 60 to 85 min | Generate first output | For 10 cases, generate priority, next action, missing information, risk flag, reason | Review for obvious errors | Filled queue |
| 85 to 105 min | Real user scores | Collate the annotations | Ask the real user to mark each line pass / concern / unsafe / useless | Scoring results |
| 105 to 120 min | Write the readout | Draft the memo | Settle the conclusion, continue / narrow / redirect / get more data / stop | MVP Readout Memo |

"Build an AI assistant" settles none of that and does not qualify as a workflow claim. "Let a claims reviewer, on opening an exception claim, see directly what material is missing and whom to chase first," that one qualifies. If you cannot write the workflow claim, you do not yet know whose work you are changing. Then however good the technology, what you are building is decoration.

## At Anchor & Helm: From AI Assistant to Exceptions Queue

Monday afternoon you hit two walls. First, you ask Kevin for 10 de-identified claim records. He agrees readily, and compliance blocks faster. Data export goes through data security approval, de-identified or not, "next week if it is quick." Second, you try to book Linda. Kevin frowns. "The front line is racing quarter-end. Whatever you need to know, just ask me."

Neither wall gets knocked down. On data you step back half a pace. No file, just 20 minutes standing at one of his staff's screens to see what 10 closed exception claims look like. No data leaves the system. You copy by hand only field names, status transitions, and de-identified case summaries. On Linda, you lay out the definition of the scoring step. The scorer must be someone whose daily work changes after launch, and Kevin is not that person. You need her for 40 minutes, you prepare the material, and he can sit in the whole time. Kevin thinks about it and agrees. "Then I will listen too."

Inside a company, what stands between you and the front line is usually your own direct manager or the other department's manager. The same move applies. Lay out the definition of the scorer, ask him to sit in, not to score on her behalf. Same move, different chips. A team from outside has paperwork to lean on, and you cannot cite a line of it. With no document to hold over the other side, the only card left is exchange. Three things buy those 40 minutes. One action that saves her effort on the spot, the readout's conclusion copied to her supervisor, and her name on the scoring sheet. The third is the cheapest and weighs the most. You write the front line's judgment up as evidence carrying her name and send it upward, a treatment she has not had in twenty years. Here is the actual run of those two hours.

**Minute 15, workflow claim, first version.** "When a claims reviewer handles an exception claim, the system gives a priority and a next action." The sentence has already narrowed. In those 20 minutes at the screen, 7 of the 10 claims were stuck in "exception handling" status, and on that you bet the real pain is in exception claims, not routine ones.

**Minute 35, the case table.** You feed the hand-copied field structure and case summaries to AI and rebuild 10 structured cases with fields for claim number (pseudonymized), line of business, reason stuck, days waiting, chase count, and missing material. The rebuild exposes the first data fact at once. The core system's "claim status" field does not match what the screen actually described. Three claims show "in progress" while the handler's note says "waiting two weeks for the customer's documents." You record that in the friction log, a running list of the places where reality and paper do not match. It becomes the lead in Chapter 9.

**Minute 60, queue design.** Columns are claim number / reason stuck / missing item / days waiting / suggested priority / suggested next action / owner / reason / Human Call. The last column, Human Call, is the soul of the table. It declares that this system advises people, it does not decide for them.

**Minute 85, AI's first output.** All ten generated. Two are obviously sensible (material missing, generate a chase list), one obviously stupid (a claim with a questionable amount marked "low priority," reason "short waiting time").

**Minute 105, Linda scores.** The first five minutes look like a polite sign-off. Linda scans the first two rows and says "fine," "okay." Kevin is sitting next to her, and she is giving the answers you give the boss. You change the question and point at row three. "If this were handled this afternoon exactly as written, what would happen?" She pauses a few seconds and picks up the pen. The rest of those 20 minutes is the densest value in the whole two hours. The result is 5 pass, 2 concern, 3 unsafe. The three unsafe point at one problem. AI took "many chases" as a high-priority signal. Linda looks at risk. "The customers who chase hardest are not necessarily the urgent ones. Claims with abnormal amounts and disputed liability, the customer does not chase, but let them sit and something big goes wrong."

Chase priority ≠ risk priority. That sentence also answers a bigger question in passing. No general-purpose chatbot could ever have Linda's judgment built in. This is where the project's real technical content lives. Take the judgment rules in Linda's head and externalize them (move them out of her head, write them down as rules a system can execute) into the system. That thread unfolds in Chapters 6 and 11.

**Minute 120, the readout memo.** Four lines of conclusion.

> 1. Direction viable. Exception handling is a real pain point, and the queue form is accepted by the front line (5/10 pass).
> 2. Key finding. Priority judgment must separate chase pressure from business risk. Linda's tacit rules need to be captured.
> 3. Data risk. The core system's status field cannot be trusted. Reconcile during discovery.
> 4. Recommend narrowing to auto exception claims and entering formal discovery. No general-purpose chatbot.

Tuesday afternoon you take the scored table and the four lines to Grant. You have no deck, but you have a front-line user's handwritten annotations and three unsafe cases. He does not react at once. He asks two questions first.

The first is scope. "The scope shrinks from AI assistant to auto exception claims. When the board asks, how do I tell it?" You answer, the telling is on this table. The three unsafe are the first hard evidence of "how AI would go wrong at this company." Plug the places that would go wrong first, and only then does efficiency get its turn.

The second is time. "Data approval is still stuck. What do you do for the next two weeks?" You answer, before the data clears, reconciliation design and interviews on front-line tacit rules. If the data is still not in place two weeks from now, he gets a readout with that fact in the first line.

Grant stares at "chase priority ≠ risk priority" for a while and says, "I am taking this to the board. Continue. Chase the data through the process, but do not hang the project on it."

Inside a company that "continue" carries no resources of its own. Stop and salaries get paid, continue and salaries get paid, so it may be nothing more than encouragement. While he is still in the room, translate it into three verifiable things. Whose schedule gives way, how many people at how many hours a week, and by when it gets reassessed. Those three go into the charter next week (the written contract, Chapter 4). Ask them now. Whichever one you cannot get an answer to is the first to collapse in the next two weeks.

In 48 hours the project went from "build an AI assistant" to "an action queue for auto exception claims." You did not get the data. The approval is still in motion. What you got is authorization to enter discovery (the formal stage of finding out how things actually are), a real list of data risks, a front-line team lead beginning to tell you the truth, and a sponsor (the executive who funds it and makes the call) who has already seen how you write bad news.

## The Five Pieces of the Field MVP Pack

When the two hours end, you should be holding five deliverables. Together they are the **Field MVP Pack**, the first template in this book you can take with you (full version in [Template 0](../appendices/template-00-field-mvp-pack.md)).

1. **Workflow Claim**, one sentence saying whose next action changes, and which one.
2. **Case Table**, 10 representative cases with structured fields.
3. **Action Queue prototype**, one table with suggestion, owner, reason, and Human Call.
4. **Scoring results**, the real user's pass / concern / unsafe / useless mark on every output, with the reason.
5. **MVP Readout Memo**, the conclusion (continue / narrow / redirect / get more data / stop) and the evidence.

Why the fourth uses a four-grade scale rather than a score was covered before the process table. The whole value is in counting unsafe and useless separately.

## Boundaries: What This MVP Is Not

The Field MVP's value comes from its honesty, and honesty comes from boundaries. Three must be declared in advance.

- **It is not a system**. No real production data, no sensitive information, no promised launch date. Tell the business side plainly, this is a probe for deciding whether the thing is worth doing, and it is a long way from version 0.1.
- **Synthetic data cannot validate data feasibility**. If the 10 cases are AI-generated, the question "is the data enough to support action" remains entirely unvalidated, and the readout must say so. Synthetic cases can only test two hypotheses, the shape of the workflow and user trust.
- **One MVP does not replace discovery**. What it gives you is the direction and the authorization to enter discovery. Linda's 40 minutes exposed that tacit knowledge exists. Capturing it takes the full method of Chapter 6.

## Failure Modes

**1. Turning the Field MVP into a mini demo.** An hour and 45 minutes of the two hours go to tuning the prompt. The interface is beautiful, and there is no real-user scoring step. The engineer's instinct is to optimize the deliverable, but the Field MVP's deliverable is a basis for judgment, and the software is only the carrier. One spreadsheet with handwritten annotations beats a polished interface nobody has scored.

**2. Picking the wrong scorer.** You show Kevin, he says "very good," and Linda never sees it. A manager judges whether the thing will look respectable in a report. The front line judges what happens when it is really used tomorrow. Both kinds of feedback are useful. Only the second can save your life. The test is simple. The scorer must be someone whose daily work the system will change after launch.

**3. Starting without a red line.** To make the Field MVP look good, you used real customer data, or let AI output suggest payout amounts directly. Excitement overrode the sense of boundary. The consequences are asymmetric. An MVP takes weeks to build trust, and one data violation or one dangerous suggestion destroys it in a minute, along with AI's reputation at this company. Red lines are set before the clock starts, not in the last minute.

**4. Treating "continue" as the only legitimate conclusion.** The scores are bad and the readout still says "overall direction validated," because you feel stopping equals your own failure. Finding in two hours that this road does not go through is one of the highest-return outcomes a Field MVP can have. You spent two hours saving the company three months and a team. A readout that dares to write "stop" is where the business side begins to trust you (Chapter 5 unfolds the Trust Equation). Stopping inside a company has one more layer of difficulty. You cannot leave, and tomorrow you will see the person who made the ask on the same floor. The judgment to stop leaves a decision trail too. It cannot live only in the readout. It goes into the kill register to be settled, with a column each for project, requester, reason for stopping, and revival conditions (Chapter 25). Write the revival conditions clearly and "not doing it" becomes "not doing it now." The other side gets an exit, and you need not hide the judgment.

**5. Turning the process into a paper discussion when inputs cannot be had.** The data does not clear, the user cannot be booked, so the process becomes a "let's talk through the requirements first" meeting. No case table, no queue, nobody scoring. The meeting is lively, and when it breaks up you still hold only those two sentences. The fallbacks in the four-inputs section, hand-copying at the screen, synthetic cases, writing "no access to real users" into the readout, each of them preserves the scoring step. A paper discussion preserves none. The test is whether, when the clock runs out, there is a table a real user has marked line by line. If not, it was a paper discussion.

## Next Monday

The four are in order. Each is the input to the next.

1. Start from the vaguest AI ask on your desk and write one workflow claim, saying whose next action this system will change, and which one. If you cannot write it, you need to find the "who" first.
2. Confirm your scorer is a real user, not the user's boss. Set the red line at this step too, and send it to the risk owner for confirmation before the clock starts.
3. Find 5 to 10 de-identified real cases (tickets, emails, spreadsheet rows) and run the two-hour process once. Use the Field MVP Pack template in [Template 0](../appendices/template-00-field-mvp-pack.md).
4. Whatever the result, write the readout memo, including the conclusion you are afraid to write.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 0 Next Monday actions. First read
templates/field-mvp/README.md and copy the four templates workflow-claim.md, case-table.md, scoring-table.md, and
readout-memo.md into the working directory I name. Then, in the role set out in templates/field-mvp/prompt-workflow-claim.md,
guide me from the de-identified requirements conversation I paste to you toward workflow claim candidates. I run the candidates
through the template's three self-checks myself, do not choose for me. Once I give you the claim and de-identified samples, draft
a case table per prompt-case-table.md, marking every place you are unsure, and wait for me to check line by line. The scorer, the
red line, and the readout memo's conclusion are mine to write, do not make them up for me. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The Field MVP two-hour process (four inputs, six steps, five deliverables); the pass / concern / unsafe / useless four-grade scoring scale
- **Templates.** [Template 0](../appendices/template-00-field-mvp-pack.md) Field MVP Pack, with Workflow Claim, Case Table, Action Queue prototype, Scoring Sheet, and Readout Memo, ready to reuse and modify
- **Key judgments**
  - "Let the disagreement blow up at hour 48, not on day 90."
  - "AI does the grunt work. People make the calls."
  - "If you cannot write the workflow claim, you are building decoration."
