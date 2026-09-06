# 8 · From Use Case to Boundary: Cut the First Thin Slice

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-08-thin-slice.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The use case is chosen, the charter is signed, and the next day the scope starts to swell. Each extension proposal is reasonable on its own. Accept all three and the project dies. And your "no," when you say it, sounds like laziness.
>
> **What You Will Be Able to Do.** Cut a use case into one thin slice with the Five Ones. Draw the decision rights boundary for an AI system. Use the scope decision log to turn every "no" into "not now," so the proposer leaves with an answer instead of a grudge.

---

> **Part III Navigation.** Chapters 8 to 13 all sit between the charter signature and the pilot launch, weeks 4 to 9.
> Three scope proposals within 24 hours of signing (week 4, this chapter) → three-way reconciliation (week 6, Chapter 9) → the multi-agent proposal at Monday's standup (week 7 Monday, Chapter 10) → the annotation session and item 37 (weeks 7 to 8, Chapter 11) → the security review meeting (week 8, Chapter 12) → that one page and Monday's 7 minutes (week 8 Friday to week 9 Monday, Chapter 13)

## The Twenty-Four Hours After the Signatures

The exceptions queue won the five-question elimination (Chapter 7), and the charter was signed in week 4, after the readout (Chapter 4). The signing itself is low-key. Grant Whitmore, Kevin Doyle, you, Owen Hartley, one page, four signatures, ten minutes start to finish.

The creep starts at minute eleven.

Putting his pen away, Grant asks, "Now that it is signed, one more question. Once this thing runs smoothly, can it go toward full automation? From claim report to payout, fully automatic. The board will ask me that next year, guaranteed."

That evening Kevin calls. "The home property team lead came to see me this afternoon. They are all exceptions, and you are building the queue anyway. Put the home property ones in too, right? Just one more class of data, isn't it?"

At the next morning's standup, the two claims-ops IT engineers bring a one-page architecture sketch. "Rather than hard-coding the exceptions logic, build the bottom layer as a general-purpose workflow platform. Fields, rules, lines of business, all configurable. Customer service and underwriting can use it later. One investment, the whole company benefits."

Twenty-four hours, three proposals. Notice that none of them is wrong. Home property really is backed up, full automation really is where the industry ends up, a platform really does avoid building the same thing twice. Nor is anyone proposing them an enemy. This is exactly the evidence that the project is finally being taken seriously. But accept all three and the user groups, the decision layers (which layers, the ladder diagram below will show), and the number of scenarios all grow at once, and the "-30%" North Star loses any attribution. Three months later you will own something that touches a bit of everything and has launched nothing.

You do hold a charter, and its "Scope and Red Lines" section is there in black and white. It cannot stop these proposals. A charter is a snapshot of the consensus on signing day. Creep is new traffic that grows every day. A thicker document does not help. You need a ruling procedure that runs continuously. This chapter gives you that procedure.

## Why This Is Hard: Creep Is the Default Outcome, Not a Management Failure

Blame scope creep on "the business side lacks discipline" or "I failed to hold the line" and you reach for the wrong medicine. Creep has three structural engines, none of them about character.

**First, your project is the only car moving.** Every stakeholder (a party with a stake in the outcome) has a few wishes nobody has picked up, and a wish can only ride on a car that is moving. The moment the queue is approved, it becomes the mounting point for every AI wish in the company. Nobody is targeting you. This is gravity.

**Second, the marginal cost of every proposal looks small.** "One more class of claim," "just leave a hook for it." Seen one at a time, the increments are linear. The validation cost multiplies. One more user group means another set of scoring and annotation. One more decision layer means another round of error classification and oversight design. Nobody is lying about this cost gap. It just does not show.

**Third, the cost of refusal is asymmetric.** Accept an extension and the project pays, and the bill shows up three months later. Refuse one and you personally pay on the spot, especially when the proposal comes from Grant. Without a defensible narrowing logic (a reason for refusing that can state its cost), your "no" sounds no different from passing the buck, so the rational choice is to accept.

One more fact, which most people never see through, is the key to this chapter's solution. Many extension proposals want an answer the proposer can repeat to someone else. A "yes" is secondary. Kevin has no plan to launch home property tomorrow. What he needs is a sentence he can give the home property team lead. See that, and "refusing" turns from confrontation into service.

