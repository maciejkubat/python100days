import turtle
from turtle import Turtle
FONT = ("Arial", 12, "normal")
FONT_WON = ("Arial", 30, "normal")

import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
states_guessed = []
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
background = Turtle()
screen.addshape(image)
background.shape(image)
cursor = Turtle()
cursor.color("black")
cursor.pu()
cursor.hideturtle()

def mark_state(state_data):
    state_x = state_data.x.item()
    state_y = state_data.y.item()
    cursor.teleport(state_x, state_y)
    cursor.write(answer_state, font=FONT)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/{len(states)} Guess the state", prompt="What's another state's name?").title()
    if answer_state in states and answer_state not in states_guessed:
        state_data = data[data.state == answer_state]
        mark_state(state_data)
        states_guessed.append(answer_state)
    if len(states_guessed) == len(states):
        game_is_on = False
        cursor.teleport(0,0)
        cursor.write("You WON!",font=FONT_WON)
    if answer_state == "Exit":
        break

for state in states_guessed:
    data = data[data['state'] != state]

data.to_csv('States_to_learn.csv')
screen.exitonclick()