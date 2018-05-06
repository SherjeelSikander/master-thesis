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
    
map_nodes = path + filename + '.nodes'
node_dict = {}

try:
    mapNodesFile = open(map_nodes, 'r', encoding="utf8")
    for line in mapNodesFile:    
        node = ET.fromstring(line)
        node_dict[node.attrib['id']] = (node.attrib['lat'], node.attrib['lon']) 
    mapNodesFile.close()
        
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()