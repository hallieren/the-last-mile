# action-queue

- **Corresponding template**: Template 17 (Action Queue Design Patterns + Decision Trail Schema) ([full appendix](../../../docs/appendices/template-17-action-queue.md))
- **One-sentence purpose**: Turn the "separate suggestion from fact, append-only" decision trail into DDL you can build a database from directly, with a weekly report query for the override loop and a sample escalation rule config.
- **File list**:

| File | What it is | How to use |
|------|--------|--------|
| `schema.sql` | The two trail-table DDL (column layout = CONVENTIONS §2.1, reused by other directories on this basis; override's required reason_code is enforced by a CHECK constraint) | `sqlite3 trail.db < schema.sql` |
| `reason-codes.json` | Sample override reason code enum (5 plus other, Anchor & Helm version) | Rewrite `label` in front-line language, feed it to the front-end dropdown |
| `weekly-override-report.sql` | Weekly report query for the override rate split by category (includes the reason code distribution and the "other" share) | `sqlite3 trail.db < weekly-override-report.sql` |
| `run_report.py` | Builds a sample database with 20 rows and runs the query above, printing the result | `python3 run_report.py` (add `--db file.db` to keep the database file) |
| `escalation-config.json` | Sample config for the rollup view plus exception escalation rules (thresholds/recipients/signal categories) | Compare against Template 17.1's "two companion pieces" and rewrite each item to your project's values |

Note: `run_report.py`'s sample data is built by the script itself, as required by Template 17 (20 decisions, Anchor & Helm categories), so this directory has no `sample/` subdirectory.
