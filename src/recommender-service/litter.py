import sys
import os

filename = 'littering'
path = os.path.dirname(__file__) + '\\preprocessing\\littering\\'
litteringFilePath = path + filename + '.random.litter'

litter = []

try:
    location = []
    litteringFile = open(litteringFilePath, 'r', encoding="utf8")
    for line in litteringFile:
        locationAndValue = line.rstrip().split(' ')
        litter.append([float(locationAndValue[0]), float(locationAndValue[1]), float(locationAndValue[2])])
    litteringFile.close()
        
except IOError:
    print ("Could not read file or file does not exist: ", litteringFile)
    sys.exit()

print ("Litter Loaded")
def getAllLitterLocations():
    return litter