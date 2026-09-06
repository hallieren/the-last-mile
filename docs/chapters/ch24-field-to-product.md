# 24 · From the Field to the Platform: Field-to-Product

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-24-f2p-memo.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The project has stepped out of the daily, and the custom code and dozen-odd platform judgments the field produced are rotting in the business line's repo and inside your head. The platform team knows none of it, and the next project writes it all again from zero.
>
> **What You Will Be Able to Do.** Run the asset recovery checklist at the asset inventory and pick out what should cross the river. Use the field-to-product memo's four sections plus the three filters to turn a field signal into a proposal the platform team can consume. Give n=1 signals a candidate register instead of forwarding them or throwing them away.

---

## Monday of Week 30, the Internal Closeout Retrospective

Friday of week 29, the last retrospective at Anchor & Helm, and you said nothing the whole time (Chapter 22). Monday morning of week 30, before you leave for Swiftway, your team holds its own asset inventory. Nobody asked for this meeting. The account of the launch given to the business side happened in week 28, and that one was Claims Operations' account to Anchor & Helm Insurance. This one has no business side in the room, and one item on the agenda. What did this project leave us?

Start with the "delivered assets" column (this meeting is the same asset inventory as Chapter 23's, written there from another angle). You put the module list from the Anchor & Helm repo on the screen and ask the same question of every item. This piece here, will the next similar project write it again? When the count was done the room went quiet for a few seconds. About 40% of the code is the kind any similar project will need. The decision trail schema (suggestion and fact tables kept separate, the six fields, reason codes, Chapters 12 and 17), the eval harness (the management and replay scripts for the golden cases), the queue skeleton (column structure, the rollup view, escalation rules as configuration). All of it sits in the repo of that one line, Anchor & Helm's claims operations.

The repo belonging to the business line is not the mistake. Clause one of the co-build agreement should be signed exactly that way (Chapter 15). The mistake is losing contact inside the same git. The same Group, the same GitLab, code anyone can click open, so everyone assumes recovery has already happened. It has not. That 40% of structure was never pulled out and never declared reusable, which is the same as it not existing. This hides better than a gap between two companies, because the code is plainly right there.

The more expensive item sits outside the code. Across twenty-nine weeks you banked a dozen or so judgments about what the platform's next version should have. The front line wants a queue, not a dialog box. The reason code is the cheapest ground-truth signal there is. The decision trail is a hard requirement and logs are only its by-product. The Group platform team knows none of it. Nobody failed at his job. Between the field and the platform runs a river nobody owns.

## Why This Is Hard: Symmetrical Complaints, a Missing Mechanism

One bank of this river is your delivery team, the other is the Group platform team. The complaints on the two banks are strikingly symmetrical. You say the platform does not understand the field and builds its roadmap behind closed doors. The platform says field requests are all noise, that every department calls its own request the most general one, and that every deliverer shouts loudest for his own department. Both sides are right and neither has a way out, because what is missing is a mechanism for filtering and translation. Goodwill is short on neither bank. Which signals are worth crossing, in what format they cross, who rules. The internal river has one more drop in it. The platform team's KPI is adoption rate, yours is business outcome, and the two appraisal sheets do not share a single line. They want you to use off-the-shelf components, the capability you want is not on their roadmap, and neither side has any obligation to give way first.

With no mechanism, a signal has two default exits. It stays locked in the deliverer's head (the organization pays the whole bill on the day he moves posts or leaves), or it gets forwarded to the platform as is (the platform, once flooded, learns to listen to none of it, and even the real signals stop crossing). Done well, your team is the platform's most expensive radar. You stand behind real users and see what no piece of research can see. Done badly, your team is a source of noise on the platform's roadmap. The radar and the noise source are the same people with the same observations. The whole difference is the mechanism.

With no shared KPI across the two banks, you have to build the channel yourself, and the way to build it is to put the f2p memo (field-to-product memo, defined in the next section) into a fixed line of the quarterly report-out. How many memos went out this quarter, what n each carried, how many the platform took, one row of numbers, read by Owen Hartley, copied to the platform lead. What gets written into the report-out gets done. Everything else is a favor done in passing.

## Prior Art, and What AI Changed

**The Amazon tradition, write backward from customer value.** The generalization case in an f2p memo has one hard rule. You may not start from what you built at Anchor & Helm. You must write backward from which other departments will hit this. Cannot name a second one, cannot send the memo. The rule comes from the PR/FAQ discipline recorded in *Working Backwards* (Bryar and Carr), where a project starts by writing a future press release and the FAQ forces answers to the hardest questions, whose behavior changes because of this and on what grounds. Its spirit is the direction of the argument. Write backward from customer value, not forward from what we made.

**The lean tradition, genchi genbutsu (go and see the actual thing in the actual place).** Toyota's discipline. Whoever makes the decision has to go to the field and see with his own eyes, and a secondhand report is no substitute. Landed on a platform role it becomes one hard rule. The platform's decision-makers must go into the field on a cycle. You can book it for him. You cannot look for him.

**What did the AI era change? Generality can be measured for the first time.** "This request is very general" used to be a piece of rhetoric, and whoever was loudest was the most general. AI delivery changed three things.

1. **Decision trail data aggregated across departments is platform-level eval insight.** Every project's override reason codes describe which class of judgment people do not trust AI on (Chapter 17). Put two departments' reason code distributions side by side, and the overlap is the platform's problem to solve, not the project's.
2. **A cross-department diff of prompts and rules is the platform candidate list.** A diff means comparing two departments' versions line by line to see what changed and what did not. Diff the extraction prompts of Anchor & Helm and Swiftway. What changes is the industry vocabulary and the field names. What does not change (output structure, validation method, the backstop on exceptions) is the platform. The line between the custom layer and the platform layer can be drawn with a diff for the first time.
3. **n turns from a claim into a number.** "How general is it" can now be argued quantitatively. That is an opportunity and a discipline at once. In an era where you can count, not counting is laziness.

All three are stronger inside a company. Anchor & Helm's and Swiftway's decision trails both land in the Group's warehouse, so putting two reason code distributions side by side is one query away, with no cross-company data export approval to clear, and a prompt diff inside the same GitLab is close to free. An outside delivery team can never do either of those two things, because every one of its projects sits behind a company wall. This is a pure advantage, and cashing it has one precondition. The decision trail schemas of the two projects have to match, which is exactly the problem the first memo in the Anchor & Helm section below sets out to solve.

## The Framework: The Field-to-Product Memo and the Three Filters

> **The field-to-product memo (f2p memo) is the one-page proposal that flows a field signal back to the platform team. Four sections, phenomenon → the generalization case → the product recommendation → the cost of not doing it.**

| Section | The Question It Answers | Rules |
|----|------------|------|
| **Phenomenon** | Which field, at what frequency, on what evidence | Quote the actual words and the decision trail data, not impressions |
| **The generalization case** | Which other departments or scenes will hit this, and what n is | Write backward from the side with the need. n must be verifiable |
| **The product recommendation** | What **capability** you are asking for | A capability, not a feature. "Ship a decision trail schema component" is a capability. "Add an export button for Anchor & Helm" is a feature. Features belong to projects, capabilities belong to the platform |
| **The cost of not doing it** | What every project pays over again, what is lost structurally | Quantify it as engineering effort. Say the most expensive one out loud |

The format discipline is not newly invented. The f2p memo obeys the one-page rule of Chapters 13 and 19, one page, lead with the conclusion, an ask at the end, delivered 48 hours before the meeting. The full statement of those four sits in Chapter 19, and this chapter only uses them, it does not re-teach them. The only difference is the reader, an executive on the business side becomes the Group platform lead. What is new is three thresholds for sending, called the three filters here. Fail any one and it does not go out.

1. **Report only at n≥2.** n=1 is custom work. n≥2 is a signal. n counts departments. The same need appearing in two business departments is what makes it the platform's problem to solve. However reasonable one department's request is, it goes into the candidate register first. The candidate register is where n=1 signals are kept, each with its trigger condition written down, promoted to a memo the second time it appears. The register has five fields, signal, source (department / proposer / date), n, status, and the trigger or revival condition.

    The live example is at Anchor & Helm. In week 23 the survey team lead proposed at the retrospective, "repair shop response time, should you not build a number for that too" (Chapter 20). Real need, real proposer, real instinct for data, but it has appeared at Anchor & Helm exactly once. It goes into the register with one line of trigger condition, "any second project that raises an 'outside party response time' need promotes this to a memo." The register is an incubator for n=1, not a wastebasket.

2. **Describe the judgment structure, not the interface.** "The business side wants a Gantt chart" does not cross the river, because a Gantt chart is this department's interface habit. "The business side needs to see waiting attributed across steps" is the transferable judgment structure. An interface description turns the platform team into an outsourcing shop. A structural description is what gives them design room.
3. **Attach what you are willing to give up for it.** A recommendation with no trade-off is a wish list item, and the platform team gets dozens a day. Which of your own requests will you give up priority on for this one? No answer means you do not much believe in it yourself.

The third one is the hardest inside a company. An outside delivery team bargains with its own schedule priority. Your hand is different, and it holds four cards. Your department goes first as the pilot. Your department retires its own ready-made custom implementation and switches to the platform version. Your department supplies people to co-build. The hardest card, file a PR straight into the platform repo and turn the proposal into a fact on the ground, which routes around the roadmap negotiation entirely, and which an outside team cannot do. Cannot produce a single one of the four, and what you want is the platform doing your work, not the platform providing a capability.

## At Anchor & Helm: One On-Site Day, Three Memos

**Tuesday of week 24, an on-site day.** Halfway through the handoff period, you cleared it with Kevin Doyle and pulled the Group platform team's lead for this capability over to Anchor & Helm to sit for a day. An outside team that wants to bring its own product manager into the field first has to clear a visitor confidentiality filing. You do not. The platform lead walks down two floors. In the morning he sat behind Linda Marsh's team and watched the queue. Eight people, and not one of them "asked" the system anything. Scan the row, confirm, override, two seconds to pick a reason code, and pick up the phone when a hard claim needs a judgment.

In the afternoon he sat in on the retrospective Linda chairs. One override disagreement, two new golden cases, one revision to the annotation guide, all through in five minutes. Three days after he got back he cut a feature already in development, a "conversational query entry point" that would let users ask a claim's status in natural language. He had sat in the field for one morning and seen with his own eyes that the user this feature assumed does not exist. The front line does not want to ask the system questions. The front line wants to be told the next action.

The chatbot that died at the start of this book (Chapter 1) nearly came back to life inside a capability the Group platform was already building. What saved it was one day in the field, which no requirements document could have done. A negative signal from the field is worth as much as a positive one, and not building this feature saved a full quarter of development.

**Week 32, memo #1.** Work starts on Swiftway's queue skeleton, and you catch yourself hand-writing the same decision trail schema a second time. The n≥2 filter fires on the spot. The memo went out that evening, four sections plus the give-up line, not one of them skipped.

> **F2P Memo #1, the decision trail component.** To the platform lead, week 32
> **Phenomenon.** Projects at two subsidiaries, Anchor & Helm (insurance claims) and Swiftway (logistics dispatch), hand-wrote the same thing one after the other. Suggestions and facts stored in separate tables, the suggestion table append-only, six-field decision trails, override reason codes. About one week of engineering each time, and the structures are near identical.
> **The generalization case.** The decision trail is a structural requirement of any "AI suggests, a person decides" system, and it has nothing to do with the industry. As long as decision rights stop at the advise layer, the system has to answer "who made the call and on what grounds." n=2, the two subsidiaries Anchor & Helm and Swiftway, and the second implementation needed no industry adaptation at all.
> **The product recommendation (a capability).** A decision trail component. The trail schema plus reason code configuration plus a review query that splits overrides by category, available to any project out of the box.
> **The cost of not doing it.** A week of rewriting on every new project is the small bill. The big one is that project schemas diverge and cross-department override aggregation analysis cannot be built at all. Both subsidiaries' decision trails sit in the Group warehouse. An outside team can never do this, we could have, and it is the only source of platform-level eval insight.
> **Willing to give up for it.** If the schedule conflicts, this team sends one person into the platform repo to co-build, and withdraws its request this quarter for custom columns in the queue interface.

The two below give only the key points. The full form is in memo #1.

**Memo #2, productizing the eval harness.** Golden cases are managed in spreadsheets at both subsidiaries today, added and removed by hand, versioned by filename, replayed by script. Every department that runs an eval will hit this, two subsidiaries already have, n=2 clears the line, and pushed further by judgment structure, nobody who manages golden cases in a spreadsheet escapes it. The capability recommended, a golden case management interface with versions, the annotation disagreement log, admission of incident cases, and replay reports.

**Memo #3, the queue scaffold.** Column structure as configuration, the rollup view, escalation rules. Refused by the platform team. It conflicts with the existing roadmap and will not be scheduled this quarter. You did not argue. You made a record. The memo goes into the register together with the reason for refusal, plus one line of revival condition (events, not dates, the same form as Chapter 8's scope decision log). Half a year later the platform roadmap shifted and somebody dug it back out of the register, but that comes later. Only one sentence needs keeping right now. A memo that was refused but recorded is still an asset. One that was refused and never recorded is the one written for nothing.

The interface at the inventory end needs a line too. From here on the internal closeout retrospective carries one more fixed segment, closeout asset recovery, four classes, code, documents, judgment, metrics, which is Chapter 23's four asset classes seen from the counting side (code = component, documents = template, judgment = judgment rule, metrics = metric model).

Give every item a destination. There are only three exits. Admit it to the library, send a memo, or leave it in the business line repo. The first two are not mutually exclusive. Anything at platform capability level usually goes into the library and gets reported as well, and a refused report still stays in the library. Only "leave it in the business line repo" is an exclusive exit. The blank sheet is [Template 24.2](../appendices/template-24-f2p-memo.md).

| Class | What Goes Through, Item by Item | Test Question | Destination |
|----|--------------|----------|------|
| **Code** | Decision trail schema / eval harness / queue skeleton / extraction pipeline structure / configuration patterns | Does it still hold in another industry | Admit and send a memo. Business-line-specific fields and integrations stay in the business line repo |
| **Documents** | charter / review packet / the three memos / runbook / annotation guide framework | The framework transfers, the content does not | The framework is admitted. The content stays in the business line repo |
| **Judgment** | Key judgments / failure modes and incident retrospectives / annotation disagreement rulings as precedent | Tacit knowledge does not transfer. The method for mining it transfers | The method is admitted. The rules of thumb themselves stay in the business line |
| **Metrics** | Metric definition tree / thresholds and acceptance lines / reason code enumeration / balancing metrics | The structure is general, the vocabulary is business-line-specific | The structure is admitted or rides along with a memo. The vocabulary stays in the business line |

The "admit it" exit runs through Chapter 23's admission review and the [Template 23](../appendices/template-23-pattern-extraction.md) register, and this chapter does not repeat that standard. Every item has to have a destination. "Leave it for now" is not allowed.

What gets recovered is structure. The code files belonged to the business line all along. And structure, as Chapter 23 put it, belongs to no repo at all.

There is one more bill after a memo is taken up, and the recovery sheet does not carry it. On the day the platform version launches, Anchor & Helm's custom implementation will not vanish by itself. The dual-track period where both run side by side is a quarter at the short end and a year at the long end, and three things go unmanaged if nobody asks. Who maintains the old one, when it gets retired, who makes the call. The way to write it is three more cells on this system's row in the PMO's AI system transfer ledger (Chapter 22), the maintainer of the old implementation, the retirement condition (the day the platform version clears Anchor & Helm's golden cases), and who makes the call (the system owner, Kevin Doyle). Leave any one of the three blank and you are feeding two systems at once.

