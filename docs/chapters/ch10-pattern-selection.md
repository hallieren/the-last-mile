# 10 · Pick the Pattern: Start with the Dumbest Thing That Works

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-10-pattern-decision.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** Does this scenario call for an agent, for RAG, or for a few rules? The whole world is talking agentic (letting the model decide its own next step and call its own tools), and the two claims-ops IT engineers arrive thrilled, carrying a multi-agent design. You know it is the wrong fit, and you cannot produce a reason that does not sound like "conservative."
>
> **What You Will Be Able to Do.** Use the pattern decision table (six patterns × five criteria) to pick the dumbest thing that works for every step where AI intervenes in your system. Turn down over-design without dousing the enthusiasm. Leave "upgrade later" one legitimate channel that admits eval evidence only.

---

## Week 7, Monday, the Multi-agent Proposal at the Standup

The source of truth decision was settled last Friday (Chapter 9). At Monday's standup in week 7, the two claims-ops IT engineers, the same two who brought the general-purpose platform sketch last time (Chapter 8), bring something new. This time it is a demo that runs. The sketch stage is over.

The younger engineer opens his laptop. "Over the weekend we put up a multi-agent frame. A detection agent reads the claim and the emails and works out which documents are missing. A chase agent drafts the chase notice and sends it straight out. An escalation agent watches overdue claims, escalates automatically when they run past the deadline, and can even text the customer a progress update. The three agents call each other. Fully automatic." He runs three de-identified sample claims. Nobody touches them the whole way, they flow through, the logs look beautiful. "Linda's team handles only what the agents cannot. The rest is automatic. That is what an AI system means. That ranked queue thing, that is a spreadsheet with suggestions on it."

Concede something first. The demo is real, on three samples it did run end to end, and the two engineers are genuinely capable. They are also this system's future maintainers. The Chapter 22 handoff, to whom? To them. So your position right now is far more delicate than "turning down a design." Turn it down the wrong way and what you lose is two future co-builders' ownership (treating this system as their own, willing to backstop it when it goes wrong), and one architecture option is the smaller loss. Do not turn it down and the decision rights boundary drawn in Chapter 8 and the reconciliation just finished in Chapter 9 are both void.

Settle one question here first, who the future maintainer actually is. Inside a company there are three possibilities, and each answer calls for a different way of persuading. The first, the business line's own IT, which is what Anchor & Helm has. The two engineers are appraised inside claims operations, they can hold it and they cannot leave, so their ownership as co-builders is worth the effort of protecting. The second, a Group-wide ops team. They take no part in the design, so co-building is off the table, and all they can hold is something that runs, has a manual, and has an action for every alert. The complexity you pick decides directly whether they can hold it. The third is your own team. This one is the most common and the least said out loud. Here, whose ownership to protect is no longer the question, and the strongest argument turns into a different sentence. Every complex pattern you pick is your own night shift for the next three years.

There is another layer of difficulty, and it is more personal. "That is what an AI system means" pokes at the doubt in your own head. Building a "spreadsheet with suggestions on it," am I falling behind?

## Why This Is Hard: The Criteria Are Misaligned

When engineers argue about patterns, the default criterion is the capability ceiling, the most it can do. And the ceiling is exactly what a demo shows. The real criterion in an enterprise setting is the shape of the error, whether an error can be caught, attributed, and rolled back. How clear the shape is can be tested on the spot, whether the ways it fails can be listed in full in advance, and whether, once it has failed, you can locate which step failed and who backstops it. The two sets of criteria point in two directions. The higher a pattern's capability ceiling, the harder its error shape is to draw.

Enterprises have no demand for "occasionally impressive." They have a hard requirement for "when it is wrong, it can be caught, attributed, and rolled back." Impressive does not settle Tuesday morning's exception claims. A backstop does. This has nothing to do with being conservative. It is a property of the environment. Chapter 7's five questions already asked, at the opportunity level, how many times AI is allowed to be wrong and who backstops it. Pattern selection is the same question pushed down to every single step.

