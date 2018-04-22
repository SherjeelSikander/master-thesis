#!src/recommender-service/api
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/route/', methods=['GET'])

def getRoute():
    startLat = request.args.get('startLat')
    startLng = request.args.get('startLng')
    destinationLat = request.args.get('destinationLat')
    destinationLng = request.args.get('destinationLng')
    return jsonify({'startLat': startLat, 'startLng': startLng, 'destinationLat': destinationLat, 'destinationLng': destinationLng})

if __name__ == '__main__':
    app.run(debug=True)