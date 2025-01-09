-- Write your PostgreSQL query statement below
WITH DeptMaxSalary AS (
    SELECT
        MAX(salary) AS max_salary,
        Department.id AS dId,
        Department.name
    FROM Employee
    LEFT JOIN Department ON Employee.departmentId = Department.id
    GROUP BY Department.id, Department.name
)
SELECT DeptMaxSalary.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
LEFT JOIN DeptMaxSalary ON Employee.departmentId = DeptMaxSalary.did
WHERE Employee.salary = DeptMaxSalary.max_salary