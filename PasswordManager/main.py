from tkinter import Canvas, PhotoImage, Label, Entry, Tk, Button
from tkinter import END
from tkinter import messagebox
from password_generator import generator

import json

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as DataFile:
            data = json.load(DataFile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data Has Been Created Yet.")
    else:
        if website in data:
            email = data[website]["email/username"]
            password = data[website]["password"]
            messagebox.showinfo(title="Search Successful!",
                message=f"""
                Email/Username: {email}
                Password: {password}
                """
            )
        else:
            messagebox.showinfo(title="Search Unsuccessful", message="Could not find a password associated with the entered website.")
        

def generate_password():
    password = generator()
    password_entry.insert(0, password)

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    user_data = {
        website: {
            "email/username": email_username,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Blank Fields",
            message="A field was left empty."
        )
    else:
        password_ok = messagebox.askokcancel(
            title="Password Confirmation",
            message=f"""
            These are the details entered:
            Email: {email_username}
            password: {password}
            Is it ok to save?
            """
        )
        if password_ok:
            try:
                with open("data.json", "r") as DataFile:
                    data = json.load(DataFile)
            except FileNotFoundError:
                with open("data.json", "w") as DataFile:
                    json.dump(user_data, DataFile, indent=4)
            else:
                data.update(user_data)
                with open("data.json", "w") as DataFile:
                    json.dump(data, DataFile, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
email_username_label = Label(text="Email/Username")
password_label = Label(text="Password")
website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
email_username_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "K0MPLEXWorksTogether")
password_entry.grid(row=3, column=1)

add_button = Button(text="Add", width=36, command=save)
generate_password_button = Button(text="Generate Password", command=generate_password)
search_button = Button(text="Search", width=13, command=search)
add_button.grid(row=4, column=1, columnspan=2)
generate_password_button.grid(row=3, column=2)
search_button.grid(row=1, column=2)

window.mainloop()