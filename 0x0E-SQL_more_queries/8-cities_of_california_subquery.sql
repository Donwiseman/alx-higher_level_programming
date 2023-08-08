-- lists all the cities of California that can be found in the database hbtn_0d_usa.
-- This uses a Subquery to find the id of california and then use it to find it's cities.
SELECT id, name
FROM cities
WHERE state_id = 
	(SELECT id
		FROM states
		WHERE name = 'California'
	)
ORDER BY id ASC;
