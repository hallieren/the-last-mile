-- Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
-- Decision trail table DDL (Template 17.2; column layout = repo convention CONVENTIONS §2.1, SQLite dialect).
--
-- Core principle: suggestions and facts live in separate tables.
--   suggestions is written only by the AI, decisions is written only by people;
--   the AI never writes a single character back to the source system.
-- Append-only discipline: both tables only INSERT, never UPDATE or DELETE.
--   Change one character in a trail and it stops being a trail.
--   A revised call means appending a new decision row, never editing the old one.

CREATE TABLE suggestions (
  suggestion_id      TEXT PRIMARY KEY,
  claim_id           TEXT NOT NULL,   -- claim number, matches the source system's primary key, so it can be looked up
  input_snapshot     TEXT NOT NULL,   -- fingerprint or snapshot reference of the input at suggestion time (trail: based on what)
  rule_model_version TEXT NOT NULL,   -- rule version hit, plus model and prompt version (trail: based on what)
  suggestion         TEXT NOT NULL,   -- priority plus next action (trail: said what)
  reason             TEXT NOT NULL,   -- the exact sentence shown to the person handling it (trail: said what)
  category           TEXT NOT NULL,   -- suggestion category, override rate is split by this column (Template 17 review cadence)
  created_at         TEXT NOT NULL    -- suggestion generation time (trail: when)
);

CREATE TABLE decisions (
  decision_id   TEXT PRIMARY KEY,
  suggestion_id TEXT NOT NULL REFERENCES suggestions,
  decision      TEXT NOT NULL CHECK(decision IN ('accept','override')),  -- trail: who made the call
  reason_code   TEXT,                 -- required on override, enum in reason-codes.json (loop-closing entry point)
  reason_note   TEXT,                 -- optional note; required when reason_code='other'
  decided_by    TEXT NOT NULL,        -- real name, inherited from the source system's identity
  decided_at    TEXT NOT NULL,        -- decision time (kept apart from suggestion time, two separate timestamps)
  CHECK(decision='accept' OR reason_code IS NOT NULL)  -- override requires reason_code, enforced at the database layer
);
