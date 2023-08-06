#! /bin/python


# # from tkinter import PhotoImage, Menu, ttk, Tk
# from PIL import ImageTk, Image
# from sys import exit
#
# import pandas as pd
# import numpy as np
#
# # from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
# # from matplotlib.figure import Figure
# # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
#

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import bargraph_stacked
from data.data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
import matplotlib.pyplot as plt
# import mpld3

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
# fig1 = bargraph_stacked.graph_income_expense

ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

# plt.show()

# Chart 2: Horizontal bar chart of inventory data
# fig2, ax2 = plt.subplots()
fig2 = bargraph_stacked.graph_income_expense
# fig2 = mpld3.fig_to_html(bargraph_stacked.graph_income_expense)

# ax2.barh(list(inventory_data.keys()), inventory_data.values())
# ax2.set_title("Inventory by Product")
# ax2.set_xlabel("Inventory")
# ax2.set_ylabel("Product")
# plt.show()

# Create a window and add charts
root = tk.Tk()
root.title("Dashboard")
# root.state('zoomed')
root.state('normal')

side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)


canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)


root.mainloop()
