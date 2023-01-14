#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json
import sys
import numpy as np
import pickle 
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import numbers
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier 
import statsmodels.api as sm

def model_knn(X_train,Y_train):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,Y_train)
    return knn

def model_kmeans(X_train,Y_train):
    kmeansMod = Kmeans(n_clusters=11, verbose=0, random_state=None, max_iter=20)
    kmeansMod.fit(X_train,Y_train)
    return kmeansMod
