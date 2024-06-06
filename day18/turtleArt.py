from turtle import Turtle, Screen
import random as r

COLORS = ['purple2', 'red','green','yellow','#006400','#800080','#5F9EA0','#FFD700','#7FFFD4','#800000','#FFA500','#483D8B']


canvas = Screen()
canvas.screensize(1000, 1000)



def masterPiece():
    #GLOBAL SETTINGS
    X = 0
    Y = 0
    SIZE = 20
    SPACE = 50
    NUM_OF_SQ = 10


    tim = Turtle()
    tim.shape('turtle')
    tim.ht()
    tim.penup()
    tim.setx(100)
    tim.sety(100)
    for y in range(NUM_OF_SQ):
        X=0
        for _ in range(NUM_OF_SQ):
            # tim.goto(X,Y)
            tim.setx(X)
            tim.sety(Y)
            for _ in range(1):
                tim.forward(SPACE)
                tim.dot(SIZE,r.choice(COLORS))
            X+= SIZE + SIZE//2
        Y+=SIZE + SIZE//2
    tim.goto(X, Y + 30)
    tim.showturtle()

    
def drawChellange():
    NUM_OF_SIDES = 4
    SIZE = 100
    LAYERS = 15

    chack = Turtle()
    chack.ht()
    chack.pencolor('black')
    for _ in range(LAYERS):
        chack.pencolor(r.choice(COLORS))
        for _ in range(NUM_OF_SIDES):
            chack.forward(SIZE)
            chack.right(360 / NUM_OF_SIDES)
        NUM_OF_SIDES+=2


def randomWalk():
   ACTIONS = ['forward(50)','backward(50)','right(90)','left(90)']
   SPEED = 0
   NUM_OF_ACTIONS = 1000

   oli = Turtle()
   oli.speed(SPEED)
   oli.pencolor(r.choice(COLORS))
   oli.pensize(10)
   for _ in range(NUM_OF_ACTIONS):
       oli.pencolor(r.choice(COLORS))
       exec(f'oli.{r.choice(ACTIONS)}')
       


   

# randomWalk()
masterPiece()



canvas.exitonclick()