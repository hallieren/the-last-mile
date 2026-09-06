# 5 · Trust Ships First: Your First Deliverable Is Not Software

!!! info "Companion Templates"
    📋 [Chapter Template](../appendices/template-05-stakeholder-map.md) · 🗂 [Template Library](../appendices/template-library-index.md)

> **The Challenge.** The business side will not give you data, meetings are all pleasantries, and the people who matter can never be booked. Nobody can fault your technical plan, and the project still does not move.
>
> **What You Will Be Able to Do.** Draw a stakeholder map with real names and find the people who decide the project's fate without ever sitting in the meeting room. Audit your trust balance with the Trust Equation's 12 behavior-level questions. Break the "cannot get the data" standoff in the other side's language of power.

---

## Day Ten, and Still No Reply

The day after the charter was signed, you emailed IT to request the exceptions data. The ask was the full history needed for reconciliation, plus a direct read-only view. The de-identified batches Kevin Doyle's staffer exports by hand every day can feed a prototype. They cannot carry a reconciliation. Read-only, de-identified, scope spelled out in full.

The reply came on day three, one line. "Please go through the data request process." You went through the process. Then silence. You chased once on day seven and again on day ten, and the ticket status stayed "In progress." As it happens, that is the very status field in the core system you already know cannot be trusted.

The meetings are off too. At Kevin's weekly, you present the data reconciliation plan and everyone nods. Of the three follow-ups you booked afterward, two were pushed off with "too busy right now," and the one person who showed up brought only the official line. Nobody opposes you. Nobody cooperates with you either.

Technically you are beyond reproach. The plan is clear, the MVP has a track record, the charter carries Grant Whitmore's signature. But this company's real reaction to you is a single subtext. It knows you exist. It does not think you have anything to do with this. You have an employee ID and a desk, and people in Claims know your name, but walking into that meeting room with you is the Digital Center's history. What the last system builder left behind, Linda Marsh remembers better than you do. "Another innovation type" (Chapter 2) is the name for that account.

The charter does in fact spell out a data boundary clause in black and white, and the resource reassessment conditions (Chapter 4) say that when the business side's promised data access goes unmet two weeks running, it escalates to the sponsor for a resource reassessment. You could take that to Grant. But you sense that is not the answer. Invoking the contract is a trust withdrawal. Whoever pulls out the clause on day ten finds every door shut tighter on day thirty, and Kevin will still be in this building next year, and next year you will still be asking him for people. The clause gives you a floor, not a key. Where the key is, is what this chapter is about.

## Why This Is Hard: Companies Run on Trust Networks

The engineer's instinct is to read "cannot get the data" as a permissions problem. Find the person with the permission, get him to click approve. That model is wrong. The org chart draws the permission system. Day to day, the company runs on the trust network. Data access, the truth, and the front line's time, the three resources a project needs most, are open only to people whose trust balance is positive. The approval process is only trust's bookkeeping. No money in the account, and the process is an indefinite "In progress."

Worse is the speed. Code can be pushed through overnight, models can be tuned in parallel, but trust has a hard cap on how fast it forms. It accrues one notch at a time through the cycle of promise and delivery, each cycle takes days, and the cycles cannot run in parallel. That means the slowest step on an AI delivery's critical path is trust. Model and integration queue behind it. Chapter 1 said it. Of the five gaps, only the trust gap has no technical means of acceleration.

So take this chapter's title literally. Trust ships first because it stands in front of every other deliverable, not because talking about integrity sounds respectable.

## Prior Art, and What AI Changed

How trust accrues, consulting worked out long ago. The formula is ready-made. Maister, Green, and Galford proposed the Trust Equation in *The Trusted Advisor* (paraphrased here).

> **trust = (credibility × reliability × intimacy) / self-orientation**

