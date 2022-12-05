CREATE DATABASE IF NOT EXISTS JoyOfPainting;
USE JoyOfPainting;
CREATE TABLE IF NOT EXISTS Episodes (
	Title VARCHAR(100) NOT NULL PRIMARY KEY,
	Season INT NOT NULL,
	Episode INT NOT NULL,
	Air_Date JSON NOT NULL,
	Colors JSON NOT NULL,
	Subjects JSON NOT NULL,
	YouTube VARCHAR(100) NOT NULL,
	Painting VARCHAR(100) NOT NULL
);