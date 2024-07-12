# -*- coding: utf-8 -*-
"""sales Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AzLvX4N-xHsg5pcSy8zfhErbypcU7NMI
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("/archive.zip")

data.fillna(data.mean(), inplace=True)

X = data[['TV']]  # Features
y = data['Sales']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Now you can predict
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

new_data = pd.DataFrame({'TV': [1000]})
predicted_sales = model.predict(new_data)
print(f'Predicted Sales for TV of 1000: {predicted_sales[0]}')