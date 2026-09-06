# 13 · The Trade-off Story: Win the Decision on One Page

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-19-memo-suite.md) (ADR Memo, 19.2, borrowed from the Chapter 19 memo set) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The plan sounds airtight to an engineer, and the executive hears it out and commits to nothing. Making it clear is not enough. You need the decision.
>
> **What You Will Be Able to Do.** Use the one-page ADR memo structure to write a technical decision as text an executive can responsibly decide on in 10 minutes, including presenting "this system will make mistakes" honestly without setting off panic.

---

## Forty Pages Against Ten Minutes

Friday evening of week 8. The security review confirmation meeting has just broken up, and Victor Reyes has co-signed the security review packet (Chapter 12). Eight weeks of work is all in hand. The reconciliation report, the eval spec, the constraint matrix, the architecture plan, stacked up, exactly 40 pages.

Now you need Grant Whitmore to approve three things. The development effort for the merged data view (Chapter 9's decision has to turn into code), confirmation that Linda's team's 2 hours a week keeps running through the pilot period (an existing charter clause, through one month after launch), and the pilot's scope and start. His assistant has given you 10 minutes at next Monday's weekly.

40 pages against 10 minutes, and most engineers solve that division by compressing. Pick the highlights, talk faster, build a 20-page deck. Compression is the wrong solution. The problem is not volume, it is order. The 40 pages are written in the order you reached your conclusion, current state, reconciliation, pattern selection, review, conclusion. Grant reads in the order he makes a decision, conclusion, cost, risk, what he has to do. The two orders are naturally opposite. This chapter teaches you to write one more page, a page whose order is completely reversed, and the 40 pages need not get any thinner.

## Why This Is Hard: Executives Are Not Short of Information, They Are Short of a Structure They Can Decide On

An engineer's default narrative is a chain of reasoning. Because A, therefore B, therefore C, conclusion at the end. That is professional instinct, not a bad habit. In the engineering world a conclusion's legitimacy comes from the derivation, and skipping a step is cheating. But an executive's day is dozens of decisions in a queue, and what he allots each one is a front-loaded stretch of attention that can be interrupted at any moment. Put the conclusion on page 38 and you have spent his most expensive first four minutes on setup.

The other half of the reason is in the decision itself. To call it, an executive has to be able to answer for it, and "the plan is correct" is only the starting point. When something goes wrong he has to answer "what did we know then, what did we give up, what was the backstop." So a text he can decide on has to align four things inside 10 minutes, the conclusion, the cost, the risk, and what he has to do. Miss one of the four and his rational choice is to commit to nothing. He is not rejecting you. He just cannot answer for it yet.

Get the narrative structure wrong and even a correct plan wins no decision. The common shape of an enterprise AI project "lost to politics" is a successful demo and a failed narrative. The system runs, the investment never arrives, and it slowly starves.

## Prior Art: The Pyramid and the One-Pager

Barbara Minto's *The Pyramid Principle* is where this chapter's skeleton comes from, and four of its rules are usable as they stand. The first two govern the opening. Answer first. The apex is the judgment you want to convey, so lead with the conclusion and give the pillars after. Open with SCQA, the shortest road from "what we agree on" to "what you have to decide." The four letters are Situation (a fact both sides agree on), Complication (the change that threatens that agreement), Question (the question that rises in the reader's mind as a result), and Answer (your conclusion).

The last two govern the body of the pyramid. MECE pillars, reasons that do not overlap and together exhaust the ground. And the one most easily forgotten, the whole structure is driven by the reader's question. At each level write what he will ask when he reaches it, not what you want to say.

The one-page rule comes from Amazon's narrative memo tradition (recorded in *Working Backwards*). Slides are banned for important decisions, and a memo written in full sentences is read silently at the start of the meeting. The reasoning has two sides. Full sentences cannot hide the parts you have not thought through. "One page" forces the author to finish the trade-off himself instead of passing its cost to the reader.

The AI era changed two things. First, the cost of writing collapsed. AI generates a well-formatted SCQA draft in seconds, and "no time to write one page" stops being an excuse. But the apex of the pyramid, what you want him to decide, AI cannot think out for you. The inputs it would need (this reader's question at this moment, the organization's power structure, the judgment you are willing to stake) are in no document. AI can lay the body of the pyramid fast, and the apex is still yours to place. Second, the trade-off story for an AI project carries a new difficulty. You have to present "this system will make mistakes" honestly to a non-technical executive without setting off panic. Say it in Chapter 11's vocabulary. Do not promise "no mistakes." Talk instead about error categories, per-category thresholds, and the human review backstop path. Panic comes from "nobody handles it when it goes wrong," and "it will make mistakes" frightens nobody on its own. Make the backstop clear and honesty turns into a sedative.

## The Core Framework: The One-Page ADR Memo Structure

> **The architecture decision memo (ADR memo). One page presenting one pending decision to the person with the authority to call it. Conclusion, evidence, the cost said out loud, risk and backstop, and what he has to do. Its purpose is to let him call it responsibly, and understanding the plan is only something picked up along the way.**

| Section | What Goes In It | Rules |
|----|--------|------|
| **SCQA opening** | S, the agreed fact / C, the threat or change / Q, the reader's question | Three lines and done; Q must be his question, not yours |
| **The conclusion in one sentence** | The decision to be called, in one sentence | The pyramid apex test. If you cannot say it in one sentence, do not start writing |
| **Three pillars** | Three reasons that hold up the conclusion, each with one line of evidence | MECE (no overlap, exhaustive together); evidence is numbers and signatures, not adjectives |
| **The trade-off said out loud** | What was given up, what it bought, and where the thing given up now sits | The soul of the memo, unpacked below |
| **Risk and backstop** | What errors will occur, how they get found, who backstops them, when to call a stop | Error categories + per-category thresholds + review path, not an apology |
| **The three things I need from you** | Concrete actions, each with a date | Without this section = asking for understanding, not asking for a decision |

ADR is taken from architecture decision record, which is the architecture decision memo in the sentence above. The S / C / Q in the table are structure names. You do not have to copy them into the text, and in the letter below they land as three lines, "background," "but," and "so the question to answer." The conclusion line works the same way. One sentence can be followed by an arithmetic note in parentheses, the arithmetic is a footnote, and the conclusion is still one sentence.

The trade-off section is the soul of the memo, because it is the only section that works against you, and therefore the only one that proves the rest of them credible. An executive's professional nose is trained on cost. Leave it out and he will guess, and a guessed cost is always worse than the real one. There is one writing rule and no exemption from it. The cost has to be written by you, and it cannot be left for the reader to discover. In the Trust Equation (Chapter 5) credibility is a multiplying term in the numerator, and the reader discovering it for you once takes it to zero. Multiplication means that once credibility is punctured, every other score goes to zero with it, not to a discount. After that every "conclusion" of yours gets audited layer by layer, the one-page privilege is withdrawn, and from then on you are only fit to write 40 pages. Once a hidden cost is exposed, you permanently lose the right to lead with the conclusion.

Where does the material come from? You do not have to invent it now.

- The C in SCQA, the Field MVP's scoring data (Chapter 0).
- Pillar evidence, the reconciliation report and the eval baseline (Chapters 9 and 11).
- The trade-off section, a transcription of the scope decision log (Chapter 8).
- The risk section, the error taxonomy plus the human oversight design (Chapters 11 and 12).

The one page needs no new writing. Take the hardest single line out of each of eight weeks of work and that is enough.

## At Anchor & Helm: That One Page

Sent on Friday evening of week 8. Here it is in full.

---

> **To Grant Whitmore, from [you], Friday of week 8**
> **Subject. The exceptions queue pilot decision, three things for your call on Monday**
> *One page of body text. The 40-page technical plan (reconciliation report / eval spec / security review packet) is attached for reference.*
>
> **Background.** The auto exceptions queue project is eight weeks in. Data reconciliation is complete, the eval baseline was co-built with Linda's team, and the security review passed this week (co-signed by Victor Reyes).
> **But**, the earliest MVP scoring gave a warning. Of 10 suggestions, 3 were unsafe, and all three traced back to "chase priority ≠ risk priority." The reconciliation showed more, 44% of the core system's status field cannot be taken at face value to drive an action. Scaling up the investment without controlling scope means mass-producing the wrong priorities.
> **So the question to answer**, do we start the pilot now, and at what scope.
>
> **Conclusion. I recommend approving an 8-week controlled pilot, scoped to auto exception claims and the eight people on Linda's review team, to validate the North Star "first-touch handling time, down 30%."** (The arithmetic behind -30% is in the charter. Across ten cases, about six tenths of the waiting time goes to "waiting on documents with nobody chasing and nobody claiming them," and the queue eats half of that. That is where -30% comes from, and it pulls a payment cycle running 1.6 times the industry average back near the average.)
>
> **Three pillars**
> 1. **Users have validated it**, with the front line scoring 5/10 pass. The 3 unsafe marks have become a zero-tolerance error category in the eval, and 50 golden cases were co-built with Linda's team.
> 2. **Data has been reconciled**, 200 records three ways, 44% of statuses distorted (the largest single class, the lagging pattern, about three in ten). The fix is the merged view. Claim status takes the merged view as its source of truth (the review team's Excel is the authority, the core system the fallback), amounts take the core system as source of truth, purely derived and read-only (it needs development effort, see item 2 below).
> 3. **Risk has been defended**, with every suggestion carrying its reason, a Human Call column, an end-to-end decision trail, and the reviewer's co-signature.
>
> **What we gave up.** To buy a pilot that can be validated inside 8 weeks, this phase explicitly gives up two things.
> - **The home property extension**, on the revival list, with the condition "the first extension after the pilot North Star hits target" (exclusive). It is first in line, and only time is missing.
> - **Full automation.** On the decision rights ladder, AI stops at the advise layer.
>
> The decision rights ladder, four layers from the top down.
>
> - **Decide**, pay or not, how much. This is a red line, never touched.
> - **Act**, send chase notices, assign, change status. Humans take over here.
> - **Advise**, priority, next step, reason. AI stops here (this phase).
> - **Sense**, gather documents, dwell time, risk signals. AI does this.
>
> Each layer up needs that layer's evidence. The advise layer's acceptance record starts accumulating with the pilot, and once it hits target we move up one layer at a time, each layer decided on its own.
>
> **Risk and backstop.** This system will make mistakes. We do not promise "no mistakes," we promise "when it is wrong, it can be found and it can be caught." Thresholds are set per error category. Missed risk is zero tolerance, and if a single one appears during the pilot, that whole category of suggestions is downgraded to human review, with suspected missed-risk cases reviewed weekly. The "empty suggestion" class (harmless but useless) is watched on trend only and must not rise. Every suggestion takes effect only after a reviewer confirms it, and overrides leave a trail. When the business side's promised input goes unmet two weeks running, the three tiers of resource reassessment are triggered (the three-tier handling already set in the charter, Chapter 4). When two consecutive evaluation cycles miss the threshold and no workable path to improvement exists, either side may propose termination (Chapter 4), and the call is yours.
>
> **The three things I need from you**
> 1. **At Monday's weekly (Monday of week 9)**, call the pilot's scope and start (auto exception claims, 8 weeks).
> 2. **By Wednesday**, approve the development effort for the merged view. Two people from the Digital Center and two from claims-ops IT, six weeks. The early part of the pilot runs on the existing read-only view, replaced as soon as the merged view is built.
> 3. **By Friday**, confirm with Kevin Doyle that Linda's team's 2 hours a week (an existing charter clause, through one month after launch) keeps running during the pilot, and that the schedule protection stays.

---

The six-section structure does not change. The center of gravity does. What an internal executive calls is rarely "do we approve this money," because the money already has a line in the annual budget. He calls whether you get people, where you rank, and who owns it after launch. So the last section of the internal version leads with people, priority and owner, not with budget. Rewrite the last section of that letter around the internal center of gravity and the three things grow into this.

1. **At Monday's weekly**, call the pilot's scope and start, and confirm that the owner of this queue after launch is Kevin Doyle.
2. **By Wednesday**, approve the people for the merged view build, two from the Digital Center and two from claims-ops IT, six weeks, and ask Owen Hartley to write those four people's schedule protection into this quarter's plan.
3. **By Friday**, ask Kevin Doyle to write Linda's team's 2 hours a week into the review team's schedule sheet and copy Grant Whitmore.

The extra half-sentence in item 1 is the watershed of the internal version. Who owns it after launch, meaning who runs this queue day to day, is not a risk owner like Victor Reyes. In a delivery with a deadline, ownership gets written on a different piece of paper, and you do not have that piece of paper. Leave it off this page and there will be no second occasion to write it, and a year later the alert at midnight rings on your phone by default (Chapter 22). The owner has to be a named person. Writing "Claims Operations" does not count.

Item 3 looks like the smallest, and it is the only execution guarantee on the whole page. Approval is not the same as happening. After Grant nods, those 2 hours still sit in the review team's own queue, and you hold no written commitment you can chase with. So inside a company every approved item has to be followed by a verifiable landing action, who, by which day, writes it into which sheet, and copies whom. The 2 hours written into the schedule sheet are the real 2 hours, and the 2 hours nodded at in a meeting are not. The copy line especially cannot be skipped. It turns "not done" from a private matter into something Grant can see too, and inside a company visibility is the only place enforcement starts.

**Monday morning, the 10 minutes.** You put the one page in front of Grant Whitmore, with the 40-page attachment beside it. For the first two minutes he reads silently and you say nothing. In the third minute you start walking the pillars, and partway through the second one, in minute 4, he raises a hand and stops you, his finger on the ladder in the trade-off section. "Home property first in line for Kevin, exclusive, I accept that. One question. Going from the advise layer up to the act layer, who decides, and on what?"

"On the acceptance record. During the pilot, every suggestion accepted as is or overridden leaves a trail. Whichever class of action gets its acceptance rate over the line, the data goes on your desk, each layer decided on its own, and the person who calls it is you."

He nods and drops the page on the table. "All three approved." Then he pats the stack of 40 pages beside it and pushes it back to you. "Keep that for Victor Reyes and Kevin Doyle's people. One more thing before we break up. Everything you send me from now on gets written the way this page is written."

A 10-minute meeting ran 7 minutes. Not one of the 40 pages was turned, and it held up every line of the one page. Because the reconciliation report exists, pillar two dares to be one line. Because the review packet exists, "risk has been defended" can stand. You could answer Grant's question in 5 seconds because the answer went into the scope decision log back in Chapter 8. The point of a 40-page plan is to let one page dare to be that short. The one page is the interest on the 40, not its summary. Meaning, without those 40 pages behind it, nobody would believe this one.

**Round two, after the meeting.** In the corridor, Grant's assistant catches up with you. The board meeting has moved up from the end of the month to next Thursday, and Grant wants the meeting to "open the system and walk through a few live claims." That is the sponsor's support, and it is also the sponsor's pressure, the kind that comes in the name of support.

In week 1 he told the board "there will be something to see in three months." Now the board has moved up, and the chip he has to pay with is the prototype in your hands, the one that changes every day and that Linda's team is still trying out informally. Demoing it live on real data means taking a thing built to change at any moment, holding it to a "does not make mistakes" standard, and staking it on the highest table in the company (Chapter 14 covers this, the prototype's game is learning speed, not performance reliability).

You do not say "no." Pushing a sponsor's request back spends trust, and taking it whole is betting your life on it. You give him something he can call, written the way this one page is written. Conclusion, the board demo becomes a three-minute screen recording, plus that scoring sheet and the decision rights ladder drawing. The cost, it does not hit as hard as clicking through live. What it buys, zero risk of the demo blowing up, and a harder story. The board sees the 3 unsafe marks a front-line reviewer made by hand and how each of them was blocked, and no demo on the market has that page.

The assistant comes back on Tuesday. Grant chose the recording, and added one line, "put a shot of Linda's handwritten scoring sheet in it." The pressure did not disappear. It was translated into a trade-off he could call responsibly.

This page often goes to more than one person. Grant can call it alone because both the people and the data sit under his line. On another project the business department supplies the people while the capacity being consumed is your team's, and the two signing points are peers. Your manager Owen Hartley asks "how many of our people for how many weeks." The business-side head asks "how many people do I put in, and will it wreck my schedule this quarter." The two questions have different answers, and writing two pages is the wrong solution, because when each of them holds a page of his own, both assume the other one is covering it.

One page stays one page. The first five sections are shared, since conclusion, cost and risk are the same thing for both readers, and only the last section splits. "What I need from you" runs in two columns, each signed, each dated. Splitting it into two columns has a side effect. Both of them can see the other's column, and whoever fails to deliver fails in front of the other one.

Three more things a team from outside does not have and you already hold. Turn all three into actions.

- **Borrow a shell.** You can pull up project approval memos this company has already approved. Write to their section names, their length and their copy line. The reader recognizes the shape, so all of his attention goes to the content.
- **Pre-read.** Before sending it, get Grant's assistant or your counterpart on the last project to read it for four minutes, then ask him what the decision is, what the cost is, and what happens when it goes wrong. Anything he cannot answer, rewrite that section. You can do this any time. A team from outside would have to spend another company's time to get it done.
- **The apex.** You know what this executive cared about most the last time he called a decision. What the board presses Grant on is the payment cycle, so the conclusion sentence lands on first-touch handling time, not on accuracy. AI can lay the body of the pyramid fast, the apex is yours to place, and you know better than an outsider where it belongs.

## Failure Modes

**1. Benefits only, and credit collapses the moment the trade-off is found.** The memo is all upside, and the cost shows up as a "supplementary note" only when someone presses. The cause is double. Fear of reporting bad news (worry that it scares the decision away), plus mistaking a memo for sales copy. Sales can talk only about benefits, because the buyer discounts by default. A decision maker does not discount, he answers for it at face value. And the cost cannot be hidden, because the professional nose of anyone who approves an investment is trained on cost. The test, the trade-off section has to contain at least one sentence that hurt to write. Not one, and you are still selling.

**2. Asking for understanding, not a decision.** The memo's logic is perfect, the executive reads it, nods, says "very clear," and then nothing happens. Engineers treat "explained it clearly" as the finish line of delivery, but understanding produces no behavior, only a dated request does. Underneath there is self-protection. A clear ask can be refused, and a vague report is always safe. But dodging the risk of refusal also dodges the chance of getting a commitment. A memo with no "what I need from you" changes nothing once it is read. The executive's nod is for you, not for the project.

**3. One page written as ten.** "It is all important, none of it can go," the body swells to ten pages, and it gets called thorough. Every detail is the author's sunk cost and every cut hurts, so the cost of the trade-off passes to the reader untouched, and the reader's solution is harsher than yours. He does not read it. One rule. The attachment can be any thickness, and a body over one page means you have not thought it through. Going over is a diagnostic signal. It says you have not found the pyramid's apex yet and still do not know what you want him to decide. Go back to the one-sentence test, and come back to write once you have it.

## Next Monday

1. Run the pyramid apex test on the project on your desk. Who you want, and what you want him to decide, written in one sentence. If you cannot write it, do not start writing. What you want may be understanding, not a decision.
2. Pick a plan of yours from recently that runs over five pages and rewrite it with the one-page structure of [Template 19](../appendices/template-19-memo-suite.md). The trade-off section must name at least two things you gave up and their revival conditions (Chapter 8's scope decision log is ready-made material). The same structure keeps coming back after the pilot starts, authorization at the open, a decision at the midpoint, renewed funding at the close, and Chapter 19 expands it into the three-memo system. Beyond those three there is a fourth kind, and it is not the same as renewed funding at the close. It handles the fact that a year after launch no bill reminds anyone that this system still needs investment, and by then one page is your only tool for winning resources back on a regular basis.
3. Dig out the last email you sent an executive and check whether it has "what I need from you + a date." If not, send a follow-up that is only that section, and watch what happens.
4. Run the four-minute test with a colleague who does not know the project. The number comes from Grant Whitmore, who raised a hand in minute 4. Give him only the one page, and after 4 minutes ask him "what is the decision, what is the cost, what happens when it goes wrong." Any question he cannot answer, rewrite that section.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 13 Next Monday actions. I will give you one sentence first, who I want and what I want him to decide.
If I cannot write it, stop and do not write it for me. Then I will paste you my recent plan that runs over five pages. Follow templates/memo-suite/prompt-memo-scaffold.md
and the one-page structure of Template 19.2 to rewrite it into a draft. The trade-off section must list at least two things given up and the revival condition for each.
Anything not in the original plan you mark [TBD] instead of inventing. The closing "what I need from you + a date" is mine to fill in. When you are done, report the draft's word count to me.
If it runs over one page, delete what you added first. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The one-page ADR memo structure (three lines of SCQA → the conclusion in one sentence → three pillars with one line of evidence each → the trade-off said out loud → risk and backstop → the three things I need from you, with dates); the pyramid apex test; how to put an error distribution to an executive (error categories + per-category thresholds + human review backstop); the four-minute test
- **Templates.** [Template 19](../appendices/template-19-memo-suite.md), Three-Memo Set (with ADR), the ADR part (19.2), memo template plus SCQA writing self-check list
- **Key judgments**
  - "Executives are not short of information. They are short of a structure they can decide on."
  - "The point of a 40-page plan is to let one page dare to be that short."
  - "A memo with no 'what I need from you' changes nothing once it is read."
  - "Once a hidden cost is exposed, you permanently lose the right to lead with the conclusion."
