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

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open('data.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found")
    else:
        if website in data:
            website_data = data[website]
            messagebox.showinfo(title=f"Password info for {website}", message=f"Email: {website_data["email"]}\nPassword: {website_data["password"]}")
            pyperclip.copy(website_data["password"])
        else:
            messagebox.showerror(title="Error", message="No details for website exist")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
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
        try:
            with open('data.json', mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
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

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

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