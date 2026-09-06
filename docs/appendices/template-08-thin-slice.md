# Template 8 · Thin Slice Definition Sheet and Scope Decision Log

> Companion chapter(s): Chapter 8. The four tools work together. Fill in the definition sheet once at project approval and recheck it at every milestone. Draw the boundary map at the same time as the definition sheet. Keep the scope decision log continuously from project approval on. Run the no slice self-check after every narrowing.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 8.1 Thin Slice Definition Sheet (the Five Ones)

> Thin slice: the smallest working slice that cuts vertically through all five layers, "real user, real decision, real data, real risk control, measurable outcome." Thin is the width. The depth must go all the way down.

**Blank template**:

| The Five Ones | What to write | Self-check question |
|--------|----------|----------|
| **One user group** | Specific to the team and the names, not a department | Who in this group will say "this solves my problem"? Cannot name them → back to Chapter 5 to find the actual user |
| **One decision** | One decision point the user **already** makes, not a newly invented action | If the system's suggestion is wrong, can the user see it on the spot and override it? |
| **One data path** | One verifiable path from data source to user interface, listing every source it passes through | Has the fitness of every source on the path been checked (Template 9)? Has "after reconciliation" actually been delivered? |
| **One risk boundary** | The decision rights boundary (which layer AI stops at) + the red lines (what it never touches) | Besides the documents, do the red lines also appear in the review materials and the product interface? |
| **One measurable outcome** | Cite the charter North Star directly (Template 4), no separate metric | When this number gets worse, does anyone hurt? |

**Anchor & Helm example** (the slice from Chapter 8):

| The Five Ones | Anchor & Helm's entry |
|--------|----------|
| One user group | Linda Marsh's auto claims review team (not "the claims department") |
| One decision | The reviewer's next step on each exception claim, which documents are missing and whom to chase first (an existing decision point, the suggestion can be overridden on the spot) |
| One data path | Core system status fields + the review team's Excel + the survey-review mailbox → merged read-only view → the queue (fitness of each source, see the Template 9 example rows) |
| One risk boundary | AI stops at the advise layer (8.2); red lines, no payout decisions, no automated outbound messages |
| One measurable outcome | First-touch handling time for auto exceptions (charter North Star, Template 4 element 1) |

**Rules**:

- Any cell containing "and / as well as / etc. / two kinds" → that cell is already creeping. Negotiate the narrowing first, then fill in the sheet.
- The five cells must lock together into one readable sentence: **"This user group, making this decision, along this data path, inside this risk boundary, improves this metric."** Wherever it does not read smoothly is where the cut is not clean.
- The definition sheet is not a one-time document. Recheck it at every milestone (prototype → pilot → launch). Have any of the Five Ones quietly become plural?

---

## 8.2 Decision Rights Boundary Map

The four-layer skeleton (bottom up). Rewrite each layer's content for your workflow:

```
Decide   [this workflow's final decision, e.g. pay or not, how much]              <- red line: never touched
Act      [actions with external effect, e.g. send chase notices, change status]   <- humans take over here (name who)
Advise   [priority, next step, each with a reason]                                <- AI stops here (this phase)
Sense    [gather, extract, reconcile, flag signals]                               <- AI does this
```

Three entries per layer:

| Layer | Owner this phase (AI / human, name the human) | Evidence needed to move up | Move-up approver |
|----|------------------------------|--------------|-----------|
| Decide | | | |
| Act | | | |
| Advise | | | |
| Sense | | | |

**Rules**:

- Moving up is a **milestone decision**, not routine tuning. "Let it just send this one automatically" is where the boundary starts to fall.
- "Evidence needed to move up" takes two forms, a human acceptance record (e.g. the acceptance rate for one class of suggestion ≥ threshold for N consecutive weeks), or a deterministic verification loop on that layer's output (errors automatically detectable, enumerable, reversible, with proof of verification coverage). Both are written as measurable facts, never as "once results stabilize."
- Every move up reruns the three oversight questions (Chapter 12). Does the overseer have time to look? The ability to judge? The authority to stop it?
- This map appears in at least three places, the scope decision log's attachment, the security review packet (Template 12), and the memo to decision makers (Template 19).

