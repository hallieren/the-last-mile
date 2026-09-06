# 23 · The Pattern Library: Turn Hero Stories into Assets

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-23-pattern-extraction.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** Every project feels like starting from zero, and the team gets through on individual heroics. How do you make the second project cost half of what the first one did?
>
> **What You Will Be Able to Do.** Use the field learning flywheel to turn a project retrospective into reusable assets. Build a pattern library that will not rot, using the four asset classes and the three admission criteria. Before the next project starts, tell apart what can be carried over as is and what has to be dug out from zero.

---

> **Part VI Navigation.** Chapters 23 and 24 are two angles on the same asset inventory, Monday of week 30. Chapter 25 goes back to the quarterly business review in week 28, and Chapter 26 is the weekend of week 30.
> The quarterly business review, where you say no (week 28, Chapter 25) → the last retrospective (Friday of week 29, Chapter 22) → the asset inventory (Monday of week 30, this chapter and Chapter 24) → Swiftway's whiteboard (week 30, this chapter) → two ledgers (the weekend of week 30, Chapter 26) → week 1 of the home queue (week 34, this chapter)

## Week 30, Another Whiteboard

The week after the last retrospective at Anchor & Helm, you are standing in a meeting room at Swiftway Logistics. Swiftway is another subsidiary of the Group, a mid-sized logistics business, and the Group has routed its ask to your team. The ask, in their own words: "Build an AI dispatch assistant."

The VP of Operations spends twenty minutes on the current state. Exception waybills pile up at the dispatch desk, drivers chase for assignments in the group chat, a waybill marked "delivered" in the system is not delivered and "in transit" is not in transit, and the dispatch team lead keeps a scheduling spreadsheet that the whole team treats as the only real one.

You stand at the whiteboard for ten minutes without writing a word. In the tenth minute you understand why nothing comes. Ideas are not missing. The ideas are suspiciously familiar. Exception waybills piling up is exception claims piling up. Drivers chasing for assignments is customers chasing claims. A status field you cannot trust is the core system's "in progress." The dispatch team lead's private Excel is the sheet Linda kept for six years.

You have seen this project before. It is Anchor & Helm with the nouns swapped.

The problem is that this "seen it before" lives, right now, in the back of one head, yours. When the Group routed the ask over, the schedule was set as starting from zero, and it eats into your team's headcount for the year. If the person standing at this whiteboard today were any colleague of yours who never worked Anchor & Helm, he would start from week 1 interviews and step into every hole you stepped into over those twenty-nine weeks, one for one. The organization does not know it already knows how to run this class of project. It only knows that one person pulled one off. That is the difference between a hero story and an organizational asset. This chapter is about turning what sits in the back of your head into what sits on the shelf.

## Why This Is Hard: Custom on the Surface, Reusable Underneath

A deliverer's work looks custom every time. Different industry, different systems, different vocabulary, different people across the table. So the organization assumes none of it transfers, and your team degrades into supplying a body to each department in turn. Headcount is fixed, so one more department means overtime, or a refusal, and the price of refusing is in Chapter 25. Scale produces no leverage, and capacity is locked to headcount. That is the ceiling of an internal delivery team. What separates this role from that ceiling is a bet that a reusable layer exists across projects, and that it thickens the more you accumulate (Palantir, mentioned in Chapter 2, is the company that turned that bet into a method, and the name of this role is one it made popular).

Where is the reusable layer? Not in the code. Move the exception queue's code to Swiftway and it dies on the field names on day one. What is reusable is the judgment structure. The exceptions queue and the waybill queue share one skeleton. Find the private source of truth → three-way reconciliation (the system field, the manual sheet, and the person handling it, cross-checked) → action queue → decision trail → adoption mechanisms. It took you twenty-nine weeks at Anchor & Helm to see this structure whole. At Swiftway's whiteboard it took ten minutes.

