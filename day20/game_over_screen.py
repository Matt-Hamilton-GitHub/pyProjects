from turtle import Turtle
from snake import GAME_SIZE_X , GAME_SIZE_Y , MOVE_TILES

class GameOverScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('gray')
        self.speed(3)
        self.ht()
        self.pensize(20)
        self.penup()
        self.write("Game Over",align="center", font=('Arial', 25, 'bold'))


class ShowStat(Turtle):
    st = 0
    def __init__(self, stat, alg, pos, color, msg):
        self.st = stat
        super().__init__()
        self.clear()
        self.penup()
        self.ht()
        self.color(color)
        self.setposition(pos)
        self.write(f"{msg} {self.st}",align=alg, font=('Arial', 15, 'normal'))

    

    


   