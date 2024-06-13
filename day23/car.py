from turtle import Turtle
import random as r


class Car(Turtle):

    COLORS = ['red','yellow','blue']
    def __init__(self, length):
        super().__init__()
        self.shapesize(1,length,0)
        self.color(self.COLORS[r.randint(0, len(self.COLORS) - 1)])


