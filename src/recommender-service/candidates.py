import sys
import os
import xml.etree.ElementTree as ET
import random

filename = 'attractions_munich'
path = os.path.dirname(__file__) + '\\preprocessing\\attractions\\'
map_attractions = path + filename + '.attractions'

tree = ET.parse(map_attractions)
attractions = tree.getroot()

# for x in range(0, len(attractions)):
#     print(attractions[x].attrib['name'])
#     print(attractions[x].attrib['lat'])
#     print(attractions[x].attrib['lon'])
    
print("Map attractions loaded")

def getRandomCandidates(numberOfRandoms):
    randomIndexes = random.sample(range(1, len(attractions)- 1), numberOfRandoms)
    selectedAttractions = []
    for x in range(0, numberOfRandoms):
        selectedAttractions.append((attractions[randomIndexes[x]].attrib['name'], attractions[randomIndexes[x]].attrib['lat'], attractions[randomIndexes[x]].attrib['lon']))

    return selectedAttractions