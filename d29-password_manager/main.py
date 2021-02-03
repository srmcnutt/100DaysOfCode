from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

#----------------------------- Search ---------------------------------------#
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="datafile not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"website: {website}\n password: {password}")
        else:
            messagebox.showinfo(title="record not found", message="website not found")

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
        messagebox.showinfo(title="oops", message="Make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Details entered:\nwebsite: {website}\n"
                    f"User: {email}\n"
                    f"Password: {password}\n"
                    f"Is this ok?"
        )

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    data = json.dump(new_data, file, indent=4)

            else:
                with open("data.json", "w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=21)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "bubba@bubbas123.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)
generate_password_buttom = Button(text="Generate Password", command=generate_password)
generate_password_buttom.grid(row=3, column=2)
add_button = Button(text="Add", width=21, command=save)
add_button.grid(row=4, column=1, columnspan=1)

window.mainloop()
