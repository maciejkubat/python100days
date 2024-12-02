import colorgram
from turtle import Turtle,Screen
from random import randint, choice

charles = Turtle()
my_screen = Screen()
my_screen.setup()
my_screen.colormode(255)

colors = colorgram.extract('image.jpg',80)
colors_rgb = []
for colour in colors:
    colors_rgb.append((colour.rgb.r, colour.rgb.g, colour.rgb.b))

colors_rgb = colors_rgb[4:]

def draw_row(turtle):
    for _ in range(10):
        turtle.pencolor(choice(colors_rgb))
        turtle.dot(20)
        turtle.pu()
        turtle.forward(50)
        turtle.pd()

def go_to_next_row(turtle):
    if turtle.heading() == 0:
        turtle.pu()
        for _ in range(2):
            turtle.left(90)
            turtle.forward(50)
        turtle.pd()
    elif turtle.heading() == 180:
        turtle.pu()
        for _ in range(2):
            turtle.right(90)
            turtle.forward(50)
        turtle.pd()


charles.teleport(-250,-250)
charles.speed(0)
for _ in range(10):
    draw_row(charles)
    go_to_next_row(charles)


my_screen.exitonclick()