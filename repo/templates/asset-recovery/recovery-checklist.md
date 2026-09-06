> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Closeout Asset Recovery Checklist (Template 24.2)

**Three triggers**: the fixed retrospective N weeks after launch, before anyone moves posts, or the quarterly asset inventory. Hook the recovery to any one of them and it gets a date; miss that window and it defaults to not happening.
**Guiding principle**: the code may sit in the same git, but structure that was never declared is the same as structure that does not exist. Code files belong to the business line repo (Chapter 15); schema designs, error taxonomies, and key judgments belong to no repo at all.

**Three questions per item**: Is it general (does it still hold in another industry)? What is n (how many projects have hit it)? Which exit does it go to?

Three exits: **admit** (goes through the Template 23.3 admission review, registered into the asset register, must have an owner) / **send a memo** (n≥2 and at platform capability level, goes through 24.1) / **leave it in the business line repo** (business-line-specific, note one line on why it is not recovered). The first two exits are not mutually exclusive; only "leave it in the business line repo" is an exclusive exit.

## Four-Class Stocktake Table (Fillable)

| Class | What to Go Through | Asset | General? | n= | Destination | owner |
|----|--------------|------|--------|----|------|-------|
| **Code** | Decision trail schema / eval harness / queue skeleton / extraction pipeline structure / configuration patterns | ____ | ____ | ____ | ____ | ____ |
| **Documents** | charter / review packet / the three memos / runbook / annotation guide **framework** (the content does not transfer) | ____ | ____ | ____ | ____ | ____ |
| **Judgment** | Key judgments / failure modes and incident retrospectives / annotation disagreement rulings as precedent | ____ | ____ | ____ | ____ | ____ |
| **Metrics** | Metric definition tree / thresholds and acceptance lines / reason code enumeration / balancing metrics | ____ | ____ | ____ | ____ | ____ |

**Anchor & Helm sample row** (what actually happened in Chapter 24, the sample taken from the book's Anchor & Helm case):

| Asset | Class | General? | n= | Destination |
|------|----|--------|----|------|
| Decision trail schema | Code | Yes (a structural requirement) | 2 | Admit + send a memo (#1) |
| The five rules of thumb | Judgment | No. Tacit knowledge does not transfer, the method for mining it transfers | 1 | Stays with the business side. The three-layer probing method is admitted |
| Reason code enumeration (the Anchor & Helm version) | Metrics | The structure is general, the vocabulary is business-line-specific | 2 | The structure rides along with memo #1. The vocabulary stays with the business side |

## Closing Three-Point Check

- [ ] Every item has a destination. "Leave it for now" is not allowed, and a stocktake with no exit is not a stocktake
- [ ] Every admitted item has an owner (an asset with no owner rots in six months)
- [ ] Every n=1 candidate has its trigger condition written down (register it in `../f2p-memo/candidates.csv`)
