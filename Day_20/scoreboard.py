from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.ht()
        self.font = FONT
        self.pu()
        self.goto(0, 260)
        self.display()


    def display(self):
        self.write(f"Score: {self.score}", move = False, align=ALIGNMENT , font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=self.font)

    def update(self):
        self.score += 1
        self.clear()
        self.display()