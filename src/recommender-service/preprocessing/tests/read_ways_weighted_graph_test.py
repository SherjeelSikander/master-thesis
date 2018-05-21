import networkx as nx
import sys
import xml.etree.ElementTree as ET
import pickle
import os
import time

filename = 'munich_large'
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\map\\'

map_ways_edgelist = path + filename + '.ways.edgelist'

loadfiletime = time.time()
graph = nx.read_edgelist(map_ways_edgelist, nodetype=str, data=(('weight',float),('emission',float)))
graphbuildtime = time.time()
print("Time to load file: %(time).2f sec" % {'time': (graphbuildtime - loadfiletime)})
print("Number of edges: ", graph.number_of_edges())
print ("done")