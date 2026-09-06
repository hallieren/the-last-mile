# 15 · Co-build with the Engineers Who Will Take Over: Handoff Starts at the First Line of Code

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-15-cobuild.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The claims-ops IT engineers have no time, uneven skill, and a fear of being replaced by AI. "Co-build" sounds fine, and the reality is silence in meetings, assigned tasks done, and never a step taken unasked. And once you move to the next project, they are the ones maintaining this system.
>
> **What You Will Be Able to Do.** Use the four clauses of the co-build agreement (code ownership, backward staffing, the AI code review rule, the rotating release) to turn "an audience on loan to help out" into the owners on handoff day. With an AI coding agent taking part in development, hold the line on "understanding the code and being able to evolve it."

---

## Week 5, Two Engineers "Helping with the Project"

This chapter's story runs backward. It starts in week 5, four weeks before the last chapter's escalation decision meeting.

After the charter was signed, Kevin Doyle dialed in two engineers to "help with the project." Their first week in, the behavior pattern went like this. On time to the weekly, seated nearest the door, answering when asked. Assigned tasks finished on time, done to the spec and not one line further. The interface integration you assigned, done. The edge cases nobody assigned, untouched. Their second week in, identical.

This is not a capability problem. In the days around the charter signing they showed up at the system boundary discussion carrying a sketch for a general-purpose platform (Chapter 8), the kind of thing only people who want to build draw. You politely filed the sketch under "after the second slice," and from then on they placed themselves as an audience on temporary loan. This is your project, and they are here to "help."

The danger is not in front of you. It is at the finish line. On handoff day in Chapter 22, these two are the ones taking this system over. Whether they are co-builders now decides whether what you hand over that day is capability or a legacy.

You have already seen half of where this line goes. Monday of week 7 they brought a multi-agent demo, and at Wednesday afternoon's decision table meeting the enthusiasm was not doused, it only landed somewhere else, on the extraction pipeline, which the two claimed on the spot (Chapter 10). This chapter is the other half, how that Wednesday afternoon's claim becomes one page of agreement and one cadence that runs all the way to handoff. The moment is project week 9, the few days after the pilot is called and before it starts on Monday of week 10.

## Why This Is Hard: What Stops Them Is Identity, Not Skill

There are two default explanations for "the co-build engineers are not invested," not skilled enough and no time. Both are usually true, and neither is the root cause. The root cause is that in a story about "doing work for another department," they have no place where they can win. Their appraisal sits on the claims operations line, the project sits under the Digital Center's name, and those two things are not in the same place.

Do their arithmetic. If the project succeeds, the credit is booked to the Digital Center, and in the year-end report it is "the Digital Center's AI project." If the project goes wrong, they are buried next to it, because the system runs in claims operations and the person woken at midnight is from their own department. Through the project their own job still presses down, their performance targets are not cut by a point, and the appraisal form has no line for "helped with a project." Do more, get more wrong. Do less, nobody blames you. Silence in meetings and assigned tasks done is the rational strategy from that seat, the same rationality as the reviewer saying no in Chapter 12. The burst behind the multi-agent demo does not contradict it. That was people who want to win looking for a place to win, and when they could not find one, they retreated to the audience. This account is harder to see than "doing work for outsiders." Inside one company there is no word for "outsider," so the account hides inside the appraisal lines.

There is one more thing they will not say to your face, the fear of being replaced by AI. Inside a company that fear is sharper. The people being taught are colleagues, and colleagues do not leave. At next year's headcount review, "the Digital Center has already taken those modules" is a ready-made reason to move someone to another post, and layoffs and reassignments inside one company are things that actually happen. The better you teach, the faster it comes, with none of the buffer an outsider provides. The fear is not an illusion. It is only pointed at the wrong object. What gets replaced is writing code to a spec. What cannot be replaced is the person who knows why this code is written this way and where to start looking when it breaks at midnight. So the place where they win has to sit on the latter. The face-to-face explanation and the turn on stage in the four clauses below both move their value from how fast they write to how well they see. Leave this fear unanswered and they will not dare take ownership or visibility, because taking it would be admitting they are training their own replacement.

