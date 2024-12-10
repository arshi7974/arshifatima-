# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:36:56 2024

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data: Size of houses (in square feet) and their prices (in thousands)
X = np.array([[1000], [1500], [2000], [2500], [3000]])  # Input feature: house size
y = np.array([250, 300, 350, 400, 450])  # Output: house price

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new house size
predicted_price = model.predict([[2200]])

# Plotting the data and the linear regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title("House Price Prediction")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price (in thousands)")
plt.show()

print(f"Predicted price for a 2200 sq ft house: ${predicted_price[0]} thousand")