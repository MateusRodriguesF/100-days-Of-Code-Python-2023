import turtle
from prettytable import PrettyTable

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.circle(60, 360)

# my_screen = turtle.Screen()
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Voltrob","Chamander"])
table.add_column("Type",["Eletric", "Electric", "Fire"])
table.align = "l"
print(table)
