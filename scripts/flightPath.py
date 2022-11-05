from ipywidgets.widgets.trait_types import date_from_json
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import csv
from scipy import stats

def CSVCleanup(file_name):
    d = []
    with open(file_name, 'r') as data:
        reader = csv.reader(data, csv.QUOTE_NONNUMERIC)
        for i, row in enumerate(reader):
            if i == 0:
                columns = row
            else:
                d.append(row)
        data.close()
    for i in range(0, len(d)-1):
        for j in range(0, len(d[i])-1):
            d[i][j] = float(d[i][j])
    finalLat = d[-1][0]
    finalLong = d[-1][1]
    for i in range(0, len(d)-2):
        if(d[i][0]==finalLat and d[i][0]==finalLong):
            break
        else:
            gap = getRepeat(d, i)
            if gap>1:
                startLat = d[i][0]
                startLong = d[i][1]
                endLat = d[i+gap][0]
                endLong = d[i+gap][1]

                latInterval = (endLat - startLat)/gap 
                longInterval = (endLong - startLong)/gap

                for k in range(i+1, i+gap):
                    d[k][0] = d[k][0] + latInterval
                    d[k][1] = d[k][1] + longInterval
    df = pd.DataFrame(d, columns = columns)
    return(df)

def getRepeat(d, i):
    counter = 1
    val = True
    while val:
        if(d[i][0] == d[i+1][0] and d[i][1] == d[i+1][1]):
            counter+=1
        else:
            val = False
        i+=1
    return counter


def tracker(lat, lon, height):
  df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height}
  fig = px.scatter_3d(df, x = 'latitude (degrees)', y = 'longitude (degrees)', z = 'height (meters)')
  fig.show()

df = CSVCleanup(r"scripts\Test Data Analysis.csv")
#df = pd.read_csv (r'Test Data Analysis.csv')
#df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)'])

# df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

lat = df['latitude (degrees)']
lon = df['longitude (degrees)']
height = df['altitude (meters)']
tracker(lat, lon, height)
