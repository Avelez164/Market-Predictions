# Linear Algebra
import numpy as np
# File manipulation
import pandas as pd
# ML for prediction
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class predict():

  def __init__(self, historical_data):
    self.historical_data = historical_data

  # Does the prediction
  # Returns: Predicted Price based on the days
  def predict(self, data, days):
    # Reshapes the data into one column
    x = np.arange(len(data)).reshape(-1, 1)
    y = data.values.reshape(-1, 1)

    # Splits the data for training and testing
    # 30% of the data for training, 70% for testing
    xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.3, random_state=1)

    # Makes a Linear Regression Model
    model = LinearRegression()
    model.fit(xTrain, yTrain)
    # Uses the model to predict the price on depending on 'days' parameter
    future = np.arange(len(data), len(data) + days).reshape(-1, 1)
    futurePrice = model.predict(future)

    #returns the future price based on 'days' parameter
    return futurePrice

  # Calls the predict function on data of only Opening Prices
  # Returns: Predicted Opening Price based on the days
  def predictOpening(self, days):
    openData = self.historical_data['Open']
    return self.predict(openData, days)

  # Calls the predict function on data of only Closing Prices
  # Returns: Predicted Closing Price based on the days
  def predictClosing(self, days):
    closingData = self.historical_data['Close']
    return self.predict(closingData, days)
