# Thin Slice Definition Sheet and Scope Decision Log (Fillable)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
> Source: Template 8 (companion: Chapter 8). Fill the definition sheet once at project approval and review it at every milestone; the scope decision log stays live from project approval onward (CSV version paired with `scope_log.py`).

---

## 1. Thin Slice Definition Sheet (8.1 The Five Ones)

| The Five Ones | Filled In for This Project | Self-Check Question |
|--------|-----------|----------|
| **One User Group** | | Specific down to the team and the names, not a department. Who in this group will say "this solves my problem"? Cannot name them? Go back to Chapter 5 and find the actual user. |
| **One Decision** | | A decision point the user already makes, not a newly invented action. When the system's suggestion is wrong, can the user spot it and override it on the spot? |
| **One Data Path** | | List every source the data passes through. Has each source's fitness been checked (Template 9)? Does "after reconciliation" actually hold? |
| **One Risk Boundary** | | The decision rights boundary (where AI stops) plus red lines. Do the red lines show up anywhere besides the documentation, in review materials and the product interface too? |
| **One Measurable Outcome** | | Cite the charter's North Star (Template 4) directly, do not invent a second metric. When this number gets worse, does anyone hurt? |

**Rules for filling this in**:

- If any cell has "and / as well as / etc. / two kinds" in it, that cell is already creeping. Talk about narrowing it before you fill in the sheet.
- The five cells must lock together into one readable sentence: "**This user group, making this decision, along this data path, inside this risk boundary, improves this metric.**" Wherever it does not read smoothly is where the cut is not clean.
- Review it at every milestone (prototype, pilot, launch): check whether any of the Five Ones has quietly become plural.

Lock-together sentence (write yours in the same form): ____

---

## 2. Scope Decision Log (8.3)

| Date | Expansion | Proposed By | Rejection Reason (cost, one sentence) | Revival Condition (a checkable event) | Status |
|------|----------|--------|--------------------------|------------------------|------|
| | | | | | shelved / revived / abandoned |
| | | | | | |

**Rules for using this**:

- **Log it on the spot, send it back to the proposer within 48 hours.** Most proposals want not a "yes" but an answer they can repeat.
- Write the rejection reason as a **cost** ("doubles the eval, delays the pilot six weeks"), not an attitude ("not considering it for now").
- Write the revival condition as an **event**, not a date. "After the pilot hits target" and when the event happens the proposer comes to open this page himself.
- The charter's "not this phase" list is this table's first batch of entries. Reread the revival list at every milestone retrospective. Renege once and this table loses its credibility.
- For platform-style proposals, always write the revival condition as "after the second slice lands."