The second layer of difficulty is signal pollution. A pattern's popularity and its applicability are badly decoupled. Put plainly, how hot a pattern is and how usable it is are two different things. Heat is driven by demos and narrative, and the more demonstrable a pattern, the hotter it runs. Applicability is decided by error tolerance, and the harder a pattern's error shape is to draw, the narrower its applicability. The same property (autonomy, unpredictability) raises the heat and narrows the applicability at once, so the hottest is precisely the narrowest. The more demonstrable a pattern, the fewer places you can use it with confidence. Chapter 1's demo inflation has a pattern-selection version here. Demonstrating an agent chain has never been cheaper. Productionizing it has not come down a cent.

The third layer is the social cost. "No agent" sounds in a meeting room like "cannot use agents." What you need is what you needed when eliminating ideas in Chapter 7, a ruling procedure that does not rest on anyone's position, that lets the evidence speak and lets the proposer reach the conclusion himself.

## Prior Art, and What AI Changed

"Pick the dumbest one" is not a new discipline. It has a fifty-year pedigree.

**Gall's law.** The systems scientist John Gall's observation in *Systemantics* (paraphrased). A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch does not work, and it cannot be patched into working. It can only be torn down and started again from a simple system that works.

**"Choose boring technology."** The engineering manager Dan McKinley's well-known 2015 argument (paraphrased). Every team holds a limited number of "innovation tokens," and they should be spent on the core of the business. Boring technology is strong because its failure modes are known. How it breaks and how it gets fixed, someone walked into all of it ahead of you.

**The trade-off discipline of architecture review.** Chapter 8 quoted it already, put the cost next to every "want." Pattern selection is its technical depth. Every notch down the pattern spectrum (the next section lines the six patterns up from dumbest to smartest), what you "want" is a higher capability ceiling, and the cost written next to it is verifiability.

The AI era changed two things in this old discipline.

**One, the object of selection changed.** Selection used to mean components, a database, a queue, and a component's behavior is deterministic. Today there is a dimension that did not exist before, how much uncertainty you put into the system and at which step. The six patterns in this chapter are, at bottom, six doses of uncertainty.

**Two, "boring" has to be redefined.** The old test for boring was "ten years in production, fully documented," and AI components are all young, with no ten years to look up. Boring in the AI era can only be judged structurally. The output can be checked, the errors can be enumerated, the behavior can be reproduced. That is what "dumbest" means. The error shape is the clearest, and how weak the capability is, is a separate question.

Inside a company, this old discipline can also borrow two things you cannot borrow outside. The first is the company's existing technology stack standards and the architecture committee's whitelist. They exist in the first place to limit freedom of selection, so cite them and you do not have to say "this framework is immature" in your own name. You only have to point out that it is not on the whitelist, and what the other side is negotiating with turns from your technical taste into an institutional document, and an institutional document does not need you to defend it in the meeting. The second is the corpses. The company's previous agent project is most likely still around. Go find out how it really died, who wrote it, who maintains it, whether anyone still uses it, and what criteria it was picked on at the time. These are things a team from outside can only guess at. You can look them up, and you can put what you find into the anti-pattern list, where it becomes evidence in your own company's version. The anti-pattern list is exactly that, those causes of death written down as entries you can check against, and this chapter's template has one. Cite the whitelist with restraint. It counts as a red line only if you can name which standard it is. A "the company does not allow it" that cannot name the clause is only a shield.

## The Framework: The Pattern Spectrum and the Decision Table

The spectrum first. The pattern spectrum is the six candidate forms for AI intervening in one step, ordered from dumbest to smartest by how clear the error shape is. The further down, the higher the capability ceiling and the harder it is to draw a shape for the error. This order gets used again and again below.

- Rules. The ways it fails can be listed in full in advance, and when it fails you know which rule matched wrongly.
- Structured extraction + rules. The error is fenced into the extraction step, and a bad format is caught by validation on the spot. Structured extraction means pulling the key information out of free text into a fixed format.
- RAG (retrieval-augmented generation, having the model look things up before it answers). The ways it fails are open-ended. A missed retrieval and a wrong retrieval both leave no visible trace, and the only check is verifying the citations one by one.
- Single-step LLM. Every call can be wrong, and the shape depends on how tightly you pin down the output format.
- Agentic workflow. Errors compound and amplify across steps, the step that failed is hard to locate, and it may not reproduce.
- Fine-tuning (changing the model weights themselves, retraining on annotated data). Errors set into the weights, invisible, and there is no way to strike out one of them on its own.

