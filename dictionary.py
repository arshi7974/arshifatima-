# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:21:33 2024

@author: lenovo
"""

elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for item in elements:
    frequency[item] = frequency.get(item, 0) + 1
    print(frequency)
    
lookup = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen'
}
currency_name = lookup.get('USD')  
print(currency_name)

data = [
    {'name': 'Alice', 'department': 'HR'},
    {'name': 'Bob', 'department': 'IT'},
    {'name': 'Charlie', 'department': 'HR'},
    {'name': 'David', 'department': 'IT'}
]

grouped = {}
for item in data:
    department = item['department']
    if department not in grouped:
        grouped[department] = []
    grouped[department].append(item['name'])
    print(grouped)