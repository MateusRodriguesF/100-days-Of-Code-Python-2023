from turtle import Turtle

cord = (0, -280)
fowrd = 30
lenght = 10

class Dashline(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.color("white")
        self.hideturtle()
        self.pensize(4)
    
    def go_go(self):
        self.penup()
        self.goto(cord)
        self.setheading(90)
        
    def dash_draw(self):
        for i in range(lenght):
            self.pd()
            self.forward(fowrd)
            self.pu()
            self.forward(fowrd)
