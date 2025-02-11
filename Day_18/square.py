import turtle
from turtle import Turtle,Screen
from random import randint, choice

charles = Turtle()
my_screen = Screen()
my_screen.setup()
my_screen.colormode(255)

def draw_square():
    for step in range(4):
        charles.forward(100)
        charles.left(90)

def draw_dotted_line():
    for step in range(15):
        charles.forward(10)
        charles.penup()
        charles.forward(10)
        charles.pendown()

def draw_figure(turtle, sides, length):
    turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for step in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)

def draw_figures(turtle,how_many):
    for sides in range(3,how_many+1):
        draw_figure(turtle,sides,50)

def random_colour():
    random_c = (randint(0, 255), randint(0, 255), randint(0, 255))
    return random_c

def random_walk(turtle, width, steps):
    turtle.width(width)
    turtle.speed("fast")
    turtle.ht()
    directions = [ 0, 90, 180, 270]
    for step in range(steps):
        turtle.pencolor(random_colour())
        turtle.setheading(choice(directions))
        turtle.forward(10)

def spiro(turtle, circles):
    angle = 360 / circles
    turtle.speed(0)
    for step in range(circles):
        turtle.pencolor(random_colour())
        turtle.circle(100)
        turtle.right(angle)

spiro(charles, 100)



 # Set up the screen size

my_screen.exitonclick()