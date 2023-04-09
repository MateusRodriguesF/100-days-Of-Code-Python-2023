from turtle import Turtle

class Playerpaddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.pu()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() +50
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() -50
        self.goto(self.xcor(), new_y)