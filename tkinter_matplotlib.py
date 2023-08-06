#! /bin/python

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib import style
import tkinter as tk
import numpy as np
# import parse_data_income_expense.py

# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig, ax = plt.subplots()

# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text = "Matplotlib + Tkinter!")
label.config(font=("Courier", 32))
label.pack()
frame.pack()

# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Plot data on Matplotlib Figure
t = np.arange(0, 2*np.pi, .01)
ax.plot(t, np.sin(t))
canvas.draw()

root.mainloop()
