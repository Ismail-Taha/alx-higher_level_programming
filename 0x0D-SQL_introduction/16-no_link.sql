--  script that lists all records of the table second_table of the database hbtn_0c_0 in MySQL server
-- Records are ordered by descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
