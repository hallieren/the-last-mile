> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/pattern-library

- **Corresponding template**: Template 23 (Pattern Extraction Sheet + Asset Register + Library Admission Checklist, Chapter 23) ([full appendix](../../../docs/appendices/template-23-pattern-extraction.md))
- **One-sentence purpose**: Keep the asset library fresh on its own. Extraction has a template, registration has two synced versions, six months with no update auto-downgrades the asset, and packing keeps three files together.

| File | What it is | How to use |
|------|--------|--------|
| `asset-register.md` | Asset register, Markdown version (for people to read; Anchor & Helm's first admission batch as a sample) | Project it during review; keep it in sync with the CSV version |
| `sample/assets.csv` | Asset register, machine-readable version = source of truth (column names match CONVENTIONS §2.5 word for word) | Copy it as your own register; also the downgrade script's default input |
| `downgrade_stale.py` | Auto-downgrade script for six months with no update: updated more than 183 days before the baseline date and active → pending-reverify | `python3 downgrade_stale.py [csv] --today YYYY-MM-DD [--write]`; default only prints the change list |
| `pattern-template.md` | Pattern extraction template, fillable version (six fields + three-step stripping check + pre-admission self-check) | Fill in one page per candidate at project close-out |
| `packing-example/` | Component packing sample: asset body + applicability boundary + verification record travel together as three files (demonstrates the decision trail schema) | Pack it this way before feeding a coding agent; read the boundary first |

Note: the baseline date always comes in through `--today` (defaults to the sample baseline date 2026-07-19), it never reads the system clock, so this is testable and reproducible. The CSV is a pure data file with no license line added, to keep the §2.5 format clean.
