#Josh Boettcher
#12/2/2021
#Module 9.2
#used Professor Krasso's code for source on connections and error handling

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

    #create variable fo query
    query = "SELECT player_id, first_name, last_name, team_name\
             FROM player\
             INNER JOIN team\
                  ON player.team_id = team.team_id"

    #execute query
    cursor.execute(query) 
    
    #return results from cursor object
    results = cursor.fetchall()

    #print results
    print("\n--DISPLAYING TEAM RECORDS--")
    for result in results:
        print("Player ID: {}".format(result[0]))
        print("First Name: {}".format(result[1]))
        print("Last Name: {}".format(result[2]))
        print("Team Name: {}\n".format(result[3]))

    input("\nPress any key to continue...")

#error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#close db
finally:
    db.close()