Three terms in the numerator. Credibility, what you say can be believed. Reliability, you do what you say. Intimacy, the other person dares to tell you the truth. One term in the denominator, and it is the killer of the whole equation. Self-orientation, how visibly you are working for yourself. Once the business side smells you optimizing your own KPI (a promotion, your department's annual KPI, a thing you call "my project"), no numerator is high enough to survive the division to zero.

Peter Block's *Flawless Consulting* adds the fastest source of intimacy. Say out loud the tension in the room. The sentence everyone feels and nobody says, "I sense people have reservations about this plan, and nobody is voicing them." When you say it first, the air in the room changes at once.

What did the AI era change? The starting point went from zero to negative. A traditional consultant walks in with a trust balance of zero and builds up from there. An AI project opens with a double trust deficit. The front line fears replacement, and in their eyes you are here to take their measurements. Add black-box suspicion. Why the system recommends what it recommends, even you cannot explain line by line. Fear plus suspicion. At the start of an AI project, the trust balance is negative, not zero.

You are a colleague. That does not make the ledger look any better. Your starting point differs from the consultant's. It is not zero, it is an inherited balance. Every time you and Kevin have worked together, the reputation the Digital Center's last system left in Claims, Linda's twenty-year summary of "system builders," all of it entered the books before your plan did. The inherited value is occasionally positive, usually negative. A business unit remembers the last time a system made a mess, not the last time one saved hours. Stack fear and suspicion on top, and the negative only deepens.

The ceiling is lower too. No prophet at home. A hired expert can draw credibility in advance on a title, and a colleague from the same building cannot. When you talk about what AI can do, Kevin hears one more person telling him what a system can do. Your judgment has to stand on its own, on evidence from this company's floor.

That changes the play, and each of the four variables has its own. Credibility cannot be counted on short term. AI's reputation is badly overdrawn right now, the more fluently you pitch the more suspect you are, and a colleague pitching is more suspect still. Intimacy needs the other side to open up first, and cannot be rushed. The only variable fully in your hands from day one is reliability. Say Friday, deliver Friday. Here you have one thing extra. Presence. The promise-and-delivery cycle runs in days, and half your day is spent at a desk in the claims area (Chapter 2). Say you will look at that spreadsheet this afternoon, and this afternoon you are at the desk. One cycle compresses to half a day. Others bank three notches a week, you can bank six. And "say the tension in the room" gets a concrete target in an AI project, the fear of replacement itself. Standing in front of Linda's team and saying "You may be worried this thing is here to replace people. That is why every output has a Human Call column, and the call stays with you" is faster than ten pages of assurances.

## Framework One: The Six Roles of the Stakeholder Map

A stakeholder map is a map with real names. It answers "which specific people does this project's success or failure depend on?" Six roles, three things per cell. The name, what they fear, what they win.

| Role | The Test | Common Mistake |
|------|----------|----------|
| **Decision-maker** | Who can, in one sentence, fund this project's next phase or kill it? | Writing only the sponsor, forgetting the sponsor answers to someone too |
| **Actual user** | Whose daily actions change after launch? | A department name instead of a person's name |
| **Data owner** | Who owns the data you need, on the business side? | Going only to IT, who holds the key, not to the data's business owner |
| **Risk owner** | When something goes wrong, whose name is on the accountability email? | Treating review as process and assuming nobody really cares |
| **Maintainer** | A year after launch, whose annual goals list this system? | Writing yourself in, which kills the cell's diagnostic power; leaving it blank, and finding nobody there at handoff (the transfer of the system) |
| **Blocker** (the person in the way) | Without whose nod does everything stop, even though he never attends? | Reading "never attends" as "not involved" |

Three rules of use.

- **First, real names.** A map that says "the IT department" is decoration. Departments do not fear and do not win. Only people do.
- **Second, one person can fill several cells.** Kevin is the workflow owner of the exceptions process, the owner of the workflow the AI changes. That title is not in the table above. He can halt the process in one sentence, so he lands in the "decision-maker" cell, the same cell as Grant, with a jurisdiction one ring smaller. He is also the business owner of the exceptions data, so his name goes in the "data owner" cell too. People in several cells are your high-leverage nodes. Owen Hartley is in the "decision-maker" cell as well. He cannot kill the project, but he controls your schedule and could reassign you tomorrow (Chapter 2). That is the extra line an internal map carries.
- **Third, the map's value is in the blanks and the wrong cells.** Once it is drawn, one question is mandatory. Which name has never been in the meeting room? That is your blind spot, and the project's future cause-of-death candidate.

The "What They Fear / What They Win" columns are the engine of this table. What he fears decides whether he blocks you. What he wins decides whether he pushes you. The goal of stakeholder management is for everyone to have their own win-loss ledger in this project. Being liked does not make the list.

Beyond the six cells, an internal map needs two extra cells. They are not new roles, the six tests stay exactly as they are. They are two accounts the six cells cannot hold.

- **Extra cell one, the peer competitor.** Another team in the company also doing AI, or a sister business unit's digital group. He does not block you, so he is not a blocker, but he competes with you for the same budget and the same sponsor's attention. What he fears is your project becoming the benchmark, so that when he files for project approval next year, he is measured against your numbers. What he wins is a place he can write into his own reporting. First contact, in the opening week, book him yourself and show him your scope boundary. The exceptions queue is yours, and his piece you will not touch. Then ask whether he has something on hand you can reuse directly. The competitor becomes your first reuser, his name goes into your reporting, and yours into his.
- **Extra cell two, the predecessor's legacy.** Same structure as extra cell one, the difference is the first contact. This business unit was hurt by a digital project once before. What the predecessor left behind, reports nobody maintains, a system nobody logs into, one line of "that is what they said last time too," all of it is booked to your account, because to the front line you are the same kind of person. What they fear is it happening again. What they win is someone admitting the last time first. First contact, go find the real cause of death of the last project. The files and the people involved are in the building, one afternoon of asking settles it (Chapter 6). Then say the cause of death out loud in front of the front line. Get it right, and half the predecessor's debt moves off your account. Get it wrong, and they will correct you, and the correction itself is the start of intimacy.

## At Anchor & Helm: One Map, Three Payoffs

The night before the charter meeting, you drew the Anchor & Helm map (the full walkthrough is in [Template 5](../appendices/template-05-stakeholder-map.md)). Drawing it exposed two fatal blind spots.

**Blind spot one, Victor Reyes.** He is in no project meeting and on no email cc. But who goes in the "risk owner" cell? Who signs the security review, who takes the fall for a data incident? All him. He holds a real veto, a single vote that stops everything, and yet he is invisible. What he fears is concrete. Being bypassed, and still taking the fall when something goes wrong. AI itself comes second. In week 1 you got one thing right on instinct, and hand-delivered a pre-mortem memo to his desk. That memo assumed the project had already failed and listed the causes of death backward, and item four said a security review that does not start until week 10 blocks the launch. He asked to meet you because of it (Chapter 1). What the map does is turn that instinct into structure. When "risk owner" and "blocker" carry the same name, bad news must always go to that person unprompted. Never wait for luck to blow it past him. The line from blocker to ally runs from this page to the security review in Chapter 12.

**Blind spot two, Linda Marsh.** The moment you wrote her name in the "actual user" cell, you realized that the person who decides whether this system lives or dies had not been invited to a single decision meeting since the MVP scoring. Of everyone sitting in the meeting room, not one would use this system daily after launch. She fears being replaced, taking the blame for AI's mistakes, and having twenty years of experience erased by one line of "the model decides automatically." What she can win is fewer chase emails, and her judgment written into the system instead of written out of it. The corrective move appeared in Chapter 4, the line "Linda's team, 2 hours a week" in the charter's business-side commitment clause. Now the secret can be told. That line was forced out by this map, not a flash of inspiration in the meeting.

**The third payoff is the standoff this chapter opened with.** On the evening of day ten, you go back to the map and look at the "data owner" cell. IT holds the key. The business owner of the exceptions data is Kevin. For ten days you have been talking to the permission system, and the key hangs in the trust network.

Going to Kevin empty-handed is useless. Why would he spend his power on your project? The pain of the monthly report, Kevin had raised to your face weeks ago, and you had filed it as "a favor you could do in passing" (Chapter 7). This week it flared up again. That spreadsheet he has a staffer export from the core system and stitch together by hand is wrong every month and questioned every month. The next afternoon, you carry your laptop over and sit down next to his staffer's desk. The files never pass through your hands, and the script runs on Claims' own machine. Forty minutes, and the field extraction logic already in the MVP generates the spreadsheet automatically, and along the way you fix two definition errors he had never managed to find. The etiquette of helping differs inside a company and outside. People from the Digital Center can already reach plenty of data in this building, so not touching unauthorized data is not a signal for you, it is the floor. Kevin watches three other things. You did not quietly pull that spreadsheet back to the Digital Center to build your own store. The data never left their machine, start to finish. Those two definition errors you did not turn into talking points in other meetings. The errors in Claims' monthly report are known only to Claims. The script stays on his staffer's computer under the staffer's name, and when next month's report comes out clean, the credit goes to Claims. All you take away is a copy of the script. You do not mention the data request.

On Friday, Kevin stops the head of the IT data team in the hallway and speaks in his own language of power. "Exceptions are my department's data. The project team wants a read-only de-identified view. I sign off, open it before Monday." Monday morning, the access arrives. A standoff ten days could not break, forty minutes and one sentence.

This is hardly scheming. You helped Kevin win a fight he was already fighting, a double deposit into reliability and intimacy. Those forty minutes also let you see the true face of the core system's fields, so the first-hand material for Chapter 9's data reconciliation is already in your hands. Let the person with the power speak for you, in his own language. It beats shouting ten times yourself.

Inside a company there is one more gate. Your help has no price tag. In Kevin's eyes those forty minutes were free, and next week his staffer will show up with five other spreadsheets, each one "in passing." Helping is an investment only when it has an exit. So before you touch anything, settle the exit for this one. Is it one-off, the script stays with them and they run it themselves from now on, or does it become a long-term commitment? Do the former. Do not take on the latter on the spot. It goes into the intake list (the gate where requests come in) and waits its turn (Chapter 25), and the waiting is itself the price. Kevin's exit this time was clean. The script bears his staffer's name, and the monthly report no longer passes through your hands. In "help him win once first," the word "once" is the gate.

## Framework Two: The Trust Equation Self-Check

The equation is easy to remember. Honesty is the hard part. Each of the four variables gets three behavior-level questions. Do not ask "do you think the business side trusts you." Ask only about behavior that can be checked.

**Credibility**
1. In the past two weeks, have you said to someone's face "I do not know, I will have an answer by X," and then delivered on time?
2. Of your last three judgments, how many carried evidence from this business unit's floor (numbers, cases, users' own words) rather than industry boilerplate?
3. Has the business side quoted you in a meeting you were not in?

