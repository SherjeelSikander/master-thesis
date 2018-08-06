import pickle
import os
from math import hypot
import sys
import networkx as nx

filename = 'munich_attractions_area'

mapPath = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'
map_nodes_serialize = mapPath + filename + '.nodes.connected.serialize'
map_ways_serialize = mapPath + filename + '.ways.serialize'
map_ways_edgelist = mapPath + filename + '.ways.edgelist'

treePath = os.path.dirname(__file__) + '\\trees\\'
treeSummaryFilePath = treePath + filename + '.trees_summary'

map_ways_weighted_edgelist = mapPath + filename + '.ways.weighted.edgelist'

node_dict = []
graph = []
trees = []

def assignWeights():
    loadNodes()
    loadGraph()
    loadTrees()

    mapTreesToEdges()
    writeGraph()
    mapPollutionToEdge(48.133283158915276, 11.566615637573221, 48.13482978762863, 11.582279738220194)
    #mapPollutionToEdges()
    #mapCleanlinessToEdges()

########### HELPER FUNCTIONS ###########
def writeGraph():
    global graph
    nx.write_edgelist(graph, map_ways_weighted_edgelist, data=['weight','trees', 'clean', 'pollution'])
    print("Weighted edgelist written")

def loadNodes():
    global node_dict
    node_dict = pickle.load(open(map_nodes_serialize, "rb"))
    print("Nodes Loaded")

def loadGraph():
    global graph
    try:
        graph = nx.read_edgelist(map_ways_edgelist, nodetype=str, data=(('weight',float),('trees',float),('clean',float),('pollution',float)))
        print("Graph Loaded")
        print("Number of edges: ", graph.number_of_edges())
    except IOError:
        print ("Error reading graph")
        sys.exit()

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

########### MAPPING TREES ###########  
def loadTrees():
    global trees
    try:
        location = []
        treeSummaryFile = open(treeSummaryFilePath, 'r', encoding="utf8")
        for line in treeSummaryFile:
            location = line.rstrip().split(' ')
            trees.append([float(location[0]), float(location[1])])
        treeSummaryFile.close()
            
    except IOError:
        print ("Could not read file or file does not exist: ", treeSummaryFile)
        sys.exit()

def mapTreesToEdges():
    print("mapping trees to edges")
    for idx, tree in enumerate(trees):
        if idx % 100 == 0:
            print(idx*100/len(trees))
        mapTreeToEdge(tree[0], tree[1])
    print("mapped trees to edges")

def mapTreeToEdge(lat, lng):
    global graph
    nearestNode = getNearestNode(float(lat), float(lng))
    for neighbor in graph[nearestNode]:
        graph[nearestNode][neighbor]['trees'] = graph[nearestNode][neighbor]['trees'] + 1
    # find all edges connecting to the node

########### MAPPING POLLUTION ###########
def mapPollutionToEdges():
    print("map Pollution to edges")

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

########### MAPPING CLEANLINESS ###########
def mapCleanlinessToEdges():
    print("map cleanliness to edges")

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

assignWeights()