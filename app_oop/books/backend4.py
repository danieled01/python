#We know this app works by using funtions so now we will transform the back-end into a class and see if it still works.

import sqlite3

class Database:
#when designing a class you first need to pick the objetc that you want to run the class against.  In our case this is the database.  You also need to specify a method that will initiate the class when its called which is what the __init__ function does - everytime you call the class this function is automatically called but not the other ones, those only get executed when specifically called.
    def __init__(self, db):
#The __init__ function always decalres the (self) parameter as when you map an object to the class the object is passed to the init function, if the __init__ function is left with no parameters such as __init__() then you will get an error when calling it.  You can also pass other parameters to the __init__ funtion which can be declared when mapping the class to the object.

#the class can now be re-worked and remove duplicate lines which are being called in each function - for example we don't need to open and close the connection in each method instead we can just open the connection everytime the class is called and the __init__function runs and leave the connection open until the class is no longer needed.
#Also as we are removing lines of code we are now passing variables between methods defined in the class, the way to reference these variables between methods is by declaring self. before them.
        self.connect_to_db=sqlite3.connect(db)
        self.cursor_object=self.connect_to_db.cursor()
        self.cursor_object.execute("CREATE TABLE IF NOT EXISTS books_stored (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connect_to_db.commit()

    def add_data(self,title,author,year,isbn):
        self.cursor_object.execute("INSERT INTO books_stored VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.connect_to_db.commit()

# as we have seen for our __init__ function when the class is called by an object the object itself is passed as an hidden parameter, therefore we need to use self as a parameter for functions within the class.  In fact this will need to be passed as a parameter to all the functions within the class.
    def read_data(self):
        self.cursor_object.execute("SELECT * FROM books_stored")
        all_data=self.cursor_object.fetchall()
        return all_data

    def search_data(self,title="",author="",year="",isbn=""):
        self.cursor_object.execute("SELECT * FROM books_stored WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        search_data=self.cursor_object.fetchall()
        return search_data

    def delete_data(self,id):
        self.cursor_object.execute("DELETE FROM books_stored WHERE id=?",(id,))
        self.connect_to_db.commit()

    def update_data(self,id,title,author,year,isbn):
        self.cursor_object.execute("UPDATE books_stored SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.connect_to_db.commit()

#In order to close our connection now we use a __del__ function which destroys our object mapped to the class whenevr the script stops running
    def __del__(self):
        self.connect_to_db.close()
