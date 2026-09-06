# 21 · Adoption Engineering: From Usable to Missed When It Is Gone

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-21-adoption-plan.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The training was held, the email went out, and the system really is good. The same few people are still the only ones using it. What does adoption actually run on?
>
> **What You Will Be Able to Do.** Use the four adoption mechanisms (super-user network / operating cadence / short-term win announcement / institutional anchoring) to turn "one team uses it" into "taking it away would hurt." Diagnose a falling adoption curve and find the root cause, which is almost always in management.

---

## Monday of Week 21, Three Daily-Active Curves

After the expansion was approved, auto review teams two and three entered the queue in week 19. Same system, same training, even the same instructor. Monday of week 21, you lay the three daily-active curves side by side. Daily actives, the share of reviewers who actually opened and worked the queue that day.

- Linda's team, 100%, not one day below since the pilot began.
- Team two, 60% in their first week on the queue, steady since.
- Team three, 60% in their first week, and already below 30% at the start of week 3.

Every variable is controlled and the curves still split three ways. Only one difference is left. Linda's team has Linda. And you cannot assign a Linda to every team.

That one sentence is the whole subject of adoption engineering. Turn the Linda effect into a mechanism you can reproduce.

## Why This Is Hard: Training Fixes Knowing How, Not Whether They Use It

The engineer's default model of adoption is the product model. Make it good and people will use it. The real model in an enterprise is the social model. The front line watches its peers, peers watch the person who leads, and that person watches whether the boss cares. Training solves a cognitive problem, whether they know how. Adoption is a habit and social problem, settled by three variables no feature list can touch. Who is using it (the peer environment), whether the people using it are doing well (visible winners), and whether not using it costs anything (institutions). The four mechanisms below grow out of these three variables. Only the operating cadence maps to none of them. It is the carrier that makes the other three happen again every week. Who is using it maps to the super-user network, doing well maps to the short-term win announcement, and whether it costs anything maps to institutional anchoring.

In one sentence, organizations do not adopt tools. Habits adopt tools. A tool enters daily work through ritual, visible winners and peer pressure, and not one of those three happens automatically because "the feature shipped." Between L3 on the outcome ladder (adopted, "taking it away would hurt") and L2 (production, the system is in production with an owner and monitoring) lies nothing but organizational engineering of this kind.

## Prior Art, and What AI Changed

**Kotter's eight steps for change, cut down to four for the field.** John Kotter's framework in *Leading Change* (paraphrased) is designed for organization-level change. The deliverer's battlefield is one size smaller, one department and one workflow, and eight steps cut to four are enough. This chapter's four mechanisms come from there, mapped as follows. Guiding coalition = the super-user network, short-term wins = early wins announced, communicating vision = said again in every weekly ritual, anchoring in culture = written into the institutions.

**Habit thinking.** The habit loop Charles Duhigg draws in *The Power of Habit* (cue-routine-reward, paraphrased), where new behavior forms through a loop of trigger, action and reward, not through one-time persuasion. Applied to adoption, the same hour every week, the same room of people, the same queue, a ritual that keeps recurring is the cue.

AI changed two things, the cold start and the fragility.

The cold start. This system gets better through use, and reason codes and override trails are the fuel for rule iteration and the golden cases (Chapter 17, the trail flowing back). But before it gets better, who uses a system that is not smart enough yet? Chicken and egg. The answer is that the super-user network carries the feeding period. A small group of seed users, given a formal identity, keep using the system at its dumbest and keep feeding it real judgment until it gets smart. The feeding period runs on design and on reward, not on goodwill you sit and wait for. And the reward has to be paid before the system gets smart. What Anchor & Helm did was put Linda's name on the five rules. The reason column of every suggestion carries the name of one of her rules, and the more the system is used the more it looks like her work. Seed users keep feeding it at its dumbest, and what they feed it is their own.

The fragility. Trust in AI is built one suggestion at a time, every suggestion is on trial, and organizations have an asymmetric memory for incidents (Chapter 18, an improvement is remembered for three days, an incident for a year). It follows that one unsafe the defense failed to catch can empty a team's daily actives. Traditional software that is hard to use only gets used slowly. An AI system gets one thing wrong and the story becomes "this thing is not reliable." The adoption curve is far more fragile than it is for traditional software, which is why adoption has to be engineered and cannot be left to grow on its own.

