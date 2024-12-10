# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:45:46 2024

@author: lenovo
"""

import pandas as pd
a = {'Name': ['arshi','sita','geeta'],
     'Surname':['fatima','sahu','mishra'],
     'city':['Raipur','durg','mahasamund'],
     'marks':[30,50,60]}
b=pd.DataFrame(a)
print(b.loc[0,'Name'])