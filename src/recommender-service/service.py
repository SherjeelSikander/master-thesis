import pickle
import os
from math import hypot
import networkx as nx
import sys
from geopy.distance import great_circle
import candidates as candidate_selection
import trees
import airpollution
import litter

filename = 'munich_attractions_area'
path = os.path.dirname(__file__) + '\\map\\'
map_nodes_serialize = path + filename + '.nodes.connected.serialize'
map_ways_serialize = path + filename + '.ways.serialize'
map_ways_edgelist = path + filename + '.ways.edgelist'
map_weighted_ways_edgelist = path + filename + '.ways.weighted.edgelist'

node_dict = pickle.load(open(map_nodes_serialize, "rb"))
print("Nodes Loaded")

candidates = []

try:
    graph = nx.read_edgelist(map_weighted_ways_edgelist, nodetype=str, data=(('weight',float),('trees',float),('clean',float),('pollution',float)))
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

def isWithinRange(startLat, startLng, endLat, endLng, rangeInKm):
    distance = great_circle((startLat, startLng), (endLat, endLng)).km
    if distance > rangeInKm:
        return False
    return True
    
def getShortestPath(startLat, startLng, endLat, endLng):
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
    
def getLeastNodesPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))
    
    print(startNode, endNode)
    print("LeastNodesPath")
    
    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def getCenterPassPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    centerNode = getNearestNode((float(startLat)+float(endLat)+float(endLat))/3, (float(startLng)+float(endLng)+float(endLng))/3)
    centerNode2 = getNearestNode((float(startLat)+float(endLat))/2, (float(startLng)+float(endLng))/2)
    endNode = getNearestNode(float(endLat), float(endLng))
    
    print(startNode, centerNode, endNode)
    print("CenterPassPath")
    
    try:
        shortest_path_to_center = nx.shortest_path(graph, source=startNode, target=centerNode2)
        shortest_path_to_center2 = nx.shortest_path(graph, source=centerNode2, target=centerNode)
        shortest_path_to_end = nx.shortest_path(graph, source=centerNode, target=endNode)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path_to_center):
        shortest_path_to_center[index] = node_dict[item]

    for index, item in enumerate(shortest_path_to_center2):
        shortest_path_to_center2[index] = node_dict[item]

    for index, item in enumerate(shortest_path_to_end):
        shortest_path_to_end[index] = node_dict[item]

    return [shortest_path_to_center, shortest_path_to_center2, shortest_path_to_end]
#getShortestPath(48.133283158915276, 11.566615637573221, 48.13482978762863, 11.582279738220194)

def getScenicTreePath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight=edgeTreeWeight)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def getScenicAirPollutionPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight=edgeAirPollutionWeight)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def getScenicLitterPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight=edgeLitterWeight)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def getScenicTreeAirLitterPath(startLat, startLng, endLat, endLng):
    startNode = getNearestNode(float(startLat), float(startLng))
    endNode = getNearestNode(float(endLat), float(endLng))

    try:
        shortest_path = nx.shortest_path(graph, source=startNode, target=endNode, weight=edgeTreeAirLitterWeight)
    except:
        print("error")
    
    for index, item in enumerate(shortest_path):
        shortest_path[index] = node_dict[item]

    return [shortest_path]

def getMultiScenicTreeAirLitterPath(startLat, startLng, endLat, endLng):
    orderedCandidateNodes = getOrderedCandidates(startLat, startLng, endLat, endLng)
    shortestPaths = []
    for x in range(0, len(orderedCandidateNodes) + 1):
        if x == 0:
            shortestPaths.append(getScenicTreeAirLitterPath(startLat, startLng, float(orderedCandidateNodes[x][1][1]), float(orderedCandidateNodes[x][1][2]))[0])
        elif x < len(orderedCandidateNodes):
            shortestPaths.append(getScenicTreeAirLitterPath(float(orderedCandidateNodes[x-1][1][1]), float(orderedCandidateNodes[x-1][1][2]), float(orderedCandidateNodes[x][1][1]), float(orderedCandidateNodes[x][1][2]))[0])
        elif x == len(orderedCandidateNodes):
            shortestPaths.append(getScenicTreeAirLitterPath(float(orderedCandidateNodes[x-1][1][1]), float(orderedCandidateNodes[x-1][1][2]), endLat, endLng)[0])
            
    return shortestPaths

#The function must accept exactly three positional arguments: the two endpoints of an edge and 
# the dictionary of edge attributes for that edge. The function must return a number.
def edgeTreeWeight(startEdge, endEdge, edgeAttributes):
    if edgeAttributes['trees'] == 0:
        treesWeight = edgeAttributes['weight'] * 4
    else:
        treesWeight = edgeAttributes['weight'] / (20 * (edgeAttributes['trees'])) 
    return edgeAttributes['weight'] + treesWeight

def edgeAirPollutionWeight(startEdge, endEdge, edgeAttributes):
    if edgeAttributes['pollution'] == 0:
        airPollutionWeight = 1
    else:
        airPollutionWeight = edgeAttributes['pollution'] / 25
    return edgeAttributes['weight'] * airPollutionWeight

def edgeLitterWeight(startEdge, endEdge, edgeAttributes):
    if edgeAttributes['clean'] == 0:
        litterWeight = 1
    else:
        litterWeight = edgeAttributes['clean'] * 2
    return edgeAttributes['weight'] * litterWeight

def edgeTreeAirLitterWeight(startEdge, endEdge, edgeAttributes):
    return edgeTreeWeight(startEdge, endEdge, edgeAttributes) + edgeAirPollutionWeight(startEdge, endEdge, edgeAttributes) + edgeLitterWeight(startEdge, endEdge, edgeAttributes)

def getTreeLocations():
    treeLocations = trees.getAllTreeLocations()
    return treeLocations

def getAirPollution():
    airPollution = airpollution.getAllAirPollution()
    return airPollution

def getLitterLocations():
    litterLocations = litter.getAllLitterLocations()
    return litterLocations

def getCandidateNodes(numberOfCandidates):
    candidates = candidate_selection.getRandomCandidates(numberOfCandidates)
    candidateNodes = []
    for x in range(0, numberOfCandidates):
        candidateNodes.append((getNearestNode(float(candidates[x][1]), float(candidates[x][2])), candidates[x]))
    return candidateNodes

def getRandomCandidateLocations():
    global candidates
    # print("Previous Candidates")
    # print(candidates)
    candidates = getCandidateNodes(5)
    return candidates

def getSetCandidates():
    if len(candidates)==0:
        return getRandomCandidateLocations()
    else:
        return candidates

def getOrderedCandidates(startLat, startLng, endLat, endLng):
    candidateNodes = getSetCandidates()
    distanceCandidateNodes = []
    orderedCandidateNodes = []

    for x in range(0, len(candidateNodes)):
        distance = great_circle((startLat, startLng), (float(candidateNodes[x][1][1]), float(candidateNodes[x][1][2]))).m
        distanceCandidateNodes.append([distance, candidateNodes[x]])

    distanceCandidateNodes.sort(key=lambda x:x[0])
    for x in range(0, len(distanceCandidateNodes)):
        orderedCandidateNodes.append(distanceCandidateNodes[x][1]) 

    return orderedCandidateNodes