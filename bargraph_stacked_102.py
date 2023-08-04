#! /bin/python

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import rc

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#
#
# import tkinter as tk
# # from tkinter import PhotoImage, Menu, ttk, Tk
# from PIL import ImageTk, Image
# from sys import exit
# import pandas as pd
#
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# import matplotlib



def example_graph():
    print('---------------')
    print('[ Example Data ]')

    data = pd.read_csv('./data/netflix_titles.csv')

    data = data.loc[data['release_year'].isin([*range(2017, 2020)]), ['type', 'release_year']].copy()
    data.dropna(inplace=True)
    data['release_year'] = data['release_year'].astype('int')

    cross_tab_prop = pd.crosstab(index=data['release_year'],
                                 columns=data['type'],
                                 normalize='index')

    cross_tab = pd.crosstab(index=data['release_year'],
                            columns=data['type'])

    print('---------------')
    print('cross_tab_prop:')
    print(cross_tab_prop)
    print('---------------')
    print('cross_tab:')
    print(cross_tab)
    print('---------------')

    cross_tab_prop.plot(kind='bar',
                            stacked=True,
                            colormap='tab10',
                            figsize=(5, 5))

    plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

    for n, x in enumerate([*cross_tab.index.values]):
        for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
                                       cross_tab_prop.loc[x].cumsum()):
            plt.text(x=n - 0.17,
                     y=(y_loc - proportion) + (proportion / 2),
                     s=f'{np.round(proportion * 100, 1)}%',
                     color='yellow',
                     fontsize=9,
                     fontweight='bold')


    plt.tight_layout()
    # plt.show()
    return plt
