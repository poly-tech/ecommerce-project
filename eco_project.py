# -*- coding: utf-8 -*-
"""02-Linear Regression Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bqL75WHkO87C7XCDxgxT2UlbYVzIhQo3

___

<a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
___
# Linear Regression Project

Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.

The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out! Let's get started!

Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails).
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

eco = pd.read_csv('Ecommerce Customers')

eco.head()

eco.describe()

eco.info()

"""## Exploratory Data Analysis

**Let's explore the data!**

For the rest of the exercise we'll only be using the numerical data of the csv file.
___
**Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?**
"""

eco.head()

sns.jointplot(x = 'Time on Website', y ='Yearly Amount Spent', data = eco)

sns.jointplot(x = 'Time on App', y ='Yearly Amount Spent', data = eco)

"""** Do the same but with the Time on App column instead. **"""

sns.jointplot(x = 'Time on App', y ='Length of Membership', data = eco, kind = 'hex')

"""** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**"""

sns.pairplot(eco)

"""**Let's explore these types of relationships across the entire data set. Use [pairplot](https://stanford.edu/~mwaskom/software/seaborn/tutorial/axis_grids.html#plotting-pairwise-relationships-with-pairgrid-and-pairplot) to recreate the plot below.

"""



"""**Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?**"""

sns.lmplot(x= 'Length of Membership', y= 'Yearly Amount Spent', data = eco)

"""**Create a linear model plot (using seaborn's lmplot) of  Yearly Amount Spent vs. Length of Membership. **"""

eco.columns

"""## Training and Testing Data

Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **
"""

X = eco[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

y = eco['Yearly Amount Spent']

"""** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)



"""## Training the Model

Now its time to train our model on our training data!


"""

from sklearn.linear_model import LinearRegression

"""**Create an instance of a LinearRegression() model named lm.**"""

lm = LinearRegression()

"""** Train/fit lm on the training data.**"""

lm.fit(X_train, y_train)

"""**Print out the coefficients of the model**"""

lm.coef_

"""## Predicting Test Data
Now that we have fit our model, let's evaluate its performance by predicting off the test values!


"""

pr = lm.predict(X_test)

"""** Create a scatterplot of the real test values versus the predicted values. **"""

sns.scatterplot(x = y_test , y= pr)

"""## Evaluating the Model

Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

"""

from sklearn.metrics import mean_squared_error, mean_absolute_error

print(f"Mae : {mean_absolute_error(y_test, pr)}")
print(f"Mse : {mean_squared_error(y_test, pr)}")
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, pr))}")

sns.displot(y_test - pr, kde = True , bins = 50)

pd.DataFrame(index = ['Avg. Session Length', 'Time on App', 'Time on Website','Length of Membership'], data = lm.coef_ , columns = ['coefficien'])

"""So let's try to boost our custumors time on app"""