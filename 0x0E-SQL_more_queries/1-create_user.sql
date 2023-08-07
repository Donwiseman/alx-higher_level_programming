-- This creates the user user_od_1 and grants it all privileges.
-- The below codes carries out the above.
CREATE USER IF NOT EXISTS
	'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
