# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:05:01 2019

@author: Nuwanthi
"""

import pandas as pd

# Reading data locally
df = pd.read_csv('D:\\MSc\\Sem1\\DS\\Assignment\\PSID (1).csv')

#Head of the data
print (df.head())

#Tail of the data
print (df.tail())

#Extracting column names
print (df.columns)

#Extracting row names or the index
print (df.index)

#Transpose data
print (df.T)