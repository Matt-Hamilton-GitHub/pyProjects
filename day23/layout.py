from turtle import Turtle



class Layout(Turtle):
    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h

        self.draw_roud()

    def draw_roud(self):
        self.pencolor("gray")
        self.penup()
        self.shapesize(1,1,0)
        self.setposition(self.width, self.height)
        self.pendown()

        w = self.width
        total = self.width * self.height
        for h in range(self.height):
            self.goto(w, h)
            self.goto(-w,h)