You have rational arithmetic of your own. Doing it all is faster. Teaching two people is slower than doing it yourself, slower every single day. The cost of co-build lands immediately, and the payoff settles only on handoff day three months out. Inside a company the account is worse, because nobody sets the handoff date for you and the settlement day can keep sliding. Stack both sides' rationality and you get a stable bad equilibrium. You do everything, they watch everything, and on handoff day all the code becomes a legacy.

So co-build is a design problem, and attitude will not solve it. Give them a place where they can win. Code ownership (an asset in their name), skill growth (capability they can take with them), internal visibility (Kevin can see their names). All three have to be designed. Not one of them happens on its own.

## Prior Art, and What AI Changed

The first source is the apprenticeship model. David Maister's argument in *Managing the Professional Service Firm* (paraphrased), the leverage in professional services comes from the master-apprentice structure. A senior person's judgment passes to a junior one through working side by side, and learning by doing is the only transfer method validated over and over. Your relationship with the engineers taking over is, at bottom, an apprenticeship with an expiry date. Inside a company nobody sets that date for you, so set it yourself. Borrow Chapter 22's five self-sufficiency tests (the check Chapter 3 mentioned, whether the receiving side can run the system on its own), and on the day you sign the agreement write down the expected graduation date, which is the week all five pass. Without that date the apprenticeship degrades into pairing forever. What you leave behind is not only the system, it is the way of building systems like it (Chapter 23 lifts this model to the team level).

The second source is the co-build discipline of *Flawless Consulting*. Chapter 1 quoted Peter Block's warning, no deliverable however good can save a counterpart who never truly committed, and the remedy is to make that counterpart a co-builder, with responsibility split 50/50. This chapter is the implementation half. Co-build does not run on invitation. It runs on structure. Ownership, staffing and cadence all get written down.

What did AI change? Both the economics of co-build and its object were rewritten.

On economics, "the business line cannot spare anyone, there is not enough capacity" used to be the all-purpose excuse for your team doing everything. Today agents do the grunt work, the scaffolding, the boilerplate, the test cases. People spend their time on judgment and understanding, and how far a small team can push is no longer decided by headcount. The capacity excuse has expired.

A new risk came with it. A coding agent generates code far faster than a human being understands code. If nobody truly understands it, what you hand over is a pile of black boxes that run and cannot be changed, worse than no code at all, because it manufactures the illusion of an asset. Hence the sentence below.

> **In the AI era, what co-build has to transfer is the ability to understand and evolve code. The code itself keeps getting cheaper. The people who can evolve it keep getting more expensive.**

## The Framework: The Four Clauses of the Co-build Agreement

> **The co-build agreement, one page, turns co-build from a wish into a structure. Four rules, signed by both sides, in force before the pilot starts.** (Template at [Template 15](../appendices/template-15-cobuild.md))