## The Core Framework: The Four Adoption Mechanisms

> **The four adoption mechanisms, the four that turn adoption from a wish into a structure. Network first, cadence fixed, wins amplified, institutions last.** (Template in [Template 21](../appendices/template-21-adoption-plan.md))

The four rows below correspond to those four steps in order.

| # | Mechanism | What It Is | What It Prevents |
|---|------|------|-----------|
| 1 | **Super-user network** | A super-user, a seed user with influence on the front line, given privileges (new features first, a direct channel for improvements) and identity (a formal name, credit in public). **Pick by influence, not by title** | Adoption resting on the project side's pitch alone; nobody to carry the feeding period |
| 2 | **Operating cadence** | A 30-minute queue retrospective every week, going over the reason code distribution, aging claims, and one improvement. **Embed it in a ritual that already exists, do not create a meeting** | A new ritual cannot win a calendar slot and dies in three weeks |
| 3 | **Short-term win announcement** | Manufacture one win worth telling inside the first month, in business language, announced by the business owner. **The winner is the business team** | The improvement goes unnoticed, or the credit goes to "AI" |
| 4 | **Institutional anchoring** | New-hire onboarding material covers queue operation; the exception claim SOP is updated to reference the system. **Lock the habit in with the cost of leaving it** | Held up by personal enthusiasm, and the curve goes to zero when the person leaves |

Two design points. The test for picking a super-user comes down to one question. A hard claim comes in, who does everyone get up and go ask? Inside a company you already have the answer to that question. You have been here a few years, and which team lead really has influence and which one only has the title is not something you need three months on site to see. Put that depth straight to work on the candidate list. The cost difference in the operating cadence is legitimacy. A new meeting has to win a calendar slot, win attention, and keep proving it deserves to exist, while a ritual that already exists comes with its own attendance. Embedding the system into an existing ritual is ten times cheaper than building a new one.

The agreement itself is one page ([Template 21.2](../appendices/template-21-adoption-plan.md)). Anchor & Helm gave Linda three privileges. New rules two weeks before everyone else, improvement suggestions going straight to the development board (the board your team schedules its own work on, not the review queue) with a reply guaranteed inside two weeks, and the right to chair the retrospective. What comes back is the feeding-period commitment. Keep using the system at its dumbest, fill in reason codes seriously, and the time invested goes into her workload. Exit is written up front. She may leave voluntarily at any time, four straight weeks of not using it or not attending voids the status automatically, and using data visibility to lean on colleagues means immediate removal.

Two clauses of this agreement go hollow most easily inside a company. One is workload. Writing it into workload does not happen by itself. It has to land on the super-user's own supervisor, either a written confirmation of how many hours a week or the item going into the super-user's OKRs for the quarter. A nod given in a meeting is eaten by the day job by week three. The other is the direct channel. Your team is split across several projects at once, and "a reply inside two weeks" is the first promise to be sacrificed, so reserve a fixed response capacity allowance in your own schedule (a fixed block each week for answering improvement suggestions) before you say that privilege out loud. A bad check can be written only once. Break faith once and the whole super-user network stops speaking for you.

### The Adoption Curve Diagnostic Order, What to Check First When a Curve Drops

- Check the unsafe trail first. Pull that team's scores and override records for the two weeks the curve turned, and look for an unsafe that landed and for concern crossing the pilot-period threshold. If there is one, the problem is the system and the incident story spreading from it, not adoption.
- Then check the manager's attendance. Pull the retrospective sign-in sheet and count how many of the last four weeks this team's manager showed up. Zero attendance and the root cause is right there. The fix sits with the owner, not with the system.
- Only then check features. When the first two come back clean, it is time to look at this team's reason code distribution and aging claims to find which feature it is actually missing.

## At Anchor & Helm: Four Weeks of One Network

