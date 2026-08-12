-- Last updated: 8/12/2026, 11:31:14 AM
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;