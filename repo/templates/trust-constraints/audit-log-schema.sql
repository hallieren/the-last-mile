-- Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
-- Audit log schema sample (Template 12 §4 trail notes; SQLite dialect).
-- Perspective note: same conventions as CONVENTIONS §2.1's two trail tables (suggestions/decisions), but this is a
-- flattened audit-view sample, so if something goes wrong, one row reconstructs "who did what, based on what, and when."
-- AI output never writes back to any source field. It exists only in trail form (Chapter 9).

CREATE TABLE audit_log (
  suggestion_id      TEXT NOT NULL,     -- suggestion ID; a re-decision appends a new row, one suggestion can have several (append-only, same as §2.1)
  input_snapshot     TEXT NOT NULL,     -- input snapshot (redacted, see redaction-rules.json)
  rule_model_version TEXT NOT NULL,     -- rule/model version
  suggestion         TEXT NOT NULL,     -- suggestion content
  reason             TEXT NOT NULL,     -- reason (what the reviewer checks against, the carrier of oversight's "ability to judge")
  human_decision     TEXT,              -- human decision plus decider (e.g. "override:doc-missing by [name]"; NULL = not yet decided)
  occurred_at        TEXT NOT NULL      -- timestamp (ISO 8601)
);

-- If the §2.1 two tables are already in place, the audit view should be derived from them, read-only, not a separate store:
-- CREATE VIEW audit_log AS
-- SELECT s.suggestion_id, s.input_snapshot, s.rule_model_version, s.suggestion, s.reason,
--        d.decision || COALESCE(':' || d.reason_code, '') || ' by ' || d.decided_by AS human_decision,
--        COALESCE(d.decided_at, s.created_at) AS occurred_at
-- FROM suggestions s LEFT JOIN decisions d ON d.suggestion_id = s.suggestion_id;

-- Review packet companion (12.2 §4 still needs to spell this out, not part of the schema): retention period, query permissions, spot-check cadence;
-- and actually run one historical suggestion through a trace-back once (Template 12.1.1's audit-row anti-formalism check).
