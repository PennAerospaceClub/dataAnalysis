from ipywidgets.widgets.trait_types import date_from_json
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import math
from scipy import stats

def getMaxCol(col):
	return max(df[col])

def getLaunchSite(lat, lon):
	return (df[lat][0], df[lon][0])

def getRecoverySite(lat, lon):
	return (list(df[lat])[-1], list(df[lon])[-1])

def distanceTraveled(lat, lon, height):
	lat = list(df[lat])
	lon = list(df[lon])
	height = list(df[height])

	totalDist = 0
	prev = None

	for i, h in enumerate(height):
		curr = (lat[i], lon[i], h)
		
		if not prev:
			prev = curr

		latMid = float((curr[0] + prev[0]) / 2.0)

		m_per_deg_lat = 111132.954 - 559.822 * math.cos(2 * latMid) + 1.175 * math.cos(4 * latMid);
		m_per_deg_lon = 111132.954 * math.cos(latMid);

		deltaLat = abs(curr[0] - prev[0]);
		deltaLon = abs(curr[1] - curr[1]);

		# print(f'Step in lat long (m): {math.sqrt((deltaLat * m_per_deg_lat)**2 + (deltaLon * m_per_deg_lon)**2)}')

		totalDist += math.sqrt((deltaLat * m_per_deg_lat)**2 + (deltaLon * m_per_deg_lon)**2 + (prev[2] - curr[2])**2)

		prev = curr

	return totalDist

def tracker(lat, lon, height, temp):
	df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height, 'TEMP': temp}
	fig = px.scatter_3d(df, x = 'latitude (degrees)', y = 'longitude (degrees)', z = 'height (meters)', color = "TEMP", color_continuous_scale=px.colors.sequential.Bluered.reverse())
	fig.show()


df = pd.read_csv (r'Test Data Analysis.csv')
df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)', 'TEMP'])

# df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

lat = df['latitude (degrees)']
lon = df['longitude (degrees)']
height = df['altitude (meters)']
temp = df['TEMP']

maxAlt = getMaxCol('altitude (meters)')
launch = getLaunchSite('latitude (degrees)', 'longitude (degrees)')
recovery = getRecoverySite('latitude (degrees)', 'longitude (degrees)')
dist = distanceTraveled('latitude (degrees)', 'longitude (degrees)', 'altitude (meters)')

print(f'MAX ALT: {maxAlt}')
print(f'LAUNCH SITE: {launch}')
print(f'RECOVERY SITE: {recovery}')
print(f'DIST TRAVELED: {dist}')

tracker(lat, lon, height, temp)
