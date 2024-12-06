from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.create_paddle(x,y)

    def create_paddle(self,x,y):
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=3, stretch_len=0.5, outline=None)
        self.pu()
        self.teleport(x,y)

    def up(self):
        if self.ycor() < 210:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -210:
            self.sety(self.ycor() - 20)
