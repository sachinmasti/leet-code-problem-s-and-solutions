-- Write your PostgreSQL query statement below
SELECT e.name, b.Bonus
FROM Employee e
LEFT JOIN  Bonus b ON
e.empID = b.empID
WHERE b.bonus < 1000 or b.bonus is NULL;
