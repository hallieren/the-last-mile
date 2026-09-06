# Template 19 · Three-Memo Set (with ADR)

> Companion chapter(s): Chapters 13 and 19. The four tools are in project order. Fill the kickoff template (19.1) before a phase starts, the decision memo, which is the ADR memo (19.2), at any midpoint where an executive has to call something, and the impact template (19.3) before a phase closes. Run the shared rules list (19.4) before every send.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 19.1 Kickoff Memo Template (Before a Phase Starts)

> Kickoff memo. The one page sent to the sponsor before a phase starts, putting on record the outcome promised, the investment needed, and the ways to die already rehearsed. It usually asks for no call (the authorization already came from the previous impact memo or from project approval). It translates that authorization into commitments that can be checked.

```
To: [sponsor]      From: [you]      Date: [Monday of the week the phase starts]
Subject: [phase name] starts, for the record. Promises, investment, and ways to die
One page of body text; the full pre-mortem and the plan attachments are there for reference.
```

- Three fixed copies, your manager, the business-side owner, and the PMO (Chapter 19)

| Section | What Goes In It | Rules |
|----|--------|------|
| ① SCQA | S = the previous impact memo's approval outcome / C = the new variable in this phase / Q = what is promised, what is needed, how it will die | For C, write "where this phase differs from the last one." If there is no new variable, no new phase is needed |
| ② The outcome promised | The North Star target to move toward + one early visible win, each with a date | Keep the charter's metric, do not set a new one; give the early win a date on the order of "inside the first month" |
| ③ Investment needed, who sends the people | People and time from other departments, named to the person, with hours per week spelled out | Cite a precedent where one exists ("on the precedent of team X"); investment left out of this section will never be recognized later |
| ③ Investment needed, who gives the word | Whose mouth this commitment has to come out of before it counts, the sponsor himself or the other side's manager | Every item landing in "who gives the word" is a political act. Work out whose standing you are spending before you write it |
| ④ Pre-mortem summary | The three most likely ways to die + the defense for each | Take the top three from Template 4's output; this is the memo's expectation management slot |
| ⑤ What I need from you | Can be as small as "hold ten minutes on your calendar" | It has to be there, even if it is only "one look at the run chart in week N" |

**Anchor & Helm worked example** (the week 19 expansion kickoff, full text in Chapter 19):

- ② Promise: the North Star reaches the charter's -30% target line (eight weeks); one business win worth announcing inside the first month.
- ③ Investment, who sends the people: Kevin Doyle, schedule protection for the two new teams, 2 hours a week each on the precedent of Linda's team; the two chase-side people continue to the end of the expansion period (already confirmed at the annual budget and headcount review, recorded here).
- ③ Investment, who gives the word: the first two sit inside Kevin's own line and his word is enough; the two on the chase side do not, so Grant Whitmore says a line to the chase side's manager at the next monthly meeting about continuing them.
- ④ One way to die, as an example: the new teams accept everything as is, with none of Linda's kind of challenge → the defense, an override rate clearly below Linda's team's baseline in the first month triggers a spot check.
- ⑤ The ask: no call needed; ten minutes at each monthly meeting, one look at the run chart in week 22 and one in week 26.

## 19.2 Decision Memo / ADR Memo (the Midpoint)

The decision memo is Chapter 13's ADR memo, the midpoint piece of the three-memo system (kickoff at the open / decision at the midpoint / impact at the close). Three tools work together. Fill the template (19.2.1) once at every point where an executive has to call something. Run the self-check list (19.2.2) before sending. Use the anti-pattern table (19.2.3) to diagnose when a memo comes back or gets read with nothing following.

**When to use it**. Any midpoint where an executive has to call something (a plan settled, added investment, a scope change, stay or go after kill criteria trigger). The test is the pyramid apex test. If you can say "who I want and what I want him to call" in one sentence, it is a decision moment.

**How it joins the other two**. When reality tests a kickoff's pre-mortem defense and the decision has to change, go to a decision memo. What a decision memo gets approved enters the evidence section of the next impact memo. Once an impact memo's option is called and a new decision point comes up during execution, you come back to a decision memo again. The split in one line. **The kickoff puts commitments on record, the decision memo asks for a call, the impact memo delivers the evidence.**

### 19.2.1 ADR Memo Template (One Page of Body Text)

