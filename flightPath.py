from ipywidgets.widgets.trait_types import date_from_json
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from scipy import stats

def tracker(lat, lon, height):
  df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height}
  fig = px.scatter_3d(df, x = 'latitude (degrees)', y = 'longitude (degrees)', z = 'height (meters)', color = "height (meters)", color_continuous_scale=px.colors.sequential.Bluered.reverse())
  fig.show()


df = pd.read_csv (r'Test Data Analysis.csv')
df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)'])

# df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

lat = df['latitude (degrees)']
lon = df['longitude (degrees)']
height = df['altitude (meters)']
tracker(lat, lon, height)
