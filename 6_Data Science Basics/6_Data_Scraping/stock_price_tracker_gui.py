import tkinter as tk
from stock_price_tracker import *

root = tk.Tk()
root.title("Stock Price Tracker")
root.geometry("400x400")
root.configure(bg="#f0f4c3")



# Stock Data List
stock_names = []
stock_values = {stock_name: get_stock_price(stock_name) for stock_name in stock_names}
    

# GUI Layout
# Title label
title_label = tk.Label(root, text="Stock Price Tracker", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Stock Frame
stock_frame = tk.Frame(
    root,
    bg="#f0f4c3"
)
stock_frame.pack(pady=10)

for i, stock_name in enumerate(stock_names[:5]):
    stock_name_label = tk.Label(
        stock_frame,
        text=stock_name,
        font=("Arial", 12),
        bg="#f0f4c3"
    )
    stock_name_label.grid(row=i, column=0, padx=5, pady=5)

    stock_value_label = tk.Label(
        stock_frame,
        text=stock_values[]
    )
