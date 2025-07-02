# Objective: Build a GUI-based Expense Tracker App that allows users to:
# Add new expenses with category, amount and description
# Display expense history in a Listbox
# Delete expenses from the list
# Save and load expenses from a file
# Calculate and display total expenses

#Core Features:
# User-friendly GUI with tkinter widgets
# Validation for numerical inputs
# Persistent data storage using a CSV file
# Total expense calculation
# Ability to delete specific expenses

# Key GUI Components
# Entry Widgets: For entering expense details
# Dropdown (OptionMenu): For selecting expense categories
# Listbox: For displaying added expenses
# Labels: To display dynamic updates (e.g. Total expenses).
# Buttons: For adding, deleting, clearing and exporting data.

# Bonus challenge
# Add a date to log date of expenses
# Search a particular expenses
# Export expenses as PDF File

from tkcalendar import DateEntry #New library
from tkinter import messagebox, StringVar, ttk
import tkinter as tk
import csv
import os

# Expense Tracker App

# File for storing expenses
EXPENSE_FILE = "./assets/expenses.csv"

# Create Main Application Window
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("600x600")
root.configure(bg="#f0f4c3")

# Expense Data List
expenses = []
search_results = []


# Load Existing Expenses from CSV
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                expenses.append(row)
                expenses_listbox.insert(tk.END, f"{row[0]} | €{row[1]} | {row[2]} | {row[3]}")
        if expenses:
            search_button.config(state="normal")


# Save Expenses to CSV
def save_expenses():
    with open(EXPENSE_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for expense in expenses:
            writer.writerow(expense)


# Add Expense
def add_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()
    date = date_entry.get()

    if not amount.isdigit() or not category or not description or not date:
        messagebox.showerror("Invalid Input", "Please enter valid expense details.")
        return

    expenses.append([category, amount, description, date])
    expenses_listbox.insert(tk.END, f"{category} | €{amount} | {description} | {date}")
    search_button.config(state="normal")
    calculate_total()
    clear_inputs()
    save_expenses()


# Delete Selected Expense
def delete_expense():
    selected = expenses_listbox.curselection()
    if selected:
        expenses_listbox.delete(selected[0])
        return

    index = selected[0]
    del expenses[index]
    save_expenses()


# Clear All Inputs
def clear_inputs():
    category_var.set("Select Category")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)


# Calculate Total Expenses
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    total_label.config(text=f"Total Expenses: €{total:.2f}")


# Clear All Expenses
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expenses_listbox.delete(0, tk.END)
        calculate_total()
        save_expenses()


# Search Expense
def search_expense():
    if not expenses:
        search_button.config(state="disabled")
        return
    search_results.clear()
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()
    date = date_entry.get()

    expenses_listbox.delete(0, tk.END)

    for expense in expenses:
        if category == expense[0] or amount == expense[1] or description == expense[2] or date == expense[3]:
            search_results.append(expense)
            expenses_listbox.insert(tk.END, f"{expense[0]} | €{expense[1]} | {expense[2]} | {expense[3]}")
    if not search_results:
        messagebox.showwarning("No result found", "No expense found for the given inputs.")
        return

    reset_button.config(state="normal")
    total = sum(float(expense[1]) for expense in search_results)
    total_label.config(text=f"Total Expenses: €{total:.2f}")
    clear_inputs()


# Reset Search
def reset_search():
    if not search_results:
        reset_button.config(state="disabled")
        return
    expenses_listbox.delete(0, tk.END)
    load_expenses()
    calculate_total()


# ----- GUI Layout -----
title_label = tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 24),
    bg="#f0f4c3"
)
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(
    root,
    bg="#f0f4c3"
)
input_frame.pack(pady=10)

# Category
category_label = tk.Label(
    input_frame,
    text="Category",
    font=("Arial", 12),
    bg="#f0f4c3"
)
category_label.grid(row=0, column=0, padx=5, pady=5)
category_var = tk.StringVar(value="Select Category")
category_dropdown = ttk.Combobox(
    input_frame,
    textvariable=category_var,
    values=["Food", "Transport", "Rent", "Utilities", "Other"]
)
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Amount
amount_label = tk.Label(
    input_frame,
    text="Amount (€)",
    font=("Arial", 12),
    bg="#f0f4c3"
)
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(
    input_frame,
    font=("Arial", 12)
)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Description
description_label = tk.Label(
    input_frame,
    text="Description",
    font=("Arial", 12),
    bg="#f0f4c3"
)
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(
    input_frame,
    font=("Arial", 12)
)
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Date
date_label = tk.Label(
    input_frame,
    text="Date",
    font=("Arial", 12),
    bg="#f0f4c3"
)
date_label.grid(row=3, column=0, padx=5, pady=5)
date_entry = DateEntry(
    input_frame
)
date_entry.configure(font=("Arial", 12))
date_entry.grid(row=3, column=1, padx=5, pady=5)

# Search functionalities
search_frame = tk.Frame(
    root,
    bg="#f0f4c3"
)
search_frame.pack(pady=10)

search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_expense,
    bg="white",
    fg="black"
)
search_button.grid(row=0, column=0, padx=5, pady=5)

reset_button = tk.Button(
    search_frame,
    text="Reset",
    command=reset_search,
    bg="#607d8b",
    fg="white"
)
reset_button.grid(row=0, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(
    root,
    bg="#f0f4c3"
)
btn_frame.pack(pady=10)

add_button = tk.Button(
    btn_frame,
    text="Add Expense",
    command=add_expense,
    bg="#4caf50",
    fg="white"
)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    btn_frame,
    text="Delete Expense",
    command=delete_expense,
    bg="#f44336",
    fg="white"
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    btn_frame,
    text="Clear All",
    command=clear_all,
    bg="#607d8b",
    fg="white"
)
clear_button.grid(row=0, column=2, padx=5)

# export_button = tk.Button(
#     btn_frame,
#     text="Export as PDF",
#     command=export_pdf,
#     bg="#607d8b",
#     fg="white"
# )
# export_button.grid(row=0, column=3, padx=5)

# Expense ListBox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expenses_listbox = tk.Listbox(frame, width=50, height=10, yscrollcommand=scrollbar.set, font=("Arial", 12))
expenses_listbox.pack()

scrollbar.config(command=expenses_listbox.yview)


# Total Label
total_label = tk.Label(
    root,
    text="Total Expenses: €0.00",
    font=("Arial", 14),
    bg="#f0f4c3"
)
total_label.pack(pady=10)


# Load Previous Data
load_expenses()
calculate_total()

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    bg="#d32f2f",
    fg="white"
)
exit_button.pack(pady=10)

# Run Application
root.mainloop()