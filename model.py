import pandas as pd
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
# Load the dataset
data = pd.read_csv('Air_Quality1.csv')

X = data[['Temperature', 'Humidity', 'Wind_Speed', 'Pollutant_Emissions']]
y = data['Air_Quality_Index']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model                  
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

with open('linear_regression.pkl','wb') as f:
    pickle.dump(model,f)

with open('linear_regression.pkl','rb') as f:
    load_model=pickle.load(f)
# Make predictions


mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
