-- Write your PostgreSQL query statement below
SELECT Employee.name as Employee
FROM Employee
INNER JOIN Employee manager on Employee.managerId = manager.id
WHERE Employee.salary > manager.salary