from turtle import Turtle, Screen


class GameLayout:

    
    def __init__(self, w, h):
        self.screen = Screen()
        self.border = Turtle()
        self.width = w
        self.height = h
        # self.screen.tracer(0)
        self.screen.screensize(self.width // 2, self.height// 2, 'black')
        self.score1_dis = Turtle()
        self.score2_dis = Turtle()
        self.score1_dis.color('white')
        self.score2_dis.color('white')
        self.score1_dis.ht()
        self.score2_dis.ht()
        self.score1_dis.setposition(-50, self.height - 50)
        self.score2_dis.setposition(50, self.height - 50)

        self.top_border = Turtle()
        self.top_border.ht()
        self.top_border.pencolor('white')
        self.top_border.penup()
        self.top_border.setposition(-self.width -27,self.height +27)
        self.top_border.pendown()
        self.top_border.pensize(5)
        self.top_border.goto(self.width + 27,self.height  +27)
        self.top_border.penup()
        self.top_border.setposition(self.width +27,-self.height -27)
        self.top_border.pendown()
        self.top_border.setposition(-self.width -27,-self.height -27)
        # self.screen.onclick()
        
        # self.screen.listen()

    def draw_border(self, num):
        self.border.pencolor('white')
        self.border.pensize(5)
        self.border.ht()
        self.border.penup()
        self.border.setposition(0, self.height)
        length = self.height // num
        self.border.shapesize(3,length,1)
        self.border.speed(3)

        move = self.height

        for i in range(num * 2):
            move -= length
            print(self.border.position())
            if i % 2 == 0:
                self.border.pendown()
                self.border.goto(0, move) 
            else:
                self.border.penup()
                self.border.goto(0, move) 

            


    def screen_update(self):
        self.screen.update()
        
    def update_score(self, s1, s2):
  
        self.score1_dis.clear()
        self.score2_dis.clear()
        self.score1_dis.write(f"{s1}", align="center",font=('Arial', 50, 'normal'))
        self.score2_dis.write(f"{s2}", align="center",font=('Arial', 50, 'normal'))

    


    

   

        
        


