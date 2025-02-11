from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(0,0)
        direction_ne = randint(0,45)
        direction_se = randint(315,360)
        direction_west = randint(135,225)
        direction = choice([direction_se, direction_ne, direction_west])
        self.setheading(direction)

    def move(self):
        self.forward(15)
        self.bounce_off_edges()

    def bounce_off_edges(self):
        if self.ycor() > 240 or self.ycor() < -240:
            self.setheading(360-self.heading())

    def bounce_off_paddle(self):
        current_heading = self.heading()
        if 0 <= current_heading < 90 or 270 <= current_heading < 360:
            self.setheading(180 - current_heading)
            self.forward(15)
        else:
            self.setheading(360 - (current_heading - 180))
            self.forward(15)