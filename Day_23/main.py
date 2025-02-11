import time
from datetime import datetime
from random import randint
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

game_is_on = True
spawned = False
while game_is_on:
    dice_throw = randint(1,4)
    if dice_throw == 3:
        car_manager.spawn_car()
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.ycor() > 300:
        scoreboard.update()
        car_manager.speed_up()
        player.restart()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()