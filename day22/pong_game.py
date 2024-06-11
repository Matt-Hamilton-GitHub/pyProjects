from turtle import Turtle, Screen
from game_layout import GameLayout
from pong import Pong
import time

WIDTH = 400
HEIGHT = 300

screen = Screen()
screen.tracer(0)

game = Pong(WIDTH, HEIGHT)

def move_up():
    game.update_position(25)

def move_down():
    game.update_position(-25)

GAME_OVER = False

x , y = 0, 0
while not GAME_OVER:

    screen.update()
    time.sleep(0.1)
    game.move_pong()

    screen.onkey(move_up,'w')
    screen.onkey(move_down,'s')

    screen.listen()