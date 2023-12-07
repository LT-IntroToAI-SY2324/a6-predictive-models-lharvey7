import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_swaured_error, r2_score







model = linear_model.LinearRegression().fit(xtrain, ytrain)