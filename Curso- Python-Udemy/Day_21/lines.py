from turtle import Turtle

#         (Left vertical line)|(right vertical line)
vertical_y_pos = [(-290, -290),(290, -290)]
#     Positions   (  X  |  Y ) ( X  | Y  )
vertical_corx = [90,90]
#       (Top horzontal line)|(down horizontal line) 
horizon_x_pos = [(-291, 270),(-291, -290)]
#      Positions (  X  |Y )  ( X  | Y  )
horizon_cory = [0,0]

class Dlines(Turtle): 
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.color("yellow")
        self.hideturtle()
        self.pensize(2)

    def draw_line_hori(self):
        """Draw a horizontal line in the screen"""
        for cord,vert in zip(horizon_x_pos,horizon_cory):
            self.penup()
            self.goto(cord)
            self.setheading(vert)
            self.pendown()
            self.forward(580)

    def draw_line_vert(self):
        """Draw a vertical line in the screen"""
        for cord,hori in zip(vertical_y_pos,vertical_corx):
            self.penup()
            self.goto(cord)
            self.setheading(hori)
            self.pendown()
            self.forward(600)
