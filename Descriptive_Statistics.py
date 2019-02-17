# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:09:12 2019

@author: Nuwanthi
"""

import pandas as pd

# Reading data locally
df = pd.read_csv('D:\\MSc\\Sem1\\DS\\Assignment\\PSID (1).csv')

#Descriptive Statistics
print (df.describe())