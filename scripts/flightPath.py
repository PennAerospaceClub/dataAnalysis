from ipywidgets.widgets.trait_types import date_from_json
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from scipy import stats

# def tracker(lat, lon, height, temp):
#   df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height, 'TEMP': temp}
#   fig = px.scatter_3d(df, x = 'latitude (degrees)', y = 'longitude (degrees)', z = 'height (meters)', surfacecolor = "TEMP", color_continuous_scale=px.colors.sequential.Bluered.reverse())
#   fig.show()


# df = pd.read_csv (r'Test Data Analysis.csv')
# df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)', 'TEMP'])

# df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

# lat = df['latitude (degrees)']
# lon = df['longitude (degrees)']
# height = df['altitude (meters)']
# temp = df['TEMP']
# tracker(lat, lon, height, temp)

#If 2 inputs are given (generates a 2D plot), NOT DEMO (given a csv)
def plot2D(xAxis, yAxis, csv):
  df = pd.read_csv (csv)
  df = pd.DataFrame(df, columns= [xAxis, yAxis])
  fig = px.scatter(df, x = xAxis, y = yAxis)
  fig.show()
  
  #df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height, 'TEMP': temp}
  #fig = px.scatter(df, x = 'latitude (degrees)', y = 'longitude (degrees)')
  #fig.show()


#lat = df['latitude (degrees)']
#lon = df['longitude (degrees)']
#height = df['altitude (meters)']
#temp = df['TEMP']
plot2D('latitude (degrees)', 'altitude (meters)', 'Test Data Analysis.csv')
