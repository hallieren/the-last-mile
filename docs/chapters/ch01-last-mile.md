# 1 · The Last Mile Problem: Why Enterprise AI Dies After the Demo

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-04-deployment-charter.md) (Pre-mortem Memo, 4.3 to 4.6) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The demo was a hit, and the applause was real. Three months later nobody uses the system. You want to know what killed it, and more, how not to die next time.
>
> **What You Will Be Able to Do.** Diagnose how far any AI project is from production with the five gaps. Run a pre-mortem at kickoff and write the causes of death up front. Redefine "how far this project has to get before it counts" with the outcome ladder.

---

## A Parallel Universe: If Anchor & Helm Had Taken the Second Road

In Chapter 0 you built a Field MVP in two hours. Now rewind and watch the you in another universe, the one who took the second road and went straight to a demo. That road is worth walking end to end. It is what is happening in companies everywhere right now, and every step feels right.

**Weeks 1 to 6.** You and two engineers build a claims knowledge chatbot. RAG (retrieval-augmented generation, the model looks things up before answering) is wired to the claims manual and the policy library. Clean interface, fluent answers. On demo day the room is full. Grant Whitmore asks it for "the deductible clause for storm damage to a vehicle," and it answers fast and right. Applause. Grant says, "Better than I expected. What is next?"

This is the project's peak. It will never be better than this moment.

**Weeks 7 to 10.** Going live means real data. Victor Reyes (Head of IT Security and Architecture) appears in a meeting for the first time and asks three questions. Does customer data leave the boundary? Who audits the model's output? Who is responsible when it is wrong? Nobody can answer. The security review is scheduled six weeks out. Meanwhile, trial accounts go to the claims department. Week 1, 47 logins. Week 2, 12. Linda Marsh's team never logs in. They knew the policy terms by heart twenty years ago. What blocks them is "which claim do I touch first today," which the chatbot cannot answer. The answer is in no document. It is in the core system, the inbox, and Linda's tracker.

**Weeks 11 to 13.** The dashboard Kevin Doyle wanted is still nowhere, because the chatbot architecture holds no claim-level data. The board asks about ROI, Grant asks you for a number, and all you have is "92% answer accuracy." Nobody can turn that into money. The quarterly report calls the project "phase one of the AI transformation, successfully completed," and archives it. The engineers are reassigned. Three months later, nobody remembers the login URL.

What is cruel about this ending? Not one meeting failed, and nobody called a stop. The demo succeeded, the review was normal process, the drop in trial usage was "users need time to build the habit," and the archive note said "successfully completed." Enterprise AI projects are rarely shot. They die of comfort.

## Why This Is Hard: The Last Mile Is a Structural Distance

From demo to production, the engineer's instinct is to push harder. Tune the prompt, raise the accuracy, add a permissions module. That instinct is wrong. Five structural gaps separate a demo from a production system, and none can be crossed by "slightly better technology."

| Gap | Demo World | Production World | Where the Anchor & Helm Chatbot Died |
|---|---|---|---|
| **Data gap** | Hand-picked clean data | Real systems that lag, have holes, and disagree on meaning | Answers in the core system, the inbox, and Excel, not the policy library |
| **Workflow gap** | Users adapt to the demo | The system embeds in what users already do | Linda's next action never changed |
| **Trust gap** | The audience wants to be impressed | Users fear being held responsible | Who is responsible when it is wrong? No answer |
| **Ownership gap** | You present, you are responsible | After launch there must be an owner | Nobody answered the three security questions |
| **Value gap** | "It works well" is enough | Must convert into a reportable business number | 92% accuracy did not convert into money |

The five gaps share one property. At the demo stage, all are invisible. A demo is, by definition, the five gaps papered over for an audience. So no inference runs from "the demo went well" to "this can go to production." The former never tested the latter.

"The last mile" names this distance. It is a different road, walked by different rules, and its length is unrelated to the road before it. The first leg is a contest of capability (model, architecture, engineering). The second is a contest of structure (data truth, workflow embedding, trust, ownership, the value story). Most teams lose by running the second leg with the first leg's playbook.

## Prior Art: This Pit Had a Name Fifty Years Ago

Consulting calls this **"the report that dies on the shelf."** Peter Block's diagnosis in *Flawless Consulting* still holds word for word. The client receives the deliverable politely and never uses it. The root cause is that the client never truly committed, nobody inside owns the change, and no deliverable quality can save it.

