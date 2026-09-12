# Five Ones definition sheet and decision rights boundary map

Source: `docs/appendices/template-08-thin-slice.md` §8.1, 8.2, 8.4 (and `repo/templates/thin-slice/thin-slice.md`; the repo wins on conflict).

| Field | Value |
|---|---|
| Project | <project> |
| Charter North Star (cited, not restated) | <metric>, baseline <baseline>, target <target> REQUIRED |
| Filled by | <owner name> REQUIRED |
| Date | <date> REQUIRED |
| Milestone this sheet was last reread at | prototype / pilot / launch |

**Thin slice definition sheet (the Five Ones).** Thin is the width; every layer goes all the way to real.

| The Five Ones | Filled in for this project | Self-check question |
|---|---|---|
| One user group | <team and names, not a department> REQUIRED | Who in this group will say "this solves my problem"? Cannot name them → go back and find the actual user |
| One decision | <a decision point the user already makes> REQUIRED | If the system's suggestion is wrong, can the user see it on the spot and override it? |
| One data path | <source> → <source> → <view> → <interface>, every source listed | Has the fitness of every source on the path been checked? Has "after reconciliation" actually been delivered? |
| One risk boundary | AI stops at <layer>; red lines: <never touched>, <never touched> REQUIRED | Besides the documents, do the red lines also appear in the review materials and the product interface? |
| One measurable outcome | <the charter North Star, cited directly> REQUIRED | When this number gets worse, does anyone hurt? |

Lock sentence: `<This user group>, making <this decision>, along <this data path>, inside <this risk boundary>, improves <the charter's North Star>.`

**Decision rights boundary map.** Rewrite each layer for your workflow, bottom up.

| Layer | What sits here | Owner this phase (AI / human, name the human) | Evidence needed to move up (a measurable fact) | Move-up approver |
|---|---|---|---|---|
| Decide | <the workflow's final decision, e.g. pay or not, how much> | never touched (red line) | / | / |
| Act | <actions with external effect, e.g. send, assign, change status> | human: <owner name> REQUIRED | <e.g. acceptance rate for <suggestion class> ≥ <threshold> for <N> consecutive weeks, or errors automatically detectable, enumerable, reversible with verification coverage <x%>> | <owner name>, at <milestone> REQUIRED |
| Advise | <priority, next step, each with a reason> | AI (this phase) | | |
| Sense | <gather, extract, reconcile, flag signals> | AI | | |

**Rules**
- Any cell containing "and / as well as / etc. / two kinds" → that cell is already creeping. Negotiate the narrowing first, then fill in the sheet.
- The five cells must lock together into one readable sentence. Wherever it does not read smoothly is where the cut is not clean.
- The definition sheet is not a one-time document. Recheck it at every milestone (prototype → pilot → launch). Have any of the Five Ones quietly become plural?
- Moving up is a milestone decision, not routine tuning. "Let it just send this one automatically" is where the boundary starts to fall.
- "Evidence needed to move up" takes two forms, a human acceptance record or a deterministic verification loop on that layer's output. Both are written as measurable facts, never as "once results stabilize."
- Every move up reruns the three oversight questions. Does the overseer have time to look? The ability to judge? The authority to stop it?
- This map appears in at least three places, the scope decision log's attachment, the security review packet, and the memo to decision makers.

**No slice self-check** (run after every narrowing; any ✗ means you cut too far)
- [ ] At least one real user in the "one user group", after hearing the slice described, will say "this solves my problem" (verify with their own words, do not answer for them).
- [ ] The slice runs end to end, data → sense → advise → human decision → outcome measurement, with no gap where "this stretch is handled by hand for now."
- [ ] The North Star's improvement is still attributable to this slice.
- [ ] The change users make to use it is smaller than the effort it saves them.

Filled in → goes to: the scope decision log (the charter's "not this phase" list becomes its first rows; the boundary map is its attachment), the data fitness scorecard (one column per source on the data path), the security review packet and the decision memo (the boundary map).
