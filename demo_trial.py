# -*- coding: utf-8 -*-
"""Demo Trial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10vuhmJLbiRTrncjkIDz6u2Wp5KyhhZrN
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('Crops  - Merged Data.csv')
data = data.dropna()
 
# display top 5 values
data.head()

import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 


data = pd.read_csv('Crops  - Merged Data.csv')
x = np.array(data['year'],data['crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["total demand(D*F)(7 0's) in mmt"]))
plt.figure(figsize = (10,5))
plt.scatter(data["crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"],data["total demand(D*F)(7 0's) in mmt"])
plt.ylim(0)
plt.xlabel("Years")
plt.ylabel("total demand(D*F)(7 0's) in mmt")
plt.tight_layout()
plt.plot()

import random
 
# using list comprehension + randrange()
# to generate random number list
year = int(input("Enter your year value "))
crop = int(input("crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"))
val = np.array(year).reshape(1,-1)
pred =lr.predict(val)[0]
print("Your predicted demand is",pred)
data.head(10)

df = pd.read_csv('Crops  - Merged Data.csv')
print('Dimension of dataset= ', df.shape)
df.head()

X = df.values[:,0:4]  # get input values from first two columns
y = df.values[:, 6]  # get output values from last coulmn
m = len(y) # Number of training examples

print('Total no of training examples (m) = %s \n' %(m))

# Show only first 5 records
for i in range(20):
    print('X =', X[i, ], ', y =', y[i])

from sklearn import linear_model
model_ols =  linear_model.LinearRegression(normalize=True)
model_ols.fit(X,y) 
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=True)

coef = model_ols.coef_
intercept = model_ols.intercept_
print('coef= ', coef)
print('intercept= ', intercept)

predictedPrice = pd.DataFrame(model_ols.predict(X), columns=['Predicted Demand']) # Create new dataframe of column'Predicted Price'
actualPrice = pd.DataFrame(y, columns=['Actual Demand'])
actualPrice = actualPrice.reset_index(drop=True) # Drop the index so that we can concat it, to create new dataframe
df_actual_vs_predicted = pd.concat([actualPrice,predictedPrice],axis =1)
df_actual_vs_predicted.T

plt.scatter(y, model_ols.predict(X))
plt.xlabel('Demand From Dataset')
plt.ylabel('Demand Predicted By Model')
plt.rcParams["figure.figsize"] = (10,6) # Custom figure size in inches
plt.title("Demand From Dataset Vs Demand Predicted By Model")

pickle.dump(model_ols, open('crops_demand.pkl', 'wb'))

#year = 2021
#crop = 2
#population = 129.8
#demand = 18.0
#price = model_ols.predict([[year, crop, population, demand]])
#print('Predicted total demand for paddy in',year,' will be', price[0].round(4),'mmt')
