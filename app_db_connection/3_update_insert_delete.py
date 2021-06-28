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

def read_data():
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM dantest")
    all_data=cursor_object.fetchall()
    connect_to_db.close()
    return all_data

def delete_data(item):
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    #watch out for the trailing comma after item.  That is required when only 1 variable is passed
    cursor_object.execute("DELETE FROM dantest WHERE item=?",(item,))
    connect_to_db.commit()
    connect_to_db.close()

def update_data(item,quantity, price):
    connect_to_db=sqlite3.connect("sqlite3_1.db")
    cursor_object=connect_to_db.cursor()
    #in this case we dont need a trailing comma after the variable passed in the parenthesis
    cursor_object.execute("UPDATE dantest SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    connect_to_db.commit()
    connect_to_db.close()

print(read_data())
update_data('Dan',99999,99999)
print(read_data())
