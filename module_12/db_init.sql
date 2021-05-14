/*
 Title: db_init.sql
 Name: James Smith
 Date: 16 July 2020
 Description: WhatABook DB initialization code
*/

use whatabook;

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
user_id INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(75) NOT NULL,
last_name VARCHAR(75) NOT NULL,
PRIMARY KEY(user_id) 
)AUTO_INCREMENT = 1;

CREATE TABLE book (
book_id INT NOT NULL AUTO_INCREMENT,
book_name VARCHAR(200) NOT NULL,
author VARCHAR(200) NOT NULL,
details VARCHAR(500),
PRIMARY KEY(book_id)
)AUTO_INCREMENT = 1;	

CREATE TABLE wishlist (
wishlist_id INT NOT NULL AUTO_INCREMENT,
user_id INT NOT NULL,
book_id INT NOT NULL,
PRIMARY KEY (wishlist_id),
CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES book(book_id),
CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(user_Id)
)AUTO_INCREMENT = 1;

CREATE TABLE store (
store_id INT NOT NULL AUTO_INCREMENT,
locale VARCHAR(500) NOT NULL,
PRIMARY KEY(store_id)
)AUTO_INCREMENT = 1;

INSERT INTO user(first_name, last_name) 
VALUES
	('Melanie', 'Johnson'),
	('Jay', 'Smith'),
	('Nellie', 'Bishop');
	
INSERT INTO book(book_name, author, details) 
VALUES
	('If You Give a Mouse a Cookie', 'Laura Numeroff', NULL),
	('All by Myself', 'Mercer Mayer', NULL),
	('Goodnight Moon', 'Margaret Brown', NULL),
	('The Very Hungry Caterpillar', 'Eric Carle', NULL),
	('Where the Wild Things Are', 'Maurice Sendak', NULL),
	('Charlottes Web', 'E.B. White', NULL),
	('The Giving Tree', 'Shel Sylverstein', NULL),
	('Green Eggs and Ham', 'Dr. Seuss', NULL),
	('Corduroy', 'Don Freeman', NULL);
	
INSERT INTO wishlist(user_id, book_id)
VALUES
	(1, 7),
	(2, 4),
	(3, 2);

INSERT INTO store(locale)
VALUES ('555 N. Central Rd., Omaha, NE 68114');