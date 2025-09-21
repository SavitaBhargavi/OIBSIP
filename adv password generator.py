import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if not (use_letters or use_digits or use_symbols):
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return

    # Build character pool
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Generate password
    password = "".join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password
def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🔐 Advanced Password Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Password entry field
password_entry = tk.Entry(root, width=30, font=("Arial", 12), justify="center")
password_entry.pack(pady=10)

# Length selection
length_var = tk.IntVar(value=12)
length_label = tk.Label(root, text="Password Length:", font=("Arial", 10))
length_label.pack()
length_slider = tk.Scale(root, from_=6, to=32, orient="horizontal", variable=length_var)
length_slider.pack()

# Options
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack(anchor="w", padx=60)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(anchor="w", padx=60)
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack(anchor="w", padx=60)

# Buttons
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", width=20)
generate_btn.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="blue", fg="white", width=20)
copy_btn.pack(pady=5)

# Run app
root.mainloop()
