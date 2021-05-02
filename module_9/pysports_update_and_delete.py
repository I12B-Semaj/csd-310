'''
James Smith
CSD 310
Module 9.3
5/2/21
'''

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    #Insert a new player record into the player table
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) " +
    "VALUES('Smeagol', 'Shire Folk', 1)")

    #SELECT query from player table with an INNER JOIN on team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id = team.team_id")
    

    # Assigns results from query to players list
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --") #Code Borrowed from Solution for styling

    #Loop through players list and display results
    for player in players: 
        print("Player ID:\t{}".format(player[0]))
        print("First Name:\t{}".format(player[1]))
        print("Last Name:\t{}".format(player[2]))
        print("Team Name:\t{}\n".format(player[3]))

    #Update the newly added player record in the player table
    cursor.execute("UPDATE player " +
    "SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' " +
    "WHERE first_name = 'Smeagol'")

    #SELECT query from player table with an INNER JOIN on team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id = team.team_id")
    

    # Assigns results from query to players list
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --") #Code Borrowed from Solution for styling

    #Loop through players list and display results
    for player in players: 
        print("Player ID:\t{}".format(player[0]))
        print("First Name:\t{}".format(player[1]))
        print("Last Name:\t{}".format(player[2]))
        print("Team Name:\t{}\n".format(player[3]))

    #Delete the newly added/updated player record in the player table
    cursor.execute("DELETE FROM player " +
    "WHERE first_name = 'Gollum'")

    #SELECT query from player table with an INNER JOIN on team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id = team.team_id")
    

    # Assigns results from query to players list
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --") #Code Borrowed from Solution for styling

    #Loop through players list and display results
    for player in players: 
        print("Player ID:\t{}".format(player[0]))
        print("First Name:\t{}".format(player[1]))
        print("Last Name:\t{}".format(player[2]))
        print("Team Name:\t{}\n".format(player[3]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()