> ADR memo. One page presenting one pending decision to the person with the authority to call it (conclusion, evidence, the cost said out loud, risk and backstop, and what he has to do). Its purpose is not to make him understand the plan. It is to let him call it responsibly.

**The bar before you start writing (the pyramid apex test)**. Who you want and what you want him to call, in one sentence. If you cannot write that sentence, do not open the template.

```
To: [the person who calls it, one name]        From: [you]        Date: [ ]
Subject: [decision name], for you to call [N] things by [date]
One page of body text; [the technical plan / the reconciliation report / the review packet, and so on] are attached for reference.
```

- Three fixed copies, your manager, the business-side owner, and the PMO (Chapter 19)

#### ① SCQA Opening (Three Lines)

| Line | What Goes In It | Rules |
|----|--------|------|
| S (Situation) | A fact both sides already agree on | Write only what he already knows and accepts. New information in S and the opening loses its anchor of agreement |
| C (Complication) | The change or risk that threatens that agreement | Use the single hardest piece of evidence (one scoring run, one distortion rate), do not pile them up |
| Q (Question) | The question that rises in the reader's mind as a result | It has to be **his** question ("should we invest now, and how much"), not yours ("which architecture do we pick") |

#### ② The Conclusion in One Sentence

The call to be made, one sentence, in bold. It carries scope, duration, and the validating metric. Give the source of the key number in one parenthesis (cite the charter or the reconciliation report), and do not unpack it.

#### ③ Three Pillars (One Line of Evidence Each)

- Pillar 1: [reason], [number / signature / scoring result]
- Pillar 2: [reason], [evidence]
- Pillar 3: [reason], [evidence]

Rules. MECE, three that do not overlap and together are enough to hold up the conclusion. Evidence is nouns ("200 records reconciled, 44% distorted," "co-signed by the security reviewer"), not adjectives ("a solid data foundation"). One line each. If it will not fit on one line, the evidence is not hard enough yet, or you are stuffing the reasoning process into a pillar.

#### ④ The Trade-off Said Out Loud (the Soul of the Memo)

