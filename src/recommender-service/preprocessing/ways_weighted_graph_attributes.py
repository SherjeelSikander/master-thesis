import pickle
import os
from math import hypot
import sys
import networkx as nx

filename = 'munich_attractions_area'
path = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'
print("=")
print(path)

map_nodes_serialize = path + filename + '.nodes.connected.serialize'
map_ways_serialize = path + filename + '.ways.serialize'
map_ways_edgelist = path + filename + '.ways.edgelist'

node_dict = pickle.load(open(map_nodes_serialize, "rb"))
print("Nodes Loaded")

try:
    graph = nx.read_edgelist(map_ways_edgelist, nodetype=str, data=(('weight',float),('tree',float),('clean',float),('pollution',float)))
    print("Graph Loaded")
    print("Number of edges: ", graph.number_of_edges())
except IOError:
    print ("Error reading graph")
    sys.exit()

def assignWeights():
    mapPollutionToEdges()
    mapCleanlinessToEdges()
    mapTreesToEdges()

def mapPollutionToEdges():
    print("map Pollution to edges")

def mapTreesToEdges():
    print("map Trees to edges")

def mapCleanlinessToEdges():
    print("map cleanliness to edges")

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

def getShortestDistancePath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))
    
    print(startNode, endNode)
    print("ShortestPath")
    
    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def mapPollutionToEdge(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))
    
    print("Aligning pollution with edges.")
    print(startNode, endNode)

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    except:
        print("error")

    print(shortest_path)

    for index, item in enumerate(shortest_path):
        if index < len(shortest_path) - 1:
            print("Edge " + str(index) + ": between " + shortest_path[index] + " and " + shortest_path[index+1])
            # Get edge between the two nodes
            # Assign the weight value to the edge
    
    print ("Done")

mapPollutionToEdge(48.133283158915276, 11.566615637573221, 48.13482978762863, 11.582279738220194)

def mapTreesToEdge(lat, lng):
    nearestNode = getNearestNode(float(lat), float(lng))
    # find all edges connecting to the node

def mapCleanlinessToEdge(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))
    
    print("Aligning cleanliness with edges.")
    print(startNode, endNode)

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    except:
        print("error")

    print(shortest_path)
    # Get edges between all the nodes of the shortest path
    # Assign the weight value to each edge accordingly