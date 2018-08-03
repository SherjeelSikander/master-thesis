import sys
import os
import xml.etree.ElementTree as ET

mapFilename = 'munich_attractions_area'
mapPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '\\map\\'

treePath = os.path.dirname(__file__) + '\\'

mapFilePath = mapPath + mapFilename + '.osm'
treesFilePath = treePath + mapFilename + '.trees'
treesSummaryFilePath = treePath + mapFilename + '.trees_summary'

print(mapPath)
print(treePath)

try:
    mapFile = open(mapFilePath, 'r', encoding="utf8")
    mapTreesFile = open(treesFilePath, 'w', encoding="utf8")
    mapTreesSummaryFile = open(treesSummaryFilePath, 'w', encoding="utf8")
    node = ""
    readingNode = False
    mapTreesFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    mapTreesFile.write('<Trees>\n')
    
    for line in mapFile:
        if line.startswith('\t<node') and line.endswith('/>\n'):
            node = ""
            nodeSummary = ""
        elif line.startswith('\t<node'):
            node = node + line
            nodeSummary = line
            readingNode = True
        elif line.startswith('\t</node'):
            node = node + line
            readingNode = False
            if 'v="tree"' in node:
                mapTreesFile.write(node)
                lat = nodeSummary[nodeSummary.find('lat="')+len('lat="'):nodeSummary.rfind('" lon')]
                lon = nodeSummary[nodeSummary.find('lon="')+len('lon="'):nodeSummary.rfind('" ')]
                mapTreesSummaryFile.write(lat + ' ' + lon + '\n')
            node = ""
            nodeSummary = ""
        elif readingNode == True:
            node = node + line

    mapTreesFile.write('</Trees>')
    mapFile.close()
    mapTreesFile.close()
    mapTreesSummaryFile.close()
    print("Trees File Created.")
        
except IOError:
    print ("Could not read file or file does not exist: ", mapFile)
    sys.exit()
