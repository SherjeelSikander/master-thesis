import networkx as nx
import sys
import pickle
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

map_ways_serialize = path + filename + '.ways.serialize'

graph = pickle.load(open(map_ways_serialize, "rb"))
print(nx.shortest_path(graph, source='274547', target='3759741031'))
print("Done")

