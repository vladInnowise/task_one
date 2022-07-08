query_one = 'select room, count(r.id) from rooms r inner join students s on r.id = s.room group by room order by count(*) desc;'

query_two = 'select r.name, avg(now() - s.birthday) d from rooms r inner join students s on r.id = s.room group by r.name order by d asc limit 5;'

query_three = 'select r.name, max(s.birthday) - min(s.birthday) d from rooms r inner join students s on r.id = s.room group by r.name order by d desc limit 5;'

query_four = 'select r.name, count(distinct(s.sex)) from rooms r inner join students s on r.id = s.room group by r.name having count(distinct(s.sex)) = 2;'
