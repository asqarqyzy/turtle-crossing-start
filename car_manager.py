from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager():
    def __init__(self):
        self.cars = []
        self.create_cars(20)
        self.start_positions()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.way = 0

    def create_cars(self, num):
        for i in range(num):
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(choice(COLORS))
            car.goto(randint(300, 340), randint(-250, 260))
            self.cars.append(car)

    def start_positions(self):
        for car in self.cars:
            car.goto(randint(-280, 280), randint(-250, 260))

    def cars_move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
        self.way += self.move_distance
        if self.way > 80:
            self.create_cars(4)
            self.way = 0


    def car_speed_add(self):
        self.move_distance += MOVE_INCREMENT

    def restart(self):
        self.move_distance = STARTING_MOVE_DISTANCE
