from turtle import Screen, Turtle
import random as r

WIDTH, HIGHT = 600, 600
MOVE_TILES = 20
GAME_SIZE_X = MOVE_TILES * 15
GAME_SIZE_Y = MOVE_TILES * 10
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP,DOWN,LEFT,RIGHT = 90, 270, 180, 0

x_ratio = GAME_SIZE_X / MOVE_TILES 
y_ratio = GAME_SIZE_Y / MOVE_TILES 

screen_settings = Screen()
screen_settings.setup(GAME_SIZE_X * 2 + 50 , GAME_SIZE_Y * 2 + 50)
screen_settings.bgcolor("black")
screen_settings.title("Snake Game")
screen_settings.tracer(0)

class Snake:
    segments = []
    moves = {}
    food_location = ()
    obstacles = []
    score = 0
    speed = 0.1
    dis_speed = 1

    def __init__(self):
        self.food = Turtle('square')

        for position in STARTING_POSITIONS:
            new_seg = Turtle('square')
            new_seg.color('white')
            new_seg.shapesize(1,1,0)
            new_seg.penup()
            new_seg.speed(0)
            new_seg.setposition(position)
            self.segments.append(new_seg)
        
        #SNAKE DEFAULT PARAMS

    def create_snake(self):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.shapesize(1,1,0)
        new_seg.penup()
        new_seg.speed(0)
        self.segments.append(new_seg)


    def add_seg(self):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.shapesize(1,1,0)
        new_seg.penup()
        new_seg.speed(0)
            
        last_seg = self.segments[len(self.segments)-1] 
        last_seg_pos = last_seg.position()



        if last_seg.heading() == 0:
            new_seg.goto(last_seg_pos[0] - 20,last_seg_pos[1])
        elif last_seg.heading() == 90:
            new_seg.goto(last_seg_pos[0],last_seg_pos[1] - 20 )
        elif last_seg.heading() == 180:
            new_seg.goto(last_seg_pos[0] + 20 ,last_seg_pos[1])
        elif last_seg.heading() == 270:
            new_seg.goto(last_seg_pos[0],last_seg_pos[1] + 20 )

        new_seg.setheading(last_seg.heading())
        self.segments.append(new_seg)

        #update speed 
        if len(self.segments) % 10 == 0:
            self.speed-=0.01
            self.dis_speed+=1

    def update_heading(self, seg):
    # print(m)
    
        if seg.position() in self.moves.keys():
            key = seg.position()
            new_heading = self.moves[seg.position()]
            seg.setheading(new_heading)
            # update_position(s)
            if self.segments.index(seg) == len(self.segments) - 1:
                self.moves.pop(key)

    def update_position(self):
        for s in self.segments:
            
            pos = s.position()
            if s.heading() == 0:
                s.goto(pos[0] + MOVE_TILES, pos[1])
            elif s.heading() == 90:
                s.goto(pos[0],pos[1] + MOVE_TILES  )
            elif s.heading() == 180:
                s.goto(pos[0] - MOVE_TILES, pos[1])
            elif s.heading() == 270:
                s.goto(pos[0], pos[1] - MOVE_TILES )
            self.update_heading(s)

    def update_heading_pos(self, angle):

        curr_heading = self.segments[0].heading()
        if angle == 'up' and (curr_heading != DOWN):
            self.segments[0].setheading(UP)
        elif angle == 'down' and (curr_heading != UP):
            self.segments[0].setheading(DOWN)
        elif angle == 'right' and (curr_heading != LEFT ):
            self.segments[0].setheading(RIGHT)
        elif angle == 'left' and (curr_heading != RIGHT):
            self.segments[0].setheading(LEFT)

        # print(self.segments[0].position(), self.segments[0].heading())
        self.moves[self.segments[0].position()] = self.segments[0].heading()
        # self.segments[0].forward(MOVE_TILES)
        
    def add_food(self):
        self.food.color('green')
        self.food.shapesize(1,1,0)
        self.food.penup()
        self.food.hideturtle()
        valid_loc = False
        new_loc = (r.randint(-x_ratio, x_ratio) * MOVE_TILES , r.randint(-y_ratio, y_ratio) * MOVE_TILES )

        while not valid_loc:
            for s in self.segments:
                if new_loc == s.position():
                    valid_loc = False
                    new_loc = (r.randint(-x_ratio, x_ratio) * MOVE_TILES , r.randint(-y_ratio, y_ratio) * MOVE_TILES )
                    break
                elif new_loc != s.position() and self.segments.index(s) == len(self.segments) - 1:
                    valid_loc = True

        self.food.setpos(new_loc)
        self.food.showturtle()

    def eat_food(self, head_loc):
        # print(self.food.position(), head_loc)
        self.food.hideturtle()
        self.add_seg()
        self.add_food()

            # FOOD_TIMER = 0
    def check_position(self, head):

        if self.food.position() == head:
            self.eat_food(head)
            self.score+=100
            return False

        elif abs(head[0]) >= GAME_SIZE_X + MOVE_TILES   or abs(head[1]) >= GAME_SIZE_Y + MOVE_TILES  :
            print(f"went out: {GAME_SIZE_X,GAME_SIZE_X}: {head[0],head[1]}")
            return True

        elif head in self.obstacles:
            return True

        for s in self.segments[1:]:
            if head == s.position():
                return True

        return False

    def generate_obstacle(self):
        new_obstacle = Turtle('square')
        new_obstacle.color('gray')
        new_obstacle.shapesize(1,1,0)
        new_obstacle.penup()
        new_obstacle.hideturtle()
        pos = (r.randint(-x_ratio, x_ratio) * MOVE_TILES , r.randint(-y_ratio, y_ratio) * MOVE_TILES )
        while pos in STARTING_POSITIONS:
             pos = (r.randint(-x_ratio, x_ratio) * MOVE_TILES , r.randint(-y_ratio, y_ratio) * MOVE_TILES )
        self.obstacles.append(pos)
        new_obstacle.setposition(pos)
        new_obstacle.showturtle()
    

#--------------------------------


        


    


