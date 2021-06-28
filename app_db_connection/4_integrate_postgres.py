#postgres is a client\server set-up so had install a docker container running postgres:
#had to install a python virtual enn and install psycopg2-binary:
#   - p -m venv postgres
#   - postgres/bin/pip install --upgrade pip
#   - postgres/bin/pip install psycopg2-binary
#1. docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
#2. docker exec -it docker-pg psql -U postgres -c "create database udemy"
#3. \l - list DBs
# To connect to the DBs use '\c db_name' then list tables with '\d'.


import psycopg2

def create_db():
    connect_to_db=psycopg2.connect("dbname='udemy' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS dantest(item TEXT, quantity INTEGER, price REAL)")
    connect_to_db.commit()
    connect_to_db.close()

def add_data(item,quantity,price):
    connect_to_db=psycopg2.connect("dbname='udemy' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    #The line below uses %s,%s,%s as variable placeholders as best practice to avoid SQL injenctions from hackers
    cursor_object.execute("INSERT INTO dantest VALUES(%s,%s,%s)",(item,quantity,price))
    connect_to_db.commit()
    connect_to_db.close()

def read_data():
    connect_to_db=psycopg2.connect("dbname='udemy' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM dantest")
    all_data=cursor_object.fetchall()
    connect_to_db.close()
    return all_data

def delete_data(item):
    connect_to_db=psycopg2.connect("dbname='udemy' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    #watch out for the trailing comma after item.  That is required when only 1 variable is passed
    cursor_object.execute("DELETE FROM dantest WHERE item=%s",(item,))
    connect_to_db.commit()
    connect_to_db.close()

def update_data(item,quantity, price):
    connect_to_db=psycopg2.connect("dbname='udemy' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    #in this case we dont need a trailing comma after the variable passed in the parenthesis
    cursor_object.execute("UPDATE dantest SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    connect_to_db.commit()
    connect_to_db.close()

update_data('george',9999,9999)
print(read_data())
