-- Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
-- Override rate weekly report query (Template 17.2 review cadence: split by suggestion category, check once a week).
-- Usage: sqlite3 trail.db < weekly-override-report.sql, or run it against the sample database with run_report.py.

-- 1. Override rate split by category (no overall average, single-category basis, Template 18.1.2)
SELECT s.category                                              AS category,
       COUNT(*)                                                AS decisions,
       SUM(d.decision = 'override')                            AS overrides,
       ROUND(100.0 * SUM(d.decision = 'override') / COUNT(*), 1) AS override_rate_pct
FROM decisions d JOIN suggestions s ON s.suggestion_id = d.suggestion_id
WHERE d.decided_at >= datetime('now', '-7 days')
GROUP BY s.category
ORDER BY override_rate_pct DESC;

-- 2. Reason code distribution (trace the rule implementation for the category with the highest hit rate, wrong-shaped cases feed the golden cases)
SELECT s.category AS category, d.reason_code AS reason_code, COUNT(*) AS count
FROM decisions d JOIN suggestions s ON s.suggestion_id = d.suggestion_id
WHERE d.decision = 'override' AND d.decided_at >= datetime('now', '-7 days')
GROUP BY s.category, d.reason_code
ORDER BY s.category, count DESC;

-- 3. Share of the "other" code (over three in ten means the enum is due for a revision, Template 17.2)
SELECT SUM(d.reason_code = 'other')                              AS other_count,
       COUNT(*)                                                  AS override_total,
       ROUND(100.0 * SUM(d.reason_code = 'other') / COUNT(*), 1) AS other_pct
FROM decisions d
WHERE d.decision = 'override' AND d.decided_at >= datetime('now', '-7 days');
