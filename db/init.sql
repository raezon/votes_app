/* EDIT ME */
CREATE database dms_db;
USE dms_db;
GRANT ALL on dms_db to root;
CREATE table votes (
	ID int auto_increment,
	FirstName varchar(255) null,
	LastName varchar(255) null,
	Choice varchar(255) null,
);