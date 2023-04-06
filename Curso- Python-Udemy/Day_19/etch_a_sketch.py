from turtle import Turtle, Screen
from time import sleep

touchet = Turtle()
screen = Screen()

def move_right():
    touchet.forward(10)
def move_left():
    touchet.backward(10)
def move_down():
    touchet.left(10)
def move_up():
    touchet.right(10)

def clear_screen():
    touchet.penup()
    touchet.clear()
    touchet.home()
    sleep(1)
    touchet.pendown()

screen.listen()
screen.onkey(key="Right", fun=move_up)
screen.onkey(key="Left", fun=move_down)
screen.onkey(key="Down", fun=move_left)
screen.onkey(key="Up", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()