# To-do list GUI : Build an app that allow user to add task dynamically, select an item, provides a button to clear all
# Bonus challenge: add task categories (high, medium, low) + task persistence

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-do List")
root.geometry("500x600")
root.configure(bg="#e3f2fd")


# Functions
# Add task
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty")


# Delete task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showerror("Error", "Select a task to delete.")


# Clear all the tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)


# Title Label
title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 24),
    bg="#e3f2fd"
)
title_label.pack(pady=10)

# Entry Field
task_entry = tk.Entry(root)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task,
    font=("Arial", 12),
    bg="#4caf50",
    fg="white"
)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task,
    font=("Arial", 12),
    bg="#f44336",
    fg="white"
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear task list",
    command=clear_tasks,
    font=("Arial", 12),
    bg="#f44336",
    fg="white"
)
clear_button.grid(row=0, column=2, padx=5)


# Frame for Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
task_listbox.pack(pady=10)

scrollbar.config(command=task_listbox.yview)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 12),
    bg="#d32f2f",
    fg="white"
)
exit_button.pack(pady=10)

# Run application
root.mainloop()
