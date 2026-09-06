# Template 5 · Stakeholder Map

> Companion chapter(s): Chapter 5. One map plus one self-check. Draw it in week 1 of the project, then update it every two weeks.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 5.1 The Six-Role Map (Main Table)

| Role | Real Name | What They Fear | What They Win | Trust Balance (- / 0 / +) | Contact Plan (see 5.3) |
|------|------|----------|----------|------------------------|---------------------|
| Decision-maker | | | | | |
| Actual user | | | | | |
| Data owner | | | | | |
| Risk owner | | | | | |
| Maintainer | | | | | |
| Blocker | | | | | |

**Rules**

- **Real names.** A cell with a department name counts as blank. Departments do not fear and do not win. Only people do.
- **One person can fill several cells.** Mark anyone in several cells with an asterisk (a high-leverage node, cultivate first).
- **Blank = project risk.** Blank maintainer → cause of death at handoff. Blank blocker → not that he does not exist, but that you have not found him yet.
- **The opening trust balance is not zero, it is inherited.** Working relationships, the reputation the last system left in this department, the standing impression of "system builders" as a type, all of it enters the books before you do. The inherited value is occasionally positive, usually negative. Fill in this column's starting point first, then add your own deposits on top.
- Two mandatory questions once the map is drawn. **Which name has never been in the meeting room? Which cell's content did you guess?** The first is a blind spot, the second goes for verification. A wrong guess at "What They Fear" is more dangerous than a blank.
- AI project reminder (the double trust deficit, see Chapter 5). If the actual user's "What They Fear" does not mention "being replaced" or "taking the blame for AI," most likely you did not ask. Not that he is unafraid.

---

## 5.2 Identifying Questions per Role and the "Fear / Win" Prompt Library

The "common fears / wins" below are a prompt library, not answers. Every entry must be replaced by field evidence.

### Decision-maker

- **Test.** Who can decide this project's next phase of resources, or kill it, in one sentence? And whom does he answer to?
- **Common fears.** The project becomes his failure; he cannot give the board or his superiors a number; he gets cornered by the "all the competitors are doing it" narrative.
- **Common wins.** A number and a story he can tell; the "mastered AI" label.
- **Contact notes.** A one-page memo on a fixed cadence (pyramid structure, Chapter 13); bring only judgments and decision requests, no process detail.

### Actual user

- **Test.** Whose daily actions change after launch? Who gets interrupted by the system's suggestions every day?
- **Common fears.** Being replaced; taking the blame for AI's mistakes; experience ignored; being monitored.
- **Common wins.** Less repetitive work; his judgment written into the system with his name on it; standing in the department.
- **Contact notes.** Go to the desk, not the meeting room; use his jargon; a fixed time slot written into the charter (say "2 hours a week"); say the fear of replacement out loud, to his face (Chapter 5).

### Data owner

- **Test.** Who owns the data you need **on the business side**? (Not who holds the database key)
- **Common fears.** Definition problems landing on him after the data is misused; poor data quality exposed.
- **Common wins.** Someone fixes a data definition for him; his own reporting gets easier.
- **Contact notes.** Solve one of his own data pains first, then talk about access; when the request stalls, let him speak in his own language of power.

### Risk owner

- **Test.** When something goes wrong, whose name is on the accountability email? Who signs the security / compliance / legal review?
- **Common fears.** Being bypassed, last to know; taking the fall; an unauditable black box.
- **Common wins.** A project that writes risk on page one; a case of prudence he can show upward.
- **Contact notes.** Invite him into the project team in week 2, do not send it for review passively in week 10; hand-deliver the pre-mortem memo (Template 4).

### Maintainer

- **Test.** A year after launch, whose annual goals list this system?
- **Common fears.** Inheriting a black box; an undocumented mess that becomes his later.
- **Common wins.** New skills; ownership of the code; a co-build credit.
- **Contact notes.** Co-build from the first line of code (Chapter 15), not a handoff document in the final week.

### Blocker

- **Test.** Without whose nod does everything stop, even though he never attends? (PMO, finance, information security, a peer digital counterpart, the architecture committee)
- **Common fears.** Every blocker is different, but behind the blocking there is always something he is protecting. Find it.
- **Common wins.** Once what he protects is written explicitly into the plan and protected, he loses his reason to block you (resistance is a diagnostic signal, Chapter 20).
- **Contact notes.** One on one, early, in person; never ambush a blocker in a big meeting.

---

## 5.3 Contact Plan

| Person | Frequency | Format | What to Bring Next Time (**what he wants, not what you want**) | Last Contact Date |
|----|------|------|------------------------------------------|--------------|
| | | | | |

**Rules**

- Bring something useful to **him** every time. A one-page risk list, a fixed spreadsheet, a data point he cares about. Contact empty-handed spends trust, it does not save it.
- A key cell with no contact for two weeks → mark it red.
- Contact ≠ meeting. A hallway, a desk, a three-line email all count.

---

## 5.4 Trust Equation Self-Check

Source. The Trust Equation is paraphrased from Maister / Green / Galford, *The Trusted Advisor*: trust = (credibility × reliability × intimacy) / self-orientation. Run it on yourself every two weeks. Any question you cannot answer with a concrete example is the next behavior you should deliberately create.

**Credibility**
- [ ] In the past two weeks, I said to someone's face "I do not know, I will have an answer by X," and delivered on time.
- [ ] Most of my last three judgments carried evidence from this business unit's floor (numbers, cases, users' own words).
- [ ] The business side quoted me in a meeting I was not in.

**Reliability**
- [ ] Of my last five "you will have it Friday" commitments, at least four landed on time.
- [ ] Meeting action items go out in writing within 24 hours.
- [ ] At least once, I shrank a commitment I could not keep, early and unprompted, instead of explaining on the deadline.

**Intimacy**
- [ ] Someone has told me something at the level of "I am only telling you this."
- [ ] I have said the tension in the room out loud, to people's faces, at least once.
- [ ] The front line uses their own jargon with me, not the official vocabulary.

**Self-orientation (lower is better, a check on any of these four is bad news)**
- [ ] "Our system / our plan" shows up in my speech more than "your claims / your metrics."
- [ ] When the business side suggests shrinking the project scope, my first reaction is defense.
- [ ] I have never advised the business side "let's not do this yet."
- [ ] What my reporting says is "the system we built," not "the Claims queue."

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/stakeholder-map/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/stakeholder-map/): the table scaffold for this template and the periodic update reminder script
