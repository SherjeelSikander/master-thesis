import sys
import os

filename = 'munich_attractions_area'
path = os.path.dirname(__file__) + '\\preprocessing\\trees\\'
treeSummaryFilePath = path + filename + '.trees_summary'

trees = []

try:
    treeSummaryFile = open(treeSummaryFilePath, 'r', encoding="utf8")
    for line in treeSummaryFile:
        trees.append(line.rstrip().split(' '))
    treeSummaryFile.close()
        
except IOError:
    print ("Could not read file or file does not exist: ", treeSummaryFile)
    sys.exit()

print ("Trees Loaded")
def getAllTreeLocations():
    return trees