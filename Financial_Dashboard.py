#! /bin/python


# from tkinter import PhotoImage, Menu, ttk, Tk
from PIL import ImageTk, Image
from sys import exit

import pandas as pd
import numpy as np

# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# import matplotlib
# from bargraph_stacked_102 import example_graph


class Project_Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Financial Dashboard')
        self.state('normal')
        # self.geometry('600x600')
        # self.attributes('-normal', True)
        # self.attributes('-zoomed', True)normal
        # self.attributes('-topmost',True)

        # self.image_screen = PhotoImage(file = './image/Screen_check.png')
        # self.wm_iconphoto(True, './image/debt_icon.png')
        # self.image_icon_titlebar = PhotoImage(file = './image/debt_icon.png')
        # self.background_image = tk.Label(self, i = self.image_screen)
        # self.background_image.pack(fill='both', expand='yes')

        # checks
        self.check_notebook = 'closed'

        # self.load_data()
        self.format_window()
        self.populate_window()
        # self.layout_debt_roster()

    def load_data(self):
        self.filename ='./data/Debts.csv'
        self.debts = pd.read_csv(filename,
                   sep = ';')
        print(debts.iloc[:15, 38])
        # return debts

    def format_window(self):
        self.create_headder()
        self.create_footer()
        self.create_panel_left()
        self.create_panel_right()
        self.create_panel_main()

    def create_headder(self):
        self.headder = tk.Frame(self, bg='red')
        self.headder.pack(side='top', fill='x', expand=0)
        self.headder_label = tk.Label(self.headder, text = 'headder', bg='red')
        self.headder_label.pack()

    def create_footer(self):
        self.footer = tk.Frame(self, bg='orange')
        self.footer.pack(side='bottom', fill='x', expand=0)
        self.footer_label_status = tk.Label(self.footer, text = 'footer', bg='orange')
        self.footer_label_status.pack()

    def create_panel_left(self):
        self.panel_left = tk.Frame(self, bg='blue')
        self.panel_left.pack(side='left', fill='y', expand=0)
        self.panel_left_label = tk.Label(self.panel_left, text = 'panel_left', bg='blue')
        self.panel_left_label.pack()

    def create_panel_right(self):
        self.panel_right = tk.Frame(self, bg='green')
        self.panel_right.pack(side='right', fill='y', expand=0)
        self.panel_right_label = tk.Label(self.panel_right, text = 'panel_right', bg='green')
        self.panel_right_label.pack()

    def create_panel_main(self):
        self.panel_main = tk.Frame(self, bg='yellow')
        self.panel_main.pack(side='top', fill='both', expand=1)
        self.panel_main_label = tk.Label(self.panel_main, text = 'panel_main', bg='yellow')
        self.panel_main_label.pack()

    def populate_window(self):
        # self.create_notebook()
        self.create_panel_left_buttons()

    def create_graph_cashflow(self, frame):
        self.example_ = self.example_graph()
        # example_.show()
        self.canvas_example = FigureCanvasTkAgg(self.example_, frame)
        self.canvas_example.draw()
        self.canvas_example.get_tk_widget().pack(side='left', fill='both', expand=True)
        # return canvas_example

    def create_notebook(self):
        self.notebook = tk.Frame(self.panel_main)

        self.notebook_cashflow = tk.Frame(self.notebook, bg='purple')
        self.label_cashflow = tk.Label(self.notebook_cashflow, text = 'Cashflow', bg='purple')
        self.label_cashflow.pack()
        self.notebook_cashflow.pack(side='top', fill='both', expand=1)
        self.create_graph_cashflow(self.notebook_cashflow)

        self.notebook_debt_reduction = tk.Frame(self.notebook, bg='white')
        self.label_debt_reduction = tk.Label(self.notebook_debt_reduction, text = 'Debt Redution Calculator', bg='white')
        self.label_debt_reduction.pack()
        self.notebook_debt_reduction.pack(side='top', fill='both', expand=1)

        self.notebook_budget = tk.Frame(self.notebook, bg='cyan')
        self.label_budget = tk.Label(self.notebook_budget, text = 'Budget', bg='cyan')
        self.label_budget.pack()
        self.notebook_budget.pack(side='top', fill='both', expand=1)

        self.notebook_data = tk.Frame(self.notebook, bg='brown')
        self.label_data = tk.Label(self.notebook_data, text = 'Data', bg='brown')
        self.label_data.pack()
        self.notebook_data.pack(side='top', fill='both', expand=1)

    def notebook_selection(self, notebook_page):
        if self.check_notebook == 'closed':
            self.create_notebook()
            self.check_notebook = 'open'

        match notebook_page:
          
            case 'Cashflow':
                if self.notebook_cashflow.winfo_ismapped():
                    self.notebook_cashflow.pack_forget()
                else:
                    self.notebook_debt_reduction.pack_forget()
                    self.notebook_budget.pack_forget()
                    self.notebook_data.pack_forget()
                    self.notebook_cashflow.pack(side='top', fill='both', expand=1)
                    self.notebook.pack(side='top', fill='both', expand=1)
                    # print('Cashflow')
                    self.footer_label_status['text'] = 'Cashflow button pressed'
                    self.footer_label_status.pack(side='left', fill='x', expand=0)

            case 'Debt':
                if self.notebook_debt_reduction.winfo_ismapped():
                    self.notebook_debt_reduction.pack_forget()
                else:
                    self.notebook_cashflow.pack_forget()
                    self.notebook_budget.pack_forget()
                    self.notebook_data.pack_forget()
                    self.notebook_debt_reduction.pack(side='top', fill='both', expand=1)
                    self.notebook.pack(side='top', fill='both', expand=1)
                    # print('Debt')
                    self.footer_label_status['text'] = 'Debt button pressed'
                    self.footer_label_status.pack(side='left', fill='x', expand=0)
            case 'Budget':
                if self.notebook_budget.winfo_ismapped():
                    self.notebook_budget.pack_forget()
                else:
                    self.notebook_cashflow.pack_forget()
                    self.notebook_debt_reduction.pack_forget()
                    self.notebook_data.pack_forget()
                    self.notebook_budget.pack(side='top', fill='both', expand=1)
                    self.notebook.pack(side='top', fill='both', expand=1)
                    # print('Budget')
                    self.footer_label_status['text'] = 'Budget button pressed'
                    self.footer_label_status.pack(side='left', fill='x', expand=0)
            case 'Data':
                if self.notebook_data.winfo_ismapped():
                    self.notebook_data.pack_forget()
                else:
                    self.notebook_cashflow.pack_forget()
                    self.notebook_debt_reduction.pack_forget()
                    self.notebook_budget.pack_forget()
                    self.notebook_data.pack(side='top', fill='both', expand=1)
                    self.notebook.pack(side='top', fill='both', expand=1)
                    # print('Data')
                    self.footer_label_status['text'] = 'Data button pressed'
                    self.footer_label_status.pack(side='left', fill='x', expand=0)

    def create_panel_left_buttons(self):
        self.button_cashflow = tk.Button(self.panel_left, text='Cashflow', command=lambda:self.notebook_selection('Cashflow'))
        self.button_debt_reduction = tk.Button(self.panel_left, text='Debt', command=lambda:self.notebook_selection('Debt'))
        self.button_budget = tk.Button(self.panel_left, text='Budget', command=lambda:self.notebook_selection('Budget'))
        self.button_data = tk.Button(self.panel_left, text='Data', command=lambda:self.notebook_selection('Data'))

        self.button_cashflow.pack(fill='x')
        self.button_debt_reduction.pack(fill='x')
        self.button_budget.pack(fill='x')
        self.button_data.pack(fill='x')


    def button_new_entry(self):
        print('\'New Entry\' button was pressed.')


    def layout_debt_roster(self):
        self.label = ttk.Label(master = self, text = 'Debt Reduction Calculator')
        self.label.pack()

        # text = tk.Text(master = self)
        # text.pack()

        # entry = ttk.Entry(master = self)
        # entry.pack()

        self.button_new_entry = ttk.Button(master = self, text = 'New Entry', command = self.button_new_entry)
        self.button_new_entry.pack()



    def example_graph(self):
        print('---------------')
        print('[ Example Data ]')

        self.data = pd.read_csv('./data/netflix_titles.csv')

        self.data = self.data.loc[self.data['release_year'].isin([*range(2017, 2020)]), ['type', 'release_year']].copy()
        self.data.dropna(inplace=True)
        self.data['release_year'] = self.data['release_year'].astype('int')

        self.cross_tab_prop = pd.crosstab(index=self.data['release_year'],
                                     columns=self.data['type'],
                                     normalize='index')

        self.cross_tab = pd.crosstab(index=self.data['release_year'],
                                columns=self.data['type'])

        print('---------------')
        print('cross_tab_prop:')
        print(self.cross_tab_prop)
        print('---------------')
        print('cross_tab:')
        print(self.cross_tab)
        print('---------------')

        self.cross_tab_prop.plot(kind='bar',
                                stacked=True,
                                colormap='tab10',
                                figsize=(5, 5))

        self.plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

        for n, x in enumerate([*self.cross_tab.index.values]):
            for (proportion, y_loc) in zip(self.cross_tab_prop.loc[x],
                                           self.cross_tab_prop.loc[x].cumsum()):
                self.plt.text(x=n - 0.17,
                         y=(y_loc - proportion) + (proportion / 2),
                         s=f'{np.round(proportion * 100, 1)}%',
                         color='yellow',
                         fontsize=9,
                         fontweight='bold')


        self.plt.tight_layout()
        # plt.show()
        # return plt

if __name__ == '__main__':
    project_root = Project_Root()
    project_root.mainloop()
