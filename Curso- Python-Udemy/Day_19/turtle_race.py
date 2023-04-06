from turtle import Turtle, Screen
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "green", "blue", "purple", "orange", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

def draw_line(position_y, heading):
    line_turtle = Turtle(shape="arrow")
    line_turtle.pensize(2)
    line_turtle.penup()
    line_turtle.goto(position_y, 0)
    line_turtle.setheading(heading)
    line_turtle.pendown()
    line_turtle.forward(100)
    


draw_line(230, 90)
draw_line(230, -90)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -240, y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                win_text = f"You've won! The {winning_color} turtle is the winner."
                screen.textinput(title="Win!", prompt=win_text)
                # print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                lost_text = f"You've lost! The {winning_color} turtle is the winner."
                screen.textinput(title="Lost!", prompt=lost_text)
                # print(f"You've lost! The {winning_color} turtle is the winner.")

        random_dist = randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()

# My solution 👇👇 !didn't work
# class Tortuga:
#     def __init__(self, x_pos, y_pos, color):
#         self.tortle = Turtle()
#         self.tortle.penup()
#         self.tortle.shape("turtle")
#         self.tortle.color(color)
#         self.tortle.goto(x=x_pos, y=y_pos)
#     def move(self):
#         while is_race_on:
#             random_dist = randint(0, 10)
#             self.tortle.forward(random_dist)

# timmy = Tortuga(x_pos= -240, y_pos= 30, color="yellow")
# tommy = Tortuga(x_pos= -240, y_pos= -30, color="blue")
# jimmy = Tortuga(x_pos= -240, y_pos= 0, color="red")
# changa = Tortuga(x_pos= -240, y_pos= 60, color="brown")
# tomas = Tortuga(x_pos= -240, y_pos= -60, color="sandy brown")