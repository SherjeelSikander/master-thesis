import sys
import os

filename = 'munich_attractions_area'
path = os.path.dirname(__file__) + '\\preprocessing\\trees\\'
treeSummaryFilePath = path + filename + '.trees_summary'

trees = []

try:
    location = []
    treeSummaryFile = open(treeSummaryFilePath, 'r', encoding="utf8")
    for line in treeSummaryFile:
        location = line.rstrip().split(' ')
        trees.append([float(location[0]), float(location[1])])
    treeSummaryFile.close()
        
except IOError:
    print ("Could not read file or file does not exist: ", treeSummaryFile)
    sys.exit()

print ("Trees Loaded")
def getAllTreeLocations():
    return trees