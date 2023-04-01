import random
import turtle as t

tim = t.Turtle()
tim.shape("arrow")
t.colormode(255)

# def turn():
#     """draw a square if the vezes parameter is equal to four"""
#     for i in range(4):
#         tim.right(90)
#         tim.forward(100)       
# turn(4)

# def dash_line(lenght):
#     for i in range(lenght):
#         tim.pd()
#         tim.forward(10)
#         tim.pu()
#         tim.forward(10)

# def square_dash(turns):
#     for i in range(turns):
#         dash_line(10)
#         tim.right(90)

# square_dash(4)
# dash_line(10)
# square_dash(3)

# import random
# colours = ["yellow", "medium blue", "red", "blue", "brown",]
# angles = [0, 90]
# movemnt = random.randint(5, 30)


# def draw_forms(num_sides):
#     """draw various geometric shapes"""
#     # angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(movemnt)
#         tim.right(random.choice(angles))

# for i in range(1, 10):
#     tim.pensize(random.randint(5, 10))
#     tim.pencolor(random.choice(colours))
#     draw_forms(i)

# ----------------------------------------------------------------

# colours = ["medium blue", "red", "blue", "brown",]
# direction = [-45, 45]
# movemnt = random.randint(5, 30)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_color = (r, g, b)
#     return rgb_color

# for i in range(random.randint(0, 100)):
#     tim.pensize(5)
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
# -----------------------------------------------------------------
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_color = (r, g, b)
#     return rgb_color


# tim.speed("fastest")

# def draw_spirograph(size_of_gap, circle_size):
#     for i in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(circle_size)
#         tim.setheading(tim.heading()+ size_of_gap) 

# draw_spirograph(1, 50)
# draw_spirograph(1, 100)











screen = t.Screen()
screen.exitonclick()