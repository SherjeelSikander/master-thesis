#!src/recommender-service/api
from flask import Flask, request
from flask_cors import CORS
import json
import service

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
    
    shortest_path = service.getShortestPath(startLat, startLng, destinationLat, destinationLng)
    return json.dumps(shortest_path)
   
if __name__ == '__main__':
    app.run(debug=True)