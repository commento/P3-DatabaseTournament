P3 Database Tournament project
=============

Required tools:

- Python
- PostgreSQL for Python

If the database is required on the Virtual Machine
- Vagrant
- Virtual Box

Instruction:

Clone the repository: https://github.com/commento/P3-DatabaseTournament.git

Access the Virtual Emulated Server with commands:
- vagrant up
- vagrant ssh

Create the Database with the commands:
- psql in the cloned repository folder
- CREATE DATABASE tournament;

Create the Database Tables with the command:
- \i tournament.sql


Repository files:
tournament.sql: SQL for Tables Creation
tournament.py : Database APIs
tournament_test.py : Test the database handler functions


Database APIs:

connect
Meant to connect to the database.

deleteMatches
Remove all the matches records from the database.

deletePlayers
Remove all the player records from the database.

countPlayers
Returns the number of players currently registered

registerPlayer
Adds a player to thetournament database.

playerStandings
Returns a list of the players and their win records,
sorted by wins. You can use the player standings
table created in your .sql file for reference.

reportMatch
This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.

swissPairings
Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players from the player standings table, zipping them up and appending them to a list with values:
(id1, name1, id2, name2)
