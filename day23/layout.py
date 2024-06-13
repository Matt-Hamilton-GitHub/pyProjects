from turtle import Turtle



class Layout(Turtle):
    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h

        self.draw_road()

    def draw_road(self):
        self.pencolor("black")
     
        self.ht()
        self.penup()
        self.shapesize(1,1,0)
        self.setposition(self.width, self.height)
        
        
        self.color("gray")
        self.begin_fill()
        self.goto(self.width, -self.height)
        self.goto(-self.width, -self.height)
        self.goto(-self.width, self.height)
        self.goto(self.width, self.height)
        self.end_fill()

        self.setposition(-self.width, -self.height)
        self.pendown()
        self.color("white")
        self.pensize(1)

      
        for seg in range(-self.width, self.width, 10):
          
            if seg % 20 == 0:
                self.pendown()
                self.setposition(seg, 0)
            else:
                self.penup()
                self.setposition(seg, 0)
                 

