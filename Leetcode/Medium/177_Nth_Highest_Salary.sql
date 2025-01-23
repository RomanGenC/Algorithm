CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT em.salary
    FROM (
      SELECT empl.salary, dense_rank() OVER (ORDER BY empl.salary DESC) AS rank
      FROM Employee empl
    ) em
    WHERE em.rank = N
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;
