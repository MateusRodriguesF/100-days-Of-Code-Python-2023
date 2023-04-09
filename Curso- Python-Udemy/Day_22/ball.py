from turtle import Turtle

class Ball(Turtle):# SuperClass now class Food is equal to turtle class in all ways

    def __init__(self):
        super().__init__()#when you import a class, the class becomes superclass
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bouncex()