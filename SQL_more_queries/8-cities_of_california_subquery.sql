-- this query help us to use subquery
SELECT id , name
FROm cities
WHERE state_id =
(SELECT id FROM states WHERE name = 'California')
ORDER BY id
;
