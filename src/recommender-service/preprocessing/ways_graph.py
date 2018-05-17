import networkx as nx
import sys
import xml.etree.ElementTree as ET
import pickle
import os
from math import hypot
from geopy.distance import great_circle

if len(sys.argv) > 2:
    print("Invalid argument list. Only 1 filename argument allowed.")
    sys.exit(0)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    path = ''
else:
    filename = 'munich_large'
    path = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'
    edge_weights = 'default'

map_ways = path + filename + '.ways'

if edge_weights=='default':
    map_ways_serialize = path + filename + '.ways.serialize'
elif edge_weights=='distance':
    map_ways_serialize = path + filename + '.ways.distance.serialize'

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
                if edge_weights == 'distance':
                    distance = great_circle(node_dict[nextNode], node_dict[prevNode]).m
                    graph.add_edge(prevNode, nextNode, weight=distance)
                
                # do not add edge weight (all edges have weight 1)
                elif edge_weights == 'default':
                    graph.add_edge(prevNode, nextNode, weight=6.6934, emission=3.2)
                
                prevNode = nextNode
        else:
            print ("Faulty File")
    mapWaysFile.close()
    # According to https://docs.python.org/3/library/pickle.html
    # protocol version 4 added in Python 3.4 adds support for very large objects. (not backward compatible)
    pickle.dump(graph, open(map_ways_serialize, "wb"), protocol=4)
    print("Done")
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()
