# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:04:16 2018

@author: u344788
"""

dt = 0.1
s = 1

for t in range(0,4):
    s = s*1.*(1-10*dt)
    
    print ("system at:",t+1,s)