One note in passing. Anyone who gets good at bridging this river gains one more career route. The starting point of a platform product owner is where field-to-product ends (Chapter 26).

## Failure Modes

**1. Every department reports its requests straight to the platform.** You forward the business side's actual words to the platform as they were said, and the more diligent you are the more responsible you look. Forwarding is free, filtering is expensive, and filtering means carrying the "I suppressed the business side's request" responsibility. On top of that you live with the business side day in and day out, and empathy naturally amplifies "my department is the most general one." Inside a company the temptation is larger still. You and the platform team work for the same company, raising a request is one message away, forwarding is far cheaper than writing a memo, and the channel burns out that much faster. The platform team's rational response once flooded is to listen to none of it, the channel is burned, and even the real signals stop crossing. This is exactly what the three filters are for. Filtering is the sender's responsibility. Fail to filter and the recipient will filter for you by not listening. The test, count the field signals you forwarded to the platform last quarter and see how many carried an n and a give-up line. None at all, and what you were doing was forwarding, not reporting.

**2. The platform team never goes into the field.** All the platform's knowledge of the field comes from your account of it. A trip to the field is permanently "important, not urgent" on the platform's schedule. The better-hidden part is that any account distorts. You will translate what you saw into requirement language without noticing, and the negative signals are the first thing lost in translation. "Nobody asks the system anything" does not form a requirement, so it never gets passed on, and yet it is precisely what cut a quarter of wrong development. The fix is to write the on-site day into the rhythm of the platform role. However good you get at retelling, it will not cover this. Genchi genbutsu is an institution, not a nice story. The test, go through your platform counterpart's calendar. If a whole year holds no record of one full day sitting behind real users, your shared knowledge of the field is entirely secondhand.

