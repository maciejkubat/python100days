from multiprocessing.managers import Value
from tkinter import *
import pandas as p
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}

# --- READ CSV ---
try:
    data = p.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = p.read_csv('data/french_words.csv')
data_dict = data.to_dict(orient="records")

# --- Display word ---
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    word = current_card['French']
    canvas.itemconfig(canvas_image, image=card_img_front)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_text, text=f"{word}", fill="Black")
    timer = window.after(3000, flip_card)

# -- Remove from list --
def remove():
    global current_card,data_dict
    data_dict.remove(current_card)
    data_frame = p.DataFrame(data_dict)
    data_frame.to_csv('data/words_to_learn.csv',index=False)
    next_card()


# --- flip card ---
def flip_card():
    word = current_card['English']
    canvas.itemconfig(canvas_image, image=card_img_back)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_text, text=f"{word}", fill="White")

# --- UI ---
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file="images/card_front.png")
card_img_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,281, image=card_img_front)
card_title = canvas.create_text(400,181, text="Title", fill="Black", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400,281, text="word", fill="Black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove)
right_button.grid(column=2, row=1)

next_card()

window.mainloop()