| # | Clause | What It Says | What It Prevents |
|---|------|------|-----------|
| 1 | **Code ownership goes to the receiving side** | From day one all code sits in modules under the name of the receiving side. CODEOWNERS (the list with the right to review and merge that module's code) names them, merge rights are theirs, oncall (on-duty) ownership is spelled out. You commit as a collaborator | The "your project" story; changing the owner only on handoff day |
| 2 | **Backward staffing** | Split the work by "whoever maintains it after handoff leads the writing now," not by "who is faster now" | All the core work going to your team, the receiving side left with chores |
| 3 | **If you cannot say it, do not merge it** | AI-generated code must be reviewed by the maintaining side and explained by them face to face, why it is written this way, where it can go wrong, how to change it | Black boxes that run and nobody can change |
| 4 | **Biweekly rotating release** | Every two weeks, a co-build engineer, not you, demonstrates progress to the owner | Co-build engineers being invisible inside the organization |

Take the four one by one. The two most easily faked are clause one and clause three, one faked when ownership exists only on paper, the other when the explanation is required of the receiving side alone.

**Clause one.** Ownership is not symbolic. Inside one GitLab, ownership has to land in three places to count. The module's CODEOWNERS names the receiving side, merge rights are theirs, and the oncall rotation spells out who owns these modules. CI (the checks and builds that run automatically after code is committed) and the release process follow the business line's existing setup from day one, so on the day you move to the next project there is no such thing as "changing the owner." Ownership also flips the psychological default. In modules under your name they are visitors. In modules under their name you are the visitor. Your AI team should not be the long-term owner of these modules. Inside a company that sentence has no exit date behind it, so two things have to enforce it. Next year's staffing budget reserves no ops headcount for this system, and on the PMO's AI system transfer ledger the owner column for these modules carries a real name from the receiving side. Those two of the three mandatory handoff mechanisms (Chapter 22) get used from the day the agreement is signed, not from handoff day.

**Clause two** connects straight to Chapter 22. The handoff begins with this staffing sheet, and does not wait for a ceremony at the finish. Leading the writing is not writing alone. The lead writer is accountable for the code, can explain it, and decides on merges. The other side pairs and reviews, and the gap narrows in every pairing session.

**Clause three** binds both sides. Code you generated with an agent has to be explained to them too. The "explanation" is tested by a different set of three questions ([Template 15](../appendices/template-15-cobuild.md)), not the three oversight questions of Chapter 12. Why is it written this way? Where can it go wrong, and how would you find out? If it has to change, where do you start?

**Clause four** turns "internal visibility," that place to win, into an institution, and neither a training session nor a status report is the point of it. Whoever stands up and demonstrates gets the credit. The person on stage is an engineer from the receiving side, and the audience is his own supervisor, not yours.

Who the four clauses get signed with depends on which kind of receiving side you have. Inside a company the co-build counterpart comes in three shapes, and the agreement changes with them. Anchor & Helm is the last row, the business line's own IT.

| Shape of the Receiving Side | Who the Co-build Counterpart Really Is | How the Four Clauses Change |
|---|---|---|
| One team, your team keeps the system itself | No engineers to hand it to, so the counterpart is the operations staff on the business side | Clauses one and two spin free. Clauses three and four apply to the operations staff, and what gets explained is rules, thresholds and exception handling, not code |
| A platform team | They keep general capability only, not your business modules | Clause two's "whoever owns it later" gets answered with "not us." Settle before signing which modules go to the platform and which stay on the business line. If that cannot be settled, do not sign |
| The business line's IT | Appraised on the business line, closest to this chapter | Use all four as written. Anchor & Helm is this one |

## At Anchor & Helm: One Page of Agreement, Two Firsts

**Thursday of week 9, signing the agreement.** The pilot was called on Monday (Chapter 13), the escalation decision meeting closed on Wednesday (Chapter 14), and on Thursday afternoon you get Kevin and four engineers into one room, two from the Digital Center and two from claims-ops IT, the same six weeks of headcount Grant approved for the merged view, and put the four clauses on one page. The staffing sheet is filled in backward.

| Module | Maintainer After Handoff | Lead Writer | Pairs |
|------|-------------|------|------|
| Extraction pipeline (emails in, schema out, validation, the spot-check tool) | Claims-ops IT | Claims-ops IT | Digital Center |
| Queue core (sorting, decision trail, the Human Call flow) | Claims-ops IT (longer term) | Digital Center | Claims-ops IT |
| Merged view (derived from two sources of truth, six weeks) | Claims-ops IT | Digital Center (lead-writer rights handed over before handoff) | Claims-ops IT |
| Rules and de-identification as configuration | Claims-ops IT | Claims-ops IT | None (Chapter 12's maintainability row, about a week) |

Claims-ops IT leading the extraction pipeline is not a favor. They claimed it on Wednesday of week 7, and the prompt inside the detection agent, with the agent shell stripped off, is version one of the extractor (Chapter 10). On the queue core you lead the writing and they pair. Its complexity right now is beyond them, but "the longer-term maintainer is claims-ops IT" is written on the sheet, so the pairing has a direction. Before signing, Kevin asked exactly one question about cost. "Whose account does their time come out of?" The project's, you said. Inside a company a project has no ledger, so that sentence has to land in two things to count. One is Kevin committing weekly hours in writing as their supervisor, written into this agreement's commitment clause, a clause of the same rank as Linda's team's 2 hours a week. Where the company has chargeback (cost transferred between departments, charged to whoever uses it), those hours are booked to the project, and the bill does the reminding for you. The other is one line each in the two engineers' quarterly objectives, lead writing and gatekeeping on these modules.

Cost has a second question, who carries their own day job. Booking the time settles only where the account goes, not who does the work, and only Kevin can answer this one. It cannot be left to two people squeezing their evenings. His only real answer is a reshuffle. Their existing schedule gives up the matching hours, and who takes them and in which week goes into the same agreement. Clause four's rotating release is the companion to it. Kevin sees with his own eyes every two weeks what this investment produces, and the reshuffle does not quietly slide back.

**Clause one** is harder to negotiate than the staffing, because it has to get through Victor Reyes's gate (Chapter 12). The conclusion first, read-only on the whole repo, write access on the modules named in the agreement. Here is how it went. Group people holding write access to a subsidiary's code repository is not something he grants by default. Code repositories are tiered for approval the way data is, he approves cross-subsidiary access one request at a time, and the detail table carried out of the company two years ago is the reason. The way out is not whether you can get in, it is what someone who gets in can touch. What you proposed is read-only on the whole repo, write access only on the modules named in the agreement, and the merge itself pressed by someone from claims-ops IT. It shares a root with the permission inheritance he set for the queue, no separate account system, and whoever can touch this in the core system is who can touch it in the repo. If even restricted write access will not clear approval, what gives way is still not ownership. You commit on a restricted branch opened inside the same repo, CODEOWNERS and CI stay on the claims operations side, and on handoff day there is still no such thing as "changing the owner."

**The first "if you cannot say it, do not merge it."** In pilot week 1 the younger engineer submits the email pull retry logic of the extraction pipeline, generated by an AI coding agent, all tests green. At review you ask only the first of the three questions. "Why three retries, and why does the interval double?" He pauses. "That is how the agent wrote it, and it runs." By clause three, sent back. Things were stiff afterward. The code is not wrong, so why not merge it? You slide the agreement across. The code passes, the explanation does not. When this code breaks at midnight, the person woken up is him, not the agent. Two days later it comes back, the retry ceiling, the backoff strategy (wait a little longer before each retry after a failure), which dead-letter queue (the queue that collects messages that keep failing) failed items land in, and he has had his hands on every one of them and can explain each. He said something himself that you still remember. "This time I know why it is written this way."

There is a second thing after that rejection. You hand over enforcement of the rule as well. From that week merges on the extraction pipeline are gatekept by the older engineer, and you are no longer this module's gatekeeper.

**The first rotating release.** Friday of pilot week 2, the first beat of the biweekly cadence. The people on stage are them, not you. The spot-check results of the extraction pipeline against two hundred real emails, the accuracy of missing-document detection, and a live walk-through of three extraction errors, what a wrong one looks like and how the spot check caught it. You sit in the audience and say nothing the whole time. Afterward Kevin keeps them back for another ten minutes. You notice one detail. For the first time he says both their names. For the six weeks before that, in Kevin's mouth they had been "those two I gave you."

Internal visibility starts compounding from that day. The rotating release runs one beat every two weeks, weekly after the team expands (Chapter 22), scheduled all the way to handoff, and the cadence sheet is in [Template 15](../appendices/template-15-cobuild.md). This cadence is also the prelude to Chapter 21's operating cadence.

There are three places where doing these three things inside a company is easier than outside. All three are written here as actions. First, the three explain-it questions do not have to go into this project's PR (pull request, the request to merge code) template alone. Open a PR against the company-wide PR template, add a field for the share generated by AI and the name of the person who explained it, change it once and every project benefits. Second, the rotating release needs no venue you build yourself. The company's internal tech talk series is a ready-made stage, put both their names on the sign-up sheet, and the audience gains a layer for free. Third, you can see the other side's performance sheet, so the place to win can be made real. Ask Kevin to write the rotating release demo into a line of their quarterly appraisal, and visibility walks out of the meeting room and into the appraisal form.

## Failure Modes

**1. Your team does it all, three fast months, dead at handoff.** You and the Digital Center's engineers write all the code, the progress looks good, and the co-build engineers' "participation" is down to a weekly meeting. Doing it all is rational in every single moment. You are fast, they are slow, and a deadline only looks at the moment. The payoff of co-build settles on handoff day, and nobody wants to pay today's cost for an account three months out. An AI coding agent digs this trap deeper. What you and an agent produce in one evening takes two weeks to teach someone else. The consequence is cashed in Chapter 22. On handoff day the code is complete and the capability is zero. One test. If the co-build engineers' share of commits has been zero two weeks running, you are already doing it all.

**2. Co-build engineers used as cheap labor.** There is a split of work in form, but what they get is writing documents, building test data and adjusting page styles, while the core modules are "too critical, we will take those first." Split by "who is faster now" and the core work necessarily goes to the experienced hands. That split is right every single time, and add them up and it is entirely wrong. Worse, it confirms their deepest fear. AI plus people from the department next door prove together that "you are optional." The identity problem gets worse, and silence ferments into resistance. The remedy is clause two. The test for staffing is "whoever owns it later," not "whoever is faster now."

**3. AI code nobody can maintain.** The repo swells at agent speed, all tests green, and not one piece of core logic can be explained face to face by anyone. The scissors gap between generation speed and comprehension speed, on top of a review whose default test is "does it run." CI can verify running. It cannot verify understanding. Leave "explanation" out of the merge bar and black boxes necessarily accumulate, because "tests passed, merge it" is faster every time. The consequence lands at the first change request after handoff. Nobody dares touch it, the system freezes at the state it was handed over in, and then it gets worked around and abandoned. There is only one defense, make understanding the bar for merging rather than a wish held after the merge.

**4. Co-build turns into custody.** All four clauses are signed, CODEOWNERS names the receiving side, and yet you make every design call, you give every PR its final review, and you rescue every release. Co-build in form, doing it all in cognition.

Custody reinforces itself. Your reviews are the best, so everything comes to you for review. Their judgment gets no practice, the gap widens instead of narrowing, and that further proves "it still has to be you."

The warning signal, three months in, you are still the merge gatekeeper on every module, and at the rotating release you answer Kevin's questions for them. The rule, gatekeeping rights (the power to decide a module's merges, [Template 15](../appendices/template-15-cobuild.md)) are handed over module by module (at Anchor & Helm, gatekeeping rights over the extraction pipeline moved the same week as that first rejection). At the rotating release you only add, you do not answer for them.

!!! note "Vendor View"
    The vendor side's clause one is physical. The code goes into the client's repo, you commit with an external collaborator account, the account is revoked on your exit date, and ownership needs no ledger behind it. Inside one company, one GitLab, ownership comes down to three lines, CODEOWNERS, merge rights and oncall. There is no account to revoke, so headcount (no ops headcount reserved) and the ledger (real names on the transfer ledger) have to do what account revocation used to do.

## Next Monday

1. Open the project repo and look at ownership. Who is in the module's CODEOWNERS, who owns oncall, do the co-build engineers have merge rights. If all of it sits with you, change CODEOWNERS this week. The later, the more expensive.
2. Draw a backward staffing sheet. For each module write "who maintains it after handoff" first, then set it against "who leads the writing now." The modules where the two columns disagree are tomorrow's legacy, so reshuffle the lead writing this week.
3. Add one rule for merging. AI-generated code merges only after the maintaining side explains it face to face, using the three explain-it questions in [Template 15](../appendices/template-15-cobuild.md). Run it on your own next PR first.
4. Schedule one rotating release. Two weeks out, a co-build engineer demonstrates progress to their owner, and you sit in the audience.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 15 Next Monday actions. First open my project repo's CODEOWNERS
and list who owns each module now, and tell me if the file does not exist. Then build a backward staffing sheet following templates/cobuild/ownership-checklist.md.
I fill in "who maintains it after handoff," you count "who leads the writing now" from the commit history, and mark the modules where the two columns disagree. Merge the three explain-it
questions in pull-request-template.md into my project's PR template, show me collaborator-access.yaml as a sample only, and leave permission changes to me.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The four clauses of the co-build agreement (code ownership goes to the receiving side / backward staffing / if you cannot say it, do not merge it / the biweekly rotating release); the three explain-it questions (why it is written this way / where it can go wrong and how you would find out / where you start to change it)
- **Templates.** [Template 15](../appendices/template-15-cobuild.md), Co-build Agreement and Knowledge Transfer Cadence, fillable clause by clause, with the backward staffing sheet and the biweekly rotating release agenda
- **Key judgments**
  - "What stops co-build is identity, not skill. Give the co-build engineers a place where they can win."
  - "In the AI era, what co-build has to transfer is the ability to understand and evolve code. The code is only the carrier."
  - "If you cannot say it, do not merge it."
  - "The test for staffing is 'whoever owns it later,' not 'whoever is faster now.'"