**3. Nobody recovers the custom code.** Roughly 40% of general structure rots in the business line repo and the next project rewrites it. An outside team at least has a closeout date, with appraisal and celebration both settling on acceptance day, and the recovery window opens in the unattended stretch where the project is dead and the next one has started, narrow, but it does open. Inside a company there is not even that window. There is no closeout event, people slide from one system to the next, and recovery never fires. The fix is to hang three triggers on recovery, the fixed retrospective three months after launch, the moment before any team member moves posts, and the quarterly asset inventory. Hang it on any one of them and recovery has a date. This is the same move as Chapter 14's resource gates and Chapter 22's three mandatory handoff mechanisms, manufacturing a moment that comes due automatically for something with no outside date. The one at Anchor & Helm hung on the third, and it happened to open on the morning you left for Swiftway, two triggers stacked on the same day, which is why it opened at all. The test, go through the retrospective notes of the last project you stepped out of the daily on. If "asset recovery" is not an item on the agenda, recovery never happened.

## Next Monday

1. Open the repo of the last project you stepped out of the daily on and go through the module list, asking of every item, "will the next project rewrite this?" The number you get is your "rot-in-the-field rate." Use [Template 24.2](../appendices/template-24-f2p-memo.md) to give each item a destination, admit / send a memo / leave it in the business line repo. "Leave it for now" is not allowed.
2. Find the one field discovery you are most sure the platform should build, and run it through the three filters. What is n? Judgment structure or interface description? What are you willing to give up for it? All three clear, and you write it up as a one-page memo with [Template 24.1](../appendices/template-24-f2p-memo.md) and send it.
3. Anything that cleared only two of them goes into a candidate register. One line of phenomenon, one line of trigger condition. Refused memos go into the table too, with the reason for refusal and the revival condition attached.
4. Book an on-site day for your platform counterpart. Not a demo day, a morning sitting behind real users. You are responsible for booking it, not for retelling it.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 24 Next Monday actions. Open the repo of the last project I stepped out of the daily on,
list the modules, "will the next project rewrite this" is mine to answer item by item, and you compute the rot-in-the-field rate. Then copy templates/asset-recovery/recovery-checklist.md
over to me, the destination of each item (admit, send a memo, leave it in the business line repo) is mine to set, and no "leave it for now" allowed. For the field discovery I am most sure about,
you only ask the three filters, what is n, judgment structure or interface description, what am I willing to give up, and only after all three clear do you draft from f2p-memo-template.md,
with candidates registered in candidates.csv. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The field-to-product memo's four sections (phenomenon → the generalization case → the product recommendation (a capability, not a feature) → the cost of not doing it) + the three filters (report only at n≥2 / by judgment structure, not by interface / attach what you will give up); closeout asset recovery (four classes, code / documents / judgment / metrics, × three exits)
- **Templates.** [Template 24](../appendices/template-24-f2p-memo.md), Field-to-Product Memo and Closeout Asset Recovery Checklist
- **Key judgments**
  - "Done well, your team is the platform's most expensive radar. Done badly, it is a source of noise on the roadmap."
  - "n=1 is custom work. n≥2 is a signal."
  - "A negative signal from the field is worth as much as a positive one."
  - "A memo that was refused but recorded is still an asset."
