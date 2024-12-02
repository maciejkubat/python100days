from turtle import Turtle, Screen
from random import randint

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

screen = Screen()
turtles = []

def initialize(turtlez):
    start_y = 200
    for index,color in enumerate(rainbow_colors):
        turtlez.append(Turtle(shape="turtle"))
        turtlez[index].color(color)
        turtlez[index].teleport(y=start_y, x=-250)
        turtlez[index].pu()
        start_y -= 50

def race(turtlez):
    while True:
        for turtle in turtlez:
            turtle.forward(randint(1,20))
            if turtle.xcor() >= 335:
                return turtle.color()[0]

def game():
    players_bet =  screen.textinput("NIM", 'On which turtle do you bet?("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"):').capitalize()
    initialize(turtles)
    winner = race(turtles)
    if players_bet == winner:
        print(f"Your bet was {players_bet}. You won!")
    else:
        print(f"Your bet was {players_bet}. {winner} won. You loose :(")

game()
screen.exitonclick()