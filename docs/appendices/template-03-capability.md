# Template 3 · Capability Self-Assessment and F1–F5 Rating

> Companion chapter(s): Chapter 3 (capability self-assessment), Chapter 26 (F1–F5 rating and the growth agreement). The first half (3.0–3.6) is the five-axis radar self-assessment: one paragraph of definition per axis, 1–5 behavior anchors, three self-check questions, and shoring-up advice by score. The second half (3.7–3.8) lays out two tools in the order you use them: rate yourself with the anchor table first (3.7), then turn the level gap into a plan with the growth agreement (3.8). Chapter 26's F1–F5 capability rating reuses the same coordinate system, so archive your scores. The last section (3.9) is for engineers who want to enter this kind of work. It translates the experience you already have into evidence on this coordinate system.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 3.0 How to Use This

- **Score on behavioral evidence, not on "I should be able to."** Read the 1–5 anchors for each axis first, and take the row that most resembles you on your most recent real project.
- **The self-check questions are for calibration.** Three per axis. Fewer than two yes answers, and you drop that axis by one point.
- **Get a coworker to score you blind and compare.** On any axis where the two of you differ by ≥2 points, take theirs. The systematic bias of self-assessment is overrating.
- **You may let AI prefill the evidence from your project records, but the score has to be yours.** The value of a self-assessment is honesty, and AI cannot be honest for you.
- **Re-score and archive every quarter (or after every project milestone)**. The F-level rating in 3.7 (Chapter 26) draws on your historical radars.

---

## 3.1 Engineering Depth

Without AI, can you still stand a system up. Data, APIs, debugging, deployment. This axis guards the floor under "AI does it, you review it." For someone who cannot review it, moving up the leverage is not a conversation.

**Anchors**:

| Score | Behavior |
|----|----------|
| 1 | Can modify code someone else built; building from scratch alone is hard |
| 2 | Completes modules alone inside a familiar stack; needs support to cross stacks or go to production |
| 3 | Can take a prototype to a working pilot alone, data integration, deployment, logging, basic monitoring |
| 4 | Can enter a business-side environment on an unfamiliar stack and locate and fix integration problems within two weeks |
| 5 | Can design and land a maintainable integration in a constrained environment (legacy systems, no documentation, strict security requirements) |

**Self-check questions**:

1. Handed an error log from an unfamiliar system, can you locate which layer the problem is in without calling anyone?
2. Was the last time you deployed a service from scratch to reachable, with your own hands, within the past six months?
3. Was the last time a review of yours caught a subtle error in AI-generated code (boundary conditions, concurrency, silent failure) within the past month?

**Shoring-up advice**:

