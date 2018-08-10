#https://www.scribblemaps.com/create/#/id=WZ_3Ady1Xm&lat=48.146512223178945&lng=11.565537750720978&z=15&t=road
import sys
import os
import xml.etree.ElementTree as ET

path = os.path.dirname(__file__) + '\\'
filename = 'dummylines'
dummylines = path + filename + '.kml'
pollutionlines = path + filename + '.pollution'

tree = ET.parse(dummylines)
root = tree.getroot()[0]

for x in range(1, len(root)):
    print(root[x])

try:
    pollutionlinesFile = open(pollutionlines, 'w', encoding="utf8")
    for x in range(1, len(root)):
        coordinatesList = root[x][2][1].text.split('\n')
        for y in range(0, len(coordinatesList)-1):
            lnglatprev = coordinatesList[y].split(',') 
            lnglatnext = coordinatesList[y+1].split(',')
            CAQI = "25"
            pollutionlinesFile.write(lnglatprev[1] + ' ' + lnglatprev[0] + ' ' + lnglatnext[1] + ' ' + lnglatnext[0] + ' ' + CAQI + '\n')
    pollutionlinesFile.close()
    print("Pollution File Created.")
        
except IOError:
    print ("Could not read file or file does not exist: ", pollutionlinesFile)
    sys.exit()


print("Done")