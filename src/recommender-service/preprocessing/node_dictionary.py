import sys
import xml.etree.ElementTree as ET
import pickle
import time
import os

if len(sys.argv) > 2:
    print("Invalid argument list. Only 1 filename argument allowed.")
    sys.exit(0)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    path = ''
else:
    filename = 'munich_small'
    path = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'

map_nodes = path + filename + '.nodes'
map_nodes_serialize = path + filename + '.nodes.serialize'
node_dict = {}

try:
    readfiletime = time.time()
    mapNodesFile = open(map_nodes, 'r', encoding="utf8")
    for line in mapNodesFile:    
        node = ET.fromstring(line)
        node_dict[node.attrib['id']] = (node.attrib['lat'], node.attrib['lon']) 
    mapNodesFile.close()
    
    dumpfiletime = time.time()
    print("Time to read file: %(time).2f sec" % {'time': (dumpfiletime - readfiletime)})
    pickle.dump(node_dict, open(map_nodes_serialize, "wb"))

    loadfiletime = time.time()
    print("Time to dump file: %(time).2f sec" % {'time': (loadfiletime - dumpfiletime)})
    node_dict_loaded = pickle.load(open(map_nodes_serialize, "rb"))

    completiontime = time.time()
    print("Time to read dumped file: %(time).2f sec" % {'time': (completiontime - loadfiletime)})
    print("Done")
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()