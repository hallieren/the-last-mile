> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/asset-recovery

- **Corresponding template**: Template 24.2 (Closeout Asset Recovery Checklist, Chapter 24) ([full appendix](../../../docs/appendices/template-24-f2p-memo.md))
- **One-sentence purpose**: Before the project team disbands, take stock of every structural asset. Go through all four classes item by item, give each one an exit, and a stocktake with no exit is not a stocktake.

| File | What it is | How to use |
|------|--------|--------|
| `recovery-checklist.md` | Closeout asset recovery checklist, fillable version (four-class stocktake × three exits, with an Anchor & Helm sample row and a closing three-point check) | Fill it in line by line as a fixed step in the closeout retrospective |

## Aligning Fields with the Template 23 Register (Four Classes ↔ the §2.5 Category Enum)

This checklist's "class" is named by **closeout stocktake order**. On admission it maps to the asset register's (CONVENTIONS §2.5) category enum. The two vocabularies each do their own job, and the register follows §2.5:

| Recovery Checklist's Four Classes (stocktake angle: where it lives) | §2.5 Category (asset angle: what it is) | Mapping Note |
|------------------------------------|-------------------------------------|----------|
| Code | component | What gets recovered is structure, not files. Schema designs and harness skeletons are admitted as "component"; the code files themselves stay in the business line repo |
| Documents | template | The **framework** of a charter / packet / memo / runbook is admitted as "template"; filled-in content does not transfer |
| Judgment | judgment-rule | Transferable judgments are admitted; tacit knowledge itself does not transfer, the method for mining it (such as three-layer probing) is admitted as "template" |
| Metrics | metric-model | The metric tree structure, error taxonomy, and threshold structure are admitted; the specific threshold numbers and business-line vocabulary stay with the business side |

One asset row may span classes (Anchor & Helm's "reason code enumeration", the structure goes in as "metric-model", the vocabulary stays with the business side); set the category by whichever part gets admitted. Admission goes through `../pattern-library/` (extraction template, review, registration in `sample/assets.csv`); product-capability-level items go through `../f2p-memo/`. The two exits are not mutually exclusive.
