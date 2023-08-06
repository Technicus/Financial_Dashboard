#! /bin/python


import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# import reserve_chart
from reserve_chart import fig, ax
import numpy as np


# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()

# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text = "Financial Dashboard")
label.config(font=("Courier", 32))
label.pack()
frame.pack()

# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas.draw()

root.mainloop()
