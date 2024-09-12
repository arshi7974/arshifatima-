# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:56:30 2024

@author: lenovo
"""

import turtle
t = turtle.Turtle()
t.speed(0.5)
t.pensize(1)

t.penup()
t.goto(-250,250)
t.pendown()
t.color("black")

for i in range(1000):    
  t.left(90)
  t.circle(100,180)
  t.left(90)
  t.forward(200)
  t.right(120)
  t.forward(250)
  t.right(130)
  t.forward(235)
  t.left(293)
   
   