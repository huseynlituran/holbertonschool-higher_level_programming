-- this query help us dont show null
SELECT score , name
FROM second_table
WHERE name != 'NULL'
ORDER BY score DESC;
