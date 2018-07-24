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


cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    username varchar (50) NOT NULL,
    email varchar (100) NOT NULL,
    password varchar (100) NOT NULL,
    password_confirmation varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp 
);''')


conn.commit()

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to MyDiary'})
@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    password_confirmation = request.get_json()['password_confirmation']

    try:
        cur.execute("INSERT INTO users (username, email, password, password_confirmation) VALUES('"+username+"', '"+email+"', '"+password+"', '"+password_confirmation+"');")
    except:
        return jsonify({'message': 'Try again'})
    finally:
        conn.commit()
    return jsonify({'message': 'successfully created'})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
    username = request.get_json()['username']
    password = request.get_json()['password']
    user_info = []
    
    try:
        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"' AND password LIKE '"+password+"'")
        rows = cur.fetchall()
        for row in rows:
            user_info.append(row[0])
            user_info.append(row[1])
            
    except:
        return jsonify({'message': 'Try again'})
    finally:
        conn.commit()
        return jsonify(user_info)
   


@app.route('/api/v1/entries', methods=['POST'])
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

    return jsonify({'message': 'Entry successfully created!'})

@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():    
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
    my_list = []
    try:
        cur.execute("SELECT * from entries")
        rows = cur.fetchall()        
        for row in rows:
            my_list.append(row[0])
            my_list.append(row[1])
            my_list.append(row[2])
            
    except:
        return jsonify({'message':'Cant retrieve entries'})
    
    finally:
         conn.close()
    return jsonify(my_list)

@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def view_entry(entry_id):
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
   
    try:
        
        cur.execute("SELECT * FROM entries WHERE ID = %s", (entry_id,))
        rows = cur.fetchall()
        for row in rows:
            return jsonify({row[0]: row[1]})
           
                  
            
    except:
        return jsonify({'message':'Cant retrieve entries'})
    
    finally:
         conn.close()


@app.route('/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    cur = conn.cursor()
    
    try:       
       
        cur.execute("DELETE FROM entries WHERE ID = %s", (entry_id,))
        conn.commit()
       
       
    except:
        return jsonify({'message':'Cant retrieve entry'})
    
    finally:        
        conn.close()
        return jsonify({'message': 'successfully deleted'})
         
       



if __name__ == '__main__':
    app.run(debug=True)
