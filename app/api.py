"""Import flask modules"""
import datetime
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
#from flask_jwt_extended import (
 #   JWTManager, jwt_required, create_access_token
#)
from app.models import *


app = Flask(__name__)
api = Api(app)
app .config['JWT_SECRET_KEY'] = '5c750c0e72ce5394dfe7720fa26d0327d616ff9ff869be19'
#jwt = JWTManager(app)

class Home(Resource):
    """This is a class for root endpoint"""
    def get(self):
        """This is am method for getting root endpoint using GET request""" 
        return jsonify({'message': 'Welcome to MyDiary'})

class EntryList(Resource):
    """This is a class for entries endpoints without IDs"""
    def get(self):
        """This is a method for retrieving entries using GET request"""
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

    def post(self):
        """This is a method for creating an entry using POST request"""
        title = request.get_json()['title']
        content = request.get_json()['content']

        if len(title) ==0:
            return jsonify({'message': 'Fill in the title'})

        if len(content) ==0:
            return jsonify({'message': 'Fill in the content'})

        cur.execute("INSERT INTO entries (title, content) VALUES('"+title+"', '"+content+"');")
        conn.commit()
        return jsonify({'message': 'Entry successfully created!'})


class Entry(Resource):
    """This is a class for getting  entries with their IDs"""

    def get(self, id):
        """ This is a method for retreiving an entry using GET request"""

        cur.execute("SELECT * FROM entries WHERE ID = %s", (id,))
        result = cur.fetchone()
        if result is None:
            return jsonify({'message': 'Entry not found!'})
        return jsonify(result)

    def put(self, id):
        """This is a method for modifying an entry using PUT request"""
        cur.execute("SELECT * FROM entries WHERE ID = %s", (id,))
        entry = cur.fetchone()
        title = request.get_json()['title']
        content = request.get_json()['content']
        today = str(datetime.datetime.today()).split()

        if entry is not None:
            if str(entry[3]).split()[0] == today[0]:
                cur.execute("UPDATE entries SET title=%s, content=%s WHERE id=%s",\
                (title, content, id))
            else:
                return jsonify({'message': 'You can only modify an entry the it was created'})
        else:
            return jsonify({'message': 'Not complete no entry'})
        conn.commit()
        return jsonify({'message': 'Entry successfully updated'})

    def delete(self, id):
        """This is a method for deleting an entry using DELETE request"""
        try:
            cur.execute("DELETE FROM entries WHERE ID = %s", (id,))
            conn.commit()
        except:
            return jsonify({'message':'Cant retrieve entry'})

        finally:
            conn.close()
        return jsonify({'message': 'successfully deleted'})


class UserRegistration(Resource):
    """This is a class for registering a user using POST request"""
    def post(self):
        """This is a method for registering a user using POST request"""
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        password_confirmation = request.get_json()['password_confirmation']

        if username is None:
            return jsonify({'message': 'Fill in username'})
        if email is None:
            return jsonify({'message': 'Fill in email'})
        if password is None:
            return jsonify({'message': 'Fill in password'})
        if password != password_confirmation:
            return jsonify({'message': 'Password should match'})
        if len(password) < 6:
            return jsonify({'message': 'Password should more than 6 characters'})
        
        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'")
        user = cur.fetchone()
        if user is None:
            cur.execute("INSERT INTO users (username, email, password, password_confirmation)\
            VALUES('"+username+"', '"+email+"', '"+password+"', '"+password_confirmation+"');")
        else:
            return jsonify({'message': 'user already exists'})             
        conn.commit()
        return jsonify({'message': 'You are successfully registered!'})


class UserLogin(Resource):
    """This is a class for logging user in """

    def post(self):
        """ This is a method for logging user using POST request"""
        username = request.get_json()['username']
        password = request.get_json()['password']

        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'\
         AND password LIKE '"+password+"'")
        rows = cur.fetchone()
        if rows is None:
            return jsonify({'message': 'Not successful  you can try again'})

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    conn.commit()

class UserInfo(Resource):
    """This is a class for retrieveing user information from the database"""

    def get(self, user_id):
        """This is a method for retrieving user information using GET request"""
        cur.execute("SELECT * FROM users WHERE ID = %s", (user_id,))
        info = cur.fetchone()
        if info is None:
            return jsonify({'message': 'That user is not available'})
        return jsonify(info)

api.add_resource(Home, '/')
api.add_resource(UserRegistration, '/api/v1/auth/register')
api.add_resource(UserLogin, '/api/v1/auth/login')
api.add_resource(UserInfo, '/api/v1/users/<int:user_id>')
api.add_resource(EntryList, '/api/v1/entries', endpoint='entries')
api.add_resource(Entry, '/api/v1/entries/<int:id>', endpoint='entry')

if __name__ == '__main__':
    app.run(debug=True)
