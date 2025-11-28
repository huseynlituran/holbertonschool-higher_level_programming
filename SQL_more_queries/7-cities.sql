-- this query show us how to create foreign key
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (
id INT NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
