from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def final_score(self):
        self.goto(0, -30)
        self.update_scoreboard()
    
    def credits(self):
        self.goto(0, -250)
        self.write("Developed by Mateus Fonseca", align="left", font=("arial", 12, "normal"))
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def __init__(self):
    #     super().__init__()

    #     self.hideturtle()
    #     self.goto(0, 280)
    #     self.color("White")
    #     self.write("Score: ", align="center", font=("arial",11,"normal"))
    
    # class Scoreboard(Turtle):
