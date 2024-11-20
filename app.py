import tkinter as tk
from tkinter import messagebox
from lib.db_driver import Connection

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    try:
        Connection().login(email=userid, password=password)
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    except Exception as e:
        messagebox.showerror("Login Failed", e)

Connection().create_database()
# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
