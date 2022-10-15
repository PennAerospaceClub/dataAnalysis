import csv
import math

thresh = 43

d = []

with open('Test Data Analysis.csv', 'r') as data:
    reader = csv.reader(data)

    for row in reader:
        d.append(row)
        
    data.close()

c = 0

for i in range(1, len(d) - 1):
    currLat = float(d[i][0])
    currLong = float(d[i][1])
    currAlt = float(d[i][2])

    nextLat = float(d[i + 1][0])
    nextLong = float(d[i + 1][1])
    nextAlt = float(d[i + 1][2])

    dist = (math.sqrt((currLat - nextLat)**2 +
                    (currLong - nextLong)**2 +
                    (currAlt - nextAlt)**2))
    
    if dist > thresh:
        print(c, dist)
        c += 1
