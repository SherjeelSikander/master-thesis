import networkx as nx
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) > 2:
    print("Invalid argument list. Only 1 filename argument allowed.")
    sys.exit(0)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    path = ''
else:
    filename = 'munich_small'
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

    for line in mapWaysFile:    
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
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()
