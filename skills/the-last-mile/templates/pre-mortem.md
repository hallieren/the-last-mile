# Pre-mortem memo

Source: `docs/appendices/template-04-deployment-charter.md` §4.3–4.6 (and `repo/templates/premortem/premortem-template.md`; the repo wins on conflict).

| Field | Value |
|---|---|
| To | <sponsor, by name> REQUIRED |
| Subject | The five most likely ways <project name> dies |
| Written | <date>, at kickoff, around when the charter is signed; 15–30 minutes |
| Premise | It is six months from now and this project is dead. Work backward to how it died |
| Next review | <date, monthly> REQUIRED |

```
To: <sponsor>
Subject: The five most likely ways <project name> dies

Assume this project has failed six months from now. Here are the most likely causes of death and their defenses.
```

| # | Gap | How it happens (concrete enough to picture the meeting on that day) | Defense (startable this week) | Owner | Start by |
|---|---|---|---|---|---|
| 1 | data | <e.g. the core system's status field cannot be trusted, and the suggestion is built on the wrong status> | <e.g. reconcile the data during discovery> | <name> REQUIRED | <date> REQUIRED |
| 2 | workflow | <e.g. the system never enters the screen the user opens every day, and no one logs in after two weeks> | | <name> REQUIRED | <date> REQUIRED |
| 3 | trust | <e.g. one wrong suggestion causes an incident, and the front line stops trusting any suggestion from then on> | | <name> REQUIRED | <date> REQUIRED |
| 4 | ownership | <e.g. the security review does not start until late in the pilot, and it blocks launch> | | <name> REQUIRED | <date> REQUIRED |
| 5 | value | <e.g. three months in, no one can say what was saved, and the project gets "archived as a success"> | | <name> REQUIRED | <date> REQUIRED |

Each cause of death must: (1) map to one of the five gaps, (2) come with a defense you can start this week, (3) name an owner for that defense.

**Reference library of common ways to die** (check against while drafting)
- Data: the source of truth is one team's private spreadsheet; the status field lags; the join keys are unstable; the data owner will not grant production access.
- Workflow: the user is asked to open an N+1th system; suggestions have no owner; exceptions have no exit; the time saved gets eaten by new review work.
- Trust: one unsafe incident in the first month decides everything; suggestions cannot be questioned because they carry no reason; the front line feels watched instead of helped.
- Ownership: the security or compliance review starts too late; no owner after launch; responsibility never fully transfers, so the system goes dark when you change roles or take leave; the business-line engineers never co-built it; you never step out of the daily and the team becomes permanent ops.
- Value: the metric is an activity, not an outcome; nobody claims the North Star; the success criteria get discussed the week before the demo; ROI can only be expressed as accuracy.

**Rules**
- Make each cause of death concrete enough that you can picture the meeting on that day. Do not write vague phrases like "low user adoption."
- Cover at least four of the five gaps. If every cause of death lands in one gap, you have not yet seen the others.
- Send the finished memo to the sponsor. The pre-mortem's second function is as a stakeholder detector. Whoever it draws out to come talk to you is often a key role you had not identified yet.
- Review it monthly. The cause-of-death list is a living document. Add new ways to die as you find them during the pilot.
- Draft it the night before the charter is signed; it is a stress test of the seven elements, and its causes and defenses are the raw material for element 7's exit conditions. Put the two documents in front of the sponsor together.

Filled in → goes to: the deployment charter element 7 (exit and reassessment triggers) and the self-checks in every cell; the stakeholder map (the name it draws out, and the risk owner it is hand-delivered to); the kill criteria at pilot approval.
