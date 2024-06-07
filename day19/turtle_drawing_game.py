from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
    tim.setheading(tim.heading() - 10)
   
def move_left():
    tim.setheading(tim.heading() + 10)

def circle_around():
     tim.circle(45)

    
def move_up():
    tim.forward(20)

def move_down():
    tim.backward(20)

def drop_pen():
     tim.penup()

def pen_back():
    tim.pendown()

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

#directions
screen.onkey(key='d', fun=move_right)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='w', fun=move_up)
screen.onkey(key='s', fun=move_down)
screen.onkey(key='c', fun=clear_screen)
#more actions
screen.onkey(key='x', fun=drop_pen)
screen.onkey(key='z', fun=pen_back)

screen.exitonclick()