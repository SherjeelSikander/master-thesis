import sys
import os
import xml.etree.ElementTree as ET

path = os.path.dirname(__file__)
filename = 'attractions_munich'
attractions = path + filename + '.kml'
attractions_extracted = path + filename + '.attractions'

tree = ET.parse(attractions)
root = tree.getroot()
placemarks = root[0][5]

# separate nodes
try:
    mapAttractionsFile = open(attractions_extracted, 'w', encoding="utf8")
    mapAttractionsFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    mapAttractionsFile.write('<Attractions>\n')
    for x in range(1, len(placemarks)):
        print (placemarks[x][0].text.strip())
        coordinates = placemarks[x][len(placemarks[x])-1][0].text.strip().split(',')
        print (coordinates[0], coordinates[1])
        print('<attraction name="'+ placemarks[x][0].text.strip() + '" lat="'+ coordinates[1] +'" lon="'+ coordinates[0] +'"/>')
        mapAttractionsFile.write('<attraction name="'+ placemarks[x][0].text.strip() + '" lat="'+ coordinates[1] +'" lon="'+ coordinates[0] +'"/>\n')
    mapAttractionsFile.write('</Attractions>')
    mapAttractionsFile.close()
    print("Attractions File Created.")
        
except IOError:
    print ("Could not read file or file does not exist: ", attractions_extracted)
    sys.exit()

