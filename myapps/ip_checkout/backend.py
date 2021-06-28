import psycopg2

def create_db():
    connect_to_db=psycopg2.connect("dbname='ipaddress' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS ips(ip NUMERIC, hostname VARCHAR (50) UNIQUE NOT NULL)")
    connect_to_db.commit()
    connect_to_db.close()

def add_data(ip,hostname):
    connect_to_db=psycopg2.connect("dbname='ipaddress' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    #The line below uses %s,%s,%s as variable placeholders as best practice to avoid SQL injenctions from hackers
    cursor_object.execute("INSERT INTO ips VALUES(%s,%s)",(ip,hostname))
    connect_to_db.commit()
    connect_to_db.close()

def read_data():
    connect_to_db=psycopg2.connect("dbname='ipaddress' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    cursor_object.execute("SELECT * FROM ips")
    all_data=cursor_object.fetchall()
    connect_to_db.close()
    return all_data

def delete_data(ip):
    connect_to_db=psycopg2.connect("dbname='ipaddress' user='postgres' host='localhost' password='docker' port=5432")
    cursor_object=connect_to_db.cursor()
    #watch out for the trailing comma after item.  That is required when only 1 variable is passed
    cursor_object.execute("DELETE FROM ips WHERE ip=%s",(ip,))
    connect_to_db.commit()
    connect_to_db.close()

create_db()