Consulting developed three remedies. Contracting (the entry conversation that sets terms of engagement), turning the client into a co-builder, and designing implementation (getting it to land) as its own stage. These three are the skeleton of Chapters 4 to 7 and 19 to 22.

Enterprise software calls it **shelfware**, software bought and never used. The SaaS era built a whole profession (Customer Success) just for adoption. Selling the software is only the start. Getting it used is what counts.

In change management, Kotter makes one point over and over in *Leading Change*. Change mostly fails because people underestimate how hard it is to get others to work differently, far less often because the strategy was wrong. Putting an AI system live is, at bottom, asking a group of people to work differently. That has always been the hardest part. You need not memorize these remedies now. Just know that this pit is not unique to AI.

What did the AI era change? The cost of a demo collapsed, and that set off demo inflation. A respectable enterprise software demo used to take months, so the demo itself was a filter. A team that could build one had real engineering capability. Today a stunning AI demo takes an afternoon. The demo has lost its signal value, and the organization's decision process has not caught up. It still treats "the demo was stunning" as evidence of "worth investing in." So the number of projects entering the last mile has exploded, and the last mile itself is not an inch shorter. That is the structural reason enterprise AI projects die en masse in pilot (real users, real use, inside a controlled scope).

Someone has to stake a professional identity on the last mile. The product engineer's achievement is "shipped." The salesperson's is "signed." The deliverer's achievement settles only one way. Vendors call this person the FDE (forward deployed engineer, the delivery engineer sent on site). Inside a company the person may be called an AI engineer, a digital specialist, or nothing in particular, just whoever got told "you go make it land." This book is written for the latter. Where the method comes from is Chapter 2.

> **The deliverer's unit of value is the production outcome, not the demo.**

The concrete scale is what this book calls the **outcome ladder**.

| Level | Name | What Reaching It Means |
|---|---|---|
| L0 | demo | Demo succeeded. The applause is here |
| L1 | pilot | Real users, real data, in use inside a controlled scope |
| L2 | production | In production, with an owner, monitoring, and rollback |
| L3 | adopted | Users' daily actions have actually changed. Taking it away would hurt |
| L4 | self-sufficient | The business side can run, maintain, and improve it on its own |

The deliverer's achievement is settled only at L3/L4.

Grant's applause was at L0. The Anchor & Helm chatbot died between L0 and L1. And each part of this book is one climb up this ladder. The two rulers measure different things. The five gaps cut across and ask which are still open now. The ladder runs upward and asks which rung you have reached. Close the gaps one by one, and your position moves up.

The five gaps do not care who employs you. This book is written for the in-house scenario. You cross departments to land AI in the business side's daily work, the business side is your counterparty, and budget and salary come out of the same finance system. If you are a vendor-side FDE, the same mechanisms sit on the table in plain view, the contract, the price tag, the exit date. How to read them from that seat is in the [Vendor Crosswalk](../appendices/internal-fde-mapping.md).

## At Anchor & Helm: Write the Cause of Death at the Start of the Project

Back to the real universe. After the Field MVP readout, you owe Grant a first formal memo. Most people would write "what we do next." You write something else, a **pre-mortem** (a post-mortem done in advance, from decision psychologist Gary Klein). Assume the project is dead and work backward to how it died.

Your memo lists five causes of death, each matched to one gap and one defense. Discovery in the first item is the stage of finding out how things actually are. The charter in the last item is the entry contract, what contracting produces. The North Star is the charter's only outcome metric, the one number the whole project recognizes.

> **The Five Most Likely Ways This Project Dies**
> 1. The core system's "claim status" field cannot be trusted, and the queue's suggestions rest on wrong statuses. The defense is data reconciliation during discovery (data gap).
> 2. The system asks reviewers to change their order of work, yet never enters the screen they open every day. The defense is to embed in the existing entry point, not open a new system (workflow gap).
> 3. One wrong suggestion gets followed, a customer complains, and from then on the front line trusts no suggestion. The defense is a reason column beside the Human Call column, and a weekly review of unsafe cases (trust gap).
> 4. The security review does not start until week 10 and blocks the launch. The defense is Victor joining the project team in week 2 (ownership gap).
> 5. Three months in, nobody can say what was saved. The defense is to lock "first-touch handling time for auto exceptions" into the charter as the only North Star (value gap).

The memo had an effect at Anchor & Helm nobody expected. Victor read it and asked to meet you. He had never seen a system builder write "the security review will block the project" on paper at the start. The blocker (the person in the way) became an ally, starting from this page (Chapter 12 continues the thread).

