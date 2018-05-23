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
    algorithmId = request.args.get('algorithmId')
    
    if service.isWithinRange(startLat, startLng, destinationLat, destinationLng, 5):
        shortest_path = service.getShortestPath(startLat, startLng, destinationLat, destinationLng, algorithmId)
        return json.dumps(shortest_path)
    else:
        return json.dumps({"status": 422, "description": "Start and End point should be within 5km."})
   
if __name__ == '__main__':
    app.run(debug=False)