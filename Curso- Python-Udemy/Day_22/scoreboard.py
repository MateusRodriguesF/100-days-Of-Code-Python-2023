from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.credits()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def credits(self):
        self.goto(210, 280)
        self.write("Developed by Mateus Fonseca", align="left", font=("arial", 10, "normal"))