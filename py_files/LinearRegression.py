"""SIMPLE LINEAR REGRESSION"""

"""There are 5 basic steps when you're implementing linear regression:

    1) Import the packages and classes you need
    2) Provide data to work with and eventually do appropriate transformations.
    3) Create a regression model and fit it with existing data.
    4) Check the results of model fitting to know whether the model is satisfactory.
    5) Apply the model for predictions."""

###################################
# 1: Import packages and classes
###################################

import numpy as np
from sklearn.linear_model import LinearRegression


###################################
# 2 Provide Data
###################################

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# You should call the .reshape() method on x, because this array is required to be two-dimensional,
# or to be more precise, to have one column and as many rows as necessary.


###################################
# 3: Create a model and fit it
###################################

model = LinearRegression()
# Creates an instance of a LinearRegression object

"""You can provide several optional parameters to LinearRegression:

    1) fit_intercept: Is a Boolean (True by default) that decides whether to calculate the intercept,
     or consider it equal to 0.
    2) normalize: Is a Boolean (False by default) that decides whether to normalise the input variables or not.
    3) copy_X: Is a Boolean (True by default) that decides whether to copy or overwrite the input variables.
    4) n_jobs: Is an integer or None (default) and represents the number of jobs used in parallel computation.
        None usually means one job, and -1 to use all processors."""

model.fit(x, y)
# With fit(), you calculate the optimal values of the weights (slopes), using the existing input and output (x & y),
# as the arguments. In other words, .fit() fits the model.
# It returns self, which is the variable model itself.


###################################
# 4: Get Results
###################################

# You can obtain the coefficient of determination (R-Squared) with the .score() method.
# This measures how much of the variance in y is explained by x.


r_squared = model.score(x, y)
print("coefficient of determination: ", r_squared)
# When you're applying the .score() method, the arguments are also the predictor 'x' and the response 'y'.


# The attributes of the model are '.intercept_' and '.coef_'
intercept = model.intercept_
print("Intercept is: ", intercept)

slope = model.coef_
print("Coefficient is: ", slope)


###################################
# 5: Predict Response
###################################

# Once there is a satisfactory model, you can use it for predictions with either existing or new data

y_pred = model.predict(x)
print("Predicted response: ", y_pred, sep="\n")


#####################################################################################################################
#####################################################################################################################

"""MULTIPLE LINEAR REGRESSION"""

"You can implement multiple linear regression following the same steps as you would for simple regression"

###################################
# 1 & 2: Import Packages and provide data
###################################

