from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# --- UI ---
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file="images/card_front.png")
card_img_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400,281, image=card_img_front)
language_text = canvas.create_text(400,181, text="English", fill="Black", font=("Arial", 35, "italic"))
word_text = canvas.create_text(400,281, text="to put", fill="Black", font=("Arial", 35, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=2, row=1)


window.mainloop()