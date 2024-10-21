import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(tk.END, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter password length:", font=('Arial', 14))
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root, font=('Arial', 14))
entry_length.grid(row=0, column=1, padx=10, pady=10)

button_generate = tk.Button(root, text="Generate Password", font=('Arial', 14), command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

entry_password = tk.Entry(root, font=('Arial', 14), width=24)
entry_password.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

button_copy = tk.Button(root, text="Copy to Clipboard", font=('Arial', 14), command=copy_to_clipboard)
button_copy.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
