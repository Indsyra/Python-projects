# To-do list GUI : Build an app that allow user to add task dynamically, select an item, provides a button to clear all
# Bonus challenge: add task categories (high, medium, low) + task persistence

import json
import tkinter as tk
from tkinter import messagebox, StringVar

root = tk.Tk()
root.title("To-do List")
root.geometry("700x800")
root.configure(bg="#e3f2fd")

# Save File
task_file = "./assets/task_file.json"


# Task insertion depending on category
def insert_task(priority, task):
    if priority == "High":
        task_listbox_high.insert(tk.END, task)
    elif priority == "Middle":
        task_listbox_middle.insert(tk.END, task)
    elif priority == "Low":
        task_listbox_low.insert(tk.END, task)


# Load tasks
def load_tasks():
    try:
        with open(task_file, 'r') as json_file:
            tasks = json.load(json_file)
            if tasks:
                return tasks
    except FileNotFoundError:
        print("Error:", "No task found.")
    except Exception as e:
        print("Error:", f"An error occurred while loading tasks: \n{e}")
    return []


# Fill list boxes
def fill_list_boxes():
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            insert_task(task["priority"], task["task"])

# Save task
def save_task(priority, task):
    try:
        tasks = load_tasks()
        tasks.append(
            {
                "priority": priority,
                "task": task
            }
        )
        with open(task_file, 'w') as json_file:
            json.dump(tasks, json_file, indent=2)
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred while saving task '{task}' with priority '{priority}': \n{e}.")


# Functions
# Add task
def add_task():
    priority = priority_opt.get()
    task = task_entry.get()
    if task.strip():
        insert_task(priority, task)
        save_task(priority, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty")


# Delete task
def delete_task():
    selected_high = task_listbox_high.curselection()
    selected_middle = task_listbox_middle.curselection()
    selected_low = task_listbox_low.curselection()
    if selected_high:
        task_listbox_high.delete(selected_high[0])
    if selected_middle:
        task_listbox_middle.delete(selected_middle[0])
    if selected_low:
        task_listbox_middle.delete(selected_low[0]) 
    if not selected_high and not selected_middle and not selected_low:
        messagebox.showerror("Error", "Select a task to delete.")


# Clear all the tasks
def clear_tasks():
    response = messagebox.askyesno("Delete all tasks", "Are you sure you want to delete all tasks ?")
    if response:
        task_listbox_high.delete(0, tk.END)
        task_listbox_middle.delete(0, tk.END)
        task_listbox_low.delete(0, tk.END)


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

# Priority
priority_opt = StringVar(value="Low")
priority_dropdown = tk.OptionMenu(
    root,
    priority_opt,
    "High",
    "Middle",
    "Low",
)
priority_dropdown.configure(font=("Arial", 12))
priority_dropdown.pack(pady=10)

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


# Frame for Listbox and Scrollbar Level High
frame_global = tk.Frame(root)
frame_global.pack(pady=10)

#High
label_high = tk.Label(frame_global, text="High", font=("Arial", 12))
label_high.grid(column=0, row=0, padx=5)

frame_high = tk.Frame(frame_global)
frame_high.grid(column=0, row=1, padx=5)

scrollbar_high = tk.Scrollbar(frame_high)
scrollbar_high.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox_high = tk.Listbox(frame_high, width=20, height=15, yscrollcommand=scrollbar_high.set, font=("Arial", 12))
task_listbox_high.pack(pady=10)

scrollbar_high.config(command=task_listbox_high.yview)

#Middle
label_middle = tk.Label(frame_global, text="Middle", font=("Arial", 12))
label_middle.grid(column=1, row=0, padx=5)

frame_middle = tk.Frame(frame_global)
frame_middle.grid(column=1, row=1, padx=5)

scrollbar_middle = tk.Scrollbar(frame_middle)
scrollbar_middle.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox_middle = tk.Listbox(frame_middle, width=20, height=15, yscrollcommand=scrollbar_middle.set, font=("Arial", 12))
task_listbox_middle.pack(pady=10)

scrollbar_middle.config(command=task_listbox_middle.yview)

#Low
label_low = tk.Label(frame_global, text="Low", font=("Arial", 12))
label_low.grid(column=2, row=0, padx=5)

frame_low = tk.Frame(frame_global)
frame_low.grid(column=2, row=1, padx=5)

scrollbar_low = tk.Scrollbar(frame_low)
scrollbar_low.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox_low = tk.Listbox(frame_low, width=20, height=15, yscrollcommand=scrollbar_low.set, font=("Arial", 12))
task_listbox_low.pack(pady=10)

scrollbar_low.config(command=task_listbox_low.yview)


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
fill_list_boxes()
root.mainloop()
