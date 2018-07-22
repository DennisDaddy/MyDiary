"""Import flask modules"""
from flask import Flask, jsonify, json, request
import psycopg2
import datetime


app = Flask(__name__)

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
conn.commit()

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to MyDiary'})

@app.route('/diary/api/v1/entries', methods=['POST'])
def create_entry():
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
    title = request.get_json()['title']
    content = request.get_json()['content']    

    try:
        cur.execute("INSERT INTO entries (title, content) VALUES('"+title+"', '"+content+"');")
        
    except:
        return jsonify({'message': 'Not successfully try again!'})
    
    finally:
        conn.commit()
        conn.close()

    return jsonify({'message': 'Entry successfully created!'})




if __name__ == '__main__':
    app.run(debug=True)
