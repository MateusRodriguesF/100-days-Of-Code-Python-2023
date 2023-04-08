from turtle import Turtle
import random

class Food(Turtle):# SuperClass now class Food is equal to turtle class in all ways

    def __init__(self):
        super().__init__()#when you import a class, the class becomes superclass
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)