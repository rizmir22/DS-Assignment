# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 09:32:41 2019

@author: Nuwanthi
"""

import pandas as pd
import matplotlib.pyplot as pl

#file to read in
infile = 'D:\\MSc\\Sem1\\DS\\Assignment\\PSID (1).csv'

#pull data into NumPy dataframe
df = pd.read_csv(infile, sep=',', na_values='.')

#get slice of data - in this case, earnings and married - to use in boxplot
slice = df.iloc[:,[5,3]]

#gives individual boxplot with all step names
bp = slice.boxplot(column='earnings', by='age')
axes = pl.gca()
axes.set_ylim([0,250000])
pl.show()