"""Import flask modules"""
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import datetime
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)
from app.models import *


app = Flask(__name__)
api = Api(app)
app .config['JWT_SECRET_KEY'] = '5c750c0e72ce5394dfe7720fa26d0327d616ff9ff869be19'
jwt = JWTManager(app)

class EntryList(Resource):
    def get(self):
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
        title = request.get_json()['title']
        content = request.get_json()['content']

        try:
            cur.execute("INSERT INTO entries (title, content) VALUES('"+title+"', '"+content+"');")
            return jsonify({'message': 'Not successfully try again!'})
        
        except:
            return jsonify({'message': 'Not successfully try again!'})
        
        finally:
            conn.commit()
        return jsonify({'message': 'Not successfully try again!'})


class Entry(Resource):
    def get(self, id):
        cur.execute("SELECT * FROM entries WHERE ID = %s", (id,))
        rows = cur.fetchall()
        output = {}
        for row in rows:
            output.update({row[0]: row[1]})        
        return jsonify(output)
    
    def put(self, id):
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
                return jsonify({'message': 'not success try again'})
        else:
            return jsonify({'message': 'Not complete no entry'})
        conn.commit()
        return jsonify({'message': 'Entry successfully updated'})
 
    
    def delete(self, id):
        try:
            cur.execute("DELETE FROM entries WHERE ID = %s", (id,))
            conn.commit()
        except:
            return jsonify({'message':'Cant retrieve entry'})
        
        finally:
            conn.close()
        return jsonify({'message': 'successfully deleted'})


class UserRegistration(Resource):
    def post(self):
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



class UserLogin(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        cur.execute("SELECT * FROM users WHERE username LIKE '"+username+"'\
         AND password LIKE '"+password+"'")
        rows = cur.fetchone()
        if rows is None:
            return jsonify({'message': 'Not successful  you can try again'})
        else:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        conn.commit()


api.add_resource(UserRegistration, '/api/v1/auth/register')
api.add_resource(UserLogin, '/api/v1/auth/login')
api.add_resource(EntryList, '/api/v1/entries', endpoint = 'entries')
api.add_resource(Entry, '/api/v1/entries/<int:id>', endpoint = 'entry')

if __name__ == '__main__':
    app.run(debug=True)
