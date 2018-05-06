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
    
map_nodes = path + filename + '.nodes'
map_nodes_serialize = path + filename + '.nodes.serialize'
node_dict = {}

try:
    mapNodesFile = open(map_nodes, 'r', encoding="utf8")
    for line in mapNodesFile:    
        node = ET.fromstring(line)
        node_dict[node.attrib['id']] = (node.attrib['lat'], node.attrib['lon']) 
    mapNodesFile.close()
    
    pickle.dump(node_dict, open(map_nodes_serialize, "wb"))
    node_dict_loaded = pickle.load(open(map_nodes_serialize, "rb"))
    print("Done")
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()