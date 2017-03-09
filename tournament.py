#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM Matches;")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM Players;")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) as count FROM Players;")
    count = c.fetchone()[0]
    DB.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO Players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT Players.name, Players.id, "
              "count(CASE WHEN Matches.winner = Players.id THEN 1 END) as wins, count(Matches.loser) as matches "
              "FROM Players left join Matches on Players.id = Matches.winner OR Players.id = Matches.loser "
              "GROUP BY Players.id ORDER BY wins DESC;")
    players = [{'id': str(row[1]), 'name': str(row[0]), 'wins': int(row[2]), 'matches': int(row[3])} for row in c.fetchall()]
    DB.close()


    return players


# SELECT Players.name, Players.id, count(Matches.loser) as matches FROM Players left join Matches WHERE Players.id = Matches.winner OR Players.id = Matches.loser GROUP BY Players.id ORDER BY wins DESC;

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO Matches (winner,loser) VALUES (%s,%s)", (winner,loser))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

# registerPlayer('ciao')
# registerPlayer('mamma')
# registerPlayer('come')
# registerPlayer('stai')
# registerPlayer('tvb')
# registerPlayer('donne')
# print(countPlayers())
print(playerStandings())
# reportMatch(21, 20)
# reportMatch(15, 16)
# reportMatch(17, 18)
# reportMatch('ciao', 'tvb')
# reportMatch('donne', 'ciao')

# deletePlayers()
# print(countPlayers())
