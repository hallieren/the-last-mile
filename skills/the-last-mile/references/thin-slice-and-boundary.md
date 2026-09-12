# Cutting the thin slice and drawing the decision rights boundary

**Load this reference when:** everyone wants their thing added the day after the charter is signed, an engineer proposes "make it a platform", or someone wants the system to act automatically or move a decision up a layer ("let it just send this one automatically"). For refusing full automation to a sponsor, see `references/saying-not-now.md`.

Source: chapter 8 (`docs/chapters/ch08-thin-slice.md`); template 8 §8.1, 8.2, 8.4 (`docs/appendices/template-08-thin-slice.md`); `repo/templates/thin-slice/thin-slice.md`.

## Contents

Decisions (why creep is structural; the decision rights boundary; the thin slice and the Five Ones; answering each proposal type; if the proposer insists; the boundary map; where red lines live) · Procedures · Detectors · Key judgments · Templates · Vendor seat

## Decisions

### Why creep is structural

- Treat creep as gravity, not as a discipline failure on either side. Three engines drive it, none about character. Your project is the only car moving, so it becomes the mounting point for every AI wish in the company. The marginal cost of every proposal looks small ("one more class of claim", "just leave a hook"), while validation cost multiplies: one more user group is another set of scoring and annotation, one more decision layer is another round of error classification and oversight design. The cost of refusal is asymmetric: accept and the project pays in three months, refuse and you pay personally on the spot.
- A charter cannot stop these proposals. It is a snapshot of consensus on signing day; creep is new traffic every day. What you need is a ruling procedure that runs continuously, not a thicker document.
- "Many extension proposals want an answer the proposer can repeat to someone else. A 'yes' is secondary." See that, and refusing turns from confrontation into service.

### The decision rights boundary

- Draw it when scope is defined, never "along the way" at the architecture stage. It is the layer on the workflow's decision chain where AI output stops, the layer where humans take over, and the evidence required to move up each layer. Error classification, oversight design and the chain of responsibility all grow out of this line. Draw a feature boundary wrong and you cut one module; draw this line wrong and you redraw the whole validation set, and the code is the least of it.

```
Decide   <the workflow's final decision, e.g. pay or not, how much>     <- red line: never touched
Act      <actions with external effect, e.g. send, assign, change status> <- humans take over here (name who)
Advise   <priority, next step, each with a reason>                       <- AI stops here (this phase)
Sense    <gather, extract, reconcile, flag signals>                       <- AI does this
```

- Evidence to move a layer up takes two forms, both written as measurable facts, never as "once results stabilize". One, a human acceptance record (which suggestions get accepted as is, which get overridden often; e.g. the acceptance rate for one class of suggestion ≥ threshold for N consecutive weeks). Two, a deterministic verification loop on that layer's output (errors automatically detectable, enumerable, reversible, with proof of verification coverage). Output verifiable → moving up need not wait for an acceptance rate to build. Output not verifiable → however high the acceptance rate, go slow.

### The thin slice and the Five Ones

- A thin slice is the smallest working slice that cuts vertically through all five layers, real user, real decision, real data, real risk control, measurable outcome. Thin is the width: one decision for one user group. Not thin is the depth: every layer goes all the way to real. Creep proposals are horizontal; the slice is vertical. What it buys is being able to afford validation; doing less is a by-product, and clean evidence only comes out of "one".

| The Five Ones | What to write | Why it must be one |
|---|---|---|
| One user group | The team and the names, not a department | Two groups = two sets of scoring, two sets of tacit knowledge, no way to say whose feedback counts |
| One decision | A decision point the user already makes, not a newly invented action | More than one and errors cannot be defined, so the eval has nowhere to start |
| One data path | One verifiable path from source to interface, every source on it listed | Every extra path doubles the fitness check and the reconciliation |
| One risk boundary | The decision rights boundary (which layer AI stops at) + the red lines (what it never touches) | More than one and oversight and the chain of responsibility have seams, and incidents find seams |
| One measurable outcome | The charter North Star cited directly, no separate metric | More than one and improvement cannot be attributed, and acceptance falls back to "leadership thinks so" |