The pre-mortem's value is turning the five gaps from "a shock at launch" into "work items at kickoff." Whether the predictions come true is secondary. The last mile is no shorter, but you are walking it from day one.

## Failure Modes

**1. Celebrating the demo as a milestone.** The demo succeeds, so there is a party, an all-hands email, a product roadmap. This treats L0 as the ladder's midpoint, when it is the warm-up before the start. Move the celebration to the first time a real user depends on it to get work done. That is the first signal of L3, and worth celebrating.

**2. Using demo praise as requirements validation.** "Demo feedback was very positive" goes into the requirements document. Audiences and users are two different species. Audiences consume amazement, users consume reliability. All demo praise validates is "this concept can be understood." There is only one way to validate requirements. Real users, real cases, and scoring that forces a position (Chapter 0).

**3. Treating launch as the finish line.** L2 is reached, the team disbands, operations are "handed to IT." Project approval and performance reviews both stop at "launched." But the ladder shows a whole stretch between L2 and L3 (Chapters 19 to 22), and most deaths happen there. Launched and unused looks worse than never launched.

**4. Substituting activity metrics for outcome metrics.** The report says "trained the model, connected the data, ran the training sessions, 92% accuracy." Activity metrics look good and are always positive. Outcome metrics (handling time, leakage rate, which is overpayments and wrong payments as a share of total paid) lag and can get worse, but only they survive the boardroom. The test is simple. When the North Star gets worse, does anyone hurt? A metric nobody hurts over cannot be the North Star.

## Next Monday

Before scoring, settle what counts as evidence. Each gap's "current evidence" is something that already happened, not an intention. Data gap, you checked the real system's fields once and know which cannot be taken at face value. Workflow gap, you sat beside a user and watched how she works today, and can say which step the system embeds in. Trust gap, real users scored outputs one by one, and someone owns the unsafe cases. Ownership gap, the person taking over after launch has a name, and the person doing the security review has already sat in a meeting. Value gap, a business number was written down before the demo, and someone has claimed the consequences of it getting worse.

For what counts as passing, borrow the four grades from Chapter 0. They originally rated a single output. Here they rate evidence, same scale, different object. You can write down such an event, pass. Half done, say the fields were checked but the source of truth (which data everyone actually believes) is not decided, concern. What is written is not wrong but does not show the gap is closed, say answer accuracy offered as value evidence, useless. There are already signs it will blow up at launch, say a security review six weeks out, unsafe, and that is your cause-of-death candidate.

1. Pick an AI project you are working on (or just demoed), score it on the five-gap table, and write one line of "current evidence" per gap. A gap with no evidence you can write is a cause-of-death candidate.
2. Mark its place on the outcome ladder. If it is at L0 and the next planned step is "improve the results," be alarmed. You are running the second leg with the first leg's playbook.
3. Run a 15-minute pre-mortem. Assume it died six months from now, and write the three most likely ways to die and the defense for each (see [Template 4](../appendices/template-04-deployment-charter.md)).
4. Send the pre-mortem to your sponsor (the executive who funds it and makes the call). Watch who it draws in. That person is often a key stakeholder (a party with a stake in the outcome) you had not identified.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 1 Next Monday actions. First build a
five-gap scoring table, five rows for data, workflow, trust, ownership, and value, each with a "current evidence" column
and a "grade" column. Grades may only be pass / concern / unsafe / useless. I will dictate the evidence line by line.
Only record it, do not fill in for me. Then run a 15-minute pre-mortem in the role set out in
templates/premortem/prompt-premortem.md, walking me backward through three ways to die and their defenses, with follow-up
questions that force concrete scenarios. Finally, write up a draft in the format of premortem-template.md, marking any
defense or owner I did not give as [TBD]. Who receives it is my decision.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The five-gap diagnostic table (data / workflow / trust / ownership / value); the outcome ladder (L0 demo → L4 self-sufficient)
- **Templates.** The Pre-mortem Memo in [Template 4](../appendices/template-04-deployment-charter.md) (4.3 to 4.6), five ways to die with a defense for each, written at project kickoff
- **Key judgments**
  - "Enterprise AI projects are rarely shot. They die of comfort."
  - "A demo is, by definition, the five gaps papered over for an audience."
  - "The deliverer's unit of value is the production outcome, not the demo; achievement is settled only at L3/L4."
