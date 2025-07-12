# Simple login system to enter credentials
# Bonus challenge: add a password strength validator, implement a registration system to add new users, Lock out functionality

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import string


# Main window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

# Predefined Credentials
USER_FILE = "./assets/user_file.json"


def load_users():
    try:
        with open(USER_FILE, 'r') as json_file:
            users = json.load(json_file)
        if users:
            return users
    except FileNotFoundError:
        print("No registered user found.")
    except Exception as e:
        print(f"An error occurred while loading users: {e}")
    return {}


def save_user(username, password):
    is_password_strong, message = validate_password_strength(password)
    if not is_password_strong:
        messagebox.showerror("Error", message)
        return
    
    try:
        users = load_users()
        users[username] = password

        with open(USER_FILE, 'w') as json_file:
            json.dump(users, json_file, indent=2)
        messagebox.showinfo("Success", f"'{username}' successfully signed in.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while registering '{username}': {e}.")


# Title Label
title_label = tk.Label(root, text="Login System", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Username input
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f4c3")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

# Password input
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f4c3")
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)


# Validate password strength
def validate_password_strength(password, num_char_min=6):
    special_characters_allowed = "!?@&$€"

    error_message = (
        f"Password should contains at least {num_char_min} characters, "
        f"should have at least one special character among '{special_characters_allowed}', "
        f"should contain at least 1 uppercase letter, 1 lowercase letter and 1 digit."
    )

    chars_in_password = list(password)

    if not any(char in string.ascii_lowercase for char in chars_in_password) or \
       not any(char in string.ascii_uppercase for char in chars_in_password) or \
       not any(char in string.digits for char in chars_in_password) or \
       not any(char in special_characters_allowed for char in chars_in_password) or \
       len(chars_in_password) < num_char_min:
        return False, error_message

    return True, ""


# Signing in
def sign_in():
    username = username_entry.get()
    password = password_entry.get()

    save_user(username, password)


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    users = load_users()
    response = None

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    elif username not in users:
        response = messagebox.askyesno("User not registered", f"User '{username}' not registered. Do you want to sign in ?")
        if response:
            save_user(username, password)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Clear Function
def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Buttons
user_frame = tk.Frame(root, bg="#f0f4c3")
user_frame.pack(pady=10)

login_button = tk.Button(user_frame, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="white")
login_button.grid(row=0, column=0, padx=15)

signin_button = tk.Button(user_frame, text="Sign in", command=sign_in, font=("Arial", 12), bg="#4CAF50", fg="white")
signin_button.grid(row=0, column=1, padx=15)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12), bg="#4CAF50", fg="white")
clear_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#4CAF50", fg="white")
exit_button.pack(pady=10)

# Run the application
root.mainloop()