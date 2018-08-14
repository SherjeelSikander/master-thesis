import sys
import os

filename = 'dummylines'
path = os.path.dirname(__file__) + '\\preprocessing\\airpollution\\'
airpollutionFilePath = path + filename + '.filter.pollution'

airpollution = []

try:
    airpollutionFile = open(airpollutionFilePath, 'r', encoding="utf8")
    for line in airpollutionFile:
        values = line.rstrip().split(' ')
        airpollution.append([float(values[0]), float(values[1]), float(values[2]), float(values[3]), int(values[4])])
        #from lat, from lng, to lat, to lng, CAQI value
    airpollutionFile.close()
        
except IOError:
    print ("Could not read file or file does not exist: ", airpollutionFile)
    sys.exit()

print ("Air Pollution Loaded")
def getAllAirPollution():
    return airpollution