## Prior Art: Put a Price on Every "Want," and the New Line AI Added

The methods for narrowing are not new. Two traditions each contribute half.

**The first comes from the solution architect's tradition of architecture review, making trade-offs explicit.** When an extension is proposed, do not rush to yes or no. Price it first. "We can. The cost is these three things. You decide whether it is worth it." Pricing lets the proposer see the scales for himself, and you go from "the person in the way" to "the person doing the arithmetic." This discipline was carried over from architecture review into scope negotiation. Quality attributes conflict with each other. Throughput costs latency, flexibility costs maintainability. So the product of a review is the cost written next to every "want." Whether the design is good is not really the point.

**The second comes from the Extreme Programming tradition, YAGNI.** "Leave a hook for it" sounds prudent. In practice it bets a certain cost today on a future that mostly never comes. "You Aren't Gonna Need It," the discipline Kent Beck laid down and Ron Jeffries kept explaining. Until the need actually appears, do not build for an imagined one. This has nothing to do with laziness. Imagined needs are mostly guessed wrong, and the complexity you pay for them is due now and due every day.

In the age of AI agents, one of these old disciplines got more expensive and the other is entirely new.

YAGNI is the one that got more expensive. An LLM is general-purpose by nature. The cost of demonstrating generality has collapsed, and the cost of producing it (each scenario's own data reconciliation, eval, and trust building) has not dropped a cent. Chapter 1 covered demo inflation. Demos got so cheap that being impressive no longer proves anything. This is its scope version. The temptation to abstract got cheap. The cost of abstracting did not.

### The Decision Rights Boundary

What is new is a boundary. A traditional system boundary answers one question, which functions the system does. An AI system must answer one more. Which layer of the decision chain does the AI's judgment reach, and at which layer do humans take over? This book calls it the decision rights boundary.

> **The decision rights boundary is, on a workflow's decision chain, the layer where AI output stops, the layer where humans take over, and the evidence required to move up each layer.**

Why does drawing this line wrong mean redoing everything? Because it is the foundation of the whole validation system, not one item on a feature list. How errors are classified (Chapter 11, eval), who watches and whether they can keep up (Chapter 12, human oversight), where the chain of responsibility ends when something goes wrong, all of it grows out of this line. Draw a feature boundary wrong and you cut one module. Draw this line wrong and you redraw the whole set, and the code is the least of it. So it has to be drawn when scope is defined. It cannot be left for the architecture stage to "settle along the way."

## Thin Slice, the Definition and the Five Ones

Now the book's formal definition.

> **A thin slice is the smallest working slice that cuts vertically through all five layers, "real user, real decision, real data, real risk control, measurable outcome." Thin is the width. It serves one decision for one user group. Not thin is the depth. Every layer must go all the way to "real."**

The key word is vertical. Creep proposals are all horizontal. One more class of claim widens the user surface, a platform abstracts the bottom layer into a general component. A thin slice goes the other way. Cut the width to the minimum in exchange for one complete deep channel from data source to user action to outcome measurement. The Chapter 0 readout narrowing to "auto exception claims" was the first cut. This chapter finishes it.

In practice a thin slice is five "ones," and none of them may be plural.

| The Five Ones | How Anchor & Helm filled it in | Why it must be "one" |
|--------|-----------|------------------|
| **One user group** | Linda Marsh's auto claims review team (eight people) | Two user groups = two sets of scoring, two sets of tacit knowledge (the knowledge people hold but cannot state), and no way to say whose feedback counts |
| **One decision** | The next step on each exception claim (whom to chase, what is missing, who takes it) | More than one decision and errors cannot be defined, so the eval (the evaluation set) has nowhere to start (Chapter 11) |
| **One data path** | The merged view of the core system + Excel after reconciliation | Every extra path doubles the fitness check (does the data qualify to drive actions, Chapter 9) and the reconciliation |
| **One risk boundary** | AI stops at the advise layer; payout decisions are never touched (red line) | More than one boundary and oversight and the chain of responsibility have seams, and incidents find seams |
| **One measurable outcome** | First-touch handling time for auto exceptions, -30% (the charter North Star) | More than one metric and improvement cannot be attributed, and acceptance falls back to "leadership thinks so" |

Three notes. One, the fifth "one" is cited straight from the charter North Star (Chapter 4). The thin slice is the North Star's engineering projection, not another negotiation. Two, the data path is still a paper promise at this point. "The merged view after reconciliation" is not delivered until the data fitness check in Chapter 9. For now you only need the path to be one, not three. Three, the five "ones" only qualify when they lock together into one sentence. This user group, making this decision, along this data path, inside this risk boundary, improves this metric. Wherever it does not read smoothly is where the cut is not clean.

Why the obsession with "one"? What a thin slice is after is being able to afford validation. Doing less is a by-product. The whole point of a pilot is clean evidence (the escalation decision in Chapter 14 depends on it), and clean evidence only comes out of "one."

## The Scope Decision Log, Turning "No" into "Not Now"

The Five Ones handle "where to cut." The other half of the problem is "what happens to the part cut off." The answer is this chapter's second piece of kit.

> **The scope decision log is one line per refused extension proposal, with what it was, who proposed it, the reason for refusal (the cost), and the revival condition.**

The revival condition is the soul of it. It is the lubricant of refusal, and it translates "no" into "not now." Home property was not rejected. It is queued as "the first extension after the pilot hits target." Writing revival conditions has one hard rule, events, not dates. "Consider in Q3" is a brush-off. Q3 arrives and nothing happens. "After the pilot North Star hits target" is a commitment. When the event happens, the proposer comes to open this page himself.

This rule has an expiry date, and most people do not think of it. Pilot events exist only during the pilot period. Once the system enters the operating period, events like "hits target" are gone, and the revival list keeps growing. The operating period often brings more proposals than the pilot did. Operating-period revival conditions switch to two kinds of anchor. One hangs on the periodic resource review, written as "ranked with the other candidates at next quarter's resource review." The other hangs on an operating metric, written as "revisit after such-and-such operating metric holds within threshold for N consecutive weeks." Both are fixed moments where other people will also be in the room, not dates you keep in your head. An entry that cannot be given either anchor is really a new project already. It should go through project approval, not squat on this sheet.

This sheet does three jobs at once. For the proposer, it is an answer they can repeat. For you, it makes refusals cumulative. The second time someone proposes a platform, open the log, no need to debate again. For the project, the revival list is an asset. On the day the pilot hits target, it is the ready-made phase-two roadmap (Chapter 23 comes back to harvest it).

The charter's existing "not this phase" list (Chapter 4, the part of the "Scope and Red Lines" section that explicitly says what is not being done) is its first batch of entries. At signing there were only conclusions. Add the cost and the revival condition now, and "not this phase" turns from a wall into a timetable.

This sheet also has a leak that only exists inside a company. It captures formal proposals. It does not capture "do me a favor." Another department wants you to support their own pilot on the side. Half a day's work. It goes through no project approval, no charter, and not this sheet either, because it is not called an extension. Help three or four times and one of your engineers is down nearly half a week, nothing shows on the weekly project report, and when you slip you cannot even produce an explanation. One rule. Any favor over half a day goes into the scope decision log. The proposer's name goes in, and the refusal reason column states which item of this phase it crowds out. Writing it down is not for refusing. Most favors should still be done. It is so this time has somewhere to show.

## At Anchor & Helm: Three Proposals, Three Responses

Three proposals, three tools, one at a time.

**Home property. Price it, then give it a place.**

Pricing means putting the cost of a proposal on the table and stating it plainly. Kevin's "just one more class of data" is an honest judgment. Seen from the queue interface, home property claims and auto claims do look about the same. You do not argue on the phone. The next day you go to see him with a three-line tally.

"Kevin, adding home property looks on paper like one more class of data. In practice three things double. First, Linda's team does not touch home property. The people using this thing every day would have to become the home property team, and the scoring, the annotation, those two hours a week, all of it gets rebuilt for the home property team. Second, home property's 'abnormal amount' is a different feel. Auto looks at the repair shop and the survey photos. Home property looks at the loss assessment report from an independent adjusting firm. Not one of Linda's five rules of thumb carries over, and the set of standard cases we test the system against starts from zero. Third, where that -30% comes from. You worked it through at the charter meeting (Chapter 4), and that was the auto tally. Mix home property in and the attribution gets muddy. Add the three up, the pilot slips at least six weeks, and the evidence gets cloudy."

Kevin frowns. "So when does the home property team get its turn? You cannot expect me to go back and say 'not doing it.'"

You open the scope decision log and write a line in front of him, reading it aloud as you go. "Home property exceptions, proposed by Kevin Doyle. Reason for refusal, user group, annotation system, and metric baseline all double, diluting the pilot evidence. Revival condition, the first extension after the pilot North Star hits target." Then you add, "'First' is exclusive. When the time comes, data reconciliation starts a month early, and the home property team does not queue for project approval again."

Kevin stares at the line for a few seconds. "Fine. That I can take back. First in line is not the same as killed." From disappointment to acceptance, and not by persuasion. His wish got a definite place instead of being thrown into a black hole.

**Full automation. Draw the ladder.**

With Grant, you draw, you do not debate. Four layers on the whiteboard, the red line at the top, what AI already does at the bottom, read from the bottom up.

```
Decide   pay or not, how much                       <- red line: never touched
Act      send chase notices, assign, change status  <- humans take over here (the reviewer clicks confirm)
Advise   priority + next step + reason              <- AI stops here (this phase)
Sense    gather documents, dwell time, risk signals <- AI does this
```

"Full automation is the question of AI climbing this ladder one layer at a time. Each layer up needs different evidence, and capability is actually secondary. For AI to go from advising to acting, the advise layer first has to build a track record, which suggestions get accepted as is, which get overridden often, and that record starts accumulating during the pilot (Chapter 17). With it, what you discuss with the board next year is 'which classes of action have a high enough acceptance rate, so which ones do we automate first.' Let the AI's suggestions earn a record of being accepted before you talk about letting it act."

Grant looks at the drawing. "This ladder goes into the next memo you write me. That is how I will put it to the board too." The scope decision log gets its second line. Revival condition, once the advise layer's acceptance data hits target, move up one layer at a time, each layer decided on its own.

The "evidence" in that line takes two forms. One is the human acceptance record, which suggestions get accepted as is and which get overridden often. The other is a machine verification loop. Can this layer's output be verified on the spot, with errors automatically detectable, enumerable, and reversible? Where verification is automatic, an error is caught at once, and you need not wait for people to accumulate usage records before you can relax. Where the output is verifiable, moving up need not rely entirely on an acceptance rate slowly building. Where the output cannot be verified, however high the acceptance rate, go slow (Chapter 10 unfolds "verifiable output" into a pattern selection criterion, and Chapter 22 uses this distinction to deliver the first move up).

**The general-purpose platform. Five counter-questions.**

The engineers' architecture sketch has no technical errors, which is exactly what makes it dangerous. You do not evaluate the design. You ask one question. "Remember the five gaps (Chapter 1)? Let's walk through them. Which gap does the platform narrow?"

First lay out the list, data gap, workflow gap, trust gap, ownership gap, value gap, and go through them one by one.

Data gap. The platform does no reconciliation for any scenario, and the core system's status fields lie exactly as before. Not narrower. Workflow gap. Configurable means embedded in no specific workflow, and "general-purpose" is precisely the antonym of closing the workflow gap. Wider. Trust gap. Linda is willing to score because this system understands exceptions, not because it is configurable. Not narrower. Ownership gap. The queue's owner is Kevin. Who owns a company-wide platform? No answer. Wider. Value gap. The North Star is first-touch handling time. "Configurability" does not convert into that number. Not narrower.

Five gaps, zero narrower, two wider. The older engineer closes the sketch himself. "Got it. The platform is what happens after the second use case shows up." You add a sentence, catching the enthusiasm rather than dousing it. "Right. A good abstraction grows out of the second case. It is not guessed from the first. Whoever writes the extraction pipeline (the chain of steps that pulls data into the queue) keeps the interfaces clean. That is the first brick of the future platform (Chapter 23 comes back to distill it)." Scope decision log, third line. Revival condition, after the second slice lands, distill what is common and revisit.

A week later, the three-line sheet is pasted at the end of the weekly project report. Not one proposer feels refused.

Nobody turning hostile is the luck of this case, not a guarantee of the procedure. Suppose Kevin reads the three lines and still insists, "the home property team lead cannot wait, put it in first." The procedure runs as before, one more round. You do not recompute the cost. The tally is done, and computing it again is fighting to win. You write both roads on the same page. One as before, home property waits, revival condition "the first extension after the pilot North Star hits target," exclusive, reconciliation starts early. The other is what he wants, home property goes in this phase, with the same tally written next to it, the pilot slips six weeks, and the North Star's attribution gets muddy.

A team from outside would, at this point, ask the owner to sign next to the cost, and with the signature the responsibility changes shoulders. You do not have that step, and you should not pretend to. Kevin is the pilot owner and the choice is his, yet three months later, when the pilot produces no conclusion, your team is the one asked, not him. So the internal version replaces the signature with a decision trail, two moves. First, both roads and their costs go into that week's project report, cc Grant, quoted verbatim, no comment, no recommendation. Second, if the second road is taken, the delay attribution column on the project board for those six weeks reads "scope change, home property added this phase." The attribution travels with the schedule, and whoever looks at progress sees it.

Be honest about what this trail buys. It does not clear you of responsibility. It only clears you of "surprise." Three months later, when someone asks why the pilot ran six weeks late, the report and the board answer for you. You do not have to reconstruct in that meeting who said what when, and you do not have to make Kevin admit it from memory. More important, it works in the moment. Kevin knows both things will happen, and that changes the choice itself. The trail's main function is not settling accounts afterward. It is making the cost visible at the moment of choosing.

Most of the time nobody chooses the second road. What he needs to take back is a sentence he can give. "First in line" is a promise. "Put it in first" means going back to explain why the whole pilot is six weeks late.

**The fourth kind of proposal, a lateral request from a peer department.** The three proposals above came from the sponsor, the business owner, and the engineers you work with. That is one vertical line, all inside this project's chain of authority. Sooner or later an internal reader gets the fourth kind, one sentence from a peer department. "You did it for claims, do one for us while you are at it, we are all one company."

This kind is the hardest to hold off, because the three things that normally hold proposals off for you are all absent. Grant's authorization covers only this project. Invoking his name may not work, and it looks like borrowing a banner. There is no written agreement between you and the other side to cite. He is not on the project approval form, and he is not on the charter. And next year he may be the person you have to go to for data, for people, for a cross-department interface. The cost of refusing is booked to your personal long-term account and settles a year later.

The response does not change. Still pricing plus a place, with one added move. Price it with the same three-line tally. One more department, and the user group, the annotation system, and the metric baseline each get rebuilt, and the pilot slips by this much. Work it out face to face. Giving it a place means logging it in the scope decision log, his name in the proposer column, the revival condition as a checkable event. The added move is the cc. Send that line, cost and all, to Grant. The cc is not tattling. It sends a lateral request into the vertical ranking, so the person with the authority to rank does the ranking. You have no ruling power, but you have the power to put things into the ruling procedure, and for this kind of proposal that is enough. The other side mostly does not expect a yes on the spot anyway. What he needs is the same, a sentence he can take back.

Behind these three responses are a few levers a team from outside does not have. First, you can price a proposal before it takes shape. Hear in the corridor that the home property team is stirring, and that same day you can go and walk through the three-line tally. By the time they formally ask, the tally is done, and the conversation is no longer whether to add but when. A team from outside has to wait until the proposal is formally made before it has a position to speak from. Second, the scope decision log is a cross-project asset. It does not reset with the project. Next year, when another department proposes the same thing, you open last year's line, cost and revival condition both there, and the cost of debating it again drops to turning a page. That is also why this sheet lives in the team's shared location, not in your local files. The third lever is that red lines can borrow the company's existing institutions, which is the next section.

## Failure Modes

**1. The platform temptation, abstracting before the use case has run.** The first scenario is still in pilot and the architecture already shows a "rules engine" and a "scenario configuration center." Abstraction is an engineer's identity currency. "Platform" is worth more on a resume than "spreadsheet." And the generality of LLMs makes a platform demo cheaper than ever, so for the first time temptation and capability are both in ample supply. But the legitimate raw material for abstraction is repetition. Before the first use case is validated, the only raw material for abstraction is imagination. One rule. Every platform proposal goes into the scope decision log, and the revival condition is always "after the second slice lands."

**2. Red lines that live only in speech.** "We agreed not to touch payout decisions." The person who said it transfers six months later, and the new product manager proposes at the requirements meeting, with enthusiasm, "give the payout amount an AI estimate." A verbal consensus lives in the memory of those who were present, and evaporates when people change. A red line that is never touched day to day and never brought up is often remembered for the first time the moment it is stepped on. Writing it into the charter is only the minimum. Nobody opens the charter day to day.

The real defense is putting the red line where it might get stepped on. The scope decision log (opened at every scope discussion), the security review packet (the packet of review materials, Chapter 12), all the way to the system interface itself. The queue has no column called "suggested payout amount," and that "no column" is the red line in physical form.

There is one more kind of hardness that only an internal reader can get. The company already has red lines for information security and compliance. They have their own review meetings, their own inspectors, their own penalties, and whoever steps on one writes a report. The red lines you wrote yourself into the charter have none of those three, and every change of people means explaining them again. So hang whatever you can on the existing ones. "No automated outbound messages" goes under the company's compliance policy on external contact. "No payout decisions" goes into the security review's conclusions. A borrowed red line does not need you in the room to remind people. The institution remembers for you. This works on you too. The person who transfers in six months may be you.

**3. Over-narrowing, the thin slice cut into a no slice.** Scope is cut down to "just missing-document detection, the queue can come later." Smallest in engineering, lowest in risk, and Linda reads it and says, "What documents are missing I can tell at a glance. What I lack is the ranking and the chasing." Once the discipline of narrowing is learned, it decays from judgment into reflex. Refusing takes less effort than thinking, and "one more cut" always looks prudent. But the criterion for the cut is wrong. The "minimum" in thin slice is the minimum that is complete in value, not the minimum that is easy to engineer. After the cut there must still be one real user who can say "this solves my problem." Take the slice description to your "one user group." If you do not hear that sentence, what you hold is a no slice.

## Next Monday

1. Write the Five Ones for the project in your hands. The items you cannot write, and the items you are forced to write in the plural ("both kinds of users need it"), are your scope risk list. Every plural owes you one narrowing negotiation.
2. Add the extension proposals you turned down verbally in the past month to the scope decision log ([Template 8](../appendices/template-08-thin-slice.md)). Give each a cost and a checkable revival condition, send it back to the proposer, and watch the reaction.
3. Draw the decision rights boundary. Which layer AI stops at, which layer humans take over, what evidence each move up requires. Then count how many documents this line appears in. A boundary that exists only in your head does not exist.
4. Check where your red lines "live" right now. A red line that lives only in the kickoff document is a verbal red line. Give it a home in the scope log, the review materials, and the product interface, one each.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 8 Next Monday actions. Copy
templates/thin-slice/thin-slice.md into the working directory I name, and ask me the Five Ones one by one. Record any
item I answer in the plural as is and mark it. That is my scope risk list, do not narrow it for me.
Then run python3 templates/thin-slice/scope_log.py --help to see how the scope decision log works, demonstrate it once
with the built-in sample, then enter, one by one, the extension proposals I turned down verbally in the past month. I
supply the cost and revival condition for each. The decision rights boundary diagram is mine to draw.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The Five Ones of the thin slice (one user group / one decision / one data path / one risk boundary / one measurable outcome); the four-layer decision rights boundary map (sense, advise, act, decide, moving up on evidence); the five-gap counter-question ("Which gap does the platform narrow?")
- **Templates.** [Template 8](../appendices/template-08-thin-slice.md), the Thin Slice Definition Sheet and Scope Decision Log, Five Ones definition sheet, decision rights boundary map, scope decision log (with how to write revival conditions), no slice self-check
- **Key judgments**
  - "Scope creep is the default outcome of organizational dynamics, not a management failure."
  - "Turn 'no' into 'not now.' Revival conditions are the lubricant of refusal."
  - "An AI system has one more boundary, the decision rights boundary. Draw that line wrong and you redo the whole validation system, not just the code."
  - "Let the AI's suggestions earn a record of being accepted before you talk about letting it act."
