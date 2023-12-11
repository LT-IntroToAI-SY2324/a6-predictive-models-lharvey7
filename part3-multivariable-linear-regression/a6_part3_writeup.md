# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The r-squared coefficient for my model is about 0.86. The r-squared tells you how accurate your model is at predicting the relationship between the data, and an r-squared value of 0.86 means that it is quite accurate at predicting the correlation and is thus quite a strong relationship.
2. Is your model accurate? Why or why not?

This model is accurate because it has an r-squared value of 0.86, and therefore an r-value of around 0.93. The r-squared value is pretty close to one, which means it is an accurate model.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

The model predicts a 10-year-old car with 89,000 miles is worth about $9,270. It predicts a 20-year-old car with 150,000 miles to be worth about $2,440.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

I think this is happenng because the model is not perfect. The relationship is being represented as linear in our model, when in reality the relationship that actually exists is not going to be perfectly linear, as r-quared is not 1. This means that the model is really only an approximation of the actual values in the relationship, and therfore will produce results that are slightly inaccurate, like values that are slightly below zero. 