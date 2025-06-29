# Build BMI calculator which accepts weight in kilograms and height in meters as input
# BMI = weight / height^2
# Display the BMI value and health status to the user
# Add BMI Categories and tips for each status
# Implement history tracker to save multiple BMI calculations
# switch metrics units

import csv
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, StringVar

bmi_history_file = "./assets/bmi_history_file.csv"
bmi_history_columns = ["date", "weight", "weight_unit", "height", "height_unit", "bmi"]

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

# Title Label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Weight Input
weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12), bg="#f0f4c3")
weight_label.pack()

weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack(pady=5)

weight_units_map = {
    "Kilograms (kgs)": "kg",
    "Pounds (lb)": "lb"
}
weight_units_values = list(weight_units_map.keys())
weight_units_opt = StringVar(value="Kilograms (kgs)")


# Convert Weight into kga
def convert_weight_kgs(value, unit):
    if unit == "lb":
        return value * 0.454
    else:
        return value


# Update Weight label
def update_weight_label(_=None):
    weight_unit = weight_units_map[weight_units_opt.get()]
    weight_label.config(text=f"Enter your weight ({weight_unit}):", font=("Arial", 12), bg="#f0f4c3")


weight_units_dropdown = tk.OptionMenu(
    root,
    weight_units_opt,
    *weight_units_values,
    command=update_weight_label
)
weight_units_dropdown.pack()

# Height Input
height_label = tk.Label(root, text="Enter your height (m): ", font=("Arial", 12), bg="#f0f4c3")
height_label.pack()

height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack(pady=5)

height_units_map = {
    "Meters (m)": "m",
    "Feet (ft)": "ft",
    "Inches (in)": "in"
}
height_units_values = list(height_units_map.keys())
height_units_opt = StringVar(value="Meters (m)")


# Update Height Label
def update_height_label(_=None):
    height_unit = height_units_map[height_units_opt.get()]
    height_label.config(text=f"Enter your height ({height_unit}):", font=("Arial", 12), bg="#f0f4c3")


# Convert Height into meters
def convert_height_meters(value, unit):
    if unit == "ft":
        return value * 0.3048
    elif unit == "in":
        return value * 0.0254
    else:
        return value


height_units_dropdown = tk.OptionMenu(
    root,
    height_units_opt,
    *height_units_values,
    command=update_height_label
)
height_units_dropdown.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4c3")
result_label.pack()


# Load BMI computation history
def load_bmi_history():
    try:
        with open(bmi_history_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]
    except Exception as e:
        print(f"Failed to load history : {e}")
    return []


# Save BMI history
def save_bmi_history(weight, weight_unit, height, height_unit, bmi):
    try:
        current_history = load_bmi_history()
        current_history.append(
            {
                "date": datetime.strftime(datetime.now(), "%Y-%m-%d"),
                "weight": weight,
                "weight_unit": weight_unit,
                "height": height,
                "height_unit": height_unit,
                "bmi": round(bmi, 2)
            }
        )
        with open(bmi_history_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=bmi_history_columns)
            writer.writeheader()
            writer.writerows(current_history)
    except Exception as e:
        print(f"Failed to save BMI history : {e}")


# Display the 5 last BMI computations
def display_5_last_BMIs():
    history_log = load_bmi_history()
    text_messagebox = "Last computation requests :"
    for line in history_log[:5]:
        text_messagebox += f"\n - {line['date']} - BMI Value: {line['bmi']} (Weight : {line['weight']} {line['weight_unit']}, Height : {line['height']} {line['height_unit']})"
    messagebox.showinfo("5 last BMIs", text_messagebox)


# Calculate BMI Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        weight_unit = weight_units_map[weight_units_opt.get()]
        height_unit = height_units_map[height_units_opt.get()]
        
        weight = convert_weight_kgs(weight, weight_unit)
        height = convert_height_meters(height, height_unit)

        bmi = weight / (height ** 2)

        status = ""
        
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obesity"

        result_label.config(text=f"BMI: {bmi:.2f}\nStatus: {status}", fg="green")
        save_bmi_history(weight, weight_unit, height, height_unit, bmi)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height")


# Buttons
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12), bg="#4caf50", fg="white")
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="", font=("Arial", 14), bg="#f0f4c3")])
reset_button.pack(pady=5)

bmi_history_button = tk.Button(root, text="BMI History", command=display_5_last_BMIs)
bmi_history_button.pack()

# Run the App
root.mainloop()