#Josh Boettcher
#11/26/2021
#Module 8.3

#import
import mysql.connector
from mysql.connector import errorcode


#Database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Connection test code
try:
    db = mysql.connector.connect(**config) 

    #declare cursor as object
    cursor = db.cursor()

    # output the connection status 
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #This is a query to select data from the team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team") 
    
    #return results from cursor object
    teams = cursor.fetchall()

    #iterate through teams and print results
    print("\n--DISPLAYING TEAM RECORDS--\n")
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    #This is a query to select data from the players table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #return results from cursor object
    players = cursor.fetchall()

    #iterate through players and print results
    print("--DISPLAYING PLAYER RECORDS--\n")
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
finally:
    db.close()
