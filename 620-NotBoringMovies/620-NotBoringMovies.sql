-- Last updated: 8/12/2026, 11:28:59 AM
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;