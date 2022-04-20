import pandas as pd
import numpy as np
from array import *
import scipy.stats
import matplotlib.pyplot as plt

# Create your two arrays (Two variables needed to test correlation)
# Both arrays need to be same length

x = np.arange(1, 50, 10)
y = array('i', [65, 72, 88, 96, 100])

# Perform the correlation:
# corrcoef() returns the correlation matrix, which is a two-dimensional array with the correlation coefficients.

correlation = np.corrcoef(x, y)
print(correlation)

# Use the Scipy.stats package to calculate {1:Pearson's r. 2: Spearman's r, 3:Kendall Tau}
# Note: These functions return two values (Correlation Coefficient / p-value)

Pearson_r = scipy.stats.pearsonr(x, y)
print(Pearson_r)

Spearman_r = scipy.stats.spearmanr(x, y)
print(Spearman_r)

Kendall_Tau = scipy.stats.kendalltau(x, y)
print(Kendall_Tau)

# ======================================================================================================================
# ======================================================================================================================

# Pandas walkthrough of Correlation
x = pd.Series(range(10,20))
y = pd.Series([2, 45, 34, 56, 78, 12, 90, 111, 14, 78])

# Pearson's r
x.corr(y)
y.corr(x)

# Spearman's rho
x.corr(y, method='spearman')

# Kendall's tau
x.corr(y, method='kendall')

# Here you use the 'corr()' method to calculate all three correlation coefficients. You define the desired statistic,
# with the parameter method=, which can take on one of several values.
# 'pearson'
# 'spearman'
# 'kendall'
# a callable

# The callable can be any function, method, or object with .__call__() that accepts two 'one-dimensional' arrays
# and returns a floating point number.


# =====================================================================================================================
# =====================================================================================================================

# Linear Correlation
# measures the proximity of the mathematical relationship between variables or dataset features to a linear function.
# if the relationship between the two features is closer to some linear function, then their linear correlation
# is stronger and the absolute value of the correlation coefficient is higher.

# Linear Regression
x = np.arange(1, 50, 10)
y = array('i', [65, 72, 88, 96, 100])

result = scipy.stats.linregress(x, y)
slope = result.slope
print("\nSlope is {}".format(slope))
intercept = result.intercept
print(intercept)
rvalue = result.rvalue
print(rvalue)
pvalue = result.pvalue
print(pvalue)
stderr = result.stderr
print(stderr)

# lineregress will return the same result if you provide the 'transpose' of xy, or a NumPy array with 10 rows and two
# columns. In NumPy, you cna transpose a matrix in many ways:
# - transpose()
# - .transpose()
# - .T

# You should also be careful and make sure your data contains no missing features/values. In data science and
# machine learning, you'll often find some missing values. The usual way to represent it in Python, NumPy, SciPy and
# Pandas is by using NaN, or Not a Number values. But if your data contains nan values,
# then you won't get a useful result with linregress()

# Note, by default, numpy.corcoef() considers the rows as features and the columns as observations.
# If you want the opposite behaviour, which is widely used in machine learning, then use the argument 'rowvar=False'.

# =====================================================================================================================
# =====================================================================================================================

# Pearson Correlation : Pandas Implementation
# Series Objects:
x = pd.Series(range(10, 20))
y = pd.Series([23, 45, 67, 34, 71, 83, 94, 103, 405, 79])
z = pd.Series([-23, 56, 81, 302, -12, -3, 76, 34, 12, 134])

# Data Frame Objects:
xy = pd.DataFrame({'x-values': x, 'y-values': y})
xyz = pd.DataFrame({'x-values': x, 'y-values': y, 'z-values': z})

# You now have three Series objects (x, y, z), and two DataFrame objects (xy, xyz)
# If you provide a nan value, then .corr() will still work, but it will exclude observations that contain nan values.
# Note : When you work with DataFrame instances, you should be aware that the rows are observations and the columns are
# the features. This is consistent with the usual practice in machine learning.

# You can also use .corr() with DataFrame objects. You can use it to get the correlation matrix for the columns.
print()
corr_matrix = xy.corr()
print(corr_matrix)
# The resulting correlation matrix is a new instance of DataFrame and holds the correlation coefficients for the columns
# xy['x-values'] and xy['y-values']

# ======================================================================================================================
# ======================================================================================================================

# This example shows two ways of accessing values:
# 1) Use .at[] to access a single value by row and column labels.
# 2) Use.iat[] to access a value by the positions of its row and column.
# You can apply .corr() the same way with DataFrame objects that contain three or more columns:

print()
xyz_correlation = xyz.corr()
print(xyz_correlation)

# Another useful method is .corrwith(), which allows you to calculate the correlation coefficients between
# the rows or columns of one DataFrame object and another Series or DataFrame object passed as the first argument.

