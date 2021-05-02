'''
James Smith
CSD 310
Module 9.2
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


    #SELECT query from player table with an INNER JOIN on team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id = team.team_id")
    

    # Assigns results from query to players list
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS --") #Code Borrow from Solution for styling

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