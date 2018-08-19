#https://www.scribblemaps.com/create/#/id=puJr4eWe6Y&lat=48.147405248376444&lng=11.567144393920898&z=16&t=road
import sys
import os
import xml.etree.ElementTree as ET

path = os.path.dirname(__file__) + '\\'
filename = 'littering'
dummypoints = path + filename + '.kml'
litteringpoints = path + filename + '.litter'

tree = ET.parse(dummypoints)
root = tree.getroot()[0]

for x in range(1, len(root)):
    print(root[x])

try:
    litteringpointsFile = open(litteringpoints, 'w', encoding="utf8")
    for x in range(1, len(root)):
        coordinates = root[x][2][1].text
        lnglat = coordinates.split(',')
        litter = "1.0"
        litteringpointsFile.write(lnglat[1] + ' ' + lnglat[0] + ' ' + litter + '\n')
    litteringpointsFile.close()
    print("Litter File Created.")
        
except IOError:
    print ("Could not read file or file does not exist: ", litteringpointsFile)
    sys.exit()


print("Done")