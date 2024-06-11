from screen_setup import ScreenSetUp
from turtle import Turtle, Screen
from layout import Layout
from turtle_crossing import TurtleCrossing
import time

WIDTH = 500
HEIGHT = 100
NUM_LANES = 5

screen_setup = ScreenSetUp(WIDTH, NUM_LANES)
screen = Screen()
screen.tracer(0)
layout = Layout(WIDTH, HEIGHT )
game = TurtleCrossing(WIDTH, HEIGHT)




run = True

while run:
    screen.update()
    game.move_car()
    time.sleep(0.4)
    







    screen.listen()
screen.exitonclick()






