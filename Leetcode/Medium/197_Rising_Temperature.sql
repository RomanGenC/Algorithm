-- Write your PostgreSQL query statement below
SELECT Weather.id
FROM Weather
INNER JOIN Weather yesterday ON Weather.recordDate = yesterday.recordDate + INTERVAL '1 day'
WHERE Weather.temperature > yesterday.temperature