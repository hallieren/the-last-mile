# Template 15 · Co-build Agreement and Knowledge Transfer Cadence

> Companion chapter(s): Chapter 15. The two tools are used in time order. The agreement (15.1) is signed after the pilot is called and before it starts, one page, signed by both sides, the "constitution" of the co-build period. The cadence sheet (15.2) is the vehicle for clause four, running from pilot week 2 to the handoff (Chapter 22), one beat every two weeks (weekly at Anchor & Helm after the team expanded).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 15.1 Co-build Agreement Template

### 15.1.0 Agreement Header

| Item | Fill In |
|----|------|
| Project | |
| Receiving-side owner (real name) | |
| Receiving-side engineers (real names, at least 1) | |
| Digital Center (real names) | |
| Effective date / expected handoff date | |
| Signatures (everyone above) | |

Signing timing, after the pilot is called and before it starts. Later than that, the do-it-all habit has already formed. Earlier than that, the staffing sheet has no factual basis yet. The owner must sign. He is clause four's audience, and clause two's labor cost is booked to his account (the co-build engineers' project time is a commitment clause, of the same rank as the user commitment, stating weekly hours: ____, and the accounting method (booked to the project / chargeback / written into their quarterly objectives, pick one) ____).

### 15.1.1 Clause One: Code Ownership Goes to the Receiving Side

| Item | Fill In | Check |
|----|------|------|
| Module CODEOWNERS | | Names the receiving side, not your team |
| Merge rights | | With the receiving side (gatekeeping rights are allocated in 15.1.2) |
| Oncall ownership | | The rotation spells out that these modules belong to the receiving side |
| CI / release process ownership | | Runs on the receiving side's existing release process, no second one built |
| Account form for your team's members | | Collaborator status, exiting after handoff |
| Exception list | | Which code does not go into the receiving side's repo (your team's internal tooling, for instance), listed item by item with reasons |

Red line: the day the AI team holds gatekeeping rights for the long run is the day permanent ops begins. There is no option of "develop on our side first and migrate at handoff."

### 15.1.2 Clause Two: Backward Staffing Sheet

The filling order is a rule. **Fill the second column first (who maintains it after handoff), then work backward to the third (who leads the writing now)**. Any row where the two disagree must have a convergence plan written out in the last column.

| Module | Maintainer After Handoff | Where the Maintainer Is Appraised | Lead Writer | Pairing / Review Side | Current Gatekeeping Rights and Transfer Condition |
|------|-------------|------------------|------|----------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

- **Leading the writing is not writing alone**: the lead writer is accountable for the code, can explain it, and decides on merges; the other side pairs.
- **Where the maintainer is appraised**: this column answers "when it breaks at midnight, whose annual objectives say to fix it." In most cases it should match the maintainer after handoff. A row where it does not is a hidden accountability vacuum, and the convergence plan has to say how that gets filled.
- **Gatekeeping rights** (the power to decide merges) get a column of their own. Your team may hold them early, but every row states the transfer condition (for example, "handed over after two consecutive reviews of that module with no rejection"). Before handoff day, gatekeeping rights on every row should sit with the receiving side.
- A module whose complexity is beyond the receiving side for now (the Anchor & Helm example, the queue core) still gets "maintainer, the receiving side (longer term)." The pairing on that row is not a courtesy, it is the convergence path.

### 15.1.3 Clause Three: The AI Code Review Rule

