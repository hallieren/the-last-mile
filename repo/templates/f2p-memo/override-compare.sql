-- Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
-- A sample cross-department comparison query for override reason-code distribution
-- (Template 24; the minimal implementation of a platform-level eval insight).
-- Merge prerequisite: the §2.1 decision trail tables are deployed per project. Do the cross-department
-- comparison in the Group's own warehouse, or do it after ATTACHing each project's exported
-- database, adding a department column at the UNION ALL. Both subsidiaries' trails already
-- sit in the Group warehouse, which is a possibility only an internal team has. An outside
-- team cannot do this. Each business line rewrites its own reason-code vocabulary in its own
-- front-line language (the structure is shared, the vocabulary is line-specific), so compare
-- code values side by side as they are. Only 'other' means the same thing across departments
-- and can be compared directly. SQLite dialect.
--
-- Run this before use (swap the paths for the two departments' (subsidiaries') exported databases):
--   ATTACH 'anchor-helm.db' AS anchor_helm;
--   ATTACH 'swiftway.db'    AS swiftway;

WITH merged_decisions AS (
  SELECT 'Anchor & Helm' AS department, decision, reason_code FROM anchor_helm.decisions
  UNION ALL
  SELECT 'Swiftway' AS department, decision, reason_code FROM swiftway.decisions
)
SELECT department, reason_code,
       COUNT(*) AS n,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY department), 1)
         AS pct_of_overrides
FROM merged_decisions
WHERE decision = 'override'
GROUP BY department, reason_code
ORDER BY department, n DESC;
-- How to read it: a code that runs high in only one department is that department's
-- vocabulary or process problem. A matching code running high across departments is
-- a structural signal, the evidence source for an f2p memo's "generalization case" section.
