-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE Players ( id serial PRIMARY KEY,
                     name varchar(255) NOT NULL );

CREATE TABLE Matches (winner int NOT NULL,
					 loser int NOT NULL,
                     FOREIGN KEY (winner) REFERENCES Players(id),
                     FOREIGN KEY (loser) REFERENCES Players(id),
                     PRIMARY KEY (winner, loser));
