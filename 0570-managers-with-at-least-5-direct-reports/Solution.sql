-- Write your PostgreSQL query statement below
SELECT  i.name
FROM employee i
JOIN employee o 
ON i.id = o.managerID
GROUP BY i.id,i.name
HAVING COUNT(o.managerID) >=5;
