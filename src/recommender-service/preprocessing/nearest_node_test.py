import pickle
import os
from math import hypot

filename = 'munich_small'
path = os.path.dirname(os.path.dirname(__file__)) + '\\map\\'
map_nodes_serialize = path + filename + '.nodes.serialize'

node_dict = pickle.load(open(map_nodes_serialize, "rb"))

def getNearestNode(lat, lng):
    minDistanceNode = list(node_dict.keys())[0]
    minDistance = hypot(node_dict[minDistanceNode][0] - lat, node_dict[minDistanceNode][1] - lng) #initialize value

    # for accurate distance the haversine formula should be used however it will have little effect in our scenario
    # a better way would be to create a search tree instead of a linear seach in the dictionary
    for node in node_dict:
        distance = hypot(node_dict[node][0] - lat, node_dict[node][1] - lng)
        if distance < minDistance:
            minDistance = distance
            minDistanceNode = node
            print(minDistanceNode, minDistance)
    
    return minDistanceNode

getNearestNode(48.13660548907217, 11.482587393554667)
    