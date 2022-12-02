from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import END
from tkinter import messagebox
from random import choice
from random import shuffle
import pyperclip
import json


# Generating Password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    randomized_letters = [choice(letters) for _ in range(0, 8)]
    randomized_numbers = [choice(numbers) for _ in range(0, 4)]
    randomized_symbols = [choice(symbols) for _ in range(0, 4)]

    password_chars = list(randomized_letters + randomized_numbers + randomized_symbols)
    shuffle(password_chars)
    joined_symbols = "".join(password_chars)
    return joined_symbols


# Copying password
def insert_generated_password():
    if generate_password_button:
        password_entry.delete(0, END)
    password_entry.insert(0, generate_password())
    pyperclip.copy(password_entry.get())


# Save password to file
def save_entry():
    password = password_entry.get()
    website = website_entry.get()
    user_id = email_username_entry.get()

    new_data = {
        f"{website}": {
            "user_id": user_id,
            "password": password
        }
    }

    data_json = "data.json"

    if len(password) == 0 or len(user_id) == 0 or len(website) == 0:
        messagebox.showerror("All fields must be filled.")

    confirmation_yes_or_no = messagebox.askokcancel(title="Confirmation", message=f"Save:\n{website}\n{user_id}\n{password} ?")

    if confirmation_yes_or_no:
        try:
            with open(data_json, "r") as json_file:
                json_data = json.load(json_file)
                json_data.update(new_data)

            with open(data_json, "w") as json_file:
                json.dump(json_data, json_file, indent=4)
        except FileNotFoundError:
            with open(data_json, "w") as json_file:
                json.dump(new_data, json_file)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# Finding the password for when user searches for website
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as json_file:
            json_data = json.load(json_file)
            messagebox.showinfo(title="Info", message=f"User: {json_data[website]['user_id']}\n"
                                f"Password: {json_data[website]['password']}\n")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
    except KeyError:
        messagebox.showerror(title="Error", message="Website details not found.")


# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Elements
canvas = Canvas(height=200, width=200)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(115, 100, image=password_manager_img)

website_label = ttk.Label(text="Website:")
email_username_label = ttk.Label(text="Email/Username:")
password_label = ttk.Label(text="Password:")

website_entry = ttk.Entry(width=32)
website_entry.focus()
email_username_entry = ttk.Entry(width=50)
email_username_entry.insert(0, "lennasuzaka1988@gmail.com")
password_entry = ttk.Entry(width=32)

search_button = ttk.Button(text="Search", width=15, command=find_password)
generate_password_button = ttk.Button(text="Generate Password", command=insert_generated_password)
add_button = ttk.Button(text="Add", width=50, command=save_entry)

# Placement
canvas.grid(row=1, column=2)

website_label.grid(row=2, column=1, pady=5)
website_entry.grid(column=2, row=2, columnspan=1, sticky="e")

email_username_label.grid(column=1, row=3, pady=5, sticky="e")
email_username_entry.grid(column=2, row=3, columnspan=2)

password_label.grid(column=1, row=4, pady=5)
password_entry.grid(column=2, row=4, sticky="e", padx=2)

search_button.grid(column=3, row=2, sticky="e")
generate_password_button.grid(column=3, row=4, sticky="w")
add_button.grid(column=2, columnspan=2, pady=5, sticky="n")



window.mainloop()