- Lock the five into one sentence: "This user group, making this decision, along this data path, inside this risk boundary, improves this metric." Wherever it does not read smoothly is where the cut is not clean. The slice is the North Star's engineering projection, not another negotiation.
- Any cell holds "and", "as well as", "etc.", "two kinds" → that cell is already creeping. Negotiate the narrowing first, then fill the sheet. Every plural owes you one narrowing negotiation; the items you cannot write and the items forced into the plural are your scope risk list.
- The data path is still a paper promise at this point ("the merged view after reconciliation"). It only has to be one, not three; delivery comes with the fitness check.
- Every milestone (prototype → pilot → launch) → reread the sheet and ask whether any of the Five Ones has quietly become plural.

### Answering each proposal type

| Proposal | Ruling | Action |
|---|---|---|
| Horizontal (one more user group, one more class of data) | Price it, then give it a place | A three-line tally of what doubles (user group, annotation system, metric baseline), the schedule cost and the evidence dilution ("the pilot slips at least six weeks" (illustrative)). Write the log row in front of the proposer, reading it aloud. Revival condition exclusive: "the **first** extension after the pilot North Star hits target", with reconciliation starting a month early and no requeue for project approval. "First in line" is a sentence he can take back |
| Vertical (full automation) | Draw the ladder, do not debate | Four layers on the whiteboard, red line at the top, what AI already does at the bottom. Each layer up needs its own evidence; capability is secondary. Revival condition: "once the advise layer's acceptance data hits target, move up one layer at a time, each layer decided on its own". Let the AI's suggestions earn a record of being accepted before you talk about letting it act |
| Platform (general-purpose bottom layer) | Do not evaluate the design; ask the five-gap counter-question | "Which gap does the platform narrow?" Walk data, workflow, trust, ownership, value one by one. A platform reconciles no scenario's data (not narrower), is embedded in no workflow (wider), earns trust in no specific team, has no owner (wider), converts into no North Star number. Catch the enthusiasm: "a good abstraction grows out of the second case; it is not guessed from the first". Whoever writes the extraction pipeline keeps the interfaces clean, the first brick. Revival condition, always: "after the second slice lands, distill what is common" |
| Lateral (a peer department, "do one for us while you are at it") | Price plus place, plus the cc | Same three-line tally, face to face. Log it with his name as proposer and an event as revival condition. Send the row, cost and all, to the sponsor. The cc is not tattling; it sends a lateral request into the vertical ranking. You have no ruling power, but you have the power to put things into the ruling procedure |

- You hear the stirring in the corridor before the proposal is formal → walk through the tally that same day. By the time they ask, the conversation is no longer whether but when.

### If the proposer insists

- The proposer reads the row and still says "put it in first" → run the procedure one more round. Do not recompute the cost; the tally is done and computing it again is fighting to win. Write both roads on one page: the slice as before, with the exclusive revival condition; and the road he wants, with the same tally next to it.
- Internally there is no owner's signature next to the cost, so a decision trail replaces it, two moves. Both roads and their costs go into that week's project report, cc the sponsor, quoted verbatim, no comment, no recommendation. The second road is taken → the delay attribution column on the project board reads "scope change, <X> added this phase", and the attribution travels with the schedule.
- Be honest about what the trail buys. "It clears you of surprise, not of responsibility." Its main function is making the cost visible at the moment of choosing, and most of the time nobody chooses the second road.

### The boundary map

- Three entries per layer: owner this phase (AI / human, name the human), evidence needed to move up, move-up approver.
- Moving up is a milestone decision, not routine tuning. "Let it just send this one automatically" is where the boundary starts to fall.
- Every move up reruns the three oversight questions: does the overseer have time to look, the ability to judge, the authority to stop it.
- The map appears in at least three places: the scope decision log's attachment, the security review packet, the memo to decision makers. Count how many documents the line appears in; a boundary that exists only in your head does not exist.