**Reliability**
1. Of your last five "you will have it Friday" commitments, how many landed on time?
2. Are meeting action items sent in writing within 24 hours, or "written up later"?
3. Has there been one time you shrank a commitment you could not keep, early and unprompted, instead of explaining on the deadline?

**Intimacy**
1. Has anyone told you something at the level of "I am only telling you this"?
2. Have you once said the tension in the room out loud, to people's faces?
3. Has the front line complained to you about their own department or their own boss? The jargon (aged claims, chase emails, "that spreadsheet") you already know, so that test does not count for a colleague.

**Self-orientation (the denominator, lower is better)**
1. In your last meeting, how many times did you say "our system / our plan" versus "your claims / your metrics"?
2. When the business side suggests something that would shrink the project's scope, is your first reaction defense or curiosity?
3. When did you last advise the business side "let's not do this yet"? If never, the denominator is quietly rising.

The usage is simple. Run it on yourself every two weeks. Read the answers for the gaps, not the total.

The scattered questions you cannot answer, each one is the next behavior you should deliberately create, and one action this week covers it. When all three questions under one variable come up empty, the nature changes. That is a line you have not been working at all, one action is not enough, and it goes on next week's calendar. The full self-check is in [Template 5](../appendices/template-05-stakeholder-map.md), next to the map.

