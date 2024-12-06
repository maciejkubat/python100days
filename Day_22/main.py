from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

screen.update()
time.sleep(0.1)

player_1 = Paddle(-280,0)
player_2 = Paddle(270,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player_1.up)
screen.onkey(key="Down", fun=player_1.down)
screen.onkey(key="w", fun=player_2.up)
screen.onkey(key="s", fun=player_2.down)

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    if ball.distance(player_1) < 25 or ball.distance(player_2) < 25:
        ball.bounce_off_paddle()

    if ball.xcor() < -300:
        scoreboard.update(1)
        ball.refresh()
    elif ball.xcor() > 300:
        scoreboard.update(0)
        ball.refresh()

screen.exitonclick()