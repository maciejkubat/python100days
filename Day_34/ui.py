from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR, pady=20, padx=20, anchor="e", justify="right")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, text="Billie Jean, was not his lover that was just a girl, he used to know.", fill="Black", font=("Arial", 15, "italic"), width=300)
        self.canvas.grid(column=0, row=1, columnspan=2)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(pady=20, padx=20, column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(pady=20, padx=20, column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(ms=1000, func=self.get_next_question)
