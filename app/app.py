"""Import flask modules"""
from flask import Flask, jsonify, request
import psycopg2
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)


app = Flask(__name__)
app .config['JWT_SECRET_KEY'] = '5c750c0e72ce5394dfe7720fa26d0327d616ff9ff869be19'
jwt = JWTManager(app)

from app.models import *


@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """This is a function for registering a user"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    password_confirmation = request.get_json()['password_confirmation']

    try:
        cur.execute("INSERT INTO users (username, email, password, password_confirmation)\
        VALUES('"+username+"', '"+email+"', '"+password+"', '"+password_confirmation+"');")
    except:
        return jsonify({'message': 'Try again'})
    finally:
        conn.commit()
    return jsonify({'message': 'You are successfully registered!'})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """This is a function for user login"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()
    username = request.get_json()['username']
    password = request.get_json()['password']
    #user_info = []

    
    cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'\
         AND password LIKE '"+password+"'")
    rows = cur.fetchone()
    if rows is None:
        return jsonify({'message': 'Not successful  you can try again'})
    else:
        access_token = create_access_token(identity=username) 
        #return jsonify({'message': 'LOGIN'})
        return jsonify(access_token=access_token)
    conn.commit()
        
 


@app.route('/api/v1/entries', methods=['POST'])
@jwt_required
def create_entry():
    """This is a fuction for creating an entry"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()
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
@jwt_required
def get_all_entries():
    """This is a function for getting all entries"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()
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

@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
@jwt_required

def modify_entry(entry_id):
    """This is a function for viewing single entry"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()
    title = request.get_json()['title']
    content = request.get_json()['content']
    cur.execute("SELECT * FROM entries WHERE ID = %s", (entry_id,))

    try:
        cur.execute("UPDATE entries SET title=%s, content=%s WHERE id=%s",\
         (title, content, entry_id))
        conn.commit()
        return jsonify({'message': 'Entry successfully updated'})

    except:
        return jsonify({'message': 'Not  updated'})
    conn.close()



@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def view_entry(entry_id):
    """This is a function for viewing single entry"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()

    cur.execute("SELECT * FROM entries WHERE ID = %s", (entry_id,))
    rows = cur.fetchall()
    output = {}
    for row in rows:
        output.update({row[0]: row[1]})
    conn.close()
    return jsonify(output)


@app.route('/api/v1/entries/<int:entry_id>', methods=['DELETE'])
@jwt_required
def delete_entry(entry_id):
    """This is a function for deleting an entry"""
    #conn = psycopg2.connect("dbname=diary user=postgres password=123456 host=localhost")
    #cur = conn.cursor()

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
