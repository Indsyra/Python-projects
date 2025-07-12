import tkinter as tk

# Take in input the name of a user and display a personalized greeting.
# It should include a reset button to clear input
# Bonus challenge: Add a dropdown menu

default_label = "Enter your name"

# Main Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(
    root,
    text="Welcome to My GUI App!",
    font=("Arial", 18),
    bg="#f0f0f0"
)
title_label.pack(pady=20)

# Name Entry
name_label = tk.Label(
    root,
    text="Enter your name:",
    font=("Arial", 12),
    bg="#f0f0f0"
)
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"{languages_map[language_opt.get()]}, {name}!", fg="green")
    else:
        greeting_label.config(text="Please enter your name!", fg="red")

# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")

# Language drop down
languages_map = {
    "Français": "Salut",
    "Deutsch": "Hallo",
    "English": "Hello",
    "Italiano": "Ciao",
    "Español": "Holà"
}
languages = list(languages_map.keys())
language_opt = tk.StringVar(value="Français")

language_dropdown = tk.OptionMenu(
    root,
    language_opt,
    *languages,
)
language_dropdown.pack(pady=10)

# Greet Button
greet_button = tk.Button(
    root,
    text="Greet Me",
    command=greet_user,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white"
)
greet_button.pack(pady=5)

# Reset Button
reset_button = tk.Button(
    root,
    text="Reset",
    command=reset,
    font=("Arial", 12),
    bg="#F44336",
    fg="white"
)
reset_button.pack(pady=5)

# Greeting Label
greeting_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#f0f0f0"
)
greeting_label.pack(pady=20)

# RUn the Application
root.mainloop()
