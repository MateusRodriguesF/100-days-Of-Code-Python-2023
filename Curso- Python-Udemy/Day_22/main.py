from turtle import Screen
from dash_line import Dashline
from player_paddle import Playerpaddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Screen configuration
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

dashed = Dashline()
dashed.go_go()
dashed.dash_draw()

lft_paddle = Playerpaddle((-370, 0))
rgt_paddle = Playerpaddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.credits()

screen.listen()
screen.onkey(fun=lft_paddle.go_up, key="w")
screen.onkey(fun=lft_paddle.go_down, key="s")

screen.onkey(fun=rgt_paddle.go_up, key="Up")
screen.onkey(fun=rgt_paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect the collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()


    # Detect the collision with the paddles
    if ball.distance(rgt_paddle) < 80 and ball.xcor() > 330 or ball.distance(lft_paddle) < 56 and ball.xcor() < -340 :
        ball.bouncex()
    
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()