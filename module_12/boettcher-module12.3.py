#Josh Boettcher
#12/17/2021
#Module 12.3
#used Professor Krasso's code as source in some areas

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#show_menu method
def show_menu():
    #print menu options
    print("---------\nMAIN MENU\n---------\n(1) View Books\n(2) View Store Locations\n(3) My Account")
    #input for user selection
    main_menu_selection = str(input("\nEnter 1 to view books, 2 to view store locations, 3 to access your account, or q to quit:  "))
    if main_menu_selection == "q":
        sys.exit(0)
    else:
        return main_menu_selection

#show_books method
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    #return results from cursor 
    available_books = _cursor.fetchall()
    print("\n---------------\nAVAILABLE BOOKS\n---------------")
    #iterate through and print all available books
    for book in available_books:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

#show_locations method
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    #return results from cursor
    stores = _cursor.fetchall()
    print("\n-----------------------\nCURRENT STORE LOCATIONS\n-----------------------")
    #print all stores in database
    for store in stores:
        print("Location: {}\n".format(store[1]))

#validate_user method
def validate_user():
    while True:
        #input for user id
        user_id = int(input("\nEnter your user ID number:  "))
        if user_id == 1 or user_id == 2 or user_id == 3:
            return user_id
        else:
            print("\n***You have made an invalid selection.  Please try again.")

#show_account_menu method
def show_account_menu():
    print("\n------------\nACCOUNT MENU\n------------")
    print("(1) Wishlist\n(2) Add Book\n(3) Main Menu")
    #input for selection
    while True:
        account_menu_selection = str(input("\nEnter 1 to view your wishlist, 2 to add a book to your wishlist, or 3 to return to the main menu:  "))
        if account_menu_selection == "1" or account_menu_selection == "2" or account_menu_selection == "3":
            return account_menu_selection
        else:
            print("\n***You have made an invalid selection.  Please try again.")

#show_wishlist method
def show_wishlist(_cursor, _user_id):
    #query to find books in wishlist by user id
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    #return results from cursor
    wishlist = _cursor.fetchall()
    print("\n----------------------\nBOOKS IN YOUR WISHLIST\n----------------------")
    #iterate through and print books in wishlist
    for book in wishlist:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[3], book[4], book[5], book[6]))

#show_books_to_add method
def show_books_to_add(_cursor, _user_id):
    #query that shows books not in users wishlist
    not_in_wishlist = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(not_in_wishlist)
    #return results from cursor
    available_books = _cursor.fetchall()
    print("\n----------------------------------\nBOOKS AVAILABLE TO ADD TO WISHLIST\n----------------------------------")
    #iterate through and print all available books
    for book in available_books:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

#add_book_to_wishlist method
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    #connect to the WhatABook database 
    db = mysql.connector.connect(**config) 

    #cursor for MySQL queries
    cursor = db.cursor()

    #display main menu
    
    display_main_menu = show_menu()
    #While loop that displays main menu until the user enters q to quit
    while display_main_menu != "q":
        #call show books method if option 1 selected
        if display_main_menu == "1":
            show_books(cursor)
        #call show locations method if option 2 selected
        if display_main_menu == "2":
            show_locations(cursor)
        #call validate_user and show_account_menu methods if option 3 is selected
        if display_main_menu == "3":
            user_id= validate_user()
            account_menu_selection = show_account_menu()

            #while user is on account menu
            while account_menu_selection != "3":

                #call show_wishlist method is option 1 is selected
                if account_menu_selection == "1":
                    show_wishlist(cursor, user_id)

                #call show_books_to_add method is option 2 is selected
                if account_menu_selection == "2":
                    show_books_to_add(cursor, user_id)
                    #add book to wishlist
                    book_id = int(input("Enter the ID number of the book to add your wishlist:  "))
                    add_book_to_wishlist(cursor, user_id, book_id)
                    db.commit()
                    print("\nID number {} was added to your wishlist.".format(book_id))

                #return to account menu
                account_menu_selection = show_account_menu()
     
        #return to main menu
        display_main_menu = show_menu()

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





