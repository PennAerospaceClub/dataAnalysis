from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import os
import pandas as pd
import json
import plotly
import plotly.express as px
# from .scripts.flightPath import fp

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('data', 'uploads')
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'pachab'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('plot.html')

@app.route('/upload', methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        uploaded_df = request.files['uploaded-file']
        data_filename = secure_filename(uploaded_df.filename)
        uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))

        session['u_data'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)

        # get and parse csv
        data_file_path = session.get('u_data', None)

        uploaded_df = pd.read_csv(data_file_path)

        uploaded_df_html = uploaded_df.to_html()

        ## include df in render_template

        return render_template('plot.html')

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