x = [[0, 1], [5, 1], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

x, y = np.array(x), np.array(y)

# In Multiple Linear Regression, x is a two-dimensional array with at least two columns,
# while y is usually a one-dimensional array. This is a simple example of Multiple Linear Regression.


###################################
# 3: Create a model and fit it
###################################

model = LinearRegression()

model.fit(x, y)


###################################
# 4: Get Results
###################################

r_squared = model.score(x, y)
print("Coefficient of Determination: ", r_squared)

intercept = model.intercept_
print("Intercept: ", intercept)

slopes = model.coef_
print("Coefficients are: ", slope)

# Notice how now we have two slope results representing our two x/independent/predictor variables.


###################################
# 5: Predict Results
###################################

y_pred = model.predict(x)
print("Predicted Response: ", y_pred, sep='"\n')


#####################################################################################################################
#####################################################################################################################
"POLYNOMIAL REGRESSION WITH SCIKIT-LEARN"

"""Implementing polynomial regression with scikit-learn is very similar to linear regression.
There is only one extra step:
    You need to transform the array of inputs to include non-linear terms such as x-squared"""

###################################
# 1: Import Packages
###################################

# You will now need to import the class 'PolynomialFeatures' from sklearn.preprocessing

from sklearn.preprocessing import PolynomialFeatures


###################################
# 2: Provide data
###################################

x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([15, 11, 2, 8, 25, 32])

# Keep in mind, you need the input (x) to be a two-dimensional array, hence the reshape() method.

# Transform the input data.
"""This is the new step you need to implement for polynomial regression!
        - You need to include x-squared, as an additional feature when implementing polynomial regression
        - For that reason you should transform the input array 'x', to contain the additional column(s) with the
        - values of x-squared (and eventually more features)"""

transformer = PolynomialFeatures(degree=2, include_bias=False)

# The variable 'transformer' refers to an instance of PolynomialFeatures which you can use to transform the input 'x'.

"""You can provide several optional parameters to PolynomialFeatures:
        1) degree=: Is an integer (2 by Default) that represents the degree of the polynomial regression function
        2) interaction_only: Is a Boolean (False by Default) that decides whether to include only interaction features,
            or all features (False)
        3) include_bias=: Is a Boolean (True by Default) that decides whether to include the bias (intercept) column
            of ones (True) or not (False)"""

# This example uses all the defaults, but it can help to experiment with the degree of a function.

# Before applying the transformer, you'll need to fit it with .fit()
transformer.fit(x)

# Once the transformer is fitted, it's ready to create a new, modified input.
x_ = transformer.transform(x)

print(x_)
# The modified input array contains two columns now, one with the original inputs and the other with their
# corresponding squared values.


###################################
# 3: Create a model and fit it.
###################################

model = LinearRegression()

model.fit(x_, y)

# Keep in mind that the first argument in fit() is our modified array input of x, not the original.


###################################
# 4: Get Results
###################################

# You can obtain the properties of the model as in the same way as Linear Regression.

r_squared = model.score(x_, y)
print("Coefficient of Determination: ", r_squared)

intercept = model.intercept_
print("Intercept is: ", intercept)

slope = model.coef_
print("Coefficient is: ", slope)


###################################
# 5: Predict Response
###################################

y_pred = model.predict(x_)

print("Predictions are: ", y_pred, sep="\n")


#####################################################################################################################
#####################################################################################################################
"ADVANCED LINEAR REGRESSION WITH STATSMODELS"

"""You can implement linear regression in python relatively easily by using the package statsmodels as well.
Typically, this is desirable when there is a need for more detailed results"""


###################################
# 1: Import Packages
###################################

import statsmodels.api as sm


###################################
# 2: Provide data and transform inputs
###################################

# You can provide inputs and outputs the same way as when you were using scikit-learn

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 1], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

x, y = np.array(x), np.array(y)

# You will need to add the column of ones to the inputs if you want statsmodels to calculate the intercept.
x = sm.add_constant(x)
print(x)

# That is how you add the column of ones to x.
# It takes the input array 'x' as an argument and returns a new array with the column on ones inserted at the beginning.
# You can now see that x has three columns with the first one replacing the intercept.


###################################
# 3: Create a model and fit it
###################################

# The regression model based on Ordinary Least Squares is an instance of the class;
# 'statsmodels.regression.linear_model.OLS'

model = sm.OLS(y, x)

# BE CAREFUL - The first argument is the output (y), not the input (x)

results = model.fit()
# This object holds a lot of information about the regression model.


###################################
# 4: Get Results
###################################

"""The variable 'results' refers to the object that contains detailed information about the results of the regression.
You can call .summary() to get the table with the results of the regression"""

print(results.summary())

# The table is very comprehensive. You can find values associated with Linear Regression including R-Squared, b0, b1, b2
# In this particular case, you may get the warning related to 'kurtosistest'.
# This is due to the small number of observations provided.

# You can extract any of the results from the table above like so;
r_squared = results.rsquared
print("Coefficient of determination: ", r_squared)

adjusted_r_squared = results.rsquared_adj
print("Adjusted Coefficient of Determination: ", adjusted_r_squared)

regr_slopes = results.params
print("Regression Coefficients: ", regr_slopes)


###################################
# 5: Predict Response
###################################

# You can obtain the predicted response on the input values used for creating the model using the .fittedvalues or
# .predict() method with the input array as the argument.

print("Predicted responses: ", results.fittedvalues, sep="\n")
print("Predicted responses: ", results.predict(x), sep="\n")


#######################################################################################################################
#######################################################################################################################
""" Linear Regression is sometimes not appropriate, especially for non-linear models of high complexity

Fortunately, there are other regression techniques suitable for the cases where linear regression doesn't work well.
Some of them are Support Vector Machines, Decision Trees, Random Forest, and Neural Networks.

The package scikit-learn provides the means for using other regression techniques in a very similar way that was done 
above. It contains the classes for Support Vector Machines, Decision Trees, Random Forests and more with the methods;
    - .fit()
    - .predict()
    - .score()
    
"""