- **1–2**. Do not fly solo on this kind of project yet. Do two complete small projects from scratch to deployment. AI assistance throughout is fine, but force yourself to understand every line and to handle every deployment failure by hand.
- **3**. Fill in the "unfamiliar environment" experience. Volunteer for one job integrating with a legacy system or working under constraints. Depth grows fastest where you are uncomfortable.
- **4–5**. Your risk is not inability, it is unwillingness to let go (Chapter 3's "coder mode"). Explicitly cede the builder time you save to the axes on the right.

---

## 3.2 AI Engineering

The engineering capability to manage uncertainty. Eval, error taxonomy, human oversight, drift. Traditional engineering delivers certainty. AI engineering delivers **managed uncertainty**. This axis is the addition that separates this role from its five predecessors.

**Anchors**:

| Score | Behavior |
|----|----------|
| 1 | Calls model APIs and writes prompts; judges quality by feel |
| 2 | Can build basic retrieval augmentation and tool calling; can read failure cases but has no method for classifying them |
| 3 | Can write an eval for one feature, golden cases, acceptance thresholds, error categories (the method in Chapter 11) |
| 4 | Can design the human-machine division of labor, what goes to the model, what stays with people, how human overrides are recorded and flow back |
| 5 | Can manage uncertainty across a system's whole lifecycle, drift monitoring, rollback strategy, an eval that evolves with the business |

**Self-check questions**:

1. For your most recent LLM feature, can you write "an acceptance threshold plus three error categories," or only "it works pretty well"?
2. In your system, at which step do people override the AI's output? Did you design that on purpose, or did it just grow that way?
3. After launch, when the model's behavior changes (an upgrade, data drift), within how many days will you know? By what means?

**Shoring-up advice**:

- **1–2**. Start from the eval, the fastest-returning move on this axis. Write 20 golden cases and one error taxonomy table for any AI feature on your desk (Chapter 11 plus Template 11).
- **3**. Move toward the operating period. Design one complete loop for an existing system, human override into the decision trail → weekly review → rules flowing back.
- **4–5**. Settle the method into a teachable asset (Chapter 23's playbook). The scarcest output from an expert on this axis is getting other people to 3.

---

## 3.3 Business Grasp

Read the business side's process, metrics, and money. What the real workflow looks like, which business number your system moved, who watches that number.

**Anchors**:

| Score | Behavior |
|----|----------|
| 1 | Can follow a description of the request; does not know how the business side makes money or where it bleeds |
| 2 | Knows the official version of the target workflow (the SOP level) |
| 3 | Knows the real workflow, workarounds, exception handling, how the front line gets around the system (the output of Chapter 6's archaeology) |
| 4 | Can convert a system change into business metrics, handling time, leakage rate, cost |
| 5 | Can anticipate the organizational reaction, which department will resist, which metric will trigger gaming, who ends up uncomfortable |

**Self-check questions**:

1. Can you draw the real version of the target workflow (workarounds included) and have front-line users agree "that is exactly it"?
2. Can you name which of the business side's numbers your system moved, and who looks at that number in which monthly meeting?
3. On the business side, who is made uncomfortable by your system doing well? Do you have a name?

**Shoring-up advice**:

- **1–2**. Go to the field. Use Chapter 6's method to shadow one real user for half a day. That half day moves this axis further than ten industry reports.
- **3**. Learn the money math. Convert your current project's North Star metric into an annualized dollar figure, and take it to the sponsor to be corrected in person. The correcting is the classroom for this axis.
- **4–5**. Business intuition is your scarcest asset. Spend it where the leverage is highest, opportunity elimination and intake judgment (Chapters 7 and 25).

---

## 3.4 Narrative

Get every level of the organization the judgment it needs, from the front line's own words to an executive memo, from good news to bad.

**Anchors**:

| Score | Behavior |
|----|----------|
| 1 | Can write clearly what you did (an activity-list report) |
| 2 | Can report by layer, detail for engineers, progress for managers |
| 3 | Answer first. The memo leads with the conclusion and the decision you want, then the evidence (Chapter 13's pyramid structure) |
| 4 | Can deliver bad news, risks, delays, "I recommend stopping." Trust goes up afterward, not down |
| 5 | Can lead the narrative, so the project is told correctly inside the business side (short-term wins, retrospectives, public postings) |

**Self-check questions**:

1. Could the reader of your latest weekly report make a decision without asking a single follow-up question?
2. When did you last volunteer bad news within 24 hours? Did the relationship get better or worse afterward?
3. For an executive, a director, and the front line, do you tell the same project in three versions with different content?

**Shoring-up advice**:

- **1–2**. Force every report into one page, "conclusion plus the decision you want from them plus three pieces of evidence." Do ten in a row and the habit grows.
- **3**. Practice bad news. The next time a risk appears, volunteer it within 24 hours and attach your defense. Bad news plus a defense is a deposit. Bad news discovered by someone else is a withdrawal.
- **4–5**. Lend the narrative capability to the business side. Help the champion and the owner tell this project well inside their own organization (Chapter 21).

---

## 3.5 Field Judgment

Make the right trade-off on incomplete information. Red lines, priorities, the timing of an identity switch, when to say no. This axis is the hardest to build in a hurry, and it is where a deliverer at F4 and above separates from a senior engineer.

**Anchors**:

| Score | Behavior |
|----|----------|
| 1 | Executes to plan; on an exception, goes and asks |
| 2 | Can spot an anomaly and escalate, knowing what has to be said today |
| 3 | Can make trade-offs under time pressure, ranking by irreversibility (Chapter 3), with a steady sense of the red lines |
| 4 | Can anticipate risk and move it forward, writing real causes of death in the pre-mortem and turning defenses into work items at kickoff |
| 5 | Can judge whether it should be done at all, deciding before taking it on whether it is worth taking (Chapter 25's intake), and daring to say no with evidence |

**Self-check questions**:

1. Looking back at your last project, can you point to three specific moments where you should have switched identity or said no?
2. In a pre-mortem you wrote, was there an entry that later actually happened, with the defense doing its job?
3. In the past year, did you kill a direction you were part of with your own hands, and argue the reason until the other side accepted it?

**Shoring-up advice**:

- **1–2**. Judgment grows out of retrospectives. Spend 15 minutes every Friday writing "the three trade-offs I made this week and what they rested on," and after a quarter look back at which were wrong and why.
- **3**. Write a pre-mortem at the start of every new project (Template 4) and check the answers when it ends. The pattern in your missed predictions is your judgment blind spot.
- **4–5**. Teach the judgment out. Judgment is the hardest asset to hand off, and it is the core proposition of F5 in Chapter 26.

---

## 3.6 Reading the Chart and Acting

**Draw the radar**. Connect the five scores into a five-point radar chart (by hand is fine; the code hook is at the end of this page).

**Three rules for reading the chart** (the same as Chapter 3):

1. **The lowest axis decides how large a project you can own alone**, and the highest axis decides nothing. The five axes multiply, they do not add.
2. **The shape predicts the failure mode**:

| Radar Shape | High-Risk Failure Mode (Chapter 3) |
|----------|--------------------------|
| Engineering depth + AI engineering high, narrative / judgment low | Coder mode |
| Narrative + business grasp high, engineering depth thin | Consultant mode (advice you cannot verify with your own hands) |
| Field judgment low, the rest passable | Firefighter mode (cannot tell "mine to fix" from "mine to teach") |
| All five around 3, no strong suit | Busyness in place of judgment (nothing only you can do) |

3. **The 30-day shoring-up rule**. Work one axis at a time, and pick the lowest. The target has to be verifiable behavior ("the next three weekly reports draw zero follow-up questions"), not an adjective ("improve communication").

**Archive**. Record the date, the scores, and one sentence of evidence for every self-assessment. The behavior anchor table in 3.7 (Chapter 26) uses the same coordinate system to define the F1–F5 capability levels. Your historical radars are your growth curve.

---

The next two sections and the self-assessment above are three instruments on the same five-axis coordinate system. The self-assessment radar fixes position (how strong each axis is at a given moment). The behavior anchors fix level (what the next level requires on each axis). The growth agreement fixes the path (turning the level gap into a year's plan). Chapter 3 makes the first assessment with the self-assessment sheet, Chapter 26 re-assesses with the anchor table and the growth agreement, and your quarterly archive is the evidence base for the rating. That is how the two ends close the loop.

## 3.7 The F1–F5 Behavior Anchor Table

**Rules**:

1. The cells hold behavior anchors ("have you done it or not"), not adjectives. An axis sits at a level only when every anchor at that level has behavioral evidence with **you as the subject** (having taken part does not count, having carried it does).
2. **Overall level = the lowest of the five axes.** The five axes multiply, they do not add (Chapter 3's rule for reading the chart).
3. Each level absorbs the one before it. Rating at F3 assumes you can still produce the F2 anchors.

### Engineering Depth

| Level | Behavior Anchor |
|----|----------|
| F1 | Completes modules inside an existing codebase and a familiar stack; needs support for deployment and integration; catches the obvious errors in AI output on review |
| F2 | Takes a prototype to production alone, data integration, deployment, monitoring, rollback, the whole loop by one person |
| F3 | Still lands a maintainable integration on an unfamiliar stack and in constrained environments (legacy systems, no documentation, strict security requirements) |
| F4 | Sets the technical baseline for several parallel projects; locates the layer of an architecture problem in someone else's project quickly |
| F5 | The organization's principles for technology choice and its standard for reusable components came from you, and were proven on several real projects |

### AI Engineering

| Level | Behavior Anchor |
|----|----------|
| F1 | Calls models, writes prompts, runs an existing eval; can describe failure cases but has no method for classifying them |
| F2 | Writes the five-part eval spec alone and uses it to rule on a plan; has designed a human oversight and decision trail loop |
| F3 | Maintains evals for several business lines at once; has ruled between conflicting error tolerances with all parties accepting it |
| F4 | The eval method settled into a pattern library asset that other projects reuse; decision trail data aggregated across projects into product-level insight (Chapter 24) |
| F5 | The organization's AI quality standard (error taxonomy, error severity vocabulary, acceptance discipline) was defined by you and stayed in use |

### Business Grasp

| Level | Behavior Anchor |
|----|----------|
| F1 | Follows the request; can repeat back the official process |
| F2 | Dug out the real workflow and the source of truth by hand; converted the North Star metric into money and had the sponsor accept it |
| F3 | Reads the interest structure of several departments at once; has anticipated who would resist and which metric would trigger gaming, and changed the design in advance |
| F4 | Recognizes isomorphic problems across industries (reusing the judgment structure, Chapter 23); can write the evidence for an n≥2 generalization argument |
| F5 | Has judged whether a class of business scenario is worth the organization's investment; the strategic value axis of the intake rubric was calibrated by you |

### Narrative

| Level | Behavior Anchor |
|----|----------|
| F1 | Reports what was done, accurately, leaving out no bad news |
| F2 | Runs the three-memo system alone; volunteers bad news within 24 hours; has traded a one-page memo for a decision |
| F3 | Holds trust on both sides between opposed sponsors; tells the same fact to conflicting parties in versions each can accept, without distorting it |
| F4 | Has designed the narrative for team members and for the business side's champion; the format that translates between the field and the product came from you |
| F5 | Speaks publicly for this method (industry exchanges, open talks); the way the organization tells its own methodology carries your hand |

### Field Judgment

| Level | Behavior Anchor |
|----|----------|
| F1 | Spots anomalies and escalates the same day; can recite the red line list and holds it |
| F2 | Ranks by irreversibility under time pressure; writes real causes of death in a pre-mortem; dares to write a readout that says "stop" |
| F3 | Judgment still holds under conflicting interests. When two decision-makers pull against each other, handles it by written principle instead of picking a side in the moment |
| F4 | Trade-offs at the portfolio level. Has judged, across several projects, which to save, which to kill, whom to send |
| F5 | Has said no to an organization-level opportunity and offered a way out; the kill register and the retrospective discipline were built by you (Chapter 25) |

**A worked rating** (mapped from Chapter 26's Anchor & Helm self-assessment). The evidence on the five axes reads F2 / F2 (close to F3) / F2 / F2 (close to F3) / F2 (barely) → overall level F2. "Close to F3" does not change the rating. It only tells you what the growth agreement should say.

---

## 3.8 The Annual Growth Agreement Template

**How to use this**. Write it at the end of a closeout season or at year end, one page or less. Once written, align it with one senior person you trust (a mentor, your manager, or a long-standing business-side lead). It must be reconciled six months later. The agreement is how Chapter 26's sentence lands. Project count is not experience. Complexity jumps are.

| Field | What to Fill In |
|----|----------|
| **What you carried this year** | A description of complexity plus behavioral evidence, not a project list ("did three projects" fails) |
| **What complexity you will carry next year** | One sentence, pointing at a specific F-level gap |
| **The gap** | Which axis, and which anchors still have no evidence with you as the subject |
| **Which project fills it** | Whether one is in the existing pipeline; if not, whom you ask for what kind of project |
| **Six-month checkpoint** | Verifiable behavior, not an adjective ("increase influence" fails) |
| **Reconciliation record** (fill in after six months) | What happened; where the agreement was wrong, and why |

**Three rules**:

1. **The checkpoint has to be a behavior**. Did it happen or not, judged at a glance.
2. **If the projects do not match, go negotiate**. Take this page to whoever assigns the work. It turns "I want good projects" into "I need evidence at this level of complexity."
3. **The reconciliation is worth more than the filling in**. The fields you got wrong are your judgment blind spots, the same way checking a pre-mortem's answers works.

**A worked example (Chapter 26, "your" Swiftway version)**:

> **What you carried this year**: one sponsor, one business line, from a vague ask all the way to L4 on your own (the top of the outcome ladder, the business side self-sufficient, L0 demo → L4, defined in Chapter 1; Anchor & Helm, graduating F2; evidence, primary responsibility from charter through handoff, with the last impact memo written by the business-side owner himself).
> **What you will carry next year**: deliver an L3 (real adoption) or above once under the conflicting interests of dual sponsors (F3's first question).
> **The gap**: the F3 anchors on field judgment and narrative. A charter co-signed by opposing parties, and information discipline under conflict, neither has evidence.
> **Which project fills it**: Swiftway Logistics (dual Group and subsidiary sponsors, two decision-makers pulling against each other).
> **Six-month checkpoint**: draw the dual-headed stakeholder map with both sides agreeing to it; the first time instructions from the two sides conflict, handle it by the principle written down in advance rather than picking a side in the moment.
> **Reconciliation record**: (fill in after six months.)

---

## 3.9 The Bridge for Newcomers: The Last Mile from Engineer to This Role

This section is for engineers who have not done this job and want to enter this kind of work (it applies to solutions engineer and similar titles). Score a radar with 3.1–3.6 first. The typical newcomer shape is high on the left and low on the right. Engineering depth and AI engineering have evidence, the three axes on the right do not. This section does three things: it translates the experience you already have into this language (3.9.1), turns the book's frameworks into interview ammunition (3.9.2), and turns internal cross-department delivery into F1 evidence (3.9.3).

### 3.9.1 How to Word Your Resume

There is one rule, taken from Chapter 0's workflow claim structure. Rewrite each item as "whose action it changed, and which business number it moved," with you as the subject of the verb (the same source as 3.7's rating rule).

| Background | Radar Strength | Weakest Axes | Rewrite Example (Original → the Deliverer's Language) |
|----------|----------|----------|------|
| Recommendation / search ML engineer | AI engineering | Business grasp, narrative | "Ranking model AUC +2%" → "Co-built the evaluation definition with the business side, converted the model improvement into $X per order of conversion revenue, and drove operations to adjust the strategy on that basis and ship it" |
| Backend engineer | Engineering depth | AI engineering, business grasp | "Refactored the order service, tripled QPS" → "Rebuilt the order path under a no-downtime constraint on a legacy system, aligned the cutover plan with the ops and risk teams, and ran two weeks of gradual rollout with zero incidents" |
| Data engineer | Engineering depth (data side) | Narrative, field judgment | "Built the ETL, X hundred million rows a day" → "Aligned three data sources with conflicting definitions into one source of truth the business side accepted, surfaced N status fields that did not match actual business, and drove the fixes" |
| Pre-sales SA | Business grasp, narrative | Engineering depth, AI engineering | "Led X POCs, win rate Y%" → "Did the data integration and deployment in the POCs with my own hands, and N of them reached production and daily use on the business side (L3 and above)" |

### 3.9.2 Common Interview Questions → Chapter Ammunition Index

Six common questions, each with the chapter numbers and a skeleton answer. The skeleton is the order of trade-offs. Go back to the chapter for the detail.

**1. "A business-side executive does not trust the model's output. What do you do?"** (Chapters 5, 11, 12) Trust is the first deliverable, accumulated through small verifiable promises, not by explaining how the model works. Bring the business experts the executive trusts into co-building the eval. They set the golden cases and the acceptance thresholds. Then show him the human oversight design explicitly, which outputs must be confirmed by a person, and how errors get found and rolled back.

**2. "The demo went well and the project will not move. How do you diagnose it?"** (Chapters 1, 17, 20) Use the outcome ladder first to locate which rung it is stuck on. A successful demo is only L0, and being stuck is usually an adoption problem, not a technical one. Then read resistance as a diagnostic signal. Whose workflow changed, who is made uncomfortable, get the names before discussing a plan. Last, check the delivery form. A dashboard changes nobody's next action, and it usually has to be rebuilt into an action queue embedded in the workflow.

**3. "The business side demands 99% accuracy and there is no ground truth. How do you take it?"** (Chapters 4, 11) Do not take the number, take the definition first. Eval as spec. Co-build the golden cases and the error categories with the business side's own experts, and "99%" decomposes, in front of concrete cases, into different tolerances for different errors. Negotiate thresholds by severity. Which class of error gets zero tolerance, which can be backstopped by a person. The thresholds you settle go into the charter's success metrics and exit conditions, never into a verbal promise.

**4. "What would you do in the first week?"** (Chapters 0, 4, 5) Run a two-hour Field MVP within 48 hours. Write the workflow claim, get 10 cases (if the data cannot leave the database, copy the structure by hand at the data owner's screen), and have a real user score them on four grades (pass / concern / unsafe / useless). Take the scoring results into the deployment charter negotiation, goal, users, data boundary, success metrics, exit conditions. Draw the stakeholder map at the same time, and confirm the actual user, the owner, the data side, the risk side, and the maintainer are all identified.

**5. "The data is bad. Do you still do the project?"** (Chapters 9, 25) Use the data fitness ladder first to locate which rung it is bad at (exists, accessible, interpretable, timely, traceable, validated, actionable), because the fix is completely different at each. Then narrow. Use a thin slice to find the one narrow business line with the best data and get that running, and write the data problems into the readout as evidence. Hit a red line (no source of truth can be built) and give the conclusion "stop or redirect" with the evidence attached.

**6. "How do you prove your project produced business value?"** (Chapters 18, 19) The metric is set in the charter before work starts, not looked for before the report. The North Star metric is converted into money and accepted by the sponsor in advance. After launch, prove the improvement instead of only showing a trend, with a baseline comparison, the human override rate, and decision trail data. Report with a pyramid memo, answer first. The hardest evidence is an impact memo the business-side owner wrote himself.

### 3.9.3 Internal Cross-Department Delivery Is the Main Stage

Internal cross-department delivery is not a second-best substitute. It is another room for the same exam. Check it against 3.7's F1 anchors. The ticket is not an external site, it is "complete a delivery inside a given boundary, review AI output competently, escalate exceptions." You can sit that exam inside your company right now, and it is easier to sit than an external project, because the requester and the data are in the same building and you are not waiting on someone else to approve access. Three steps.

**Step one, pick a cross-department delivery project.** The users are not on your team (operations, sales, finance, another department), the ask is vague (at the "help us be more efficient" level), and there is real data and there are real users. Internal tools, process automation, and report rebuilds all count. The test. The requester and the user are not the same person, and if nobody uses it when it is done, you can observe that. Meet both and it is a mock exam room for F1.

**Step two, produce the artifacts the way the book does.** A one-page charter before work starts (Template 4). A two-hour Field MVP with real users scoring on four grades (Template 0). Twenty golden cases plus acceptance thresholds before launch (Template 11). A one-page impact memo at closeout, with the business numbers confirmed by the using side. The four artifacts make up your F1 evidence base, and you are the subject of every one.

**Step three, write it into your resume by 3.9.1's rule.** Not "developed an internal tool," but behavioral evidence. "Converged department X's vague ask into a workflow claim, and narrowed the scope after real users scored it line by line. After launch, metric Y improved Z%, confirmed by the using side. The system stayed in daily use after I stepped out." That last half sentence (the system stayed in daily use after you left) is the scarcest evidence on a newcomer's resume.

When an interviewer says "you have never worked an external site," answer with the artifacts from these three steps. The requester, the user, and the data owner in a cross-department project are a scaled-down interest structure, and the four artifacts prove you carried it (3.7's rating rule counts only having carried it).

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/self-assessment/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/self-assessment/): the radar chart generation script and team roll-up template for the capability self-assessment sheet (3.0–3.6)
- [`templates/f-levels/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/f-levels/): the F-level rating questionnaire and the "historical radar → F level" comparison script, sharing one data format with the radar chart script in [`templates/self-assessment/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/self-assessment/), so quarterly self-assessment archives feed straight into the annual growth agreement
