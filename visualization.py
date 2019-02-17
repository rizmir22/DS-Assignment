# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 06:51:08 2019

@author: Nuwanthi
"""

#This outputs different types of visualization diagrams

import pandas as pd
# Import the module for plotting
import matplotlib.pyplot as plt
# Import the seaborn library
import seaborn as sns

# Reading data locally
df = pd.read_csv('D:\\MSc\\Sem1\\DS\\Assignment\\PSID (1).csv')

plt.style.use('ggplot') # Sets the plotting display theme to ggplot2
plt.show(df.plot(kind = 'box'))

plt.show(sns.distplot(df.ix[:,5], rug = True, bins = 15))

with sns.axes_style("white"):
    plt.show(sns.jointplot(df.ix[:,5], df.ix[:,6], kind = "kde"))
    
plt.show(sns.lmplot("earnings", "hours", df))
