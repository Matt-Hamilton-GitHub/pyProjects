from turtle import Screen, Turtle
import random as r
import time
from snake import Snake, screen_settings
from walls import Walls
from game_over_screen import GameOverScreen, ShowStat
from snake import GAME_SIZE_X , GAME_SIZE_Y , MOVE_TILES

GAME_OVER = False
SPEED = 0.1

dis_speed = 1
screen_settings
walls = Walls()
snake = Snake()
snake.generate_obstacle()

def move_right():
    snake.update_heading_pos('right')
   
def move_left():
    snake.update_heading_pos('left')

def move_up():
    snake.update_heading_pos('up')
   
def move_down():
    snake.update_heading_pos('down')

snake.add_food()
show_speed = ShowStat(snake.dis_speed, 'left',(-GAME_SIZE_X  , GAME_SIZE_Y - 10 ), 'white', 'Speed:')
show_score = ShowStat(snake.score, 'right',(GAME_SIZE_X , GAME_SIZE_Y - 10), 'white', 'Score:') 

ready = ShowStat('', 'left',(0  , 0 ), 'white', 'READY')
screen_settings.update()
time.sleep(1)
ready.clear()
ready = ShowStat('', 'left',(0  , 0 ), 'white', 'STEADY')
screen_settings.update()
time.sleep(1)
ready.clear()
ready = ShowStat('', 'left',(0  , 0 ), 'white', 'GO')
time.sleep(1)
screen_settings.update()
ready.clear()

while not GAME_OVER:


    screen_settings.update()
    time.sleep(snake.speed)
    snake.update_position()
    head_loc = snake.segments[0].position()
    GAME_OVER = snake.check_position(head_loc)

    
    show_speed.clear()
    show_score.clear()
    show_speed = ShowStat(snake.dis_speed, 'left',(-GAME_SIZE_X  , GAME_SIZE_Y - 10 ), 'white', 'Speed:')
    show_score = ShowStat(snake.score, 'right',(GAME_SIZE_X , GAME_SIZE_Y - 10), 'white', 'Score:')    

    screen_settings.onkeypress(move_right, 'd')
    screen_settings.onkeypress(move_left, 'a')
    screen_settings.onkeypress(move_up, 'w')
    screen_settings.onkeypress(move_down, 's')

    if GAME_OVER :
        show_game_over = ShowStat('', 'left',(0, 0), 'white', 'Game Over!')
    screen_settings.listen()


print('Game Over')
    
screen_settings.exitonclick()


