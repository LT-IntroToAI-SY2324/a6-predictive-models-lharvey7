# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The model becomes less accurate when the Standard Scalar is commented out, as its r-squared value goes from around 0.86 to around 0. This happens because the Standard Scalar standardizes all of the data so it can be compared better, so when it is removed, the data point will be farther apart from each other and the model will be less accurate.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

The model with the Standard Scalar is more accurate, with an r-squared value of about 0.86. I think it is accurate enough for the given use case because the r-squared is close to one, and there are only two outcomes.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

