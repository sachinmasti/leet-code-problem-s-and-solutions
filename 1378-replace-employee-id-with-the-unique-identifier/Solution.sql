-- Write your PostgreSQL query statement below
SELECT l.name,r.unique_id
FROM Employees l
LEFT JOIN EmployeeUNI r
ON l.id = r.id;
