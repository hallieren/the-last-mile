> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/adoption

- Corresponding template: Template 21 (Adoption Plan, Super-user Agreement, Operating Cadence Sheet, Chapter 21) ([full appendix](../../../docs/appendices/template-21-adoption-plan.md))
- One-sentence purpose: turn adoption from a feeling into a number, with a weekly report query for daily active use and usage depth by group, plus a one-page auto-draft you can bring straight into the retro.

| File | What it is | How to use |
|------|--------|--------|
| `weekly-usage.sql` | Weekly report query for daily active use plus usage depth (override rate / reason code fill rate / other share) by group, SQLite dialect | Run against the §2.1 decision trail database; swap the roster CTE for your own org roster table |
| `retro_onepager.py` | Retro one-pager script: reason code distribution plus the aging top rows (pending suggestion age), printed as Markdown | `python3 retro_onepager.py [--decisions f] [--suggestions f] [--today YYYY-MM-DD]` |
| `sample/decisions.csv` | Sample CSV export of the decisions table (column names word for word from §2.1; sample data comes from the book's Anchor & Helm case) | Default script input; can also be imported into SQLite to check the SQL |
| `sample/suggestions.csv` | Sample CSV export of the suggestions table (column names word for word from §2.1) | Same as above |

Convention: daily active = the share of a group's rostered users who have a decisions row that day. Reason code values follow the enum in `../action-queue/reason-codes.json` (Anchor & Helm version). Of the three depth metrics, the reason code fill rate and the other share are the detectors for failure mode 2, "going-through-the-motions compliance." What to check first when daily active drops, in fixed order: the unsafe trail, then manager attendance, then the feature (Template 21.1's three check questions). The sample CSVs are pure data files, with no license line added, to keep the §2.1 column format clean.
