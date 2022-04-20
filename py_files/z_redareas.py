# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:50:42 2020

@author: Danilo.Bento
"""
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\Users\alexk\Documents\ICON\Results_RedAreas.csv')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df.dtypes)
df['RedAreas (M_AREA)'] = df['RedAreas (M_AREA)'].fillna(0)

smallred = df.loc[df['RedAreas (M_AREA)'] < 0.12]
bigred = df.loc[df['RedAreas (M_AREA)'] < 0.12]

# =============================================================================
# DESCRIPTIVE STATS
# =============================================================================
df['Red Areas'].value_counts()
df.loc[df['Red Areas'] == 'Yes'].mean()
df.loc[df['Red Areas'] == 'No'].mean()
df.describe(include='all').round(2)
df['RedAreas (M_AREA)'].describe()


# =============================================================================
# BOX PLOTS 
# =============================================================================
sns.boxplot(x=df["Red Areas"], y=df["avgPred"])
sns.boxplot(x=df["Red Areas"], y=df["stdPred"])
sns.boxplot(x=df["Red Areas"], y=df["minPred"])

# =============================================================================
# CORRELATIONS
# =============================================================================
df['RedAreasPresent'] = np.nan
df.loc[(df['Red Areas']=="Yes"),'RedAreasPresent'] = 1
df.loc[(df['Red Areas']=="No"),'RedAreasPresent'] = 0
sum(df['RedAreasPresent'])

pea = df.corr(method='pearson')
sns.heatmap(pea, 
            xticklabels=pea.columns.values,
            yticklabels=pea.columns.values, 
            cmap="YlGnBu",
            annot=True)

spe = df.corr(method='spearman')
sns.heatmap(spe, 
            xticklabels=spe.columns.values,
            yticklabels=spe.columns.values, 
            cmap="YlGnBu",
            annot=True)

# =============================================================================
# REGRESSIONS
# =============================================================================

# Single
x = np.array(df['avgPred']).reshape((-1, 1))
y = np.array(df['RedAreasPresent']) 

model = LinearRegression().fit(x, y)
print('coefficient of determination:', model.score(x, y))
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# Multiple
x = np.array(df[['M_AREA', 'RedAreas (M_AREA)','avgPred',
                 'minPred', 'maxPred', 'stdPred']])
y = np.array(df['RedAreasPresent']) 

model = LinearRegression().fit(x, y)
print('coefficient of determination:', model.score(x, y))
# get importance
importance = model.coef_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))

