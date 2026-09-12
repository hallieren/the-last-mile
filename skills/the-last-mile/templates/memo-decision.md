# Decision memo (ADR memo)

Source: `docs/appendices/template-19-memo-suite.md` §19.2 (and `repo/templates/memo-suite/prompt-memo-scaffold.md`, which drafts the body and leaves the apex blank).

Use at any midpoint where an executive has to call something (a plan settled, added investment, a scope change, stay or go after a kill criteria trigger). The bar before writing, the pyramid apex test: who you want and what you want him to call, in one sentence. Cannot write it → do not open the template.

| Header field | Fill in |
|---|---|
| To | <the person who calls it, one name> REQUIRED |
| From / Date | <you>, <date, 48–72 hours (rule) before the meeting> |
| Subject | <decision name>, for you to call <N> things by <date> REQUIRED |
| Body | One page; <technical plan / reconciliation report / review packet> attached for reference |
| Copies | <your manager>, <business-side owner>, <PMO> REQUIRED |

**① SCQA opening (three lines)**

| Line | Fill in | Rule |
|---|---|---|
| S, Situation | <a fact he already knows and accepts> | New information in S and the opening loses its anchor of agreement |
| C, Complication | <the single hardest piece of evidence, one scoring run, one distortion rate> | Do not pile them up |
| Q, Question | <his question, "should we invest now, and how much"> | Not yours ("which architecture do we pick") |

**② The conclusion in one sentence** (bold): <the call>, carrying <scope>, <duration>, <validating metric> (<source of the key number, one parenthesis>) REQUIRED

**③ Three pillars, one line of evidence each**
- Pillar 1: <reason>, <number / signature / scoring result>
- Pillar 2: <reason>, <evidence>
- Pillar 3: <reason>, <evidence>

**④ The trade-off said out loud**
- Given up 1: <what>, revival condition <a checkable event>
- Given up 2: <what>, revival condition <event>; for an AI system, the decision rights ladder pasted in as it stands (decide / act / advise / sense, which layer AI stops at, on what evidence it moves up)
- What it buys: <one sentence, "a result that can be validated inside N weeks">

**⑤ Risk and backstop**: <error categories> → <threshold and tolerance per category, zero-tolerance classes listed separately> → <backstop path, at which step human review catches it, whether overrides leave a trail> → <resource reassessment conditions, citing the charter's three tiers>

**⑥ The three things I need from you** (each his action, dated to the day; internally lead with people, priority and owner, and confirm the post-launch owner by name)
1. <date / occasion>: <verb> <action>
2. <date>: <action>
3. <date>: <action, with the landing action: who writes it into which sheet by which day, copying whom>

**Rules**
- S: write only what he already knows and accepts. C: use the single hardest piece of evidence. Q: it has to be his question.
- The conclusion carries scope, duration, and the validating metric; give the source of the key number in one parenthesis, and do not unpack it.
- Pillars are MECE. Evidence is nouns, not adjectives. One line each. If it will not fit on one line, the evidence is not hard enough yet.
- Give every item given up a place (a revival condition), turning "no" into "not now." Transcribe from the scope log, do not invent it here. This section must contain at least one sentence that hurt to write. Once a hidden cost is exposed, you permanently lose the right to lead with the conclusion.
- Promise no "it will not make mistakes," say "when it is wrong, it can be found and it can be caught." Every sentence needs a subject and a mechanism, with no "we will try" and no "in principle."
- Three at most. Each one is his action, not your plan. Dates down to the day. Without this section the memo is a report, not a request.

**SCQA self-check, run before sending** (any "no" → fix, do not send): one sentence for what he must call; S carries no new information; C is one hardest fact and Q rises on its own; Q is his; conclusion on the first screen; the pillars cover why believe it / what it costs / what happens when it goes wrong, none overlapping; every evidence a verifiable noun, no "significant," "solid," "basically"; the trade-off has the sentence that hurt, every item given up has a revival condition; the ladder is drawn in, errors are categories and thresholds, not one accuracy number; the backstop names people and steps, the reassessment cites the three tiers; all three asks dated and his; body inside one page.

**The four-minute test** (rule): give the page to someone who does not know the project for four minutes, then ask "what is the decision, what is the cost, what happens when it goes wrong." Any question he cannot answer → rewrite that section.

**What a wrong filling looks like**
- Starts from "project background," conclusion on the last page: the order of the work, not the order of the reader.
- Upside throughout, cost left waiting to be asked about: one exposure takes credibility to zero.
- Logic perfect, reader nods, nothing happens: no "three things I need from you" with dates; the nod is for you, not the project.
- "It is all important, none of it can go," ten pages: the apex has not been found; all detail goes to the attachments.

Filled in → goes to: the 10-minute meeting, silent reading first; within 24 hours (rule) the approval outcome is written back into the project record and becomes the S of the next memo (`templates/memo-impact.md` at the close, or the kickoff of the next phase).
