# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 05:38:48 2018

@author: u344788
"""

import numpy as np
import copy

x = np.zeros(12)


rules = {}

rules[(1,1,1)] = 0
rules[(1,1,0)] = 1
rules[(1,0,1)] = 1
rules[(1,0,0)] = 0
rules[(0,1,1)] = 1
rules[(0,1,0)] = 1
rules[(0,0,1)] = 1
rules[(0,0,0)] = 0

#print(rules)

x[9] = 1

print (x)

for i in range(0,9):
    x_temp = copy.deepcopy(x)
    for j in range(1,11):
        x_temp[j] = (rules[x[j-1],x[j],x[j+1]])
        
    x = copy.deepcopy(x_temp)

    print (i,":",x)