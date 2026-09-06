> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# templates/intake

- **Corresponding template**: Template 25 (Intake Rubric + Red Line List + Saying No Scripts + Kill Register, Chapter 25) ([full appendix](../../../docs/appendices/template-25-intake-redlines.md))
- **One-sentence purpose**: The gate at the team's door. Red lines come before scoring, a "no" lands in the register, and someone gets reminded when a revival condition comes due.

| File | What it is | How to use |
|------|--------|--------|
| `intake-scorecard.md` | Red line checklist + five-dimension scorecard, fillable version (the order is fixed: red lines before scoring, any one of them vetoes) | Run each candidate through it one by one; the saying-no scripts are in Template 25.3 |
| `sample/kill-log.csv` | Kill register sample (five columns: candidate / proposed_by / kill_reason / revival_condition / one_year_review; two Anchor & Helm rows plus a placeholder row) | Copy it as your own register; write revival conditions as events, not dates |
| `revival_reminder.py` | Revival-condition due-date reminder script: rows whose condition holds a YYYY-MM-DD date are compared against a baseline date; rows written as events get flagged for a "manual pass through the table" | `python3 revival_reminder.py [csv] --today YYYY-MM-DD` |

Note: the register's discipline is to write revival conditions as events, not dates. The script only reminds on date-type conditions (such as an annual review date); event-type conditions can only be passed through by hand, and that is the whole point of the annual review. A register that stays empty for a long time is also a signal. It does not mean every call was right, it means the gate is not working. The CSV is a pure data file, with no license line added.
