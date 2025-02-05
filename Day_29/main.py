from tkinter import *
from tkinter import messagebox
from passgen import password_generator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    password_entry.delete(0,END)
    generated_password = password_generator()
    pyperclip.copy(generated_password)
    password_entry.insert(0,generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Do not leave any fields empty")
    else:
        with open('data.json', mode="w") as file:
            data = json.load(file)
            data.update(new_data)
            json.dump(new_data, file, indent=4)
        website_entry.delete(0,END)
        email_entry.delete(0, END)
        email_entry.insert(0, "maciek.kubat@gmail.com")
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "maciek.kubat@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=pass_gen)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()