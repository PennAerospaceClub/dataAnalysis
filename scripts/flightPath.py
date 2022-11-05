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
 
def plot3DWithoutColor(xAxis, yAxis, zAxis, csv):
  df = pd.read_csv (csv)
  df = pd.DataFrame(df, columns= [xAxis, yAxis, zAxis])
  fig = px.scatter_3d(df, x = xAxis, y = yAxis, z = zAxis)
  fig.show()
  
def plot3DWithColor(xAxis, yAxis, zAxis, color, csv):
  df = pd.read_csv (csv)
  df = pd.DataFrame(df, columns= [xAxis, yAxis, zAxis, color])
  fig = px.scatter_3d(df, x = xAxis, y = yAxis, z = zAxis, surfacecolor = color, color_continuous_scale=px.colors.sequential.Bluered.reverse())
  fig.show()

#Tests the 3 methods
#plot3DWithoutColor('latitude (degrees)', 'longitude (meters)', 'TEMP', 'Test Data Analysis.csv')

def userEnd():
  csvName = input("Enter csv name: ")
  numCol = input("Number of columns: ")
  while (int(numCol) < 2 or int(numCol) > 4):
    print("Please select at least 2 columns and no more than 4.")
    numCol = input("Number of columns: ")
  #Show all possible columns
#   with open(csvName) as csvFile:
#     reader = csv.reader(csvFile)
#     row1 = reader.next()
#   columnNames = row1.split(', ')
df_first = pd.read_csv(csv, nrows = 1)
  for name in df_first:
    print(name)
  if numCol == 2:
    x = input("x-axis: ")
    y = input("y-axis: ")
    plot2D(x, y, csv)
  elif (numCol == 3):
    x = input("x-axis: ")
    y = input("y-axis: ")
    z = input("z-axis: ")
    plot3DWithoutColor(x, y, z, csv)
  else:
    x = input("x-axis: ")
    y = input("y-axis: ")
    z = input("z-axis: ")
    color = input("color axis: ")
    plot3DWithColor(x, y, z, color, csv)

userEnd()

#Get CSV file, show columns, get columns, go to appropriate function based on number of inputs
