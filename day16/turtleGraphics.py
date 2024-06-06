from turtle import *
import random as r

matt = Turtle()
matt.shape('turtle')
matt.color('green')

my_screen = Screen()
# my_screen.exitonclick()
for i in range(0,100):
    # matt.forward(r.randint(0,300))
    matt.goto(r.randint(0,300),r.randint(0,300))

