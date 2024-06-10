from turtle import Turtle, Screen
from game_layout import GameLayout
import time
import random as r


class Pong:

    move_tiles_x = 15
    move_tiles_y = 10

    plr1_score = 0
    plr2_score = 0

    def __init__(self,w,h):

        self.width = w
        self.height = h

        self.player1 = Turtle('square')
        self.player2 = Turtle('square')
        self.player1.penup()
        self.player2.penup()

        self.player1.color('white')
        self.player1.shapesize(5,0.5)
        self.player1.setposition(self.width,0) 

        self.player2.color('white')
        self.player2.shapesize(5,0.5)
        self.player2.setposition(-self.width,0) 

        self.pong = Turtle('circle')
        self.pong.color('white')
        self.pong.shapesize(1,1) 
        self.pong.penup()
        self.pong.setposition(0,0)  
        self.pong.setheading(0)
        self.pong.speed(0)

        self.score = GameLayout(self.width, self.height)
        self.score.draw_border(20)
        self.score.update_score(0,0)
        self.score.update_score(self.plr1_score, self.plr1_score)

    

    def update_position(self, y):
        if abs(y + self.player1.position()[1]) + 20 <= self.height:
            self.player1.setposition(self.width, self.player1.position()[1] + y)

    def update_position_agent(self, y):
        if abs(y + self.player2.position()[1]) + 20 <= self.height:
            self.player2.setposition(-self.width, self.player2.position()[1] + y)

    def move_pong(self):
        curr_pos = self.pong.position()
        curr_heading = self.pong.heading()

        self.computer_agent()
        self.check_bounce(curr_heading, curr_pos)
        # print(f'distance to player 1: {self.player1.distance(curr_pos[0],curr_pos[1]  )}',curr_pos)
        if self.player1.distance(curr_pos[0], curr_pos[1]) <= 20 or self.player1.distance(curr_pos[0], curr_pos[1] + 25) <= 20 or self.player1.distance(curr_pos[0], curr_pos[1] - 25) <= 20:
            self.pong.goto(curr_pos[0] - 2, curr_pos[1])
            self.pong.setheading(180)
            self.pong.goto(curr_pos[0] - self.move_tiles_x, curr_pos[1] + self.move_tiles_y)
        elif  self.player2.distance(curr_pos[0], curr_pos[1]) <= 20 or self.player2.distance(curr_pos[0], curr_pos[1] + 25) <= 20 or self.player2.distance(curr_pos[0], curr_pos[1] - 25) <= 20:
            self.pong.goto(curr_pos[0] + 2, curr_pos[1])
            self.pong.setheading(0)
           
            self.pong.goto(curr_pos[0] + self.move_tiles_x , curr_pos[1] + self.move_tiles_y)
        else:

            if abs(curr_pos[0]) + 10 > self.width:
                if curr_pos[0] > 0:
                    self.plr1_score+=1
                    self.score.update_score(self.plr1_score, self.plr2_score)
                    self.reset((self.player1.position()[0] // 2, 10),180)
                else:
                    self.plr2_score+=1
                    self.score.update_score(self.plr1_score, self.plr2_score)
                    self.reset((self.player2.position()[0] // 2, 10), 0 )


            elif curr_heading == 0:
               self.pong.goto(curr_pos[0] + self.move_tiles_x , curr_pos[1] + self.move_tiles_y)
            elif curr_heading == 180:
                self.pong.goto(curr_pos[0] - self.move_tiles_x , curr_pos[1] + self.move_tiles_y)
               
            
            

    def check_bounce(self, h, p):
        if p[1] >= self.height:
            self.move_tiles_y = r.randint(10,25)
            self.move_tiles_y = -abs(self.move_tiles_y)
            print('bounced')
        
        elif abs(p[1]) >= abs(self.height):  
            self.move_tiles_y = r.randint(10,25)
            self.move_tiles_y = abs(self.move_tiles_y)
            print('bounced')
        
    def reset(self, p, a):
        self.pong.setposition(p)
        # print('reset')
        time.sleep(1)
        self.pong.setheading(a)

    def computer_agent(self):
        p_pos = self.pong.position()
        p_head = self.pong.heading()

        a_next = self.player2.position()[1]
        
        if p_head > 0 and self.player2.distance(p_pos[0], p_pos[1]) > 10:
            if self.player2.distance(p_pos[0], p_pos[1] + 20) < self.player2.distance(p_pos[0], p_pos[1] - 20):
                self.update_position_agent(-r.randint(10,20))
            else:
                self.update_position_agent(r.randint(10,20))
            




