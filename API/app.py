"""Import python modules"""
from flask import Flask, jsonify , request,  abort

app = Flask(__name__)

entries = [{'id' : 1, 'title' : u'this is one', 'content' : u'this is content'},
            {'id' : 1, 'title' : u'this is two', 'content' : u'this is content'}]

@app.route('/diary/api/v1/entries', methods=['post'])

def add_comment():
    """ This is a funtion for creating an entry"""
    if not request.json or not 'title' in request.json:
        abort(400)
    entry = {
        'id' : entries[-1]['id'] + 1,
        'title': request.json['title'],
        'content': request.json['content']
    }
    entries.append(entry)
    return jsonify({'entry' : entry})

if __name__ == '__main__':
    app.run(debug=True)