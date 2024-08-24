# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:05:44 2024

@author: lenovo
"""

import turtle
t = turtle.Turtle()
t.speed(0.5)
t.pensize(1)


t.pendown()
t.color("black")

for i in range(1000):    
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.left(90)
    t.left(87)
