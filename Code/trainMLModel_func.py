#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow as tf
from tf.keras import models, layers
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
import RidgeRegression, RidgeRegressionMod
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from random import randrange
import LinearRegression,LinearRegressionMod
import RandomForest, Bagging, BaggingClassifier
import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier as DecTree
from sklearn.ensemble import BaggingClassifier as BagClass

%matplotlib inline

class Regression():
    def RidgeRegression(xTrain,yTrain):
        RepFold = RepeatedKFold(n_splits=25, random_state=40)
        if (RepFold>=0):
            RidgeRegressionMod = RepFold(cv=cv,alphas=arange(0, 1, 0.01))
            RidgeRegressionMod.fit(xTrain,yTrain)
        y_pred = RidgeRegressionMod.intercept_ + np.sum(RidgeRegressionMod.coef_ * X, axis=1)

    def LinearRegression(xTrain,yTrain):
        from sklearn.linear_model import LinearRegression
        LinearRegressionMod = LinearRegression().fit(xTrain,yTrain)
        if (LinearRegressionMod==True):
            ScoreLR = LinearRegressionMod.score(X, y)
            coefficientsLR,interceptLR = LinearRegressionMod.coef_, LinearRegressionMod.intercept_

    def Bagging(xTrain,yTrain):
        baggClass = BaggingClassifier(DecTree(),n_estimators=250,n_jobs=-1,bootstrap=True)
        baggClass.fit(xTrain,yTrain)
    
    def RandomForest(xTrain,yTrain):
        from sklearn.ensemble import RandomForestRegressor
        RandomForestClassifier=RandomForestRegressor(n_estimators=100, min_sample_leaf=5, max_depth)
        RandomForestClassifier.fit(xTrain,yTrain)
