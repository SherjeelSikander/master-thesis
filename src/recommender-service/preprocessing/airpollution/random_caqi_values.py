import sys
import os
from random import randint

path = os.path.dirname(__file__) + '\\'
filename = "dummylines"
pollutionlines = path + filename + ".filter.pollution"
pollutionlinesRandom = path + filename + ".randomcaqi.filter.pollution"

try:
    pollutionlinesFile = open(pollutionlines, 'r', encoding="utf8")
    pollutionlinesRandomFile = open(pollutionlinesRandom, 'w', encoding="utf8")
    
    for line in pollutionlinesFile:
        values = line.rstrip().split(' ')
        CAQI = randint(2, 99)
        pollutionlinesRandomFile.write(str(float(values[0])) + ' ' + str(float(values[1])) + ' ' + str(float(values[2])) + ' ' + str(float(values[3])) + ' ' + str(CAQI) + '\n')
   
    pollutionlinesFile.close()
    pollutionlinesRandomFile.close()

except IOError:
    print("Unable to open file ", pollutionlines)
    sys.exit()
