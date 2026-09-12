# Deployment charter

Source: `docs/appendices/template-04-deployment-charter.md` §4.1–4.2 (and `repo/templates/deployment-charter/charter.md`; the repo wins on conflict).

| Field | Value |
|---|---|
| Project | Deployment Charter · <project name> |
| Version / date / drafted by | v<n> / <date> / <your name> |
| Signed by | <business-side decision-maker> REQUIRED · <business-side owner> REQUIRED · <you> REQUIRED · <your manager> REQUIRED |
| Preconditions (missing any one, reschedule) | decision-maker confirmed · role charter aligned with the sponsor · Field MVP evidence pack · draft pre-filled with contested cells marked · extracts of existing approval / ticket acceptance wording |

| # | Element | Field | Content |
|---|---|---|---|
| 1 | North Star outcome metric (one, measurable) | Metric definition | <business outcome metric, precise down to how it is measured> REQUIRED |
| | | Baseline | <current value + data source; if unverified, "as set by discovery's reconciliation"> REQUIRED |
| | | Target change | <e.g. -N%; how derived, citing the Field MVP / the data breakdown> REQUIRED |
| | | Settlement point | <when measured, over what window, who produces the number> REQUIRED |
| 2 | actual user and owner (by name) | actual user | <name(s)>, the people whose daily work changes REQUIRED |
| | | owner | <name, title>, owns and operates it after launch (not the deliverer) REQUIRED |
| | | executive sponsor | <name, title>, settles resources and metrics REQUIRED |
| 3 | Scope and red lines | This phase does | <what gets built> |
| | | This phase does not | <every discussed and excluded request, by name> REQUIRED |
| | | Red lines (not touched at all) | <e.g. no automated <core decision>; no automated outbound messages; no identifiable customer information> REQUIRED |
| 4 | Data boundary and access commitments | List of data needed | <dataset × form (read-only / export / de-identified sample) × purpose> |
| | | De-identification and data-exit rules | <what may leave the business side's environment (usually none); who sets the standard> |
| | | Approvers and deadlines | <named approver per dataset + committed delivery date> REQUIRED |
| | | Security review timing | <start and finish in the schedule, named owner> REQUIRED |
| 5 | Business-side commitment (people × time, by name) | <person / team> | <hours per week> for <purpose>, <term>, <constraints: booked in advance, not during peak> REQUIRED |
| | | <business-line engineers × n> | <days per week> for co-build, take over maintenance |
| | | <the owner in person> | the weekly meeting plus a decision response time |
| | | Your team's commitment and protection conditions | <you and your team, by name, x days a week>, from discovery through completion of handoff; countersigned by <your manager>; pulling anyone goes through <the sponsor's weekly> first REQUIRED |
| 6 | Launch release conditions (tied to the eval) | Release mechanism | The eval spec both sides co-build is the authority, <n> golden cases plus agreed thresholds; a score over the line releases the launch REQUIRED |
| | | Releasers | <business-side owner> plus <risk owner>, not you REQUIRED |
| | | Eval spec status | <who co-builds it, by when; becomes an attachment once written> |
| | | Release methods explicitly excluded | The demo passed, the boss is happy, trial feedback was good, are not grounds for release |
| 7 | Exit and resource reassessment (three parties) | Delivery side may call reassessment | Trigger: promised data access / staffing unmet two weeks running. Action: three tiers, sponsor weekly → "awaiting inputs" on the PMO register with the missing input named → people released and recorded openly REQUIRED |
| | | Business side may call reassessment | Trigger: <a key risk event; a compliance change>. Action: sponsor weekly decides between cutting scope, going manual, adding input REQUIRED |
| | | Sponsor may call re-prioritization | Trigger: <a higher-priority project; a budget shift>. Action: re-place in the schedule, both sides reconfirm the cadence REQUIRED |
| | | Termination | When two consecutive evaluation cycles miss the threshold and no workable path to improvement exists, either side may propose termination |

**60-minute agenda**: 0:00–0:10 open with evidence (MVP scores and readout, no vision deck) · 0:10–0:25 North Star (definition → baseline with data risk → derivation; answer a target dispute with a data breakdown, never "I think") · 0:25–0:35 names and commitments (names not departments; hours confirmed in the room by the person or their manager) · 0:35–0:45 scope, red lines, data boundary (excluded requests onto "not this phase" by name; each dataset an approver and a date; security review date into the schedule) · 0:45–0:55 acceptance then exit (sign the mechanism first, ride it into exit; warn them the silence is coming) · 0:55–1:00 read back and commit (write-up within 48 hours, signing within a week).

**Rules**
- One page maximum; you draft it, it gets changed together in the meeting, and both sides sign. Every cell must be changed by the business side at least once during the contracting meeting. A charter with no business-side fingerprints on it is not an agreement.
- The charter and the project approval form are two documents. The approval form governs budget and process compliance, the charter governs the work and the expectations.
- Only one North Star. A second "important metric" is demoted to an observation metric and listed separately. Could this sentence fail to come true? A goal that cannot fail is not a goal. When the metric gets worse, does it hurt anyone?
- Write names, not departments. If the owner cell holds you or your own team, the handoff is already destined to fail.
- The "not this phase" list is the main defense against scope creep. A request that was turned down has to leave its name on paper, or it revives at every meeting.
- An access commitment with no date is not a commitment.
- This cell (element 5) left blank = a one-sided love letter. The hours written down have to enter the other side's calendar system. Your team's row only counts once your manager countersigns.
- Sign the mechanism now, fill in the numbers later. "Release criteria to be determined" is unacceptable. "Release mechanism settled, thresholds per the attachment" is acceptable.
- All three parties can raise reassessment; none of the rows says who may pause. The person who calls a stop does not have to be the villain.
- A change = a renegotiation. Any side changing any element must notify all signatories and get their confirmation, and the version number goes up by one. Written up within 48 hours of the meeting with every "changed in the meeting" spot marked; signed within a week; conflicting old approval wording filed through a project approval change review.

**What a wrong filling looks like**
- Element 1: "complete the launch and train everyone; also improve reviewer satisfaction." An activity that cannot fail, plus a smuggled second North Star.
- Element 2: "the relevant colleagues in the department; owner: the delivery team (during the transition)." Not a name; owner = you writes the handoff failure into the charter.
- Element 3 "not this phase": blank. Every turned-down request can revive at the next meeting.
- Element 4: "IT will give strong support and open the relevant access as soon as possible." No approver, no date; the death email nobody answers.
- Element 5: "the business department strongly supports this and agreed verbally at its weekly." No name, no hours, in nobody's calendar.
- Element 6: "release criteria to be agreed after launch." Expressly unacceptable. Element 7: "if the business side is not satisfied, it may terminate at any time." One-way, no trigger, a disclaimer.

Filled in → goes to: the pre-mortem (drafted the same night; its causes of death feed element 7), the Five Ones sentence and boundary map (element 3), the data fitness table (element 4), the eval spec (element 6 attachment), the kill criteria (element 7's pilot-level sibling).
