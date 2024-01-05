-- Write your PostgreSQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
Left JOIN Address a ON p.personId = a.personId;