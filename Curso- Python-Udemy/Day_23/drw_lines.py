from turtle import Turtle

# horizon_x_pos = [(-300, 1)]
# #      Positions (  X  |Y )  ( X  | Y  )
# horizon_cory = [0,0]

dash_horizon_x = [(-300, 270)]
#      Positions (  X  |Y )  ( X  | Y  )
y_dash_horizon_cord = (0,0)

class DwLines(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
    
    # def draw_line_hori(self):
    #     """Draw a horizontal line in the screen"""
    #     for cord,hori in zip(horizon_x_pos,horizon_cory):
    #         self.pensize(508)
    #         self.shapesize(stretch_wid=10, stretch_len=1)
    #         self.color("gray")
    #         self.penup()
    #         self.goto(cord)
    #         self.setheading(hori)
    #         self.pendown()
    #         self.forward(605)

    def dash_line(self):
        """Draw a horizontal line in the screen"""
        for cord,hori in zip(dash_horizon_x,y_dash_horizon_cord):
            self.pensize(2)
            self.shapesize(stretch_wid=1, stretch_len=1)
            self.color("black")
            self.penup()
            self.goto(cord)
            self.setheading(hori)
            # for i in range(30):
            #     self.pd()
            #     self.forward(30)
            #     self.pu()
            #     self.forward(30)
            self.pendown()
            self.forward(610)
