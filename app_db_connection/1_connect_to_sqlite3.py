#sqlite3 is the library used by python to interact with sqlite dbs.  Essentially what happens is that python acts as a wrapper to the sql commands that you can run wthin the script.
#To connect to a db via python you need to carry out the following 5 steps:
#   1. Connect to the DB
#   2. Create a cursor object
#   3. Write SQL query
#   4. Commit the changes
#   5. Close the database connection

import sqlite3

# 1. Connect to the DB - the connect() function will connect to the DB and if not there it will create the file as sqlite is a portable db that stores data in a file.
connect_to_db=sqlite3.connect("sqlite3_1.db")

# 2. Create a cursor object via the cursor() function.
cursor_object=connect_to_db.cursor()

# 3. Write SQL query - this is the SQL code passed as string via the execute() function.  This is pointed to the cursor object created in step 2.
cursor_object.execute("CREATE TABLE IF NOT EXISTS dantest(item TEXT, quantity INTEGER, price REAL)")

# 4. Commit the changes - this done via the commit() function against the connection created in step 1
connect_to_db.commit()

# 5. Close the database connection - via the close() function against the connection
connect_to_db.close()

# To add data into our DB we would follow the same approach - as you can see the same logic is applied with just the SQL code changing to INSERT data instead of creating a table.  Moving forward we want to wrap all these steps into functions so we avoid code repetion and incorrect entries.
connect_to_db=sqlite3.connect("sqlite3_1.db")
cursor_object=connect_to_db.cursor()
cursor_object.execute("INSERT INTO dantest VALUES('Dan', 39, 23031980)")
connect_to_db.commit()
connect_to_db.close()
