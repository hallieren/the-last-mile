# Template 4 · Deployment Charter and Pre-mortem Memo

> Companion chapter(s): Chapter 4 (the pre-mortem sections, Chapter 1). The fillable one-page charter with its seven elements, the 60-minute contracting meeting agenda, and the pre-mortem memo, ready to copy and modify.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 4.1 The Deployment Charter One-Pager (Seven Elements)

> Rules: **one page maximum; you draft it, it gets changed together in the meeting, and both sides sign**. Every cell must be changed by the business side at least once during the contracting meeting. A charter with no business-side fingerprints on it is not an agreement. The charter and the project approval form are two documents. The approval form governs budget and process compliance, the charter governs the work and the expectations.

```
Deployment Charter · [project name]
Version: v[ ]  Date: [ ]  Drafted by: [ ]  Signed by: [business-side decision-maker] [business-side owner] [you] [your manager]
```

### Element 1, North Star Outcome Metric (One, Measurable)

| Item | Content |
|---|---|
| Metric definition | [the business outcome metric, precise down to how it is measured, e.g., first-touch handling time for auto exceptions (defined as calendar days from claim report to first handling completed)] |
| Baseline | [current value plus data source; if the baseline data is still unverified, write "as set by discovery's reconciliation"] |
| Target change | [e.g., -30%; state how this number was derived (cite the Field MVP / the data breakdown analysis)] |
| Settlement point | [when it gets measured, over what window, and who produces the number] |

**Self-Check**:
- Only one North Star. A second "important metric" is demoted to an observation metric and listed separately.
- An outcome (handling time, leakage rate), not an activity ("development complete," "launch training done"). The test, could this sentence fail to come true? A goal that cannot fail is not a goal.
- When the metric gets worse, does it hurt anyone? A metric nobody hurts over is not the North Star (Chapter 1).

### Element 2, actual user and owner (by Name)

| Role | Name / Title | Notes |
|---|---|---|
| actual user | [e.g., Linda Marsh and her review team (eight people)] | The people whose daily work the system changes after launch |
| owner | [e.g., Kevin Doyle, Director of Claims Operations] | The person who owns and operates this system after launch (not the deliverer) |
| executive sponsor | [e.g., Grant Whitmore, COO] | The person who settles resources and metrics |

**Self-Check**: Write names, not departments. If the owner cell holds you or your own team, the handoff (Chapter 22) is already destined to fail.

### Element 3, Scope and Red Lines

| Category | Content |
|---|---|
| This phase does | [e.g., the auto exceptions action queue, covering missing documents / abnormal amount / disputed liability] |
| This phase does not | [write out explicitly what was discussed and excluded, e.g., the management dashboard, non-auto lines of business, routine claims] |
| Red lines (not touched at all) | [e.g., no automated payout decisions; no automated outbound messages; no handling of identifiable customer information] |

**Self-Check**: The "not this phase" list is the main defense against scope creep. A request that was turned down has to leave its name on paper, or it revives at every meeting.

### Element 4, Data Boundary and Access Commitments

