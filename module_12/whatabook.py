'''
James Smith
CSD 310
Module 11.2
5/4/21
'''

import tkinter
from tkinter import *
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

root = Tk()

def center_window(main):

    main.title("WhatABook Application")
    main.update_idletasks()
    width = 400
    height = 400
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def enable_button(key):
    validate_user_btn['state'] = NORMAL

def show_menu(frame):
    frame.tkraise()

def show_books(_cursor):
    #SELECT query from book table
    _cursor.execute("SELECT * FROM book")
        

    # Assigns results from query to books list
    books = _cursor.fetchall()
    print("\n  -- DISPLAYING ALL BOOKS --")
    for book in books:
        print("Book ID:\t{}\nBook Name:\t{}\nAuthor:\t\t{}\nDetails:\t{}\n".format(book[0],book[1],book[2],book[3]))

def show_locations(_cursor):
    #SELECT query from store table
    _cursor.execute("SELECT * FROM store")
        

    # Assigns results from query to books list
    stores = _cursor.fetchall()
    print("\n  -- DISPLAYING ALL STORE LOCATIONS --")
    for store in stores:
        print("Store ID:\t{}\nAddress:\t{}".format(store[0],store[1]))

def validate_user(_cursor):
    global user_id
    text = user_entry.get()
    user_entry.delete(0, END)
    validate_user_btn['state'] = DISABLED

    try:
        int(text)
        #SELECT query from user table with user input as the WHERE criteria
        _cursor.execute("SELECT user_id, first_name, last_name " + 
        "FROM user " +
        "WHERE user_id = {}".format(text))
        

        # Assigns results from query to users list
        users = _cursor.fetchall()
        if(len(users) == 0):
            print("A user with {} as the ID does not exist. Please try again (Hint: 1, 2, or 3).".format(text))
        else:
            user_id = text
            print("Welcome to the WhatABook App, {} {}".format(users[0][1],users[0][2]))
            show_menu(account_menu)

    except:
        print("Invalid Entry. Please enter an integer value.")

def show_wishlist(_cursor, _user_id):
    #SELECT query from wishlist table
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, " +
    "book.book_id, book.book_name, book.author " +
    "FROM wishlist " +
    "INNER JOIN user ON wishlist.user_id = user.user_id " +
    "INNER JOIN book ON wishlist.book_id = book.book_id " +
    "WHERE user.user_id = {};".format(_user_id))
        

    # Assigns results from query to wishes list
    wishes = _cursor.fetchall()
    print("\n  -- DISPLAYING WISHLIST FOR {} {} --".format(wishes[0][1], wishes[0][2]))
    for wish in wishes:
        print("User ID:\t{}\nFirst Name:\t{}\nLast Name:\t{}\n".format(wish[0],wish[1],wish[2]) +
        "Book ID:\t{}\nBook Name:\t{}\nAuthor\t\t{}".format(wish[3],wish[4],wish[5]))



#-------------------------------------------------Main Code-------------------------------------------------
try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the whatbook database 
    user_id = 0
    book_id = 0
    cursor = db.cursor()
    center_window(root)

    #Establish different frames for navigation purposes
    main_menu = Frame(root)
    validate_account = Frame(root)
    account_menu = Frame(root)

    #Place all frames in tkinter window
    for menu in (main_menu, validate_account, account_menu):
        menu.grid(row=0,column=0,sticky='nsew')

    #Display Main Menu
    show_menu(main_menu)

    #=========================================Main Menu Code
    main_menu_title = Label(main_menu, text='Main Menu')
    main_menu_title.pack(fill='x')
    show_books_btn = Button(main_menu, text="Show Books", command=lambda:show_books(cursor))
    show_stores_btn = Button(main_menu, text="Show Locations", command=lambda:show_locations(cursor))
    my_account_btn = Button(main_menu, text="My Account", command=lambda:show_menu(validate_account))
    show_books_btn.pack()
    show_stores_btn.pack()
    my_account_btn.pack()

    #=========================================User Validation Menu Code
    validation_text = Label(validate_account, text='Enter a user ID:')
    validation_text.pack(fill='x')
    user_entry = Entry(validate_account, width=20)
    user_entry.pack()
    user_entry.bind("<Key>", enable_button)
    validate_user_btn = Button(validate_account, text="Validate", state = DISABLED, command=lambda: validate_user(cursor))
    validate_user_btn.pack()

    #=========================================Account Menu Code
    account_menu_title = Label(account_menu, text='Account Menu')
    account_menu_title.pack(fill='x')
    show_wishlist_btn = Button(account_menu, text="Show Wishlist", command=lambda:show_wishlist(cursor,user_id))
    show_wishlist_btn.pack()
    show_books_to_add_btn = Button(account_menu, text="Show Books to Add")
    show_books_to_add_btn.pack()
    main_menu_btn = Button(account_menu, text="Main Menu", command=lambda:show_menu(main_menu))
    main_menu_btn.pack()
    prompt_text = Label(account_menu, text='Enter a book ID:')
    prompt_text.pack(fill='x')
    book_entry = Entry(account_menu, width=20)
    book_entry.pack()
    add_book_btn = Button(account_menu, text="Add Book", state = DISABLED)
    add_book_btn.pack()
    root.mainloop()

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

