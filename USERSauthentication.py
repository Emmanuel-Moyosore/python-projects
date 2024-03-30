# GUI
import tkinter as tk
from tkinter import messagebox

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct (this is a simple example)
    user_name=input('Enter ur name: ')
    pass_word = input('Enter password: ')
    if username == user_name and password == pass_word:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login")

# Create labels, entries, and button
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Show '*' for password entry
password_entry.pack()

login_button = tk.Button(root, text="Login", command=authenticate)
login_button.pack()

# Start the main loop
root.mainloop()



