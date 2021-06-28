#as we are treating this app as a frntend and backend its a sensible approach to define the functions for our buttons here and then import this script into frontend.py and map the functions to the command= for each button.

import sqlite3

#as we import this script into frontend.py we state that everytime we run the frontend.py script the create_db() function gets executed so if a db isnt present it will be created.
def create_db():
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS books_stored (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connect_to_db.commit()
    connect_to_db.close()

def add_data(title,author,year,isbn):
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    #The line below uses ?,?,? as variable placeholders as best practice to avoid SQL injenctions from hackers.  Also for the first value we pass NULL as that is already set as a self incrementing value.
    cursor_object.execute("INSERT INTO books_stored VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    connect_to_db.commit()
    connect_to_db.close()

def read_data():
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM books_stored")
    all_data=cursor_object.fetchall()
    connect_to_db.close()
    return all_data
#    print(all_data[-1])

#The search function steated below will allow a user to search through the DB by using just 1 field.  We pass default empty strings in case the user only has one field that they want to search on.
def search_data(title="",author="",year="",isbn=""):
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM books_stored WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    search_data=cursor_object.fetchall()
    connect_to_db.close()
    return search_data

#the delete funtion will take the id as the unique identifier to chose what item to delete.  This means that if we have 2 items with the same name than they will not be deleted - unlike our app_tkinter example.
def delete_data(id):
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    #watch out for the trailing comma after item.  That is required when only 1 variable is passed
    cursor_object.execute("DELETE FROM books_stored WHERE id=?",(id,))
    connect_to_db.commit()
    connect_to_db.close()

#Update data funtion will work similarly to delete where we point it to the id of the item we wish to update.
def update_data(id,title,author,year,isbn):
    connect_to_db=sqlite3.connect("books.db")
    cursor_object=connect_to_db.cursor()
    #in this case we dont need a trailing comma after the variable passed in the parenthesis
    cursor_object.execute("UPDATE books_stored SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    connect_to_db.commit()
    connect_to_db.close()

#add_data("boom","rory",1267,353453534)
#delete_data(6)
read_data()
create_db()
