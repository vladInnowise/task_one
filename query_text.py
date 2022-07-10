"""queries mentioned in task file"""

query_one = 'SELECT room, count(r.id) FROM rooms r INNER JOIN students s on r.id = s.room GROUP BY room ORDER BY COUNT(*) desc;'

query_two = 'SELECT r.name, avg(now() - s.birthday) d FROM rooms r INNER JOIN students s on r.id = s.room GROUP BY r.name ORDER BY d ASC LIMIT 5;'

query_three = 'SELECT r.name, max(s.birthday) - min(s.birthday) d FROM rooms r INNER JOIN students s on r.id = s.room GROUP BY r.name ORDER BY d DESC LIMIT 5;'

query_four = 'SELECT r.name, count(distinct(s.sex)) FROM rooms r INNER JOIN students s on r.id = s.room GROUP BY r.name HAVING COUNT(distinct(s.sex)) = 2;'

index_one = 'CREATE INDEX valera on ROOMS(id)'

index_two = 'CREATE INDEX valer4ik on STUDENTS(id)'
