from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR, pady=20, padx=20, anchor="e", justify="right")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)


        self.window.mainloop()