This sheet does not retire at launch. Trust is a permanent account for you. It is not settled on launch day, the business side is still here next year and so are you, and every slow response after launch is drawn from the same account. One unanswered alert in month 14 can empty every bit of reliability the charter period banked. What Linda's team remembers will not be those forty minutes, it will be the one time nobody picked up. So after launch the way you deposit changes. It is no longer say Friday, deliver Friday. It is alerts get answered, there is a name on the oncall (on-duty) rotation, someone shows up at the retrospective. Who owns each of these, the responsibility transfer agreement (Chapter 22) spells out. Any cell it leaves unclear is charged to your account.

## Failure Modes

**1. Cultivating only the sponsor.** Inside a company this is called cultivating only the boss, and there are two bosses, Grant, who gives the mandate, and Owen, who runs your review. Excellent relationship with Grant, and Linda's team cannot say your name. The root is asymmetric feedback. The sponsor and your manager talk, give positive feedback, one holds the budget and the other your performance review. The front line gives you only silence and suspicion, and people drift naturally toward where the feedback is. Inside a company this structure is only stronger. The boss sets your review, the front line does not. But on settlement day the roles swap. The sponsor gives you the project. The front line gives you the outcome. After launch Grant will not log in, and neither will Owen. Linda will, or will not. Whether she logs in depends on how much trust you banked with her.

