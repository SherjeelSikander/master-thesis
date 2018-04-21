#!flask/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

tasks = [
    {
        'id': 1,
        'title': u'Do Master Thesis.',
        'description': u'Find, Best, Tourist, Path', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Graduate',
        'description': u'Please.', 
        'done': False
    }
]

@app.route('/route/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)