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
def getShortestRoute():
    startLat = request.args.get('startLat')
    startLng = request.args.get('startLng')
    destinationLat = request.args.get('destinationLat')
    destinationLng = request.args.get('destinationLng')
    algorithmId = int(request.args.get('algorithmId'))
    
    if service.isWithinRange(startLat, startLng, destinationLat, destinationLng, 5):
        if algorithmId == 0: # shortest path
            shortest_path = service.getShortestPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 1: # least number of hops
            shortest_path = service.getLeastNodesPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 2: # pass through the center
            shortest_path = service.getCenterPassPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 3: # tree route
            shortest_path = service.getScenicTreePath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 4: # air pollution route
            shortest_path = service.getScenicAirPollutionPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 5: # litter route
            shortest_path = service.getScenicLitterPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 6: # scenic (tree + air + litter)
            shortest_path = service.getScenicTreeAirLitterPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 7: # multi scenic (tree + air + litter)
            shortest_path = service.getMultiScenicTreeAirLitterPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 8: # multi shortest path
            shortest_path = service.getMultiShortestPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 9: # multi tree path
            shortest_path = service.getMultiScenicTreePath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 10: # multi pollution path
            shortest_path = service.getMultiScenicAirPollutionPath(startLat, startLng, destinationLat, destinationLng)
        elif algorithmId == 11: # multi litter path
            shortest_path = service.getMultiScenicLitterPath(startLat, startLng, destinationLat, destinationLng)

        return json.dumps(shortest_path)
    else:
        return json.dumps({"status": 422, "description": "Start and End point should be within 5km."})

@app.route('/trees/', methods=['GET'])
def getTreeLocations():
    trees = service.getTreeLocations()
    return json.dumps(trees)

@app.route('/airpollution/', methods=['GET'])
def getAirPollution():
    airpollution = service.getAirPollution()
    return json.dumps(airpollution)

@app.route('/litter/', methods=['GET'])
def getLitterLocations():
    litter = service.getLitterLocations()
    return json.dumps(litter)  

@app.route('/candidates/', methods=['GET'])
def getRandomCandidateLocations():
    candidates = service.getRandomCandidateLocations()
    return json.dumps(candidates)  

if __name__ == '__main__':
    app.run(debug=False)