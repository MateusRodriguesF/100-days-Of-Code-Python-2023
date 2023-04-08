from turtle import Screen
from time import sleep
from lines import Dlines
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Screen Configurations
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

drw_linesh = Dlines()
drw_linesh.draw_line_hori()

drw_lineshv = Dlines()
drw_lineshv.draw_line_vert()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.snake_move()

# Detect collisions
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
# Detect collisions with wall
    if snake.head.xcor() > 289 or snake.head.xcor() < -289 or snake.head.ycor() > 269 or snake.head.ycor() < -289:
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        scoreboard.game_over()
        scoreboard.final_score()
        scoreboard.credits()
# Detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            screen.clear()
            screen.bgcolor("black")
            scoreboard.game_over()
            scoreboard.final_score()
            scoreboard.credits()
            

screen.exitonclick()