#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import json
import sys
import pickle
import numpy as np
from sklearn.externals import joblib
from Txn_cat_input import *
import pickle 
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import numbers
from sklearn.metrics import accuracy_score


df_train=pd.read_csv('SP500Train')
df_test=pd.read_csv('SP500Test')
def train():
    no_rolling=4
    rolling1=['01-01-2016','12-31-2017']
    rolling2=['04-01-2016','03-31-2018']
    rolling3=['07-01-2016','06-30-2018']
    rolling4=['10-01-2016','09-30-2018']
    for i in range(0,4):
        for window in rolling+str(i):
            if (df_train['year'].is in range (window)):
                lr=LinearRegression(df_train[df_train['year']>window[0]][0:3],df_train['close_price']) and df_train[df_train['year']<window[1]][0:3],df_train['close_price']))
                rr=RidgeRegression(df_train[df_train['year']>window[0]][0:3],df_train['close_price']) and df_train[df_train['year']<window[1]][0:3],df_train['close_price']))
                x_train=df_train[df_train['year']>window[0]][0:3] and df_train[df_train['year']<window[1]][0:3],df_train['close_price'])
                y_train=df_train[df_train['year']
                if (lr is None and rr is None):
                    bagging=Bagging(x_train,y_train)
                    rf=RandomForest(x_train,y_train)
    pickle.dump(lr,'linearReg.pickle')
    pickle.dump(rf,'randomForest.pickle')
    pickle.dump(bagging,'bagging.pickle')
    pickle.dump(rr,'ridgeReg.pickle')
    
def test():

    #--------------loading the model used for prediction---------------#
    print(".......................LOADING MODEL.....................")
    model= test_modelpath
    loaded_model_lr = joblib.load("linearReg.pickle")
    loaded_model_rr = joblib.load("ridgeReg.pickle")
    loaded_model_rf = joblib.load("randomForest.pickle")
    loaded_model_bagg= joblib.load("bagging.pickle")
    
    no_rolling=4
    rolling1=['01-01-2018','03-31-2018']
    rolling2=['04-01-2018','06-30-2018']
    rolling3=['07-01-2018','07-31-2018']
    rolling4=['10-01-2018','12-31-2018']
    for i in range(0,4):
        for window in rolling+str(i):
            if (df_test['year'].is in range (window)):
                x_test=df_test[df_test['year']>window[0]][0:3] and df_test[df_test['year']<window[1]][0:3],df_test['close_price'])
                y_test=df_test[df_test['year']
                y_pred_lr=loaded_model_lr.predict(x_test)      
                y_pred_rf=loaded_model_rf.predict(x_test)      
                y_pred_rr=loaded_model_rr.predict(x_test)      
                y_pred_bagging=loaded_model_bagg.predict(x_test)      
    
    