Scope, **all code generated or rewritten by an AI coding agent, on both sides alike** (your team's commits are checked too).

The rule in one sentence, **if you cannot say it, do not merge it.** The module's maintaining side reviews, and the submitter goes through the three explain-it questions face to face (or over video):

1. **Why is it written this way?** Every non-obvious choice (retry count, timeout value, algorithm, edge handling) has a reason he can state. "That is how the agent wrote it" is not a reason.
2. **Where can it go wrong, and how would you find out?** The failure path, who catches it, what the log or the alert looks like.
3. **If it has to change, where do you start?** The next foreseeable change request, where the change lands and how far it reaches.

Any question unanswered → sent back. A rejection does not mean the code failed, it means the explanation failed. Before resubmitting, the submitter must actually have had his hands on it (rewriting, simplifying or adding tests all count). "Memorize it and say it again" is not accepted.

Suggested addition to the PR template, one field for the share of this commit generated by AI and the signature of the person who explained it (a PR template carrying that field is in Code Hooks at the end).

### 15.1.4 Clause Four: Rotating Release Cadence

| Item | Fill In | Default |
|----|------|--------|
| Frequency | | Every two weeks, 30–45 minutes |
| Presenter | | The receiving side's engineers in rotation. Your team does not take the stage, only adds, never answers for them |
| Standing audience | | The receiving-side owner (required) + all co-build members |
| Date of the first one | | Within pilot week 2 |

The rotating release is not a training session (there is no one-way teaching) and not a status report (nothing is reported to your team). It is the receiving side's engineers showing their own organization's owner the progress that stands under their own names. Agenda in 15.2.1.

### 15.1.5 Anchor & Helm Example (Extract from the Version Signed in Week 9)

- Clause one: code goes into modules under claims-ops IT's name, CODEOWNERS and merge rights with claims-ops IT, oncall ownership spelled out. Digital Center engineers (you included) commit as collaborators, and cross-subsidiary code repository access was approved by Victor Reyes.
- Clause two: extraction pipeline, maintainer claims-ops IT / lead writer claims-ops IT / pairing Digital Center. Queue core, maintainer claims-ops IT (longer term) / lead writer Digital Center / pairing claims-ops IT. Merged view, lead writer Digital Center, lead-writer rights handed over before handoff. Rules and de-identification as configuration, lead writer claims-ops IT (the trust constraint matrix's maintainability row).
- Clause three: first enforced in pilot week 1, when the email pull retry logic was sent back for failing the first of the three questions. After the rewrite was merged, gatekeeping rights for that module moved to claims-ops IT.
- Clause four: Fridays every two weeks, from pilot week 2. Kevin Doyle as owner is required.

---

## 15.2 Knowledge Transfer Cadence Sheet

### 15.2.1 Biweekly Rotating Release Agenda Template (30–45 Minutes)

| Time | Segment | Content and Rules |
|------|------|------------|
| 0:00–0:05 | Review of the last beat | Reconcile last time's commitments item by item, with reasons for anything unfinished |
| 0:05–0:20 | Demonstration | The receiving side's engineers demonstrate the effect on real data. Show "what it can do" and also "what a wrong one looks like and how it gets caught." A release that shows only successes does not pass |
| 0:20–0:30 | Owner Q&A | The owner asks, the presenter answers. Your team adds only when named, and never answers for them |
| 0:30–0:40 | Commitment for the next beat | The presenter, not your team, states the goal for the next two weeks |
| 0:40–0:45 | Cadence sheet update | Update the milestones against 15.2.3. Were gatekeeping rights handed over? Were lead-writer rights rotated? |

### 15.2.2 The Three Explain-It Checks (Use Before Merging)

| Question | What a Passing Answer Looks Like | Failing Signal |
|----|--------------------|------------|
| Why is it written this way? | He can state the alternatives and the reason for not picking them | "That is how it came out" / "It runs" |
| Where can it go wrong, and how would you find out? | He can point to the specific failure path and the matching log, alert or backstop | "It should not go wrong" / "The tests all passed" |
| If it has to change, where do you start? | He can state the change point and how far it reaches | A long scroll through the code hunting for the entry point |

Usage, this is the enforcement tool for clause three and a self-check tool as well. Before you merge AI-generated code yourself, put the questions to yourself first.

### 15.2.3 Cadence Sheet: Biweekly Milestones from Pilot to Handoff

Fill it in by release beat. Besides the demonstration, every beat marks one "transfer action." The progress of knowledge transfer is not read from how many training sessions were held, it is read from how many items of power and responsibility were handed over:

| Beat | Time | What Was Demonstrated | Transfer Action This Beat (Examples) |
|------|------|----------|----------------------|
| 1 | Pilot week 2 | | Gatekeeping rights of the first module handed over |
| 2 | Pilot week 4 | | The receiving side's engineer handles a production issue alone for the first time (your team watches) |
| 3 | Pilot week 6 | | Lead-writer rights of another module rotate to the receiving side |
| 4 | Pilot week 8 | | The receiving side's engineer leads the pilot technical retrospective |
| … | After launch | | Gatekeeping rights of the remaining modules handed over beat by beat; your team's share of commits declines |
| Last beat | Handoff (Chapter 22) | The receiving side's engineers demonstrate the whole system to the owner | Gatekeeping and release rights on every module sit with the receiving side, and the handoff checklist (Template 22) should have no new items |

Health self-check (three numbers every beat), the receiving side's engineers' share of commits (should rise), the number of modules where your team holds gatekeeping rights (should fall), the number of questions at the rotating release that your team answers for them (should trend to zero). If any one of the three runs the wrong way for two beats running, go back to Chapter 15's failure modes and find your match.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/cobuild/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/cobuild/): the repo structure and CI ownership checklist, the external collaborator permission config sample, and the PR template (with the three explain-it questions field)
