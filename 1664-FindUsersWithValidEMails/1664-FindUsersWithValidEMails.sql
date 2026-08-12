-- Last updated: 8/12/2026, 11:27:29 AM
SELECT *
FROM Users
WHERE REGEXP_LIKE(
    mail,
    '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$',
    'c'
);