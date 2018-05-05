import sys
import xml.etree.ElementTree as ET

# if len(sys.argv) < 2:
#     print("Missing 1 filename argument.")
#     sys.exit(0)

# if len(sys.argv) > 2:
#     print("Invalid argument list. Only 1 filename argument allowed.")
#     sys.exit(0)

# filename = sys.argv[1]
map = 'D:/Documents/Thesis/master-thesis/src/recommender-service/map/munich_small.osm'
map_nodes = 'D:/Documents/Thesis/master-thesis/src/recommender-service/map/munich_small.nodes'

try:
    mapFile = open(map, 'r', encoding="utf8")
    mapNodesFile = open(map_nodes, 'w', encoding="utf8")
    for line in mapFile:
        if line.startswith('\t<node'):
            if line.endswith('/>\n'):
                mapNodesFile.write(line)
            elif line.endswith('>\n'):
                line = line[:-2] + '/>\n'
                mapNodesFile.write(line)
    mapFile.close()
    mapNodesFile.close()
    print("Done")
        
except IOError:
    print ("Could not read file or file does not exist: ", map)
    sys.exit()