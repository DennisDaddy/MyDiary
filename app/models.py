"""Import flask modules"""
import psycopg2

#Connect using psycopg
conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
#Activate connection cursor
cur = conn.cursor()

# Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS entries(
    id serial PRIMARY KEY,
    title varchar (50) NOT NULL,
    content varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp 
);''')


cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    username varchar (50) NOT NULL,
    email varchar (100) NOT NULL,
    password varchar (100) NOT NULL,
    password_confirmation varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp 
);''')
conn.commit()
