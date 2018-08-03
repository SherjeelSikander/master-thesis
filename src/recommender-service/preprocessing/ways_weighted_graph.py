import networkx as nx
import sys
import xml.etree.ElementTree as ET
import pickle
import os
from geopy.distance import great_circle

filename = 'munich_attractions_area'
path = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'

map_ways = path + filename + '.ways'
map_ways_edgelist = path + filename + '.ways.edgelist'
map_nodes_serialize = path + filename + '.nodes.serialize'

try:
    node_dict = pickle.load(open(map_nodes_serialize, "rb"))
    print("Nodes Loaded")

    mapWaysFile = open(map_ways, 'r', encoding="utf8") 
    graph = nx.Graph()
    wayBegin = False
    nodeCounter = 0
    prevNode = 0
    nextNode = 0
    lineCounter = 0
    for line in mapWaysFile:
        lineCounter = lineCounter + 1
        if (lineCounter % 10000) == 1:
            print(lineCounter)    
        if line.startswith('\t<way') and wayBegin == False:
            wayBegin = True
            continue
        elif line.startswith('\t</way') and wayBegin == True:
            wayBegin = False
            nodeCounter = 0
        elif line.startswith('\t\t<nd ref'):
            nodeCounter = nodeCounter + 1
            node = ET.fromstring(line)
            if nodeCounter == 1:
                prevNode = node.attrib['ref'] 
            elif nodeCounter > 1:
                nextNode = node.attrib['ref'] 
                # add edge weight: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
                distance = great_circle(node_dict[nextNode], node_dict[prevNode]).m
                graph.add_edge(prevNode, nextNode, weight=distance, trees=0, clean=0, pollution=0)
                prevNode = nextNode
        else:
            print ("Faulty File")
    mapWaysFile.close()
    
    # Pickle gives memory error for large graphs. Hence we will try storing just the edge data
    nx.write_edgelist(graph, map_ways_edgelist,data=['weight','trees', 'clean', 'pollution'])
    print("Edge list created.")
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()