**Week 19, the person standing at the front of the expansion training is Linda.** That is by design, not coincidence. A peer's testimony beats the project side's pitch, and the front line only believes the front line. It works the same way inside a company. The project side is your own team, and the front line will not count you as a peer just because you and they draw pay from the same company. Page one of the handout carries the five rules of thumb, amount, report delay, photo count, prior claim linkage, repair shop list, signed by Linda, with the system screenshots further back. That day Kevin gave her a formal identity in front of everyone, queue co-builder. Not "system administrator," not "training instructor." The name itself says that half the system is hers. One section of the training is devoted to the repair shop list, now an operating asset with an owner (Chapter 18), and the first thing a new team does on arrival is add the shops in its own district.

Standing in the audience you think back to Chapter 0. Her first feedback on this system was three unsafe marks. From skeptical scorer to the front of the room there was never one act of persuasion. Her judgments went into the system one at a time. The five rules (Chapter 6), the annotation rulings (Chapter 11), the implementation flaw the reason codes fished out (Chapter 17). You did not turn Linda into a believer in the system. You turned the system into Linda's work.

**The operating cadence was planted back in pilot week 2.** You did not create a "system weekly" then. You asked Kevin only for the last 30 minutes of his existing weekly, to go through this week's override reason code distribution and the top aging claims and settle on one improvement. The engineering side's prelude came earlier. The biweekly rotating release (Chapter 15) had already set the beat of "the claims-ops IT engineers demonstrate to the business owner," and the business side's weekly retrospective meshes with it into a complete cadence. From week 19 the retrospective is chaired by Linda, and you move back into the audience.

**After the week 21 retrospective, the 25% diagnosis.** The curve that dropped below 30% on Monday settles at 25% after this week's retrospective. Your first reaction is the lesson of Chapter 18. Was there an unsafe? You check the trail. Team three, three weeks, zero unsafe, and concern inside the threshold too. The system is not at fault. Then you check the retrospective sign-in sheet. Team two's lead is there every week, team three's lead has zero attendance across three weeks. This week is no exception. He leaves when the first half of the standing meeting ends, "the second half is your project's business." His team read that sentence instantly. This thing does not count in our team.

When an adoption curve drops, the first thing to suspect is not the system. It is the manager's attention. Whether team members use it depends first on whether their own boss looks at it, and how good the system is comes second. The fix sits with Kevin, not with the system. You added no feature and sent no email. You put the curve and the sign-in record side by side in front of Kevin. He read them and said one thing. "This is on me." In week 22, attendance at the retrospective goes into the team lead's job description. In week 23, team three's daily actives climb back above 80%. You did not change a line of code.

Inside a company this step needs one more calculation. Handing the sign-in record to Kevin means reporting on the attendance of a team lead who works for the head of a peer department, across a reporting line that is not yours, and it reads easily as tattling. The steadier order is to let the number walk into his view on its own. Per-team daily actives and retrospective attendance belong in claims operations' own monthly operating data anyway, and Kevin will see them when he turns the page of his own report. Or let Linda raise it at the retrospective as a super-user, because coming from the front line it is a peer's opinion and coming from you it is the department next door passing judgment. Only when neither road works do you lay the two sheets side by side, and even then you put down the data only, with no conclusion.

**Also week 21, something nobody announced.** Thursday evening you are on site and walk past Linda's desk. For six years the last thing she did before leaving was back up that Excel, step 14 of Chapter 6's fourteen steps, one of the three steps Chapter 17 ruled "Kept." Today she closes the laptop and goes. You catch up and ask her. She says, "It is all in the queue." She pauses, then adds, "I stopped the day before yesterday. You are only noticing now?"

You checked afterward. That six-year-old file was last opened on Monday of this week. No ritual, no email, nobody's approval. In Chapter 17 you wrote that the day she stops on her own is the true measure of trust. The measure arrived, on a Thursday evening nobody noticed. Trust never holds a launch event.

The source of truth did not fall with it. At the week 13 retest the core system's status field had already reached validated (Chapter 9), on the strength of the daily write-back discipline Kevin claimed at gate three (Chapter 14), and from that week the merged view stopped deferring to the Excel. Her stopping the backup is evidence that the discipline runs in her hands, not the case Chapter 9 warned about, where the system kills its own source of truth with its own hands.

