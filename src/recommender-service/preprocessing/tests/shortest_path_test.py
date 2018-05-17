import networkx as nx
import sys
import pickle
import os

filename = 'munich_small'
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\map\\'

map_ways_serialize = path + filename + '.ways.serialize'

graph = pickle.load(open(map_ways_serialize, "rb"))
print(nx.shortest_path(graph, source='274547', target='3759741031'))
print("Done")

