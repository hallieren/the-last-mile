> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/f2p-memo

- **Corresponding template**: Template 24.1 (Field-to-Product Memo, Chapter 24) ([full appendix](../../../docs/appendices/template-24-f2p-memo.md))
- **One-sentence purpose**: Carry a field signal across the "project to product" river. Three filters guard the crossing, and both n=1 signals and refused memos stay in the register as assets.

| File | What it is | How to use |
|------|--------|--------|
| `f2p-memo-template.md` | The fillable four-section f2p memo (phenomenon → the generalization case → the product recommendation (a capability, not a feature) → the cost of not doing it), with a three-filter self-check | Copy and fill in. If any filter fails, do not send it. |
| `candidates.csv` | The candidate register structure (columns follow Template 24.1.3; the first row is Anchor & Helm's "repair-shop response-time metric" n=1 example) | n=1 is registered, not reported. A refused memo goes into the table together with the reason for refusal. Go through the table once a quarter. |
| `override-compare.sql` | A cross-department comparison query for override reason-code distribution (§2.1 columns, side by side by department) | Run it against the Group's own warehouse, or ATTACH each project's exported database first. See the file header for the merge prerequisites. |

Three rules (24.1.3). n=1 is registered, not reported. A refused memo goes into the table together with the reason for refusal, and its revival condition is written as events, not dates. A memo that was refused but recorded is still an asset. `candidates.csv` is a pure data file, with no license line added so it does not leak into the table body.
