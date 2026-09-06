-- Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
-- Sample weekly report query for daily active use and usage depth by group (Template 21; table layout and column names in CONVENTIONS §2.1, SQLite dialect).
-- Assumption: the trail tables only carry decided_by. Group and roster membership come from the
-- business side's org roster; this uses a VALUES placeholder here. In real use, swap it for your
-- own roster table (decided_by, grp). Sample roster comes from the book's Anchor & Helm case.

WITH roster(decided_by, grp) AS (
  VALUES ('Linda Marsh', 'Group 1'), ('Reviewer A', 'Group 1'),
         ('Reviewer B', 'Group 2'), ('Reviewer C', 'Group 2')
),

-- (1) Daily active by group: daily active = users with a decisions row that day / rostered users in the group
daily_active AS (
  SELECT DATE(d.decided_at) AS day, r.grp,
         ROUND(COUNT(DISTINCT d.decided_by) * 1.0 /
               (SELECT COUNT(*) FROM roster r2 WHERE r2.grp = r.grp), 2) AS active_ratio
  FROM decisions d JOIN roster r ON r.decided_by = d.decided_by
  GROUP BY day, r.grp
),

-- (2) Usage depth (grouped by week): override rate / reason code fill rate / "other" code share
--     The last two are the detectors for failure mode 2, "going-through-the-motions compliance" (Template 21 Code hooks)
weekly_depth AS (
  SELECT strftime('%Y-W%W', d.decided_at) AS week, r.grp,
         COUNT(*) AS decisions_n,
         ROUND(AVG(d.decision = 'override'), 2) AS override_rate,
         ROUND(AVG(CASE WHEN d.decision = 'override'
                        THEN d.reason_code IS NOT NULL AND d.reason_code != '' END), 2)
           AS reason_fill_rate,
         ROUND(AVG(CASE WHEN d.decision = 'override'
                        THEN d.reason_code = 'other' END), 2) AS other_rate
  FROM decisions d JOIN roster r ON r.decided_by = d.decided_by
  GROUP BY week, r.grp
)

SELECT 'daily_active' AS report, day AS bucket, grp,
       active_ratio AS v1, NULL AS v2, NULL AS v3
FROM daily_active
UNION ALL
SELECT 'weekly_depth', week, grp, override_rate, reason_fill_rate, other_rate
FROM weekly_depth
ORDER BY report, bucket, grp;
-- v1/v2/v3 meaning: daily_active rows = daily active ratio; weekly_depth rows = override rate / reason code fill rate / other share.
-- What to check first when daily active drops, in fixed order: the unsafe trail, then manager attendance, then the feature (Template 21.1's three check questions).