### Where red lines live

- A red line that lives only in speech evaporates when people change and is remembered for the first time the moment it is stepped on. The charter is the minimum; nobody opens it day to day. Put the red line where it might get stepped on: the scope decision log (opened at every scope discussion), the security review packet, and the system interface itself, e.g. a "suggested payout amount" column that must not exist, so "no column" is the red line in physical form.
- Borrow the company's existing institutions wherever you can. "No automated outbound messages" goes under the compliance policy on external contact; "no payout decisions" goes into the security review's conclusions. A borrowed red line has its own inspectors and penalties and does not need you in the room. The person who transfers in six months may be you.

## Procedures

**Cut the first slice.**
1. Take the charter North Star as the fifth One, unchanged.
2. Name the user group down to the team and names, and the one decision they already make.
3. List every source on the single data path; send the path to the fitness check.
4. Draw the four-layer boundary and name the red lines; put both in the risk boundary cell.
5. Write the lock sentence. Any plural, any "and" → negotiate the narrowing before filling the sheet.
6. Run the no-slice self-check (below). Any ✗ → you cut too far.
7. Turn the charter's "not this phase" list into the first batch of scope log rows, adding a cost and a revival event to each.

**Draw the boundary map.**
1. For each layer write the owner this phase; a human owner is a name.
2. Write the evidence to move up as a measurable fact, one of the two forms.
3. Name the move-up approver; a move up is decided at a milestone.
4. Attach the map to the scope log, the security review packet and the decision memo.

**No-slice self-check, after every narrowing.** Any item ✗ means the thin slice has become a no slice.
1. At least one real user in the one user group, after hearing the slice described, says "this solves my problem". Verify with their own words; do not answer for them.
2. The slice runs end to end, data → sense → advise → human decision → outcome measurement, with no gap where "this stretch is handled by hand for now".
3. The North Star's improvement is still attributable to this slice; if what is left cannot move the metric, the metric is an empty promise.
4. The change users make to use it is smaller than the effort it saves them.

## Detectors

- If the first scenario is still in pilot and the architecture already shows a "rules engine" or a "scenario configuration center", you are abstracting from imagination; the legitimate raw material for abstraction is repetition.
- If your red line was agreed verbally and the person who agreed it has transferred, a new product manager will propose the forbidden feature with enthusiasm at the next requirements meeting.
- If you read the slice to your one user group and do not hear "this solves my problem", what you hold is a no slice, cut to what is easy to engineer, not to what is complete in value. A slice that avoids every risk also avoids the risk of success.
- If a Five Ones cell contains "and", "etc." or "two kinds", that cell is already creeping.
- If you cannot count the documents the boundary line appears in, it exists only in your head.
- If "one more cut" has started to feel prudent by reflex, narrowing has decayed from judgment into reflex; refusing takes less effort than thinking.
- If an engineer is down half a week and the weekly report shows nothing, favors over half a day (rule) are bypassing the log.

## Key judgments

- "Scope creep is the default outcome of organizational dynamics, not a management failure."
- "Turn 'no' into 'not now.' Revival conditions are the lubricant of refusal."
- "An AI system has one more boundary, the decision rights boundary. Draw that line wrong and you redo the whole validation system, not just the code."
- "Let the AI's suggestions earn a record of being accepted before you talk about letting it act."

## Templates

- `templates/five-ones-and-boundary.md`: the Five Ones definition sheet, the lock sentence, the boundary map, the no-slice self-check.
- `templates/scope-decision-log.md`: the row format and rules for every refused extension; the four-stage frame is in `references/saying-not-now.md`.
- `templates/data-fitness-and-source-of-truth.md`: where the one data path goes to be checked.

## Vendor seat

A vendor prices every extension through a change order against the statement of work and has the client owner sign next to the cost, so the responsibility changes shoulders with the signature; internally the signature is replaced by the decision trail (the report cc'd verbatim, the delay attribution column). A line in a contract is not a working mechanism.
