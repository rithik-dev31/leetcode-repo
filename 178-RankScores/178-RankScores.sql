-- Last updated: 8/12/2026, 11:31:25 AM
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;