**Week 23, two things land in the same week.** First, auto team two clears its exception claim backlog, the first short-term win worth telling. Kevin announces it at the monthly business review, one page, two minutes. On that page, one side is the date the backlog hit zero, the other is team two's first-touch handling time curve coming down. The subject from start to finish is "team two," and not once does the room hear "the AI launch was a success."

Second, the survey team lead comes to the retrospective with self-check numbers for the first time, the waiting time for his own step, which he pulled himself on the new standard (Chapter 20). The "waiting on external" status and the three visibility pledges (Chapter 20) let him see his own team's data first, and this time he brings data and comes looking for improvements. In week 24 Kevin names him the second super-user. The former opponent is the most convincing spokesman. One sentence from him, "this thing is not appraising us," lands harder than a hundred from you, and the whole department remembers the question he asked with his pen set down in front of everyone.

What landed this week is the first three mechanisms. The fourth is still owed. Institutional anchoring rides on two documents, the new-hire onboarding material (the set that teaches a new hire how the work is done) and the exception claim SOP (the standard handling steps for this class of claim). The person who changes them is not you. It is the process owner, and at Anchor & Helm that is Kevin.

That sentence is only half true inside a company. You can write the change as revision text and hand it straight to the process owner, and you can file the SOP revision request yourself in the process management system, an entrance an outside consultant does not have. The price is that once filed it goes through compliance or quality management review, one more gate, two more weeks. Of the four, institutional anchoring is the biggest lever in the internal reader's hands. The first three you have to push every week. The fourth, once changed, needs nobody to remember it, so the moment to start is earlier than you think. You do not have to guess the moment either. Attendance is already written into the team lead's job description, so these two documents are the next thing to move.

What you do is write the change as two sentences and hand it over. Add a section on queue operation to the onboarding material, and everywhere the exception claim SOP says "check the core system," change it to "check the queue." That onboarding section does not have to be assembled from scratch either. The company already runs a new-hire training program, and slotting a section into it lives longer than building a separate one of your own. At Anchor & Helm the two documents were settled in week 24 and issued by Kevin. The queue operation section of the onboarding was written by Linda, who by then was already an instructor in new-hire training ([Template 21.2](../appendices/template-21-adoption-plan.md)). The SOP was revised by Kevin's own operations team, and the revised version went back out to every team lead. Only after this step does opening the queue turn from a personal habit into a job duty.

The North Star stopped at -22% when the pilot ended, and it will reach -31% in week 26, but that is the next chapter's stretch of time. The more important measure right now is what the week 23 retrospective was made of. Linda chaired it, the data came from the survey team lead, and the attendance rule was signed by Kevin. The right to chair the operating cadence is already in the business side's hands. The handoff (Chapter 22) has already begun, and it does not wait to be announced.

## Failure Modes

Five. The first two treat adoption as training or as an order. The last three each get one thing wrong, in the super-user, in the win announcement, and in institutional anchoring.

**1. One training session treated as adoption.** Launch comes with one training session and a manual, and three months later daily actives are zero. Training is a cognitive intervention, adoption is habit engineering. A habit needs repeated cues and a peer environment, and a one-off event structurally cannot reach that far. Training is also easy to deliver, easy to tick off, and has a completion date, while adoption has no deadline, so only the first one survives in the performance review. The test, look only at the daily-active curve in weeks two and three after the training, not at the sign-in sheet.

**2. Pushed through by order.** The boss orders "you must use it," and daily actives hit target within a week. An order changes login behavior, not decision behavior. The front line will invent the cheapest compliance available, accept everything, and pick "other" for the reason code without looking. And an AI system eats the data it produces itself. Going-through-the-motions trails flow into rule iteration and the golden cases (Chapter 17), garbage in, the system gets dumber, and that in turn proves "it is not useful." Pushing traditional software through wastes licenses. Pushing an AI system through poisons its own fuel. The test, high daily actives with an override rate near zero and the share of "other" reason codes shooting up means nobody is actually judging. Do not read it as a perfect system.

