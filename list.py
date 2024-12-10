# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:16:53 2024

@author: lenovo
"""

data = [23, 45, 12, 67, 34]
data.append(89)  # Add an item
data.remove(45)
print("show list  with append and remove:-",data)

stack = []
stack.append('a')  # Push onto stack
stack.append('b')
print("Show Stack:-",stack)
print("Show Stack with pop :-",stack.pop())

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum of all numbers: {total}")

results = []
for i in range(10):
    results.append(i * i)
print("Show Lists:-",results)

sentence = "Python lists are powerful"
words = sentence.split()
for word in words:
    print(word.upper())
    