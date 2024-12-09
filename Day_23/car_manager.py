from turtle import Turtle
from random import choice, randint
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
WAIT_TIME = [0,0.5,1,1.5,2]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def spawn_car(self):
        if len(self.cars) < randint(25, 50):
            random_y = randint(-280,280)
            car = Turtle("square")
            car.turtlesize(stretch_len=2, outline=None)
            car.color(choice(COLORS))
            car.pu()
            car.teleport(280 + randint(25,75),random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -340:
                car.setx(car.xcor() - self.speed)
            else:
                self.cars.remove(car)