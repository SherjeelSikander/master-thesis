#!src/recommender-service/api
from flask import Flask, request
from flask_cors import CORS
import os
import networkx as nx
import pickle
import sys
import json

app = Flask(__name__)
CORS(app)
graph = nx.Graph()
nodes = {}

def loadGraph():
    
    nodes_path = "D:/Documents/Thesis/master-thesis/src/recommender-service/map/munich_large.nodes.serialize"
    global nodes 
    nodes = pickle.load(open(nodes_path, "rb"))
    print("Nodes Loaded")
    
    path = "D:/Documents/Thesis/master-thesis/src/recommender-service/map/munich_large.ways.serialize"
    global graph 
    graph = pickle.load(open(path, "rb"))
    print("Graph Loaded")

loadGraph()

@app.route('/')
def index():
    return "Hello, World!"
    
@app.route('/route/', methods=['GET'])
def getRoute():
    startLat = request.args.get('startLat')
    startLng = request.args.get('startLng')
    destinationLat = request.args.get('destinationLat')
    destinationLng = request.args.get('destinationLng')
    
    shortest_path = nx.shortest_path(graph, source='274547', target='3759741031')
    for index, item in enumerate(shortest_path):
        shortest_path[index] = nodes[item]
    return json.dumps(shortest_path)
   
if __name__ == '__main__':
    app.run(debug=True)