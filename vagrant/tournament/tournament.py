#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        DB=psycopg2.connect("dbname={}".format(database_name))
        cursor=DB.cursor()
        return DB,cursor
    except:
         print("Counld not connect to database..")

def deleteMatches():
    """Remove all the match records from the database."""
    DB,c=connect()
    c.execute("DELETE FROM match")
    DB.commit()
    DB.close

def deletePlayers():
    """Remove all the player records from the database."""
    DB,c=connect()
    c.execute("DELETE FROM players_detail")
    DB.commit()
    DB.close

def countPlayers():
    """Returns the number of players currently registered."""
    DB,c=connect()
   
    c.execute("SELECT count(*) AS number FROM players_detail")
    no_of_players= c.fetchone()[0]
    DB.close

    return int(no_of_players)

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB,c=connect()
    
    c.execute("INSERT INTO players_detail(name) VALUES (%s)",(name,))
    DB.commit()
    DB.close          

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
    DB,c=connect()
   
    c.execute("SELECT * FROM playerStandings")
    players_list=c.fetchall()
    DB.close
    return players_list

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB,c=connect()
   
    c.execute("INSERT INTO match(winner,loser) VALUES (%s,%s)",(winner,loser,))
    DB.commit()
    DB.close  
 
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
    result=playerStandings()
    pairs=[]
    for i in range(0,len(result),2):
        pair=(result[i][0],result[i][1],result[i+1][0],result[i+1][1])
        pairs.append(pair)
    
    return pairs
