import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def generate_and_display_password():
    try:
        username = entry_username.get()
        length = int(entry_length.get())
        password = generate_password(length)
        result_label.config(text=f"Hi {username}, Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

# Creation of the main window:-
root = tk.Tk()
root.title("Password Generator")

# the user name section :-
label_username = tk.Label(root, text="User name:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Length Section :-
label_length = tk.Label(root, text="Enter the desired length of the password:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Generate Buttons :-
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

# Result Section :-
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Running of the main loop :-
root.mainloop()
