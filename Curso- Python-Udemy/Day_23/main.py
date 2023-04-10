import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from drw_lines import DwLines
###################################
# Screen Configurations
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

################################
# Variables
player = Player()
car_manager = CarManager()
drw_lines = DwLines()
scoreboard = Scoreboard()
tim = Turtle()

def credits():
    tim.pu()
    tim.hideturtle()
    tim.goto(290, 275)
    tim.write("Developed by Mateus Fonseca", align="right", font=("Arial", 10, "normal"))
############################### 


screen.listen()
screen.onkey(fun=player.move_fwd, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    credits()
    drw_lines.dash_line()
    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

    #detect sucessful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()