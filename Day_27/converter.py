from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

km_result_label = Label(text="0", font=("Arial", 12))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

def button_clicked():
    km_result = int(miles_input.get()) * 1.60934
    km_result_label.config(text=km_result)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()