The decision table is this chapter's main kit, six patterns × five criteria, a judgment in every cell and no scores. Scores get averaged. A judgment can only be rebutted (Chapter 7 covered how a weighted average kills elimination).

Where the five criteria come from. Error tolerance carries on from Risk, one of Chapter 7's five questions. Verifiability and data requirements stand on Chapter 9's fitness ladder. Maintainability by the receiving side draws on Chapter 22's handoff. Latency and cost get their own accounting in Chapter 16.

The maintainability column is the one most easily read too lightly inside a company. A team from outside leaves when its term is up, and this column's cost settles in a single payment on the day they go, visible and impossible to dodge. You do not leave, so the cost never settles on any one day. It spreads by the week into your ordinary days, into two extra alerts a week, three extra days of regression at every model generation change, two extra weeks for every new hire coming up to speed. A cost spread that thin has no due date, so nobody adds it up for you, and the fifth criterion becomes the cell in the whole table most likely to be filled in as "should be fine." Before you fill this cell, name the receiving side. If you cannot name one, the receiving side is you.

Read the table top down, and all five cells in a row have to pass. If one cell's judgment does not hold in your step, look at the next row. Stop at the first pattern whose five cells all pass.

| Pattern | Error tolerance | Verifiability | Data requirements | Latency and cost | Maintainability by the receiving side |
|------|-----------|----------|----------|------------|--------------|
| **Rules** | Ways it fails are enumerable, fit for zero-tolerance steps | Reproducible and explainable rule by rule | Fields only need to be interpretable | Milliseconds, near zero | The business line's IT can change it themselves |
| **Structured extraction + rules** | Error is fenced into the extraction step, schema (the fixed field structure the extraction output must satisfy) validation intercepts most of it | Extraction output can be validated and spot-checked | Unstructured source accessible, plus a spot-check sample set | One call per claim, batchable | Rules go to the business side; schema and prompts need a handoff |
| **RAG** | Ways it fails are open-ended (missed retrieval, wrong retrieval), needs a human backstop | Verified by checking citations, a rotten corpus rots everything | One genuinely trustworthy corpus | Two hops, retrieval plus generation | What gets maintained is really the corpus, and decay is hidden |
| **Single-step LLM** | Wrong on any call, only for steps where a person reviews | Hard; pinning the output format and requiring a reason partly makes up for it | No training data needed, but no eval means no threshold | One hop, controllable | Prompt drift goes unnoticed |
| **Agentic workflow** | Errors compound and amplify across steps | Path varies, failures are hard to locate and hard to reproduce | Every step has to pass fitness and eval on its own | Multiplied by hops, latency unpredictable | Hardest to hand off, debugging often needs the builder himself |
| **Fine-tuning** | Errors set into the weights, fixing one means retraining | Behavior changes globally, every retrain needs a full regression | Hundreds to thousands of annotations (as of writing, the bar is still falling) | Training cost paid up front and paid again | The receiving side can hardly take it over at all |

Three rules for using it.

**One, pick per step, not per project.** "Does this project use agents" is a fake question. Inside one system, error tolerance differs wildly from step to step, and the pattern follows the step.

**Two, read top down and stop at the first pattern that passes all five criteria.** That is the operational definition of "start with the dumbest thing." The test for "works" is five cells passing, not the most impressive result. A cell passes when its judgment still holds once dropped into your step, and the risk left over has a backstop you can name or a checkpoint. Name neither and the cell does not pass. If rules can solve it, no LLM. If a single step is enough, no agent.

**Three, an upgrade has exactly one legitimate channel, eval data showing that the dumber pattern cannot clear the threshold (Chapter 11).** "It does not feel smart enough" is not a reason to upgrade, and "I want to learn this framework" is even less of one. Start with the dumbest thing, and let the evidence force the upgrade.

