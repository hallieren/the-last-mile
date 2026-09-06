> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Asset Body: The Decision Trail Schema (Component)

One line: AI suggestions and human decisions live in separate tables, append-only and never edited, override always carries a reason code, so "who made the call, and on what basis" becomes checkable from then on.

Structure (SQLite dialect, column names are exactly CONVENTIONS §2.1):

```sql
-- suggestions (suggestion table, written by AI, append-only)
CREATE TABLE suggestions (
  suggestion_id TEXT PRIMARY KEY, claim_id TEXT NOT NULL, input_snapshot TEXT NOT NULL,
  rule_model_version TEXT NOT NULL, suggestion TEXT NOT NULL, reason TEXT NOT NULL,
  category TEXT NOT NULL, created_at TEXT NOT NULL);

-- decisions (human decision table, written by people)
CREATE TABLE decisions (
  decision_id TEXT PRIMARY KEY, suggestion_id TEXT NOT NULL REFERENCES suggestions,
  decision TEXT NOT NULL CHECK(decision IN ('accept','override')),
  reason_code TEXT, reason_note TEXT, decided_by TEXT NOT NULL, decided_at TEXT NOT NULL);
```

Design invariants (must not be broken on reuse):

1. Suggestion and fact live in separate tables: AI writes the suggestion table, people write the decision table, neither overwrites the other.
2. Append-only: neither table has an UPDATE or DELETE path; changing a call means appending a new decision, never editing the old one.
3. `reason_code` is required when `decision = 'override'`; the enum holds 7 values or fewer plus `other`, and the vocabulary gets rewritten in each business line's own front-line language (the structure is generic, the vocabulary is business-line specific).
4. `input_snapshot` stores the input snapshot at the moment the suggestion was generated, so a later retrospective never depends on the source system's current state.
