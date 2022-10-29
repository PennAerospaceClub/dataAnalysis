from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    # df = pd.DataFrame({
    #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    #     "Amount": [4, 1, 2, 2, 4, 5],
    #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    # })

    # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    df = pd.read_csv (r'data/Test Data Analysis.csv')
    df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)'])

    lat = df['latitude (degrees)']
    lon = df['longitude (degrees)']
    height = df['altitude (meters)']

    df = {'latitude (degrees)': lat, 'longitude (degrees)': lon, 'height (meters)' : height}
    fig = px.scatter_3d(df, x = 'latitude (degrees)', y = 'longitude (degrees)', z = 'height (meters)', color = "height (meters)", 
                        color_continuous_scale=px.colors.sequential.Bluered.reverse())

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Flight Path"
    description = """
    A 3-d visualization of the flight path based on data collected from a high-altitude balloon.
    """
    return render_template('plot.html', graphJSON=graphJSON, header=header,description=description)