**3. Picking champions by title.** Champion, what the change literature calls an internal advocate. Every team lead is appointed a "rollout ambassador." Titles are easy to find on the roster and appointing costs nothing to negotiate. Influence only shows up if you sit in the field, and "who does everyone ask when a hard claim comes in" and "who is the team lead" are often not the same person. Picking by title also insults the real opinion leader for free, the person who got skipped. Neither of Anchor & Helm's two super-users came by title. Linda came by twenty years of field authority, the survey team lead by the turnaround of "even he came around."

**4. The win announced as "AI succeeded."** At the monthly meeting, "our company's AI project has achieved phased results," with a system screenshot. The project side is under reporting pressure, and the "AI succeeded" story pays the project side immediately. But it rewrites the business team from winner into backdrop. Team two did three weeks of work and the credit went to the system. The super-users' account stops balancing at once. They staked their standing to vouch for the system and the return was taken away. Steal the credit once and the network falls apart. A side cost, raised expectations (Chapter 19) make the next incident a longer fall. The rule, the subject of the announcement must be the business team, the measure must be a business number, and the system's name goes in the last paragraph or nowhere. Inside a company, the business team means the department that uses the system, not the platform or data team you sit in, and drawing pay from the same company does not change that rule. The credit has to go on their side of the ledger.

**5. No institutional anchor, held up by people.** The network is built, the cadence is running, the win has been announced, and the one thing nobody went back to do is change the onboarding material and the exception claim SOP. For the months the super-users are around, the curve looks fine. But people move. The super-user transfers, team leads rotate, and a new hire still gets the old process that says "check the core system," so the old process is what he learns, and the system slides from "should be used" back to "may be used." The first three anchor to people, the fourth anchors to the job, and only the fourth needs nobody to remember it. The test, find someone who joined recently, ask how a claim of this kind should be handled, and see whether what he recites is the queue or the old SOP.

## Next Monday

1. Pull per-team daily actives and depth of use (override rate, reason code fill rate) once, and find your "Linda's team" and your "team three." For a team with an abnormal curve, check the trail for an unsafe first, then that team's manager's attendance at the adoption ritual over the last four weeks, and only then the features.
2. Write down three names, the people everyone asks first when a hard claim comes in. That is your super-user candidate list. Check it against the org chart, and if all three are team leads, pick again.
3. Find a standing meeting that already exists and negotiate its last 30 minutes for the queue retrospective. Do not create a meeting. Lay out the cadence with [Template 21.3](../appendices/template-21-adoption-plan.md), and use 21.2 to write down the privileges and the identity with your first super-user.
4. Check the most recent announcement that went out. Is the subject the business team or the system? If it is the latter, rewrite the next one, and confirm the business owner is willing to say it in his own voice.
5. Dig out the new-hire onboarding material and this workflow's SOP, list every paragraph still carrying the old system's name into one list of changes to make, and hand it to the process owner along with the wording. If the documents do not change, the first four all walk out with the people.

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 21 Next Monday actions. First run python3 templates/adoption/retro_onepager.py
on the built-in sample to show me a one-page queue retrospective, then open weekly-usage.sql and explain how per-team daily actives and depth of use are computed. I will give you the decision trail export,
you only run the queries and draw the tables, and which team is "Linda's team" and which is "team three" is my call. The three super-user names are mine to write, you only check them against
the org chart and flag whether all three are team leads. Build the operating cadence sheet per Template 21.3, and the name of the standing meeting and how to negotiate its last 30 minutes are mine to handle.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The four adoption mechanisms (super-user network picked by influence / operating cadence embedded in an existing ritual / short-term win announced in business language / institutional anchoring into onboarding and the SOP); the adoption curve diagnostic order (check the unsafe trail first, then the manager's attendance, then the features)
- **Templates.** [Template 21](../appendices/template-21-adoption-plan.md), Adoption Plan, Super-user Agreement, Operating Cadence Sheet
- **Key judgments**
  - "Adoption is a habit and social problem. Training only solves the cognitive one."
  - "Embedding the system into an existing ritual is ten times cheaper than building a new one."
  - "An adoption problem is mostly a problem of the manager's attention. The fix sits with the owner, not with the system."
  - "The former opponent is the most convincing spokesman."
  - "The business winner must be the business team. Steal the credit once and the network falls apart."
