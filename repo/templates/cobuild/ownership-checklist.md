# Repo Structure and CI Ownership Checklist (Template 15.1 Clause One and Clause Two Companion)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

## 1. Code Ownership Goes to the Receiving Side (Clause One)

| Item | Fill In | Check |
|----|------|------|
| Module CODEOWNERS | ____ | Name the receiving side, not your team |
| Merge rights | ____ | With the receiving side (gatekeeping rights assigned in the table below) |
| Oncall ownership | ____ | The rotation schedule states these modules belong to the receiving side |
| CI / release process ownership | ____ | Follow the receiving side's existing release process, do not build a new one |
| Your team members' account type | ____ | Collaborator status, exit after handoff (sample config in `collaborator-access.yaml`) |
| Exception list | ____ | Which code does not go into the receiving side's repo (such as your team's internal tools); list item by item with reasons |

Red line: the day the AI team holds gatekeeping rights long-term is the day permanent ops begins. There is no option of "develop on our side first, migrate at handoff." Migration day would just become the day you deliver a black box.

## 2. Module Ownership: The Backward Staffing Table (Clause Two)

Fill-in order is disciplined: fill "maintainer after handoff" first, then work backward to "lead writer." Any row where the two columns disagree must carry a convergence plan in the last column.

| Module | Maintainer After Handoff | Maintainer's Performance Accountability | Lead Writer | Pairing / Review Side | Gatekeeper (Current) | Handoff Condition |
|------|-------------|------------------|--------|----------------|----------------|----------|
| ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ____ | ____ | ____ | ____ | ____ | ____ | ____ |

- **Leading the writing is not writing alone**: the lead writer is accountable for the code, can explain it, and decides what merges; the other side pairs.
- **Maintainer's performance accountability**: this column answers "when it breaks at midnight, whose annual objectives say to fix it." In most cases it should match the maintainer after handoff; a row where they disagree is a hidden accountability vacuum, and the convergence plan must spell out how to close it.
- **Gatekeeper** (who decides what merges) gets its own column: your team can hold it early on, but every row states its handoff condition (such as "hands over after two consecutive reviews of that module with no rejection"). Before handoff day, every row's gatekeeper should sit with the receiving side.
- A module whose complexity is temporarily beyond the receiving side's ability still gets written as "maintainer: the receiving side (longer term)." The pairing on that row is not a courtesy, it is the convergence path.

Anchor & Helm sample fill-in (Template 15.1.5, the week-9 signed version): the extraction pipeline, maintained by claims-ops IT / led by claims-ops IT / paired with the Digital Center; the queue core, maintained by claims-ops IT (longer term) / led by the Digital Center / paired with claims-ops IT; the merged view, led by the Digital Center, with lead-writer rights handed over before handoff; rules and de-identification as configuration, led by claims-ops IT.

## 3. Health Self-Check (Three Numbers Every Beat, Template 15.2.3)

- [ ] The receiving side's engineers' share of commits (should rise)
- [ ] Number of modules your team still holds gatekeeping rights on (should fall)
- [ ] Number of questions your team answers on the receiving side's behalf at the rotating release (should trend to zero)

If any one of the three numbers moves the wrong way for two beats running, go back to Chapter 15's failure modes and match your case to one.