---

## 8.3 Scope Decision Log

| Date | Expansion | Proposer | Proposer's relation to you | Reason for refusal (the cost, one sentence) | Revival condition (a checkable event) | Status |
|------|----------|--------|--------------------|--------------------------|------------------------|------|
| | | | | | | shelved / revived / abandoned / transferred |
| | | | | | | |

Anchor & Helm example (as recorded in Chapter 8):

| Date | Expansion | Proposer | Proposer's relation to you | Reason for refusal (the cost) | Revival condition | Status |
|------|----------|--------|--------------------|------------------|----------|------|
| Proposed the day of signing, logged the next day | Home property exceptions | Kevin Doyle | pilot owner | User group, annotation system, and metric baseline all double, diluting the pilot evidence | The **first** extension after the pilot North Star hits target (exclusive) | shelved |
| Day of signing | Full automation | Grant Whitmore | sponsor | The decision rights boundary stops at the advise layer this phase, and the act layer has no acceptance data | Once the advise layer's acceptance data hits target, move up one layer at a time, each layer decided on its own | shelved |
| Day after signing | General-purpose workflow platform | The older engineer | co-build engineer (claims-ops IT, same project team) | Not one of the five gaps narrows with a platform, and two widen | After the second slice lands, distill what is common | shelved |

**Rules**:

- **Log it on the spot, send it back to the proposer within 48 hours.** The log itself is the proposer's answer. Most proposals want not a "yes" but an answer they can repeat. For a proposal from another department, cc the sponsor when you send it back. The cc is not tattling. It sends a lateral request into the hands of the person with the authority to rank it.
- Write the reason for refusal as a **cost**, not an attitude ("not for now" and "not a priority" are attitudes; "eval doubles, pilot slips six weeks" is a cost).
- Write revival conditions as **events**, not dates. "Look again in Q3" and nothing happens when Q3 comes. "After the pilot hits target" and when the event happens the proposer comes to open this page himself. Once the system enters the operating period, pilot events like "hits target" no longer occur, and revival conditions switch to operating-period anchors. One kind hangs on the periodic resource review, written as "ranked with the others at next quarter's resource review." The other hangs on an operating metric, written as "revisit after such-and-such operating metric holds within threshold for N consecutive weeks." An entry that cannot be given either anchor is really a new project already and should go through project approval.
- The charter's "not this phase" list (Template 4) is this log's first batch of entries. After signing, add the cost and revival condition to each.
- **The half-day rule**: any "favor" over half a day (scattered support that goes through no project approval and no charter) also goes in this log. The proposer writes their name and their relation to you, and the refusal reason column states which item of this phase it crowds out.
- **Reread the revival list** at every milestone retrospective. Entries whose revival condition is met either start or get their condition explicitly rewritten. Renege once and this log loses its credibility. On the day the pilot hits target, this log is the ready-made phase-two roadmap (Chapter 23).
- Platform proposals all get the same revival condition, "after the second slice lands." A good abstraction grows out of the second case. It is not guessed from the first.

---

## 8.4 No Slice Self-Check (Over-Narrowing Check)

Run this after every narrowing. Any item marked ✗ means you cut too far, and the thin slice has become a no slice:

- [ ] At least one real user in the "one user group," after hearing the slice described, will say "this solves my problem" (verify with their own words, do not answer for them).
- [ ] The slice runs end to end, data → sense → advise → human decision → outcome measurement, one whole path, with no gap where "this stretch is handled by hand for now."
- [ ] The North Star's improvement is still attributable to this slice (if what is left cannot move the metric, the metric has become an empty promise).
- [ ] The change users make to use it is smaller than the effort it saves them (otherwise the resistance of Chapter 20 arrives early).

**Judgment**: the "minimum" in thin slice is the minimum that is complete in value, not the minimum that is easy to engineer. A slice that avoids every risk also avoids the risk of success.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/thin-slice/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/thin-slice/): table scaffolds for this template set and a lightweight maintenance script for the scope decision log
