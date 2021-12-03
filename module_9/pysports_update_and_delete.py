#Josh Boettcher
#12/2/2021
#Module 9.3
#used Professor Krasso's code for source

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

    # insert query 
    insert_query = """INSERT INTO player(first_name, last_name, team_id)
                        VALUES
                        ("Smeagol", "Shire Folk", 1)"""

    #declare cursor as object
    cursor = db.cursor()

    # insert a new player record
    cursor.execute(insert_query)

    # commit the insert to the database 
    db.commit()

   #create variable for query
    query = "SELECT player_id, first_name, last_name, team_name\
             FROM player\
             INNER JOIN team\
                  ON player.team_id = team.team_id"

    #execute query
    cursor.execute(query) 
    
    #return results from cursor object
    results = cursor.fetchall()

    #print results
    print("\n--DISPLAYING PLAYERS AFTER INSERT--")
    for result in results:
        print("Player ID: {}".format(result[0]))
        print("First Name: {}".format(result[1]))
        print("Last Name: {}".format(result[2]))
        print("Team Name: {}\n".format(result[3]))

    #query to update player
    update_query = """UPDATE player\
                      SET team_id = 2,\
                        first_name = 'Gollum',\
                        last_name = 'Ring Stealer'\
                      WHERE first_name = 'Smeagol'"""

    # execute the update query
    cursor.execute(update_query)

   #create variable for query
    query = "SELECT player_id, first_name, last_name, team_name\
             FROM player\
             INNER JOIN team\
                  ON player.team_id = team.team_id"

    #execute query
    cursor.execute(query) 
    
    #return results from cursor object
    results = cursor.fetchall()

    #print results
    print("\n--DISPLAYING PLAYERS AFTER UPDATE--")
    for result in results:
        print("Player ID: {}".format(result[0]))
        print("First Name: {}".format(result[1]))
        print("Last Name: {}".format(result[2]))
        print("Team Name: {}\n".format(result[3]))


    #query to delete query 
    delete_query = """DELETE FROM player\
                      WHERE first_name = 'Gollum'"""

    #execute query
    cursor.execute(delete_query)

   #create variable for query
    query = "SELECT player_id, first_name, last_name, team_name\
             FROM player\
             INNER JOIN team\
                  ON player.team_id = team.team_id"

    #execute query
    cursor.execute(query) 
    
    #return results from cursor object
    results = cursor.fetchall()

    #print results
    print("\n--DISPLAYING PLAYERS AFTER DELETE--")
    for result in results:
        print("Player ID: {}".format(result[0]))
        print("First Name: {}".format(result[1]))
        print("Last Name: {}".format(result[2]))
        print("Team Name: {}\n".format(result[3]))

    input("\n\nPress any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()