# Only for reference and testing. Not being used.
 
import sys
import xml.etree.ElementTree as ET
import pickle
import time
import os

filename = 'munich_small'
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\map\\'

map_ways = path + filename + '.ways'
map_nodes_serialize_from_ways = path + filename + '.nodes.from_ways.serialize'
map_nodes_serialize = path + filename + '.nodes.serialize'
node_dict_from_ways = {}

try:
    node_dict = pickle.load(open(map_nodes_serialize, "rb"))
    print("Nodes loaded")
    mapWaysFile = open(map_ways, 'r', encoding="utf8") 
    for line in mapWaysFile:
        if line.startswith('\t\t<nd ref'):
            node = ET.fromstring(line)
            node_dict_from_ways[node.attrib['ref']] = node_dict[node.attrib['ref']]

    print("Dumping Node Dictionary")
    pickle.dump(node_dict_from_ways, open(map_nodes_serialize_from_ways, "wb"))
    print("Done")
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()