from turtle import Turtle
from snake import GAME_SIZE_X , GAME_SIZE_Y , MOVE_TILES

PEN_SIZE = 10

class Walls:

    def __init__(self):
        self.width = GAME_SIZE_X + MOVE_TILES
        self.hight = GAME_SIZE_Y + MOVE_TILES
        self.draw_borders()

    
    def draw_borders(self):
        borders = Turtle()
        borders.pencolor('gray')
        borders.speed(2)
        borders.ht()
        borders.pensize(10)
        borders.penup()
        borders.setposition(self.width,-self.hight)
        borders.pendown()
        borders.goto(-self.width,-self.hight)
        borders.goto(-self.width,self.hight)
        borders.goto(self.width,self.hight)
        borders.goto(self.width,-self.hight)

    
        

