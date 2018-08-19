import sys
import os
from random import randint

path = os.path.dirname(__file__) + '\\'
filename = "littering"
litteringpoints = path + filename + ".litter"
litteringpointsRandom = path + filename + ".random.litter"

try:
    litteringpointsFile = open(litteringpoints, 'r', encoding="utf8")
    litteringpointsRandomFile = open(litteringpointsRandom, 'w', encoding="utf8")
    
    for line in litteringpointsFile:
        values = line.rstrip().split(' ')
        litterValue = randint(0, 10)
        litteringpointsRandomFile.write(str(float(values[0])) + ' ' + str(float(values[1])) + ' ' + str(litterValue) + '\n')
   
    litteringpointsFile.close()
    litteringpointsRandomFile.close()

except IOError:
    print("Unable to open file ", litteringpointsFile)
    sys.exit()
