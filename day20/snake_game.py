from turtle import Screen, Turtle
import random as r

WIDTH, HIGHT = 500, 500
SNAKE_HEAD_LENGTH = 3
head_LENGTH = 0
POSITION_X = 0
POSITION_Y = 0
HEADING_ANGLE = 0
GAME_OVER = False
FOOD_TIMER = 0
BODY_LEN = 0
MOVE_TILES = 5
MOVES = {}
SNAKE = []


#SCREEN SETUP
screen = Screen()
screen.setup(WIDTH, HIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

#-------------------------

#SNAKE DEFAULT PARAMS
head = Turtle()
head.color('white')
head.shape('square')
head.shapesize(1,1,0)
head.penup()
head.speed(0)
SNAKE.append(head)


tail = Turtle()
tail.color('yellow')
tail.shape('square')
tail.shapesize(1,1,0)
tail.penup()
tail.speed(0)
SNAKE.append(tail)

food = Turtle()
food.shape('circle')
food.color('green')
food.shapesize(1,1,0)
food.penup()
food.hideturtle()

#--------------------------------

def update_position(s):
    idx = SNAKE.index(s)
    if idx != 0:
        idx -= 1
    


    pos = SNAKE[idx].position()
    if s.heading() == 0:
        s.setpos(pos[0] + MOVE_TILES ,pos[1])
    elif s.heading() == 90:
        s.setpos(pos[0],pos[1] + MOVE_TILES)
    elif s.heading() == 180:
        s.setpos(pos[0] - MOVE_TILES,pos[1])
    elif s.heading() == 270:
         s.setpos(pos[0] ,pos[1] - MOVE_TILES)


def update_heading(s, idx, m):
    idex = SNAKE.index(s)
    if s.position() in m.keys():
        new_heading = m.keys[s.position()]
        s.setheading(new_heading)
        update_position(s)
        


def add_tail():
    last_tail = SNAKE[len(SNAKE)-1] 
    size = last_tail.shapesize()[1] - 1
    last_pos = last_tail.position()
    new_tail = tail.clone()
    new_tail.st()
    new_tail.setheading(last_tail.heading())

    if last_tail.heading() == 0:
        new_tail.setpos(last_pos[0] - 20*size,last_pos[1])
    elif last_tail.heading() == 90:
        new_tail.setpos(last_pos[0],last_pos[1] - 25 *size)
    elif last_tail.heading() == 180:
        new_tail.setpos(last_pos[0] + 20 *size,last_pos[1])
    elif last_tail.heading() == 270:
        new_tail.setpos(last_pos[0],last_pos[1] + 20 *size)
    
    SNAKE.append(new_tail)

def add_food():
    food.hideturtle()
    food.setpos(r.randint(-WIDTH//2, WIDTH//2), r.randint(-HIGHT//2, HIGHT//2))
    food.showturtle()

def eat_food():
    if food.position() == head.position():
        food.hideturtle()
        add_tail()
        FOOD_TIMER = 0
        

def move_right():
    head.setheading(head.heading() - 90)
    print(head.position(), head.heading())
    MOVES[head.position()] = head.heading()
   
def move_left():
    head.setheading(head.heading() + 90)
    MOVES[head.position()] = head.heading()
    

add_food()
add_tail()
add_tail()
add_tail()
add_tail()
add_tail()
screen.listen()

p = 1
while not GAME_OVER:
    if p > len(SNAKE) - 1:
        p = 1
   
    for i in SNAKE:
        update_position(i)
        update_heading(i, p, MOVES)
    
    if not food.isvisible() and FOOD_TIMER == 500:
        add_food()
    eat_food()
    p+=1

    FOOD_TIMER+=1

    
    screen.onkeypress(move_right, 'd')
    screen.onkeypress(move_left, 'a')

screen.exitonclick()
