import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



data = pd.read_csv("data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y ,test_size = .2)
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)
print(xtrain, ytrain)
# Create the model
model = LinearRegression().fit(xtrain, ytrain)

coef = round(float(model.coef_), 2)
r_squared = model.score(xtrain, ytrain)
intercept = round(float(model.intercept_), 2)
# Print out the linear equation and r squared value:
print("Model's Linear Equation: y=",coef, "x=", intercept)
print("R Squared value:", r_squared)


print(xtest)
xtest = xtest.reshape(-1, 1)
print("this is the xtest", xtest)

# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)


# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)


# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
print("x value:", float(x_coord), "Predicted Y Value: ", predicted_y, "Actual Y Value: ", actual)


