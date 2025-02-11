from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.scores = [0,0]
        self.ht()
        self.font = FONT
        self.pu()
        self.goto(0, 180)
        self.display()


    def display(self):
        self.write(f"{self.scores[0]} : {self.scores[1]}", move = False, align=ALIGNMENT , font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=self.font)

    def update(self,which):
        self.scores[which] += 1
        self.clear()
        self.display()