-- creates the table unique_id on your MySQL server.
-- Creates and declares the table contents.
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	)
