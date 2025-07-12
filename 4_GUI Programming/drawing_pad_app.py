# Build a drawing pad app that allows freehand drawing on a canvas, provides a color picker for different color drawing colors, includes a clear button to reset, provides a mean to specify thickness
# Add undo/redo functionalities

import tkinter as tk
from tkinter import colorchooser, filedialog, StringVar
from PIL import Image

# Main window
root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("800x800")
root.configure(bg="#f0f0f0")

# Global Variables
current_color = "black"
current_thickness = 2
events_stored = []
cancelled_events = []
start_x = start_y = 0
current_shape = None
available_shapes = ["Oval", "Line", "Rectangle"]
available_modes = ["Fixed", "Draw"]

# Buttons to define shape and whether it is handfree or fixed
header_frame = tk.Frame(
    root,
    bg="#f0f0f0"
)
header_frame.pack(pady=10)

shape_opt = StringVar(root, "Oval")
shape_dropdown = tk.OptionMenu(
    header_frame,
    shape_opt,
    *available_shapes
)
shape_dropdown.grid(row=0, column=0, padx=10)


# Define options depending on shape
def get_options_for_shape(shape):
    return {
        "outline": current_color,
        "width": current_thickness
    } if shape != "Line" else {
        "fill": current_color,
        "width": current_thickness
    }


# Define functions for fixed shapes
def on_mouse_down(event):
    global start_x, start_y, current_shape, current_color
    start_x, start_y = event.x, event.y
    shape = shape_opt.get()

    coords = (
        start_x,
        start_y,
        event.x,
        event.y
    )

    options = get_options_for_shape(shape)

    # Start drawing a rectangle (could be line or oval)
    if shape == "Oval":
        current_shape = canvas.create_oval(*coords, **options)
    elif shape == "Line":
        current_shape = canvas.create_line(*coords, **options)
    elif shape == "Rectangle":
        current_shape = canvas.create_rectangle(*coords, **options)


def on_mouse_drag(event):
    global current_shape, current_color
    # Update shape size dynamically
    coords = (
        start_x,
        start_y,
        event.x,
        event.y
    )

    shape = shape_opt.get()

    options = get_options_for_shape(shape)

    action = {
        "type": shape.lower(),
        "coords": coords,
        "options": options,
        "id": current_shape
    }

    canvas.coords(current_shape, *coords)
    events_stored.append(action)
    cancelled_events.clear()


# Create canvas
canvas = tk.Canvas(
    root,
    width=500,
    height=400,
    bg="white",
    relief="ridge",
    bd=2
)
canvas.pack(pady=20)


# Draw on Mouse Drag
def draw(event):
    global events_stored, cancelled_events, current_color

    x, y = event.x, event.y

    coords = (
        x - current_thickness,
        y - current_thickness,
        x + current_thickness,
        y + current_thickness
    )

    options = {
        "fill": f"{current_color}",
        "outline": f"{current_color}",
    }

    shape = shape_opt.get()

    if shape == "Oval":
        draw_id = canvas.create_oval(
            *coords,
            **options
        )
    elif shape == "Line":
        draw_id = canvas.create_line(
            *coords,
            fill=current_color
        )
    elif shape == "Rectangle":
        draw_id = canvas.create_rectangle(
            *coords,
            **options
        )

    action = {
        "type": shape.lower(),
        "coords": coords,
        "options": options,
        "id": draw_id
    }
    events_stored.append(action)
    cancelled_events.clear()


# Undo event
def undo_action():
    global events_stored, cancelled_events

    if len(events_stored) == 0:
        undo_btn.config(state="disabled")
    else:
        undo_btn.config(state="normal")
        action = events_stored.pop()
        canvas.delete(action["id"])
        cancelled_events.append(action)


# Redo event
def redo_action():
    global events_stored, cancelled_events

    if len(cancelled_events) == 0:
        redo_btn.config(state="disabled")
    else:
        redo_btn.config(state="normal")
        action = cancelled_events.pop()
        if action["type"] == "oval":
            id = canvas.create_oval(*action["coords"], **action["options"])
        elif action["type"] == "line":
            id = canvas.create_line(*action["coords"], **action["options"])
        elif action["type"] == "rectangle":
            id = canvas.create_rectangle(*action["coords"], **action["options"])
        action["id"] = id
        events_stored.append(action)



# Notify on window
def show_temp_message(msg, duration_ms = 2000):
    message_label = tk.Label(
        root,
        text=msg,
        font=("Arial", 12),
        fg="green"
    )


# Save image
def save_image():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPG files", "*.jpg"),
            ("All files", "*.*"),
        ]
    )

    if not file_path:
        return

    ps_file = file_path + ".ps"
    canvas.postscript(file=ps_file, colormode='color')

    img = Image.open(ps_file)
    img.save(file_path)

    show_temp_message(f"Image successfully saved at {file_path}")


# Clear Function
def clear_canvas():
    canvas.delete("all")


# Change Color
def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color


# Change thickness
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)


# Bind drawing
def conditional_events_bindings(_=None):
    mode = mode_opt.get()
    if mode == "Fixed":
        canvas.bind("<Button-1>", on_mouse_down)
        canvas.bind("<B1-Motion>", on_mouse_drag)
    elif mode == "Draw":
        canvas.bind("<B1-Motion>", draw)

canvas.bind("<B1-Motion>", draw)

mode_opt = StringVar(root, "Draw")
mode_dropdown = tk.OptionMenu(
    header_frame,
    mode_opt,
    *available_modes,
    command=conditional_events_bindings
)
mode_dropdown.grid(row=0, column=1, padx=10)

# Control Panel
control_frame = tk.Frame(
    root,
    bg="#f0f0f0"
)
control_frame.pack(pady=10)

# Color Button
color_btn = tk.Button(
    control_frame,
    text="Choose Color",
    command=change_color,
    bg="#4caf50",
    fg="black",
    font=("Arial", 10)
)
color_btn.grid(row=0, column=0, padx=10)

# Clear Button
clear_btn = tk.Button(
    control_frame,
    text="Clear Canvas",
    command=clear_canvas,
    bg="#f44336",
    fg="black",
    font=("Arial", 10)
)
clear_btn.grid(row=0, column=1, padx=10)

# Thickness Control
thickness_label = tk.Label(
    control_frame,
    text="Thickness",
    bg="#f0f0f0",
    font=("Arial", 10)
)
thickness_label.grid(row=0, column=2, padx=10)

thickness_slider = tk.Scale(
    control_frame,
    from_=1,
    to=10,
    orient="horizontal",
    command=change_thickness,
    bg="#f0f0f0"
)
thickness_slider.set(2)
thickness_slider.grid(row=0, column=3, padx=10)

# Undo Redo Buttons
undo_btn = tk.Button(
    control_frame,
    text="Undo",
    command=undo_action,
    fg="black",
    font=("Arial", 10)
)
undo_btn.grid(row=1, column=0, padx=10)

redo_btn = tk.Button(
    control_frame,
    text="Redo",
    command=redo_action,
    fg="black",
    font=("Arial", 10)
)
redo_btn.grid(row=1, column=1, padx=10)

# Save image button
save_btn = tk.Button(
    root,
    text="Save",
    command=save_image,
    fg="black",
    font=("Arial", 10),
    width=20
)
save_btn.pack(pady=10)

# Run application
root.mainloop()