
import sqlite3

def create_db():
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS dantest(item TEXT, quantity INTEGER, price REAL)")
    connect_to_db.commit()
    connect_to_db.close()

def add_data(item,quantity,price):
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    #The line below uses ?,?,? as variable placeholders as best practice to avoid SQL injenctions from hackers
    cursor_object.execute("INSERT INTO dantest VALUES(?,?,?)",(item,quantity,price))
    connect_to_db.commit()
    connect_to_db.close()

add_data('Rory',123455,11111)

#To read the data we use the fetchall() function and assign it to a variable and then return the variable from the function
def read_data():
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM dantest")
    all_data=cursor_object.fetchall()
    connect_to_db.close()
    return all_data

print(read_data())
