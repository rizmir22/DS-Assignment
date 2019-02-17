# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 05:47:29 2019

@author: Nuwanthi
"""

#Generate samples of size 50 from distribution with  μ  = 3 and  σ2  = 5;
#Use the 95% confidence level;
#Repeat the process 100 times; then
#Compute the percentage of the confidence intervals containing the true mean.

import numpy as np
import scipy.stats as ss

def confidenceLevel(n = 50, mu = 14244.5, sigma = np.sqrt(11000), p = 0.025, rep = 100):
    scaled_crit = ss.norm.ppf(q = 1 - p) * (sigma / np.sqrt(n))
    norm = np.random.normal(loc = mu, scale = sigma, size = (rep, n))
    
    xbar = norm.mean(1)
    low = xbar - scaled_crit
    up = xbar + scaled_crit
    
    rem = (mu > low) & (mu < up)
    m = np.c_[xbar, low, up, rem]
    
    inside = np.sum(m[:, 3])
    per = inside / rep
    
    
    desc = "There are " + str(inside) + " confidence intervals that contain " \
           "the true mean (" + str(mu) + "), that is " + str(per) + " percent of the total CIs"
    return {"Matrix": m, "Decision": desc}

print(confidenceLevel())