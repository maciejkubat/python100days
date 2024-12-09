from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as file:
            hs_file = file.read()
        self.color("white")
        self.score = 0
        self.high_score = int(hs_file)
        self.ht()
        self.font = FONT
        self.pu()
        self.goto(0, 260)
        self.display()


    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align=ALIGNMENT , font=self.font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=self.font)

    def update(self):
        self.score += 1
        self.display()