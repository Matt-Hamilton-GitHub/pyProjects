from turtle import Screen


class ScreenSetUp():

    padding = 50
    screen = Screen()

    def __init__(self, width, rows):
        self.screen.screensize(width + self.padding, rows*20)
        self.screen.bgcolor('white')


    



