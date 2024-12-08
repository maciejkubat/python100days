from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.ht()
        self.font = FONT
        self.pu()
        self.goto(-200, 250)
        self.display()

    def display(self):
        self.write(f"Level: {self.level}", move = False, align=ALIGNMENT , font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=self.font)

    def update(self):
        self.level += 1
        self.clear()
        self.display()