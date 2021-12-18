/*Josh Boettcher
12/2/2021
Module 10.3
Used Professor Krasso's code as a source
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- make user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- give privileges to new user
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- make tables
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


-- insert store
INSERT INTO store(locale)
VALUES("1313 Mockingbird Lane");

-- insert books
INSERT INTO book(book_name, author)
VALUES("The Outsider", "Stephen King");

INSERT INTO book(book_name, author)
VALUES("Doctor Sleep", "Stephen King");

INSERT INTO book(book_name, author)
VALUES("The Dark Tower", "Stephen King");

INSERT INTO book(book_name, author)
VALUES("The Republic of Thieves", "Scott Lynch");

INSERT INTO book(book_name, author)
VALUES("American Gods", "Neil Gaiman");

INSERT INTO book(book_name, author)
VALUES("The Light Fanstastic", "Terry Prachett");

INSERT INTO book(book_name, author)
VALUES("Secondhand Souls", "Christopher Moore");

INSERT INTO book(book_name, author)
VALUES("The Stand", "Stephen King");

INSERT INTO book(book_name, author)
VALUES("Dance of Dragons", "George R.R. Martin");

-- insert users
INSERT INTO user(first_name, last_name) 
VALUES("Josh", "Boettcher");

INSERT INTO user(first_name, last_name)
VALUES("Cecilia", "Boettcher");

INSERT INTO user(first_name, last_name)
VALUES("Aiyana", "Boettcher");

-- insert wishlist for each user
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Josh"), 
        (SELECT book_id FROM book WHERE book_name = "The Dark Tower")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Cecilia"),
        (SELECT book_id FROM book WHERE book_name = "Dance of Dragons")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Aiyana"),
        (SELECT book_id FROM book WHERE book_name = "The Republic of Thieves")
    );