"""Import python modules"""
from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x996\no\xa52\x19Fp\x9c\x97\xf6\x9fz\x08\x0b\x80l\xde\xf8\xd7\xc1\t\x03'

entries = [{'id' : 1, 'title' : u'this is one', 'content' : u'this is content'},
           {'id' : 2, 'title' : u'this is two', 'content' : u'this is content'}]
user_info = {}


@app.route('/', methods=['GET'])
def index():
    """This is a function for root endpoint"""
    return jsonify({'message': 'Welcome to mydiary'})

@app.route('/diary/api/v1/auth/register', methods=['POST'])
def register():
    """This is a function for registering a user"""
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    password_confirmation = request.get_json()["password_confirmation"]


    if username in user_info:
        return jsonify({'message': 'username already exists'})

    user_info.update({username:{"email": email, "password": password,
                                "password_confirmation" : password_confirmation}})
    return jsonify({'message': "You are successfully registered"})
@app.route('/diary/api/v1/auth/login', methods=['POST'])
def login():
    """This is a method for logging in a user"""
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    if username in user_info:
        if password == user_info[username]["password"]:
            session['logged_in'] = True
            return jsonify({"message": "You are logged in now"})
    return jsonify({"message": "You are not a registered user"})

@app.route('/diary/api/v1/account', methods=['GET'])
def get_user_details():
    """This function retrieves user info"""
    return jsonify(user_info)

@app.route('/logout', methods=['DELETE'])
def logout():
    """Function for logging out"""
    session.pop('logged_in', None)
    return jsonify({'message': 'you are successfully logged out'})

@app.route('/diary/api/v1/entries', methods=['POST'])
def create_entry():
    """ This is a funtion for creating an entry"""
    if not request.json or not 'title' in request.json:
        return jsonify({"message": "Enter the right title"})
    entry = {
        'id' : entries[-1]['id'] + 1,
        'title': request.json['title'],
        'content': request.json['content']
    }
    entries.append(entry)
    return jsonify({'entry' : entry})

@app.route('/diary/api/v1/entries', methods=['GET'])
def get_entries():
    """This is a function for viewing a list of diary entries"""
    return jsonify({'entries' : entries})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['GET'])
def view_one_entry(entry_id):
    """This is a function for getting a single entry"""
    entry = [entry for entry in entries if entry['id'] == entry_id]
    return jsonify({'entry': entry[0]})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    """This is a function for modifying an entry"""
    entry = [entry for entry in entries if entry['id'] == entry_id]
    entry[0]['title'] = request.json.get('title', entry[0]['title'])
    entry[0]['content'] = request.json.get('content', entry[0]['content'])
    return jsonify({'entry': entry[0]})

@app.route('/diary/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """This is a function for deleting an entry"""
    entry = [entry for entry in entries if entry['id'] == entry_id]
    entries.remove(entry[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
