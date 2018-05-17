import networkx as nx
import sys
import xml.etree.ElementTree as ET
import pickle
import os

filename = 'munich_large'
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\map\\'

map_ways_edgelist = path + filename + '.ways.edgelist'

G = nx.read_edgelist(map_ways_edgelist, nodetype=str, data=(('weight',float),('emission',float)))

print ("done")