print()
xy_with_z_Correlation = xy.corrwith(z)
print(xy_with_z_Correlation)

# In this case the result is a new Series object with the correlation coefficient for the column xy['x-values'] and the
# values of z, as well as the coefficient for xy['y-values'] and z.
# .corrwith() has the optional parameter 'axis' that specifies whether columns or rows represent the features.
# The default value of axis is 0, and it also defaults to columns representing features.
# There is also a drop parameter, which indicates what to do with missing values.

# =====================================================================================================================
# =====================================================================================================================

# Rank Correlation:
# Compares the ranks or the orderings of the data related to two variables or dataset features.
# if the orderings are similar, then the correlation is strong, positive and high.
# However, if the orderings are close to reversed, then the correlation is strong, negative and low.
# In other words, rank correlation is concerned only with the order of values, not with the particular values
# from the dataset.

# You can use scipy.stats to determine the rank for each value in an array. First you'll import the libraries and
# create NumPy arrays.


x = np.arange(10, 20)
y = np.array([2, 1, 3, 5, 6, 12, 18, 15, 25, 96])
z = np.array([5, 3, 2, 1, 0, -2, -8, -11, -15, -16])

# Now that you have prepared the data, yu can determine the rank of each value in a
# NumPy array with scipy.stats.rankdata()

scipy.stats.rankdata(x)
scipy.stats.rankdata(y)
scipy.stats.rankdata(z)

# ======================================================================================================================
# ======================================================================================================================

# Rank Correlation : NumPy and SciPy
# You can calculate the Spearman correlation coefficient with scipy.stats.spearmanr():

result = scipy.stats.spearmanr(x, y)
print(result)
result.correlation
result.pvalue

rho, p = scipy.stats.spearmanr(x, y)

# As you can see you can access particular values in two ways:
# Using dot notation, and through unpacking.

xy = np.array([[2, 1, 3, 5, 6, 12, 18, 15, 25, 96],
               [5, 3, 2, 1, 0, -2, -8, -11, -15, -16]])
rho, p = scipy.stats.spearmanr(xy, axis=1)

# The optional parameter 'axis' determines whether columns (axis=0) or rows (axis=1) represent the features.
# The default behaviour is that the rows are observations and the columns are features.

# Another optional parameter 'nan_policy' defines how to handle nan values. It can take one of three values.
#   1) propogate = returns nan if there's a nan value among the inputs. This is the default behaviour
#   2) raise = raises a ValueError if there's a nan value among the inputs.
#   3) omit = ignores the observations with nan values.

# Rank Correlation:
# Pandas Implementation

# You can calculate the Spearman and Kendall correlation coefficients with Pandas. Just like before,
# you start by importing pandas and creating some Series and DataFrame instances.
# Unlike with SciPy, you can use a single two-dimensional data structure (a dataframe)


# =====================================================================================================================
# ======================================================================================================================

# Visualisation of Correlation.
# Learn how to visually represent the relationship between two features with an x-y plot.
# You'll also use heatmaps to visualise a correlation matrix.

# To get started import matplotlib.pyplot
# Use ply.stlye('ggplot') to set the style of the plots.

plt.style.use('ggplot')

x = np.arange(10, 20)
y = np.array([2, 1, 3, 5, 6, 12, 18, 15, 25, 96])
z = np.array([5, 3, 2, 1, 0, -2, -8, -11, -15, -16])
xyz = np.array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                [2, 1, 3, 5, 6, 12, 18, 15, 25, 96],
                [5, 3, 2, 1, 0, -2, -8, -11, -15, -16]])

# now that you've got your data, you are ready to plot.

# X-Y Plots with Regression
# First you'll see how to create an x-y plot with the regression line, its equation, and the
# Pearson correlation coefficient. You can get the slope and intercept of the regression line, as well as the
# correlation coefficient with lineregress()

slope, intercept, r, p, stderror = scipy.stats.linregress(x, y)

# You can also get the string with the equation of the regression line and the value of the correlation coefficient.
# f-strings are very convenient for this purpose.

line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
print(line)

# Now you create the x-y plot with plot.()

fi, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data Points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()

# The red squares represent the observations, while the blue line is the regression line.
# Its equation is listed in the legend, together with the correlation coefficient.

# ======================================================================================================================
# ======================================================================================================================

# Heatmaps of Correlation Matrices
# The correlation matrix can become really big and confusing when you have a lot of features.
# Fortunately, you can present it visually as a heatmap where each field has a color that corresponds to its value.
# You'll need the correlation matrix.

corr_matrix = np.corrcoef(xyz).round(decimals=2)
print(corr_matrix)

# It can be convenient for you to round the numbers in the correlation matrix with .round() as they're going to be
# shown on the heatmap
# Finally, create your heatmap with .imshow() and the correlation matrix as its argument.

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
ax.yaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
ax.set_ylim(2.5, -0.5)

