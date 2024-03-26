from flask import Flask, render_template, request
import pickle
import numpy as np
import csv

app = Flask(__name__)

# Load the pre-trained model
with open('linear_regression.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset
dataset = []
with open('Air_Quality1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Define route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the request form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        wind_speed = float(request.form['wind-speed'])
        pollutant_emissions = float(request.form['pollutant-emissions'])

        # Make prediction
        input_data = np.array([[temperature, humidity, wind_speed, pollutant_emissions]])
        prediction = model.predict(input_data)[0]

        # Get the corresponding air quality index from the dataset
        air_quality_index = get_air_quality_index(temperature, humidity, wind_speed, pollutant_emissions)

        # Render the template with prediction result and air quality index
        return render_template('index.html', prediction=prediction, air_quality_index=air_quality_index)
    else:
        # Render the template for the initial page load
        return render_template('index.html')

# Function to get air quality index from the dataset
def get_air_quality_index(temperature, humidity, wind_speed, pollutant_emissions):
    for row in dataset[1:]:
        if float(row[0]) == temperature and float(row[1]) == humidity and float(row[2]) == wind_speed and float(row[3]) == pollutant_emissions:
            return row[4]  # Return the air quality index value from the dataset

if __name__ == '__main__':
    app.run(debug=True)
