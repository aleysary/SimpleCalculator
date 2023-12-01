import tkinter as tk
from tkinter import ttk

def on_click(value):
    current = str(entry.get())
    new_value = str(current) + str(value)
    entry.delete(0, tk.END)
    entry.insert(0, new_value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        result = eval(entry.get())
        result = round(result**0.5, 8)  # Round to avoid floating-point precision issues
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def percentage():
    try:
        result = eval(entry.get())
        result = result / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(window, width=20, font=('Arial', 14), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4, pady=5)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(window, text=button, style='TButton', command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
ttk.Button(window, text='C', style='TButton', command=clear_entry).grid(row=row_val, column=col_val, padx=2, pady=2)
ttk.Button(window, text='=', style='TButton', command=calculate).grid(row=row_val, column=col_val + 1, padx=2, pady=2)
ttk.Button(window, text='√', style='TButton', command=square_root).grid(row=row_val + 1, column=col_val, padx=2, pady=2)
ttk.Button(window, text='%', style='TButton', command=percentage).grid(row=row_val + 1, column=col_val + 1, padx=2, pady=2)
ttk.Button(window, text='⌫', style='TButton', command=backspace).grid(row=row_val + 1, column=col_val, padx=2, pady=2)

# Configure style for buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

# Run the main loop
window.mainloop()