| Item | Content |
|---|---|
| List of data needed | [dataset × form (read-only / export / de-identified sample) × purpose] |
| De-identification and data-exit rules | [what data may leave the business side's environment (usually none); who sets the de-identification standard] |
| Approvers and deadlines | [the named approver for each dataset plus the committed delivery date] |
| Security review timing | [review start and finish written into the schedule, with a named owner] |

**Self-Check**: Every row of data needs "who approves it, when it arrives." An access commitment with no date is not a commitment, it is that week 9 email nobody answers.

### Element 5, Business-Side Commitment (People × Time, by Name)

| Person / Team | Commitment | Purpose | Term | Constraints |
|---|---|---|---|---|
| [e.g., Linda's team] | [2 hours a week] | [case annotation, rule confirmation] | [from discovery through one month after launch] | [booked in advance, not during peak hours] |
| [e.g., business-line engineers ×2] | [x days a week] | [co-build, take over maintenance] | [ ] | [ ] |
| [the owner in person] | [the weekly meeting plus a decision response time] | [ ] | [ ] | [ ] |
| **Your team's commitment and protection conditions** | [you and your team members, x days a week, by name] | [discovery, co-build and handoff] | [from discovery through the completion of handoff] | [countersigned by your manager, stating whose weekly must clear it before anyone is pulled] |

**Self-Check**: This cell left blank = a one-sided love letter. "What you want" (element 1) and "what you are willing to put in" (this element) must be settled in the same room, and if you cannot agree you do not sign. The hours written down have to enter the other side's calendar system, not stay in their wishes. Your team's commitment row cannot be blank either. Your schedule is a resource too, and it only counts once your manager countersigns.

### Element 6, Launch Release Conditions (Tied to the Eval)

| Item | Content |
|---|---|
| Release mechanism | The eval spec both sides co-build is the authority, [n] golden cases plus agreed thresholds, and a score over the line releases the launch |
| Releasers | [the business-side owner plus the risk owner, not you] |
| Eval spec status | [usually not built yet at signing; state who co-builds it, by when, and that it becomes an attachment to this charter once written] |
| Release methods explicitly excluded | Subjective methods, the demo passed, the boss is happy, trial feedback was good, are not grounds for release |

**Self-Check**: Sign the mechanism now, fill in the numbers later. "Release criteria to be determined" is unacceptable. "Release mechanism settled, thresholds per the attachment" is acceptable. How to build the eval spec is in Chapter 11.

### Element 7, Exit and Resource Reassessment Conditions (Three Parties)

| Direction | Trigger | Action |
|---|---|---|
| The delivery side may call a resource reassessment | [e.g., the business side's promised data access / staffing goes unmet two weeks running] | [three tiers: escalate to the sponsor weekly / the project turns to "awaiting inputs" on the PMO register / your team's people are released and it is recorded openly, see the three tiers of resource reassessment (Chapter 4)] |
| The business side may call a resource reassessment | [e.g., a key risk event; a change in compliance requirements] | [escalate to the sponsor weekly, where the sponsor decides between cutting scope, going manual, or adding input] |
| The sponsor may call a re-prioritization | [e.g., a higher-priority project appears; the budget cycle shifts] | [re-place this project in the schedule, and both sides reconfirm the delivery cadence against the new schedule] |

**Self-Check**: All three parties can raise it. A charter written for the business side only is a disclaimer. One written for the delivery side only is a one-sided contract. Inside a company there is no pause card (Chapter 4), salaries get paid either way, so all three rows are about reassessment and re-prioritization, and none of them says who may pause. The function of exit and resource reassessment conditions is to make sure the person who calls a stop does not have to be the villain. The full judgment on kill criteria is in Chapter 14.

---

## 4.2 The 60-Minute Contracting Meeting Agenda

**Before the meeting** (missing any one item, reschedule):
- [ ] The decision-maker has confirmed attendance (someone who can settle metrics and commitments on the spot)
- [ ] The role charter (Template 2) is aligned with the sponsor (say who you are first, then talk about what the project does)
- [ ] The Field MVP evidence pack, the original scoring results, the readout memo, the key data breakdown analysis
- [ ] The charter draft (all seven elements pre-filled, with the cells you expect to be contested marked)
- [ ] Extracts of the acceptance and scope wording from any existing project approval form or ticket (if it conflicts with the charter, say so in the meeting and agree how to handle it)

**Agenda**:

| Time | Segment | Key Points | Facilitation Rule |
|------|------|------|----------|
| 0:00–0:10 | Open with evidence | Retell the MVP scoring results and the readout conclusion, no vision deck | Anchor every negotiation to evidence; when someone returns to the vision story, pull them back to the scoring sheet |
| 0:10–0:25 | North Star negotiation | Metric definition → baseline (with the data risk stated) → how the target was derived | Answer a disagreement over the target with a breakdown of the data, never with "I think"; if the baseline is not clean, write "as set by the reconciliation" |
| 0:25–0:35 | Names and commitments | actual user and owner by name; the business-side commitment settled row by row | Names, not departments; get the person or their manager to confirm the hours in the room |
| 0:35–0:45 | Scope, red lines and the data boundary | The three lists of "do / do not / do not touch"; each dataset gets an approver and a date | Excluded requests go on the "not this phase" list by name; the security review date goes into the schedule |
| 0:45–0:55 | Acceptance and exit | Sign the acceptance mechanism first (eval plus thresholds to follow), then ride it into the exit conditions | Warn them the silence is coming; explain that exit conditions mean the person who calls a stop does not have to be the villain, two-way and equal |
| 0:55–1:00 | Read back and commit | Read the seven elements back out loud; agree on writing it up within 48 hours and signing within a week | The facilitator does the read-back, and the business side's corrections are the last round of alignment |

**Within 48 hours of the meeting**:
- [ ] The charter is written up and sent, with every "changed in the meeting" spot marked (so the business side sees its own fingerprints)
- [ ] Collect the edits (every edit is a cheap expectation gap blowing up, so welcome it)
- [ ] Complete the signing within a week; where it conflicts with existing project approval wording (the old ticket's acceptance clause, say), file it through a project approval change review

**Change rule**: the charter is a living document, but a change = a renegotiation. Any side changing any element must notify all signatories and get their confirmation, and the version number goes up by one. A charter changed quietly is worse than no charter.

---

The pre-mortem memo below sits in the same template unit as the charter, and not by accident. The pre-mortem is written around the time the charter is signed. Writing down the causes of death the night before signing is a stress test of the seven elements. The causes of death and defenses it lists are the best raw material for element 7's exit conditions (and for the self-checks in every cell). Draft the two documents together and put them in front of the sponsor together, and only then is contracting complete.

> Companion chapter(s): Chapter 1. Write it at project kickoff (around when the charter is signed), 15–30 minutes. The method comes from Gary Klein's pre-mortem (a post-mortem done in advance). This template adapts it for the deliverer's setting.

## 4.3 How to Write It

The premise. **It is six months from now and this project is dead.** Work backward to how it died.

Each cause of death must: (1) map to one of the five gaps, (2) come with a defense you can start this week, (3) name an owner for that defense.

## 4.4 Template

```
To: [sponsor]
Subject: The five most likely ways [project name] dies

Assume this project has failed six months from now. Here are the most likely causes of death and their defenses.

Cause of death 1 (data gap):
  How it happens: [e.g., the core system's status field cannot be trusted, and the suggestion is built on the wrong status]
  Defense: [e.g., reconcile the data during discovery]  Owner: [ ]  Start by: [ ]

Cause of death 2 (workflow gap):
  How it happens: [e.g., the system never enters the screen the user opens every day, and no one logs in after two weeks]
  Defense: [ ]  Owner: [ ]  Start by: [ ]

Cause of death 3 (trust gap):
  How it happens: [e.g., one wrong suggestion causes an incident, and the front line stops trusting any suggestion from then on]
  Defense: [ ]  Owner: [ ]  Start by: [ ]

Cause of death 4 (ownership gap):
  How it happens: [e.g., the security review does not start until week 10, and it blocks launch]
  Defense: [ ]  Owner: [ ]  Start by: [ ]

Cause of death 5 (value gap):
  How it happens: [e.g., three months in, no one can say what was saved, and the project gets "archived as a success"]
  Defense: [ ]  Owner: [ ]  Start by: [ ]
```

## 4.5 Rules

- Make each cause of death concrete enough that you can picture the meeting on that day. Do not write vague phrases like "low user adoption."
- Cover at least four of the five gaps. If every cause of death lands in one gap, you have not yet seen the others.
- Send the finished memo to the sponsor. The pre-mortem's second function is as a stakeholder detector. Whoever it draws out to come talk to you is often a key role you had not identified yet.
- Review it monthly. The cause-of-death list is a living document. Add new ways to die as you find them during the pilot.

## 4.6 Reference Library of Common Ways to Die (by Gap, to Check Against While Drafting)

- **Data**: the source of truth is one team's private Excel; the status field lags; the join keys are unstable; the data owner will not grant production access
- **Workflow**: the user is asked to open an N+1th system; suggestions have no owner; exceptions have no exit; the time saved gets eaten by new review work
- **Trust**: one unsafe incident in the first month decides everything; suggestions cannot be questioned because they carry no reason; the front line feels watched instead of helped
- **Ownership**: the security or compliance review starts too late; no owner after launch; responsibility never fully transfers, so the system goes dark when you change roles or take leave; the business-line engineers never co-built it; you never step out of the daily and the team becomes permanent ops
- **Value**: the metric is an activity, not an outcome; nobody claims the North Star; the success criteria get discussed the week before the demo; ROI can only be expressed as accuracy

---

## 4.7 Counterexample: A Tidy-Looking Wrong Answer

Every one of the seven elements has words in it, and both sides will sign, because it binds nobody. Excerpts:

```
Element 1 North Star: complete the exceptions action queue launch and train everyone; also improve reviewer satisfaction.
Element 2: actual user: the relevant colleagues in Claims; owner: the delivery team (holding it during the transition).
Element 3 not this phase: (blank, "no requests currently need excluding")
Element 4 data: IT will give strong support and open the relevant access as soon as possible.
Element 5 business-side commitment: the business department strongly supports this and agreed verbally at its weekly.
Element 6 release: the specific release criteria will be agreed between the two sides after launch.
Element 7 exit: if the business side is not satisfied, it may terminate the cooperation at any time.
```

Item by item:

1. "Complete the launch and the training" is an activity, not an outcome. It cannot fail to come true, so it fails element 1's test. And "also improve satisfaction" stuffs in a second North Star. The correct form is one measurable outcome metric plus a baseline plus a derivation of the target.
2. "The relevant colleagues" is not a name. Filling owner with the delivery team itself writes the Chapter 22 handoff failure into the charter back in Chapter 4 (see element 2's self-check).
3. "Not this phase" left blank means every request that was ever turned down can revive at the next meeting.
4. "Strong support" has no named approver and no date. This is that week 9 email nobody answers.
5. The commitment cell, "the business department strongly supports this and agreed verbally at its weekly," has no name, no hours, and has entered nobody's calendar system. That is a one-sided love letter.
6. "Criteria to be determined" is exactly the wording element 6 declares unacceptable. What is acceptable is "the release mechanism is signed, thresholds to follow in the eval spec attachment."
7. The exit clause is one-way with no trigger condition. That is a disclaimer, not a mechanism for making sure the person who calls a stop does not have to be the villain. Only when all three parties are equal and each trigger condition is written down explicitly do you have workable resource reassessment conditions.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/deployment-charter/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/deployment-charter/): the document scaffolding for this template and the AI prompt script that turns meeting minutes into a charter
- [`templates/premortem/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/premortem/): the pre-mortem facilitation prompt
