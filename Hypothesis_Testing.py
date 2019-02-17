# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:13:29 2019

@author: Nuwanthi
"""
from scipy import stats as stat
import pandas as pd

# Reading data locally
df = pd.read_csv('D:\\MSc\\Sem1\\DS\\Assignment\\PSID (1).csv')


#Perform one sample t-test using 32872.5 as the true mean of earnings
print (stat.ttest_1samp(a = df.loc[:, 'earnings'], popmean = 32872.5))