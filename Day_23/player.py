from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.restart()

    def restart(self):
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.pu()
        self.setposition(STARTING_POSITION)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)
