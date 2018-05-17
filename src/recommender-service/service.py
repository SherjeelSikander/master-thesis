import pickle
import os
from math import hypot
import networkx as nx

filename = 'munich_small'
path = os.path.dirname(__file__) + '\\map\\'
map_nodes_serialize = path + filename + '.nodes.connected.serialize'
map_ways_serialize = path + filename + '.ways.distance.serialize'

node_dict = pickle.load(open(map_nodes_serialize, "rb"))
print("Nodes Loaded")

graph = pickle.load(open(map_ways_serialize, "rb"))
print("Graph Loaded")

def getNearestNode(lat, lng):
    minDistanceNode = list(node_dict.keys())[0]
    minDistance = hypot(node_dict[minDistanceNode][0] - lat, node_dict[minDistanceNode][1] - lng) #initialize value

    # for accurate distance the haversine formula should be used however it will have little effect in our scenario
    # a better way would be to create a search tree instead of a linear seach in the dictionary
    for node in node_dict:
        distance = hypot(node_dict[node][0] - lat, node_dict[node][1] - lng)
        if distance < minDistance:
            minDistance = distance
            minDistanceNode = node
    
    return minDistanceNode

def getShortestPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))
    print(startNode, endNode)

    shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return shortest_path
    
#getShortestPath(48.133283158915276, 11.566615637573221, 48.13482978762863, 11.582279738220194)