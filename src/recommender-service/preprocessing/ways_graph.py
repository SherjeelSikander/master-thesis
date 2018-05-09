import networkx as nx
import sys
import xml.etree.ElementTree as ET
import pickle

if len(sys.argv) > 2:
    print("Invalid argument list. Only 1 filename argument allowed.")
    sys.exit(0)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    path = ''
else:
    filename = 'munich_large'
    path = 'D:/Documents/Thesis/master-thesis/src/recommender-service/map/'

map_ways = path + filename + '.ways'
map_ways_serialize = path + filename + '.ways.serialize'

try:
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
                graph.add_edge(prevNode, nextNode)
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