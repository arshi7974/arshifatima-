# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:42:00 2024

@author: lenovo
"""

a = 'Arshi Fatima'
#incresing pattern
for i in range(1,len(a)+1):
    print(a[:i])
    
#decreasing pattern
for i in range(len(a)-1,0,-1):
    print(a[:i])