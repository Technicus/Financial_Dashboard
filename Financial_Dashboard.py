#! /bin/python


import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# import reserve_chart
from reserve_chart import reserve_fig, reserve_ax
import numpy as np


# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
root.attributes('-type', 'dialog')

# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text = "Financial Dashboard")
label.config(font=("Courier", 32))
label.pack()
frame.pack()

panel_left = tk.Frame(frame, bg='blue')
panel_left.pack(side='left', fill='y', expand=0)
panel_left_label = tk.Label(panel_left, text = 'panel_left', bg='blue')
panel_left_label.pack()

panel_main = tk.Frame(frame, bg='yellow')
panel_main.pack(side='top', fill='both', expand=1)
panel_main_label = tk.Label(panel_main, text = 'panel_main', bg='yellow')
panel_main_label.pack()

notebook = tk.Frame(panel_main)

notebook_monetary_guage = tk.Frame(notebook, bg='purple')
label_monetary_guage = tk.Label(notebook_monetary_guage, text = 'Cashflow', bg='purple')
label_monetary_guage.pack()
notebook_monetary_guage.pack(side='top', fill='both', expand=1)
# create_graph_cashflow(notebook_monetary_guage)
notebook_monetary_guage.pack(side='top', fill='both', expand=1)

notebook_debt_reduction = tk.Frame(notebook, bg='white')
label_debt_reduction = tk.Label(notebook_debt_reduction, text = 'Debt Redution Calculator', bg='white')
label_debt_reduction.pack()
notebook_debt_reduction.pack(side='top', fill='both', expand=1)

button_monetary_guage = tk.Button(panel_left, text='Monetary Guage', command=lambda:self.notebook_selection('Cashflow'))
button_debt_reduction = tk.Button(panel_left, text='Debt', command=lambda:self.notebook_selection('Debt'))# Create Canvas

canvas = FigureCanvasTkAgg(reserve_fig, master=notebook_monetary_guage)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas.draw()

root.mainloop()
