Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.


Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

SELECT DISTINCT num as "ConsecutiveNums"
FROM (
  SELECT l.id,
         l.num,
         LAG(l.num) OVER (ORDER BY l.id) AS prev_num,
         LEAD(l.num) OVER (ORDER BY l.id) AS next_num,
         LAG(l.id) OVER (ORDER BY l.id) AS prev_id,
         LEAD(l.id) OVER (ORDER BY l.id) AS next_id
  FROM Logs l
) t
WHERE t.num = t.prev_num AND t.num = t.next_num and (next_id - prev_id) = 2;