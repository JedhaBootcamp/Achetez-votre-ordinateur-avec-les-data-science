# -*- coding: utf-8 -*-
"""
Written in May 2018 by Guillaume Vilain for Jedha Bootcamp
"""

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as mat

# import Dataset 
dataset = pd.read_csv("PrixOrdiOccaz.csv")
X = dataset.iloc[:,[6,8,9,11,12,13,14,15,18,19,20,21,22,23,25,26,28,30,31,32,33]].values
Y = dataset.iloc[:,1].values

                
# Missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= "NaN", strategy="mean", axis=0)
imputer.fit(X[:,[0,2,3,4,6,10,12,13,14,15,16,17,20]])
X[:,[0,2,3,4,6,10,12,13,14,15,16,17,20]] = imputer.transform(X[:,[0,2,3,4,6,10,12,13,14,15,16,17,20]])

# Encoding Categorical Variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,1]= labelencoder_X.fit_transform(X[:,1])
labelencoder_X = LabelEncoder()
X[:,5]= labelencoder_X.fit_transform(X[:,5])
labelencoder_X = LabelEncoder()
X[:,7]= labelencoder_X.fit_transform(X[:,7])
labelencoder_X = LabelEncoder()
X[:,8]= labelencoder_X.fit_transform(X[:,8])
labelencoder_X = LabelEncoder()
X[:,9]= labelencoder_X.fit_transform(X[:,9])
labelencoder_X = LabelEncoder()
X[:,11]= labelencoder_X.fit_transform(X[:,11])
labelencoder_X = LabelEncoder()
X[:,18]= labelencoder_X.fit_transform(X[:,18])
labelencoder_X = LabelEncoder()
X[:,19]= labelencoder_X.fit_transform(X[:,19])
Xprep=X.astype(float)
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X=np.delete(X, (5), axis=1)
XprepA=X.astype(float)
onehotencoder = OneHotEncoder(categorical_features=[13])
X = onehotencoder.fit_transform(X).toarray()
X=np.delete(X, (3), axis=1)
XprepB=X.astype(float)
onehotencoder = OneHotEncoder(categorical_features=[17])
X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
XprepC=X.astype(float)
onehotencoder = OneHotEncoder(categorical_features=[19])
X = onehotencoder.fit_transform(X).toarray()
X=np.delete(X, (1), axis=1)
XprepD=X.astype(float)
onehotencoder = OneHotEncoder(categorical_features=[22])
X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
XprepE=X.astype(float)

onehotencoder = OneHotEncoder(categorical_features=[27])
X = onehotencoder.fit_transform(X).toarray()
X=np.delete(X, (3), axis=1)
Xprep2=X.astype(float)

# Ajouter une constante 1
import statsmodels.formula.api as sm
X = np.append(arr=np.ones((26,1)).astype(int), values =X, axis =1)
Xprep3=X.astype(float)

# Regression linéaire multi-variable à coefficients positifs (positive=True)
from sklearn.linear_model import Lasso
lin = Lasso(precompute=True,max_iter=1000,
            positive=True, random_state=9999, selection='random')
Ylin=lin.fit(X,Y)
res=lin.coef_
sparse = lin.sparse_coef_.astype(float)
