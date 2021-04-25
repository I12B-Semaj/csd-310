'''
James Smith
CSD 310
Module 8.3
4/25/21
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
    #SELECT query from team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Assigns results from query to teams list
    teams = cursor.fetchall()
    print("\n  -- DISPLAYING TEAM RECORDS --") #Code Borrow from Solution for styling

    #Loop through teams list and display results
    for team in teams: 
        print("Team ID:\t{}".format(team[0]))
        print("Team Name:\t{}".format(team[1]))
        print("Mascot:\t\t{}\n".format(team[2]))

    #SELECT query from player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Assigns results from query to players list
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS --") #Code Borrow from Solution for styling

    #Loop through players list and display results
    for player in players: 
        print("Player ID:\t{}".format(player[0]))
        print("First Name:\t{}".format(player[1]))
        print("Last Name:\t{}".format(player[2]))
        print("Team ID:\t{}\n".format(player[3]))

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