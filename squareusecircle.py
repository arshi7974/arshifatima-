# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:34:21 2024

@author: lenovo
"""

import turtle
t = turtle.Turtle()
t.speed(0.5)
t.pensize(1)

t.pendown()
t.color("brown")
    
for i in range(1000):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.left(67)
