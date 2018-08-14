import pickle
import os
from math import hypot
import sys
import networkx as nx
from geopy.distance import great_circle

filename = 'munich_attractions_area'

mapPath = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'
map_nodes_serialize = mapPath + filename + '.nodes.connected.serialize'
map_ways_serialize = mapPath + filename + '.ways.serialize'
map_ways_edgelist = mapPath + filename + '.ways.edgelist'

treePath = os.path.dirname(__file__) + '\\trees\\'
treeSummaryFilePath = treePath + filename + '.trees_summary'

airPollutionFilename = "dummylines"
airPollutionPath = os.path.dirname(__file__) + '\\airpollution\\'
airPollutionFilePath = airPollutionPath + airPollutionFilename + '.pollution'
airPollutionFilteredFilePath = airPollutionPath + airPollutionFilename + '.filter.pollution'

map_ways_weighted_edgelist = mapPath + filename + '.ways.weighted.edgelist'

reuse_weight_file = True

calculate_tree_weights = False

calculate_airpollution_weights = False
use_airpollution_filtered_file = False
filter_airpollution = True

calculate_cleanliness_weights = False

node_dict = []
graph = []
trees = []
airpollution = []

def assignWeights():
    loadNodes()
    loadGraph()
    
    if calculate_tree_weights == True:
        loadTrees()
        mapTreesToEdges()
    
    if filter_airpollution == True:
        loadAirPollution()
        filterAirPollution()

    if calculate_airpollution_weights == True:
        loadAirPollution()
        mapAirPollutionToEdges()
    
    if calculate_cleanliness_weights == True:
        loadCleanliness()
        mapCleanlinessToEdges()

    #writeGraph()
    
    #mapPollutionToEdge(48.133283158915276, 11.566615637573221, 48.13482978762863, 11.582279738220194)
    
#region HELPER FUNCTIONS

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
        if reuse_weight_file == True:
            graph = nx.read_edgelist(map_ways_weighted_edgelist, nodetype=str, data=(('weight',float),('trees',float),('clean',float),('pollution',float)))
        elif reuse_weight_file == False:
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
    
    return [minDistanceNode, minDistance]

def getShortestDistancePath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))[0]
    endNode = getNearestNode(float(endLat), float(endLng))[0]
    
    print(startNode, endNode)
    print("ShortestPath")
    
    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

#endregion

#region MAPPING TREES 
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
    nearestNode = getNearestNode(float(lat), float(lng))[0]
    for neighbor in graph[nearestNode]:
        graph[nearestNode][neighbor]['trees'] = graph[nearestNode][neighbor]['trees'] + 1
    # find all edges connecting to the node

#endregion

#region MAPPING POLLUTION
def loadAirPollution():
    global airpollution
    try:
        airpollution = []
        if use_airpollution_filtered_file == True:
            airPollutionFile = open(airPollutionFilteredFilePath, 'r', encoding="utf8")
        elif use_airpollution_filtered_file == False:
            airPollutionFile = open(airPollutionFilePath, 'r', encoding="utf8")
        for line in airPollutionFile:
            values = line.rstrip().split(' ')
            airpollution.append([float(values[0]), float(values[1]), float(values[2]), float(values[3]), int(values[4])])
        airPollutionFile.close()
            
    except IOError:
        print ("Could not read file or file does not exist: ", airPollutionFilePath)
        sys.exit()

def mapAirPollutionToEdges():
    print("mapping air pollution to edges")
    for idx, airpollutionEdge in enumerate(airpollution):
        if idx % 100 == 0:
            print(idx*100/len(airpollution))
        mapAirPollutionToEdge(airpollutionEdge[0], airpollutionEdge[1], airpollutionEdge[2], airpollutionEdge[3], airpollutionEdge[4])
    print("mapped air pollution to edges")