- Given up 1: [what], revival condition: [a checkable event]
- Given up 2: [what], [required for an AI system, the decision rights boundary map, which layer AI stops at and on what evidence it moves up (paste in Template 8.2's four-layer ladder as it stands)]
- What it buys: [one sentence, usually "a result that can be validated inside N weeks"]

Rules. Give every item given up a **place** (a revival condition), turning "no" into "not now" (Chapter 8). Transcribe the material straight from the scope decision log (Template 8.3), do not invent it here. Self-check. This section must contain at least one sentence that hurt to write. Not one, and you are selling, not reporting. **Rule. Once a hidden cost is exposed, you permanently lose the right to lead with the conclusion.**

#### ⑤ Risk and Backstop

Write four things. What errors will occur (**error categories**, not a vague "there may be some error") → the threshold and tolerance for each category (zero-tolerance classes listed separately) → the backstop path (at which step human review catches it, and whether overrides leave a trail) → the resource reassessment conditions (what signal triggers a resource reassessment, citing the three tiers of resource reassessment, Chapter 4).

Rules. Put it the way a non-technical decision maker hears it. Promise no "it will not make mistakes," and say instead "when it is wrong, it can be found and it can be caught." Panic does not come from "it will make mistakes," it comes from "nobody handles it when it goes wrong." This section is a commitment, not an apology. Every sentence needs a subject and a mechanism, with no "we will try" and no "in principle."

#### ⑥ The Three Things I Need From You (Each With a Date)

1. [date / occasion]: [action, starting with a verb]
2. [date]: [action]
3. [date]: [action]

Rules. Three at most. Each one is **his** action (call it, approve it, confirm it), not your plan. Dates down to the day. Without this section the memo is a report, not a request.

- **Anchor & Helm example** (the ADR memo in Chapter 13): 1. Call the pilot's scope and start at next Monday's weekly; 2. By next Wednesday, approve the development effort for the merged view, two people from the Digital Center and two from claims-ops IT, six weeks; 3. By next Friday, confirm with Kevin Doyle that Linda's team's 2 hours a week keeps running through the pilot, with the business-side owner confirmed down to a name, and the landing action and the person accountable written out.

### 19.2.2 SCQA Writing Self-Check List (Run It Before Sending)

Ask yourself item by item. Any "no" and you go back and fix it, you do not send:

- [ ] **The pyramid apex test**. Can you say in one sentence what you want him to call? (If you cannot → you have not thought it through, and AI cannot think it through for you)
- [ ] Is S a fact he already accepts? Does it smuggle in new information that needs arguing?
- [ ] Does C use the single hardest piece of evidence? Will Q rise in him on its own after reading it?
- [ ] Is Q his question, or your question with the subject swapped?
- [ ] Is the conclusion on the first screen? Delete the rest of the body, keep only SCQA plus the conclusion, and does he know what you want?
- [ ] Do the three pillars cover his three "can I answer for it" questions (why believe it / what does it cost / what happens when it goes wrong)? Are any two of them overlapping?
- [ ] Is every piece of evidence a verifiable noun? Do "significant," "solid," or "basically" appear?
- [ ] Does the trade-off section have the sentence that hurt to write? Does every item given up have a revival condition?
- [ ] AI system item. Is the decision rights boundary drawn in? Are errors put as categories and thresholds, or as one vague accuracy number?
- [ ] Does the backstop path have specific people and steps? Do the resource reassessment conditions cite the three tiers of resource reassessment (Chapter 4)?
- [ ] Do all three things carry dates? Are they all his actions?
- [ ] Is the body inside one page? (attachments unlimited)
- [ ] The four-minute test. Give it to someone who does not know the project for 4 minutes. Can he repeat back "what is the decision, what is the cost, what happens when it goes wrong"?

### 19.2.3 Anti-pattern Table

| Anti-pattern | Symptom | Root Cause | Fix |
|--------|------|------|------|
| **Chain-of-reasoning narrative** | It starts from "project background" and the conclusion sits on the last page | It copies the order of the work, not the order of the reader | Once it is written, move the last paragraph to the front; at every paragraph ask "what will he ask when he gets here" |
| **Benefits only** | Upside throughout, with the cost left waiting to be asked about | Treating the memo as sales copy; fear that bad news scares the decision away | Make the trade-off section mandatory; remember that one exposure takes credibility to zero |
| **Asking for understanding, not a decision** | The logic is perfect, the reader nods, and then nothing happens | Treating "explained it clearly" as the finish line of delivery; a vague request dodges the risk of refusal | Add "the three things I need from you + dates"; the nod is for you, not for the project |
| **A body over one page** | "It is all important, none of it can go," and the body runs ten pages | The cost of the trade-off is passed to the reader; the apex has not been found yet | Treat going over as a diagnostic signal. Back to the pyramid apex test, think it through and then write; all detail goes into the attachments |

## 19.3 Impact Memo Template (Before a Phase Closes)

> Impact memo. The one page sent to the person who calls it when a phase closes, presenting the result with running evidence, presenting the gap honestly, and giving next-step options with one of them recommended. Its purpose is not to sum up the past. It is to trade the past for the next step.

```
To: [the person who calls it]      From: [you]      Date: [48 hours before the retrospective or the annual budget and headcount review]
Subject: [phase name] retrospective, for you to call the next step at [occasion]
One page of body text; the full run chart, the incident retrospective record, and the metric tree detail are attached.
```

- Three fixed copies, your manager, the business-side owner, and the PMO (Chapter 19)

| Section | What Goes In It | Rules |
|----|--------|------|
| ① SCQA | S = the phase and scope in one sentence / C = the hardest result number (including a missed target) / Q = was it worth it, what next | Write the number straight into C, target hit or missed. A gap you hide ends up found for you by the reader |
| ② The conclusion in one sentence | Whether the validation holds + which option is recommended | In bold; carries scope and duration |
| ③ Evidence | The run chart cited + the mechanism explained + the defense's field record | See "run chart citation rules" below |
| ④ The honest gap | Target number against actual number; attributed to verifiable events; levers started but not run through; a void condition of its own | See "the three parts of an honest gap" below |
| ⑤ Next-step options | 2–4 of them, each with content / investment / when to choose it | See "option rules" below |
| ⑥ What I need from you | Call one of the options, with a date and an occasion | Mark the recommendation as "we recommend N" |

**Run chart citation rules**. Every point goes on the chart, the baseline median as one reference line, and the name of the special cause rule used is stated (such as "six points on one side"). No cropped stretches, and no trend drawn between two points. Write the defense record whether it looks good or bad. Incident count, what was caught, which layer the retrospective attributed it to, flow-back into the golden cases, and the kill criteria check result. **Zero triggers still gets written as "zero triggers,"** because it is the evidence that the clause for stopping has teeth.

**The three parts of an honest gap**. ① Number against number ("-22% against -30%, 8 percentage points short," never "close to target"). ② Attributed to verifiable events (when the people arrived, when the fix took effect), never to "we need more time." ③ Carrying its own void condition ("if the metric stops improving inside X weeks, this judgment is void and we go back to option N"). If you cannot write ③, then ① and ② are a justification, not an attribution.

**Option rules**. Options other than the recommendation have to be real options, each stating "when to choose it." Two standing options. **Revival list items** are stated by their revival condition (is the condition ripe, how far short), not by mood. **Hold and watch** always sits last. It is the exit for "the evidence says not yet" (the closeout form of Chapter 7's re-evaluation condition). State the ceiling on the watching period and its cost, and when it comes due with no new evidence, "another month of watching" has to go through project approval again (Chapter 14).

**Anchor & Helm worked example** (the week 18 pilot retrospective, full text in Chapter 19):

- ① C: the North Star finished at -22%, short of the charter's -30%.
- ③ One piece of evidence, as an example: all eight weekly points below the eight-week baseline median, and "six points on one side" holds. A shift, not fluctuation.
- ④ The gap: the chase-side people covered only half the stretch and the list's weak-signal prompt went live only in week 15, so neither lever has run a full cycle; void condition = if it stops falling four weeks into the expansion, we go back to option three.
- ⑤ Options: expand and go deeper (recommended) / start home property (revival condition = "the first extension after the pilot North Star hits target" · exclusive; the -30% target line against -22% today, condition not ripe) / hold and watch (four more weeks, cost = stopping the scale-up just as the levers start working).

## 19.4 The Shared Rules List for All Three (Run It Before Sending)

- [ ] One page of body text, attachments unlimited (over a page = not thought through)
- [ ] Lead with the conclusion, a three-line SCQA opening (self-check with 19.2.2)
- [ ] The ending carries "what I need from you," a concrete action with a date. A kickoff's ask can be as small as "hold ten minutes," but it has to be there
- [ ] The expectation management slot is in place. The kickoff has the pre-mortem summary / the decision memo has the decision rights ladder / the impact memo has the honest gap
- [ ] Numbers match the charter and the run chart, with no orphan numbers (every number traces back to an attachment)
- [ ] The "I will tell you the moment X shows up" promised in the last memo, has it been honored? (the message that honors it = one line plus one chart, carrying no request)
- [ ] Is the copy line complete (your manager / the business-side owner / the PMO)? If the investment needed means going over a peer department to ask for people, does that need cross-department administrative coordination, and is it marked?

**Send timing table**:

| Memo | When to Send | Meeting Shape |
|------|----------|----------|
| kickoff | Monday of the week the phase starts; inside one week of the approval meeting | Usually no meeting needed. For the record plus one calendar request |
| decision | Delivered 48–72 hours before the meeting where it gets called | A 10-minute meeting. Silent reading first, then the pillars |
| impact | Delivered 48 hours before the retrospective or the annual budget and headcount review | The meeting works the options around the document, and the approval comes as it breaks up |

The shared rule on timing. **Document before meeting.** The executive reads the one page before the meeting, and only then is the meeting the place where it gets called rather than the place where it gets reported for the first time. Within 24 hours of the meeting, write the approval outcome back into the project record (that is the S of the next memo).

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/memo-suite/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/memo-suite/): outline scaffolding for the three memos (ADR memo included), with sample prompts that take phase data (charter metrics, run chart, pre-mortem items) and generate draft SCQA and evidence sections; the conclusion sentence is forced to stay empty, because only a person places the apex
- [`templates/memo-suite/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/memo-suite/): the run chart plotting script plus the generator for the one-line "point N" short notice (it takes the metric tree data source of Template 18)
- [`templates/memo-suite/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/memo-suite/): a send timing reminder sample, generating the three memos' deadline reminders from the phase calendar (worked back from 48 hours before the meeting)
