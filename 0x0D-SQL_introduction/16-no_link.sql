-- lists all non NULL records of the table second_table of the database
-- Query to retrieve data
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
