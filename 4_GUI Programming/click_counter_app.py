import tkinter as tk
import time

# Tracks the number of clicks, allow the counter to reset, display updates of clicks
# Bonus challenge: Add a decrement button, always keep a track on the highest count performed
# Main Window
root = tk.Tk()
root.title("Click Counter App")
root.geometry("500x400")
root.configure(bg="#e3f2fd")

# Load the highest value for counter
max_counter_file = './assets/highest_counter.txt'
try:
    with open(max_counter_file, 'r') as file:
        max_counter_value = int(file.read().strip())
except Exception as e:
    max_counter_value = 0

# Counter Variable
counter = 0

# Increment Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

# Decrement Function
def decrement():
    global counter
    counter -= 1
    counter_label.config(text=f"Clicks: {counter}")

# Save highest counter
def save_highest_counter():
    global counter, max_counter_value
    if counter > max_counter_value:
        max_counter_value = counter
    with open(max_counter_file, 'w') as file:
        file.write(str(max_counter_value))

# Reset Function
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks: 0")

# Exit window
def exit():
    global start_time
    save_highest_counter()
    end_time = time.perf_counter()
    time_execution = end_time - start_time
    print(f"Exiting the Click Counter App. Executed in {time_execution} seconds.")
    root.destroy()

# Title Label
title_label = tk.Label(
    root,
    text="Click Counter",
    font=("Arial", 20),
    bg="#e3f2fd"
)
title_label.pack(pady=20)

# Highest Value Label
highest_value_label = tk.Label(
    root,
    text=f"Highest value reached: {max_counter_value}",
    font=("Arial", 12),
    bg="#e3f2fd"
)
highest_value_label.pack(pady=5)

# Counter Label
counter_label = tk.Label(
    root,
    text="Clicks: 0",
    font=("Arial", 16),
    bg="#e3f2fd"
)
counter_label.pack(pady=5)

# Increment Button
increment_button = tk.Button(
    root,
    text="Increment",
    command=increment,
    font=("Arial", 14),
    bg="#4caf50",
    fg="white"
)
increment_button.pack(pady=5)

# Decrement Button
decrement_button = tk.Button(
    root,
    text="Decrement",
    command=decrement,
    font=("Arial", 14),
    bg="#4caf50",
    fg="white"
)
decrement_button.pack(pady=5)

# Reset Button
reset_button = tk.Button(
    root,
    text="Reset",
    command=reset,
    font=("Arial", 14),
    bg="#f44336",
    fg="white"
)
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    command=exit,
    font=("Arial", 14),
    bg="#607d8b",
    fg="white"
)
exit_button.pack(pady=20)

# Run the application
start_time = time.perf_counter()
root.mainloop()