## The Complexity You Choose Is Your Own Night Shift

Outside, these three rules are engineering discipline. Inside a company they are also an account in your own name. When a team doing external delivery picks an agentic workflow, the pain is borne by the receiving side from the day of handoff onward. When you pick an agentic workflow, the pain will most likely be borne by you and your team forever, because you cannot leave (Chapter 2's permanent ops). A model generation change means rerunning the regression eval, a framework upgrade means revalidating every step, and when that step fails at two in the morning, the person woken up is you. There is no such thing as a project ending. There is only the next project starting while the last one still hangs on you.

So the discipline of "start with the dumbest thing" is one an internal reader is better placed to state than anyone, and what he is talking about is his own calendar, not somebody else's architectural taste. Translate it into a sentence you can say out loud in a meeting. "Every extra notch of complexity we pick is another slice of ops headcount this system takes next year, and that headcount comes out of our team's capacity for new projects." The sentence needs no moral position. It is headcount.

The fifth criterion gets stricter in this situation, not looser. When there is a receiving side, handoff day is a mandatory physical. The five self-sufficiency tests (Chapter 22, the ones mentioned in Chapter 3, which test whether the receiving side can run this system on its own) expose the complexity you picked back then on the spot. When the maintainer is your own team, that physical does not exist, and nobody comes to check whether you can maintain what you wrote yourself. The criterion has to be set by you. Suppose this step is being debugged at midnight three years from now by a colleague who has not been hired yet. Could he possibly handle it alone? No answer, and this cell does not pass, by exactly the same standard as when there is a receiving side.

## At Anchor & Helm: Three Steps, Three Pattern Choices

The queue has two steps where AI intervenes, and the engineers' proposed "fully automatic" counts as a third. Take them through the table one at a time.

**Step one, missing-document detection, structured extraction plus rules.** The rules row does not pass in this step. The cell that says "fields only need to be interpretable" does not hold, because emails are free text and have no fields. The first conclusion the decision table produces is an upgrade, from rules to the next row down. The real detail of "waiting for the customer to send documents" lives in the emails (Chapter 9), and this is exactly the job only an LLM can do, understanding a line like "the advance payment receipt will start coming in next Monday." But it is allowed to output only one fixed schema, document type, party to act, promised time, source email number, four fields, and any output outside those fields is rejected.

The rules layer takes the schema and decides how the queue displays and whom to chase. The LLM will still be wrong, but the error is fenced tight inside the extraction step. Schema validation intercepts format errors on the spot, and a weekly spot check of twenty rows watches for semantic errors. In one sentence, put the LLM where its output can be checked.

**Step two, the priority suggestion, rules as the floor and a single-step LLM for the long tail.** Linda's five rules of thumb (Chapter 6) are made explicit as the rules layer, most claims get their suggestion from the rules, and the reason column says outright which rules matched, "report delay + missing photos." The long tail the rules do not reach, signals contradicting each other, a prior claim linkage that looks likely on weak evidence, goes to a single-step LLM, with the output confined to a suggested priority, a reason, and which signals it cited. Either road, every suggestion carries its reason, and the "Human Call" column decides. This arrangement also holds the line Chapter 6 warned about. The rules are made explicit but not hardcoded into if-else that nobody reviews, people keep the decision, and overrides leave a trail. The decision trail is the detector for rule drift.

**Step three, fully automatic processing. Turned down, but let them turn it down themselves.**

At the standup you rule on nothing. You only say, "Interesting design. Block two hours Wednesday afternoon and we will take one table through it. Not judging the design good or bad, filling it in row by row against the criteria. You fill it in."

Wednesday, an empty decision table is drawn on the whiteboard. First row, error tolerance. You ask, "The chase agent's notice goes straight out. Out to whom?" "The surveyor, and in some scenarios the customer." You ask next, "The escalation agent texts the customer automatically. What is the consequence of one wrong text? Who sees it?"

The room goes quiet for a dozen seconds. The older engineer gets there first. Once a text leaves the company it has reached the customer, the error is external and cannot be recalled, and it is the same reason the service chatbot died in the Risk cell in Chapter 7. What an insurer says to the outside is regulated. He writes it into the first row himself. Tolerance near zero, and nobody backstops it, since the whole point of an agent is to route around people.

Second row, verifiability. "Three agents passing work between them, one claim comes out with a wrong result. Which step got it wrong? Does the same input still reproduce it?" The logs look beautiful, but those are the logs of three samples that went smoothly. What the logs of a failure path look like, the demo did not answer.

Third row, data requirements. You raise one number and nothing else. "The detection agent and the escalation agent both consume claim status. In last week's reconciliation, 87 of 200 cannot be taken at face value (Chapter 9). A person who sees 'in progress' goes and checks the emails. Every step of the agent chain acts on face value, and the action goes out the door."

The fourth row never gets filled in. The older engineer puts down his pen. "No need. Inside the advise layer, this thing is not needed. Outside the advise layer, not one criterion passes." He pauses. "The maintainability row I will fill in for myself. When the queue breaks at midnight, tracing an agent chain and tracing 'which rule matched wrongly' are two different lives. The two of us are the ones taking over maintenance." The table stops there, and that is allowed. A table may stop at the first cell that does not pass, and the rest need not be filled in. One cell failing puts the design out, and filling in the cells that remain only supplies material for a design already out.

What you add is not consolation. "The design is not wrong. The layer is. The ladder is still that same ladder (Chapter 8). Let the AI's suggestions earn a record of being accepted before you talk about letting it act. On the day we do talk about acting, whether to use agents is for the eval to say."

The scope decision log gains a line, next to Grant's line from Chapter 8. That line governs which layer decision rights stop at. This one governs the implementation. Multi-agent automatic processing, proposed by the two claims-ops IT engineers, reason for refusal, the errors go outside and cannot be recalled, they are hard to locate, and the data does not support it. Revival condition, once the advise layer's acceptance data hits target and the eval shows that rules plus a single step cannot clear the threshold, move up one layer at a time along the decision rights boundary.

Then you point them at the hardest engineering in the whole system, the extraction pipeline. Emails in, schema out, validation, the spot-check tool. "This is the most technically demanding stretch in the system, and it is also what you two will own later. The prompt inside your detection agent, strip off the agent shell around it, and it is version one of the extractor." The two claim it on the spot. The demo was not built for nothing, the enthusiasm was not doused, it only landed somewhere else. This Wednesday afternoon is the starting point of Chapter 15's co-build (building alongside the engineers who will take over).

If the proposer is your manager, or the Group architecture committee, this meeting has to be run a different way. Across a company boundary, "let the evidence speak" is a neutral procedure by nature. Inside a company, the same move can be read as a subordinate using procedure against a superior, and once it is read that way, whichever cell you win counts for nothing. First do one thing that has nothing to do with the design. Take "ruling by the table" to the sponsor (the executive who funds it and makes the call) as a procedure, once, and once is enough. What you want is not his backing for one design. It is his endorsement of the rule, that every step where AI intervenes gets filled in row by row against the same table, that it stops at the first cell that does not pass, and that the rule treats every proposal alike, including the ones you make yourself. With the procedure endorsed, the meeting is not you against him. It is a proposal against a table.

Then hold three things in the meeting. You are not the facilitator. Ask the business-side owner (the person in the business department accountable for this system) or the proposer himself to chair, and you only ask questions, you do not rule. The conclusion goes into the scope decision log, with the reason for refusal and the revival condition, and not a word about whose judgment is faulty. The table stops at the first cell that does not pass, and whichever cell it stopped at is the cell you record, so the conclusion points at that cell's evidence and not at the proposer.

## Failure Modes

**1. Resume-driven architecture.** Somewhere in the selection discussion comes "this project is a good chance to get fluent in the agent framework." An engineer's market value is calibrated by how new his stack is, a project's success or failure settles three months later, and a resume can be updated the same day. The two accounts settle on different cycles, and people rationally settle the faster one first. Chapter 8 said abstraction is an engineer's identity currency, and on a resume "platform" is worth more than "spreadsheet." Patterns are another kind of the same thing. The newest pattern is worth more than the most suitable pattern, in the labor market, not on the project. Inside a company this account carries on under a different name, whether this project can go into your promotion package, and it still settles faster than the project's success or failure.

And you are not the only one keeping this account. The department's annual report also needs a line that says "we shipped agents," and that pressure runs top down, landing on the line that runs your schedule and your review, which is harder to push back on than one resume.

The defense is procedure, not morals. Every pattern proposal goes through the decision table first, and the criteria do not recognize a resume, nor the wording of an annual report.

**2. The demo's pattern straight into production.** The demo used agents and wowed the room, and once the project is approved "it already runs" carries it forward. Demo and production select on different criteria. A demo is picked for how impressive it is, production for whether it can be backstopped. "It already runs" manufactures the illusion of a sunk cost, and changing pattern looks like going backwards. What this step walks into is exactly the data gap and the ownership gap among Chapter 1's five gaps. A demo's samples are always clean, and a demo's errors are never attributed to anyone. One rule. Build the demo with whatever pattern you like, and any pattern going into production goes through the decision table again.

**3. Putting uncertainty into a step that cannot be wrong.** An LLM-generated amount flows straight into the payout calculation, a generated date straight into a regulatory filing. Probabilistic behavior is invisible on an architecture diagram, where an LLM is only a box and looks the same as a database. Error tolerance is a property of the step, not of the system, and if it is not drawn nobody aligns on it. Once they blur together, the whole system is in fact running to the standard of its loosest step. The defense, mark on the architecture diagram, at every AI intervention point, that step's tolerance and its backstop. For a generated number to enter a deterministic step, there has to be a layer of validation or a person in between.

## Next Monday

1. List the AI intervention points in the system in your hands, mark the current pattern on each step, then ask "why not one notch dumber." For any step where you cannot answer with evidence, drop a notch and try it for a week.
2. Check where every LLM output lands. Is any generated number or fact flowing straight into a step that cannot be wrong (a calculation, a filing, an outbound message)? If so, put a layer of validation or a person in between.
3. Next time somebody proposes an agentic design, do not debate it. Book two hours and have the proposer fill in the decision table in [Template 10](../appendices/template-10-pattern-decision.md) row by row himself.
4. Find where the criterion for "upgrading" is written down in your project. If you cannot produce it, you do not have an eval yet. Go read Chapter 11 first, then talk about upgrading.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 10 Next Monday actions. First, following
templates/pattern-selection/decision-table/prompt-intervention-points.md, list the AI intervention points from the process I
describe, mark each step's current pattern, then for each one ask me "why not one notch dumber." Flag the ones I cannot answer
with evidence. Whether to drop a notch is mine to decide. Then copy decision-table.md to me to fill in row by row. Finally run
python3 templates/pattern-selection/schema-check/check_schema.py and python3 templates/pattern-selection/spot-check/sample_cases.py
with the built-in samples to show what validation and spot-checking look like. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The six-pattern spectrum (rules → structured extraction + rules → RAG → single-step LLM → agentic workflow → fine-tuning, ordered by how clear the error shape is); the pattern decision table (six patterns × five criteria, a judgment in every cell and no scores; pick per step, read top down and stop at the first that passes all five, upgrade only on eval)
- **Templates.** [Template 10](../appendices/template-10-pattern-decision.md), the Pattern Decision Table and Anti-pattern List, the full decision table ready to copy, how to use it, anti-pattern warning signals and their corrective actions
- **Key judgments**
  - "Enterprises have no demand for 'occasionally impressive.' They have a hard requirement for 'when it is wrong, it can be caught, attributed, and rolled back.'"
  - "Start with the dumbest thing, and let the evidence force the upgrade. The only legitimate reason to upgrade is eval data showing that the dumber pattern cannot clear the threshold."
  - "A pattern's popularity and its applicability are badly decoupled. The hottest is precisely the one with the narrowest applicability."
  - "Put the LLM where its output can be checked."
