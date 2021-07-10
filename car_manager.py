from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_collection = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randrange(1, 6)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(-300,random.randint(-250,250))
            self.car_collection.append(car)

    def move(self):
        for car in self.car_collection:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