def mapAirPollutionToEdge(startLat, startLng, endLat, endLng, pollutionValue):
    global graph
    nearestStart = getNearestNode(float(startLat), float(startLng))
    startNode = nearestStart[0]
    startNodeDistance = nearestStart[1]
    nearestEnd = getNearestNode(float(endLat), float(endLng))
    endNode = nearestEnd[0]
    endNodeDistance = nearestEnd[1]
    
    print("Nearest nodes are " + str(startNodeDistance) + ' ' + str(endNodeDistance) + " meters away")

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
        shortest_path_length = nx.shortest_path_length(graph, source=startNode, target=endNode, weight='weight')
        straight_line_distance = great_circle((startLat, startLng), (endLat, endLng)).m
    except:
        print("error")
    
    if straight_line_distance == 0 or shortest_path_length/straight_line_distance > 1.5:
        print("Invalid - nodes: " + str(len(shortest_path)) + ' distance: ' + str(shortest_path_length) + ' straightLine: ' + str(great_circle((startLat, startLng), (endLat, endLng)).m) + '\n')
        return
        
    for index, item in enumerate(shortest_path):
        if index < len(shortest_path) - 1:
            #print("Edge " + str(index) + ": between " + shortest_path[index] + " and " + shortest_path[index+1])
            if pollutionValue > graph[shortest_path[index]][shortest_path[index+1]]['pollution']:
                graph[shortest_path[index]][shortest_path[index+1]]['pollution'] = pollutionValue
    
    #print ("Done")

#endregion

#region Filter Pollution
def filterAirPollution():
    try:
        airPollutionFilteredFile = open(airPollutionFilteredFilePath, 'w', encoding="utf8")
        
    except IOError:
        print ("Could not read file or file does not exist: ", airPollutionFilteredFile)
        sys.exit()

    print("filtering air pollution")
    for idx, airpollutionEdge in enumerate(airpollution):
        if idx % 100 == 0:
            print(idx*100/len(airpollution))
    
        nearestStart = getNearestNode(float(airpollutionEdge[0]), float(airpollutionEdge[1]))
        startNode = nearestStart[0]
        startNodeDistance = nearestStart[1]
        
        nearestEnd = getNearestNode(float(airpollutionEdge[2]), float(airpollutionEdge[3]))
        endNode = nearestEnd[0]
        endNodeDistance = nearestEnd[1]
        
        print("Nearest nodes are " + str(startNodeDistance) + ' ' + str(endNodeDistance) + " meters away")

        try:
            shortest_path_length = nx.shortest_path_length(graph, source=startNode, target=endNode, weight='weight')
            straight_line_distance = great_circle((airpollutionEdge[0], airpollutionEdge[1]), (airpollutionEdge[2], airpollutionEdge[3])).m
        except:
            print("error")
        
        if straight_line_distance == 0 or shortest_path_length/straight_line_distance > 1.5:
            print("Invalid distance: " + str(shortest_path_length) + ' straightLine: ' + str(great_circle((airpollutionEdge[0], airpollutionEdge[1]), (airpollutionEdge[2], airpollutionEdge[3])).m) + '\n')
        else:
            airPollutionFilteredFile.write(str(airpollutionEdge[0]) + ' ' + str(airpollutionEdge[1]) + ' ' + str(airpollutionEdge[2]) + ' ' + str(airpollutionEdge[3]) + ' ' + str(airpollutionEdge[4]) + '\n')
    
    airPollutionFilteredFile.close()
    print("filtered air pollution")
#endregion

#region MAPPING CLEANLINESS
def loadCleanliness():
    print("load cleanliness")

def mapCleanlinessToEdges():
    print("map cleanliness to edges")

def mapCleanlinessToEdge(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))[0]
    endNode = getNearestNode(float(endLat), float(endLng))[0]
    
    print("Aligning cleanliness with edges.")
    print(startNode, endNode)

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight='weight')
    except:
        print("error")

    print(shortest_path)
    # Get edges between all the nodes of the shortest path
    # Assign the weight value to each edge accordingly

#endregion

assignWeights()