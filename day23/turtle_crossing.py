from car import Car
from turtle import Turtle
import random as r
import time

class TurtleCrossing(Turtle):
    LOCATION = [(10,)]
    CARS = []
    
    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h

        self.place_car()
       
    def place_car(self):
    
        time.sleep(r.randint(0,5)* 0.1)
        new_car = Car(r.randint(1,4))
        new_car.setheading(180) 
        new_car.shape('square')
        new_car.ht()
        new_car.penup()
        new_car.setposition(self.width , self.height / 20 * r.randint(1, self.height / 40))
        new_car.st()
        new_car.speed(r.randint(0,2))
        self.CARS.append(new_car)
        print('car added')
            

    def move_car(self):
        for i in self.CARS:
            print(f"{i.color()} moved to")
            # i.goto(-self.width, i.position()[1])
            i.setposition(i.position()[0] - r.randint(10, 50) , i.position()[1])
            if i.position()[0] < - self.width:
                self.CARS.pop(self.CARS.index(i))
                i.reset()
                i.clear()

        for i in range(len(self.CARS), 4):
            self.place_car() 
            




        