**2. Delaying bad news.** "The data is worse than expected" has been sitting in your mouth for two weeks. You booked reporting bad news as a credibility expense. You booked it backward. Bad news delivered early, unprompted, with a plan, is a double deposit into credibility and intimacy. Every concealment is a withdrawal from reliability, with interest. Bad news does not disappear, it only appreciates. Wait for the business side to find it themselves, and the cost is ten times higher, and every piece of good news from you afterward is discounted along with it.

**3. Self-orientation leakage.** "Our system" shows up in your sentences more and more. Your KPI (a promotion, your department's annual KPI, next phase's resources, your name near the top of the year-end report) is real and cannot be hidden. It leaks out through language, and the frequency of "our system" is the leak meter. The business unit smells the same thing every time. What you are fighting for is whose name this system ends up under. Their reaction is the one this chapter opened with. Nods in the meeting, no cooperation after. The denominator is the only division in the equation. However high the other three climb, one whiff of self-interest zeroes them out. The fix is to put the motive on the table, since nobody believes feigned selflessness. "If this project succeeds, of course that is good for our team. But it only counts as succeeding when your handling time really drops 30%." A motive said out loud is no longer a leak. It is a boundary.

## Next Monday

1. Use [Template 5](../appendices/template-05-stakeholder-map.md) to draw the stakeholder map for the project on your desk. Real names, six cells plus the two extras, "What They Fear / What They Win" filled in. Find the name that has never been in the meeting room.
2. Send that name something, a pre-mortem, a one-page risk list, so he knows you wrote what he fears on page one.
3. Run the 12-question self-check, pick the weakest variable, and create one concrete behavior this week to shore it up.
4. The "cannot get X" you are stuck on right now, ask three things instead. Who is X's business owner? What fight is he fighting? Can I help him win once first, and where is the exit for that once?

**Want an agent to get you started?** In the repo you set up following [Start Here](../index.md), paste this to your coding agent:

```text
In the repo/ directory of the the-last-mile repository, help me with the Chapter 5 Next Monday actions. Copy
templates/stakeholder-map/stakeholder-map.md into the working directory I name, then walk me through the six cells plus the
two extra cells one by one, asking for real names and "What They Fear / What They Win." I dictate, you fill in. Mark any
cell I cannot answer as [TBD] and remind me that cell may be the person who has never been in the meeting room. When it is
filled in, run python3 templates/stakeholder-map/remind.py to see the reminder output on the built-in sample, then run it
again pointed at my file. I answer the 12-question self-check myself, do not judge the weakest variable for me.
If any command errors, stop and show me the output.
```

---

## Chapter Kit

- **Judgment frameworks.** The six roles of the stakeholder map (decision-maker / actual user / data owner / risk owner / maintainer / blocker, real names + What They Fear / What They Win, two extra cells for the peer competitor / the predecessor's legacy); the Trust Equation self-check (4 variables × 3 behavior-level questions)
- **Templates.** [Template 5](../appendices/template-05-stakeholder-map.md) (Stakeholder Map), six-role map + "fear / win" prompt library + contact plan + Trust Equation self-check
- **Key judgments**
  - "The org chart draws the permission system. Day to day, the company runs on the trust network."
  - "At the start of an AI project, the trust balance is negative, not zero."
  - "The sponsor gives you the project. The front line gives you the outcome."
  - "Let the person with the power speak for you, in his own language."
