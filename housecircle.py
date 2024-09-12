# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:17:40 2024

@author: lenovo
"""

import turtle
t = turtle.Turtle()
t.speed(0.5)
t.pensize(1)

t.penup()
t.goto(-100,30)
t.pendown()
t.color("black")

for i in range(1000):
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.backward(150)
    t.left(150)
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(49)