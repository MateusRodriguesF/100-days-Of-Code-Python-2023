from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 5:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(0)
            new_car.goto(x= random.randint(302, 304), y= random.randint(-240,250))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color(random.choice(COLORS))
#         self.shape("square")
#         self.penup()
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.setheading(0)
#         self.goto(x= random.randint(305, 400), y= random.randint(-250,250))
    
#     def car_move(self):
#         self.setheading(180)
#         self.forward(STARTING_MOVE_DISTANCE)