Two structural facts make it hard. The first, a judgment structure hides in people by nature, not in things. The things a project leaves behind, the repo, the documents, the configs, go to the business line under clause one of the co-build agreement (Chapter 15), and they all sit on the Group's own GitLab, and the organization forgets anyway, for three reasons. A reorganization comes, teams split and merge, and nobody claims the assets. Repos scatter across subsidiaries and outside contractors, and nobody can say how many copies exist. The judgment structure was never written down, the code is there and "why it was designed this way" is not. The day someone changes posts, all three fire at once. The second structural fact, nobody owns admission. The retrospective ends and people are scheduled onto the next department's ask. Accumulating assets is important and not urgent, the same lesion as starting the handoff too late (Chapter 22's failure mode, where the important and not urgent always gives way). Without an explicit mechanism, every generation of deliverers reinvents the same wheel, and the organization pays full price for each reinvention.

## Prior Art, and What AI Changed

**Maister's practice economics.** David Maister's argument in *Managing the Professional Service Firm* (paraphrased), how much output a professional services organization can move is decided not by how smart it is but by its leverage structure, how much delivery by non-senior people a senior person's judgment can move. Leverage comes from two things, reusable IP (methods, templates, tools) and the master-apprentice ladder (judgment passing down the ladder). The argument does not care who employs you. A team with neither, however good, is a set of expensive sole traders sharing a department name.

**The SRE runbook tradition.** Google's SRE practice writes down the knowledge of firefighting at midnight as a runbook. The engineer on duty facing an alert opens what a predecessor wrote, check this first, then that, escalate at this point. The core insight is that turning the hero moment into a checklist raises the organization's floor from the worst person on the team to the checklist. A pattern library is the same thing at project scale.

**What did AI change? A double-edged blade.**

The good side, the carrier of an asset moved up. A runbook can only be read by a person. A pattern library can also be fed to a coding agent. An agent carrying the queue skeleton, the decision trail schema, and the reconciliation checklist in its context starts the next project at 80% of a skeleton instead of an empty folder. For the first time an asset can become productive capacity directly, without passing through a person reading it and retelling it.

The bad side, the cost of pollution collapsed to zero. One prompt gets AI to produce a professional-looking playbook, complete in structure, standard in vocabulary, with no field provenance at all. On the shelf it looks exactly like a real asset, right up to the day the next project starts from it and it blows up. So the first principle of building a library in the AI era is that the admission standard matters more than the library. A pattern with no field provenance is a negative asset, worse than an empty shelf, because it occupies trust in the shape of an asset.

## The Core Framework: The Flywheel, the Four Classes, the Three Criteria

Two definitions first. **Pattern**, a reusable practice that still holds once the field context is stripped off a specific project. **The pattern library**, an organization-level store that accumulates patterns under one admission standard. A full set of patterns for one class of project, from discovery (finding out how things actually are) through to handoff, is together called a **playbook**.

**The field learning flywheel** makes accumulation a loop rather than a one-time action.

```
deploy (deliver the project)
  → capture (the closeout retrospective produces candidate patterns)
  → generalize (strip the field context, write where it applies and where it does not)
  → reuse (field-test it on the next project)
  → feed back and revise (the test results go back into the asset) → back to deploy
```

The flywheel breaks most easily at two points. Capture has no owner (the retrospective ends and everyone leaves), and reuse has no feedback (it works badly, nobody fixes it, and the asset stays at 1.0 forever). So every step needs a named owner, the same as every metric on the metric tree (Chapter 18).

Inside a company there is one more break. The moment of capture never arrives at all. There is no closeout event. The first project has not wrapped up and the second department's ask is already on the schedule. You have to manufacture the moment, and there are two ways to hang it. Hang it on the first week after the responsibility transfer agreement (Chapter 22) is signed, or hang it on a retrospective a fixed number of weeks after launch, written into the project approval resolution so the meeting happens automatically when the date comes due, without waiting for anyone to remember. Anchor & Helm used the first, Monday of week 30.

**The four asset classes.** Different assets are reused in different ways. Mix them together and the library becomes unusable.

| Class | What It Holds | Anchor & Helm Example | Reuse Profile |
|----|------|---------|---------|
| Template | Documents and process | The charter template, the three-layer probing script, the four adoption mechanisms | Easiest, usable across industries as is |
| Component | Code and schema | The queue skeleton, the decision trail schema, the extraction pipeline interface | Medium, needs adapting to the data source |
| Judgment rule | Transferable judgments | "Chase priority ≠ risk priority", "If you cannot say it, do not merge it" | Carried away in one sentence, with the boundary attached |
| Metric model | The structure of a metric definition | The three tiers of the metric tree, the error severity vocabulary | Swap the North Star, keep the structure |

**The three admission criteria.** All three pass or it does not go on the shelf.

1. **At least one field validation.** Running in a demo does not count. Surviving on the business side's floor counts.
2. **A written boundary.** Where it does not apply is worth more than where it does.
3. **A named owner.** An asset with no owner rots in six months. The vocabulary goes stale, the links break, it drifts from reality, and then it starts misleading people. What is frightening about rot is not that the asset stops working. It is that it keeps being cited after it stops working.

Two rules that exist only inside a company. One, the owner column often holds a real name from another team, the platform team or the engineering productivity team, and you have no authority to hand another team an owner role. There are only two routes to a claim. A shared manager settles it in one meeting, or you push the library into a carrier that already exists, the company knowledge base, the platform team's component repo, the architecture review checklist, so an existing owner picks it up along the way. Two, the library has to declare its force level, reference, recommended, or mandatory, one of the three, written on the library's front page. Declare nothing and it is taken as mandatory by default, and every time a business department finds it awkward to use, that is on you.

Turn the flywheel one more notch and the carrier of an asset can move up another level, straight into an agent. Teams doing deployment engineering are already on this road (from several teams' talks in 2026, paraphrased. Some give every delivery engineer a delivery-cycle assistant agent, some let an agent take over the first half of the way from gathering requirements to writing the spec, and some make automating themselves out of the job a team goal). Put inside this framework, it is not a fifth asset class. It is the executable form of the four classes. The reconciliation checklist grows into a reconciliation agent, the three-layer probing script grows into an interview preparation agent.

Two rules do not move. The three admission criteria still apply, and field provenance is waived for nothing. What an agent produces is always a draft, and the standard and the boundary are ruled on by a person. A deliverer who uses AI to amplify the business side's front line should also use agents to amplify himself. In Maister's leverage structure this is the third lever, after reusable IP (methods, templates, tools) and the master-apprentice ladder (judgment passing down the ladder).

## From Anchor & Helm to Swiftway: A Reuse Field Test

**Monday of week 30, the team's own asset inventory.** It is a different thing from the week 28 account of the launch given to the business side (Chapter 24 writes this meeting from another angle). That one had Grant Whitmore in the room, it was the account for the business side, and it came first. This one has only your team, hung on the first Monday after the responsibility transfer agreement was signed. The queue's weekly retrospective carries on as usual, and the last one you attended (Friday of week 29) came after that account, with this inventory last of all. The meeting has one rule. Do not ask how the project went. Ask only what here the next project can still use. That is capture.

First on the admission list, in the component class, is the extraction pipeline interface. In Chapter 8 you said one sentence to the claims-ops IT engineer, "Whoever writes it keeps the interfaces clean. That is the first brick of the future platform." At the time it was a line for catching enthusiasm. Now it cashes out literally. Emails in, schema out, validation, the spot-check tool. The interface has nothing to do with the line of insurance. Strip off Anchor & Helm's fields and it takes waybills. First brick, admitted. The rest go in by the four classes.

- Components, the queue skeleton and the decision trail schema.
- Templates, the three-way reconciliation checklist, the four adoption mechanisms, the three-layer probing script.
- Judgment rules, "chase priority ≠ risk priority," with a boundary of any ranking scenario where the people being served can apply pressure.
- Metric models, the metric tree structure and the error severity vocabulary.

The same meeting went through the three lines on Chapter 8's revival list. Home property, whose revival condition "the first extension after the pilot North Star hits target" held in week 26, is on Anchor & Helm's own agenda. Full automation still moves up the decision rights ladder one layer at a time, each layer decided on its own, and is not opened here. The general platform's revival condition reads "after the second slice lands, distill what is common and revisit." Nobody knew then who the second slice would be. Now it is known, Swiftway. And distilling what is common is itself the pattern library. The way that revival condition is honored is by becoming this chapter.

**Weeks 31 to 32, Swiftway discovery, two weeks.** Anchor & Helm took six weeks from taking it on to settling the reconciliation. Swiftway took two. These carried over as is. The queue skeleton (waybills replace exception claims, the column structure unchanged, suggested priority, suggested next action, reason, owner, Human Call, not one column missing). The three-way reconciliation method (the system field, the dispatch team lead's Excel, asking the handler, and in week 1 it located the largest single class of waybill status mismatch). The four adoption mechanisms (pick the super-user by influence, and the dispatch team lead who maintains the scheduling spreadsheet is Swiftway's Linda candidate). Plus the three-layer probing method for mining tacit knowledge, anchor on an instance, compare, boundary counterexample, works as is.

The grunt work of reconciliation was not written from scratch either. The admitted reconciliation checklist, together with its boundary, was fed to a coding agent, which generated the sampling and comparison scripts. People ruled only on the standard and on who owns the source of truth.

What has to be dug from zero is just as clear. The golden cases are all new. A waybill is not a claim, and not one carries over. The rules of thumb reset to zero. The dispatch team lead's "one look and I know this one is going bad" runs on a combined feel for shipper, route, and driver, and does not overlap the repair shop list by a single word. You mined for two afternoons with the three-layer probing method, and every rule that came out was new. Not one of them came from Anchor & Helm.

| Class | Carried Over As Is | Has to Reset to Zero |
|----|---------|---------|
| Template | The three-way reconciliation method, the four adoption mechanisms, the three-layer probing method | What goes into the templates. The super-user is picked again for the new field |
| Component | The queue skeleton, waybills replacing exception claims, not one column missing | Fields and data sources. Move them over and they die on the field names on day one |
| Judgment rule | Sentences that hold across scenarios, like "chase priority ≠ risk priority," with the boundary attached | The rules of thumb. The dispatch team lead's combined feel does not overlap the repair shop list by a single word |
| Metric model | The metric tree structure and the error severity vocabulary | The golden cases. A waybill is not a claim, and not one carries over |

> **Tacit knowledge does not transfer. The method for mining it transfers.** Chapter 6's line, "'Seeing that the Excel exists' is in no dataset," gets its second confirmation here.

There is one asset an outside team can never accumulate, and it belongs to the metric model class. The auto and home property queues share one decision trail schema, so the override reason codes can be laid side by side, and the overlapping part is a company-level answer to which kinds of judgment AI is not trusted on. The waybill queue will be the third once it launches. An outside team is bound by confidentiality and cannot aggregate across companies. You do not have to wait for anyone's approval. All three queues sit in the Group's own warehouse, and one query gets you the table. Register it under the metric model class, owner column, yourself.

The four weeks saved are the pattern library's price. They land on no invoice. They land on capacity. Your headcount is fixed, so four weeks cash out as a few more departments covered this year, and the half the second department is cheaper by is capacity, not money. Only you keep this account. The business side sees a system go live and does not see the four weeks you did not spend. Owen Hartley's inventory sheet carries headcount, not weeks. So the bookkeeping has to go into the asset register. Log the weeks saved on every reuse, and at the annual review that column is a number you can write down, with no need for vague phrasing like "efficiency gains." The part where the second project is cheaper than the first is the interest the organizational asset pays.

These two weeks held one more deliberate arrangement. The person running the reconciliation changed. The engineer on your team who had worked Anchor & Helm took the reconciliation checklist and led the writing, and you only gatekept. The three explain-it questions moved up a level, from the claims-ops IT engineer explaining it to you (Chapter 15) to your apprentice explaining it to you. This is where Maister's leverage structure lands, reusable IP × the master-apprentice ladder = capacity. The IP saves the apprentice from working it out from nothing, and the ladder saves the IP from having to be executed by your own hands. As for Swiftway's dual Group-and-subsidiary structure, that is another kind of training ground, and the last chapter takes it up.

**Week 34, an email.** From Kevin Doyle, subject line "week 1 of the home queue." The body says the home property exceptions queue went live and the run chart put down its first point. The whole thing reused that one set of patterns from the auto queue. Linda led the annotation build, supplying the method and not the judgments, with the disagreement records, the ruling process, and the guide format all following the rules set back then, and the judgments themselves coming from home property's own reviewers. The claims-ops IT engineer changed the configuration and shipped it, with little new code written. The golden cases were gathered from zero, and they knew on their own that they had to be, with nobody reminding them.

The escalation tree caught two new exceptions, and one of them was not free. Priorities were ranked wrong for half a day, and the escalation path caught it and routed it to manual only in the afternoon. The balancing metrics raised a small bump that day and came back down the next, and the incident case went into the golden cases that evening. The last line of the email. "Did not have to bother you this time."

You checked. The exit date you set yourself in the responsibility transfer agreement (Chapter 22) has two months left. P1s received, zero. Nobody is coming to revoke your access. You wrote that date yourself, and you are the only one watching the countdown.

This email is proof of three things. First, the end of Chapter 22 said the home property revival condition formally held and went on the agenda, and that it was the next chapter's story. This is the story. Second, L4 was defined in Chapter 1, the business side can run, maintain, and improve it on its own. The highest form of improving it is opening a second front with the same method, and fixing bugs is only the start. Third, the playbook's first reuse was done by the business side, with no hand from you. The best acceptance a pattern library gets is that it runs when you are not in the room. And home property's rules of thumb were dug from zero all over again, the third confirmation that tacit knowledge does not transfer. This time, not even the digging was yours.

## Failure Modes

**1. Keeping the code, not the judgment.** The library is all repo links and starter kits, with not one sentence of "why." Code is visible, countable, and can be signed off. A judgment structure is none of the three. What gets kept is decided by what is easy to appraise, not by what is worth something. But code becomes scrap in another industry (the field names kill it on day one), and a judgment structure does not. The test, if the library has fewer words on when this does not apply than on code comments, what you left behind is a specimen, not an asset.

**2. Assets with no owner, and the library becomes a document graveyard.** The last team's "best practices" lie on the wiki, and nobody knows which of them are still alive. Building a library is a project. Keeping one is operations. Organizations will approve and decorate projects, and will not reserve headcount for operations. Leave the owner column blank and the updates sit forever behind everything urgent. Six months later nobody dares use anything in the library. Someone burned once by a stale asset never comes back. The test, pull three assets from the library at random and check whether the owner column holds a real name and which project the last revision came back with. The ones you cannot answer for are already in the graveyard.

**3. Treating custom work as reuse, forcing the answer to fit.** Taking Anchor & Helm's answers to Swiftway and deploying straight past discovery. The pleasure of reuse eats the sense of boundary. Taste the sweetness of saving four weeks once and you want to save six. And a pattern's boundary is written in the least conspicuous column of the register, which the people racing a deadline never read. The result is the five gaps stepped into again on the spot. The golden cases are auto's, the rules are Linda's, and the adoption mechanisms have no super-user of Swiftway's own. The test, if nothing on your "reuse" list is ruled "has to be redone," what you are doing is forcing a fit, not reusing.

**4. Retrospectives that write down only successes.** The library is all winning moves and not one way to die. A retrospective is a social occasion, and writing down a failure names the person responsible, so failures get smoothed into three lines of "lessons learned" and the information about where the real holes are evaporates at the meeting room door. But failure modes are the most valuable entries in the library. Every project's successful path looks different. The holes are the same batch of holes. The book you are reading has a "Failure Modes" section in every chapter. That is not a writing preference. That is the same discipline applied to a book. The test, count the output of your last retrospective, how many winning moves and how many ways to die. Ways to die at zero, and those notes are a victory record, not an asset.

**5. Filling the library with AI-generated entries.** The problem has two layers, that the count rises fast, and that what comes up has been validated by nobody. The library swells from 12 entries to 200 in one quarter, every one of them impeccably tidy. Once building the library carries an entry-count KPI, AI is the perfect tool for running up that KPI, and professional-looking is exactly what a large model is best at producing. Trust in a library is indivisible. Someone burned by one fake pattern doubts all two hundred. The defense is not deleting the library. The defense is at the door. Library admission has to be able to answer which project, which weeks, who was in the room, where the validation record is ([Template 23.3](../appendices/template-23-pattern-extraction.md)). AI can draft, structure, and rewrite. The one thing it cannot supply is field provenance. The test, look at the library's growth rate. The stretch where the entry count grew faster than the project count is the stretch with no field provenance.

!!! note "Vendor View"
    The vendor side's pattern library carries a price tag. The four weeks saved land on the quote, four weeks of day rate not billed, and the pattern library is what gives a firm the nerve to price on outcome instead of day rate. Your four weeks land on capacity, an account only you keep, so the bookkeeping has to go into the register.

## Next Monday

1. Reopen the retrospective of your most recently finished project for 30 minutes and ask one question only. "What here can the next project still use?" Force out at least one entry in each of the four classes, and strip the field context with [Template 23.1](../appendices/template-23-pattern-extraction.md).
2. Write a "does not apply when" line for every candidate asset. The one you cannot write is not admitted. If you cannot write the boundary, you do not understand it yet.
3. Find a "best practice" on the team wiki that nobody has touched in over six months, and check its owner and its last field validation. Both come back missing, run it through 23.3. Re-claim it, or delete it.
4. Pick one validated component-class asset, feed it together with its boundary to a coding agent, and have it generate the next project's skeleton in a sandbox. See how far that is from ready to start. The gap is the part of the asset you have not written down clearly yet.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 23 Next Monday actions. First run python3 templates/pattern-library/downgrade_stale.py
with the built-in sample to show the demotion output for stale assets, then open asset-register.md and pattern-template.md. The candidate assets I name during the retrospective,
you strip of field context in the 23.1 format and write up as drafts. The "does not apply when" line for each is mine to write, and the one I cannot write you mark "not admitted."
Last, read through packing-example/ and tell me which fields are needed to feed an asset together with its boundary to a coding agent.
Which asset gets fed is my pick. If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The field learning flywheel (deploy → capture → generalize → reuse → feed back and revise); the four asset classes (template / component / judgment rule / metric model); the three admission criteria (one field validation / a written boundary / a named owner)
- **Templates.** [Template 23](../appendices/template-23-pattern-extraction.md), Pattern Extraction Sheet, Asset Register, Library Admission Checklist
- **Key judgments**
  - "What is reusable is the judgment structure, not the code."
  - "Tacit knowledge does not transfer. The method for mining it transfers."
  - "An asset with no owner rots in six months."
  - "The four weeks the second project saves are the pattern library's price."
  - "The admission standard matters more than the library. A pattern with no field provenance is pollution."
