from turtle import Turtle, Screen
import random as r

COLORS = ['red','green','blue','yellow','orange','black']
TURTLES = []
STARTING_POS = (-400,-100)
FINIS_X = 500

class TurtleRace:

    def __init__(self, Turtle, color):
        self.turtle = Turtle()
        self.color = color


screen = Screen()
screen.setup(width=900, height=400)



tim = Turtle()
tim.shape('turtle')
tim.penup()
tim.hideturtle()


for i in range(len(COLORS)):
    newTurtle = tim.clone()
    newTurtle.showturtle()
    newTurtle.color(COLORS[i])
    newTurtle.goto(STARTING_POS[0], STARTING_POS[1])
    STARTING_POS = (STARTING_POS[0], STARTING_POS[1] + 40)
    TURTLES.append(newTurtle)

user_bet = screen.textinput("Make your bet",'Which turtle will win? Enter color: ')

finish = False
winner = ""
while not finish:
    for i in TURTLES:
        i.speed(r.randint(0,4))
        i.forward(r.randint(5,40))
        i.speed(0)
        i.dot()
        if i.xcor() >= 400:
            finish = True
            winner = i.color()[0]
            break

if user_bet == winner:
    print(f'You won! {winner.upper()} turtle came to the finish first')
    
else:
    print(f'You lost! You bet for {user_bet.upper()} but {winner.upper()} came first to the finish')

screen.mainloop()





