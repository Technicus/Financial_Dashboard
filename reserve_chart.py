#! /bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mtick
from data_income_expense import data_budget_quantities, data_budget_proportions, data_budget_quantities_proportions
import itertools


def reserve_chart(chart_data = None, invert = False, sort = None):

    def autolabel(bar_group, labels, height_offset):
        for (bar, label, height_offset) in zip(bar_group, labels, height_offset):
            height = bar.get_height()

            ax.annotate(
                text = '${:,.2f}'.format(label), #str(label),
                fontsize=9,
                fontweight='bold',
                # color='yellow',
                xy = ((bar.get_x() + bar.get_width() / 2, height + height_offset - 0.04)),
                ha = 'center',
                xytext = (0, 3),
                textcoords = 'offset points',
                bbox = dict(facecolor = 'greenyellow', alpha =0.8)
                )

    if sort != None:
        chart_data = chart_data.reindex(sort)

    if invert:
        index = chart_data.index.values
        income = {'quantities': pd.Series(chart_data['Income']).tolist(),
                  'proportions': pd.Series(chart_data['Income_Proportion']).tolist()}
        reserve = {'quantities': pd.Series(chart_data['Reserve']).tolist(),
                   'proportions': pd.Series(chart_data['Reserve_Proportion']).tolist()}
    else:
        index = chart_data.index.values
        income = {'quantities': pd.Series(chart_data['Reserve']).tolist(),
                   'proportions': pd.Series(chart_data['Reserve_Proportion']).tolist()}
        reserve = {'quantities': pd.Series(chart_data['Income']).tolist(),
                  'proportions': pd.Series(chart_data['Income_Proportion']).tolist()}

    width = 0.5
    # x_income  = [x - width for x in range(len(index))]
    x_income  = [x for x in range(len(index))]
    x_reserve = [x for x in range(len(index))]

    # ytickformat('$%,.0f')
    fig, ax = plt.subplots()

    if invert:
        bar_reserve = ax.bar(x_income,  reserve['proportions'],  width, label = 'income',  color = 'lightgrey')
        bar_income  = ax.bar(x_reserve, income['proportions'], width, label = 'reserve', bottom = reserve['proportions'], color = 'palegreen')
    else:
        bar_income  = ax.bar(x_income,  income['proportions'],  width, label = 'income',  color = 'palegreen')
        bar_reserve = ax.bar(x_reserve, reserve['proportions'], width, label = 'reserve', bottom = income['proportions'], color = 'lightgrey')

    # ax.plot(index, [0, 0, 0])
    ax.set_title('')
    ax.set_ylabel('')
    ax.set_xlabel('')
    ax.legend()
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
    ax.set_axisbelow(True)

    plt.xticks(range(0, len(index)))
    ax.set_xticklabels(index)
    # ax.set_xlabels(index)
    # ax.bar_label('p', label_type='center')

    # autolabel(bar_income, income['quantities'], income['proportions'],)
    print('autolabel_offset:')
    autolabel_offset = []
    print(type(autolabel_offset))
    print(autolabel_offset)
    # for entry in index:
    for x in range(len(index)):
        autolabel_offset.append(0)
        print(autolabel_offset)

    if invert:
        autolabel(bar_reserve, reserve['quantities'], autolabel_offset)
        autolabel(bar_income, income['quantities'], reserve['proportions'])
    else:
        autolabel(bar_income, income['quantities'], autolabel_offset)
        autolabel(bar_reserve, reserve['quantities'], income['proportions'],)

    plt.yticks(range(0, 1))
    plt.yticks([0, 0.25, 0.50, 0.75, 1.00])

    # plt.grid(axis = 'y')
    # plt.grid(True, color = "grey", linewidth = "1.4", linestyle = "-.")
    plt.grid(axis = 'y', color = "grey", linewidth = "1")

    plt.legend(
        bbox_to_anchor=(0., 1.02, 1., .102),
        loc='lower center',
        ncol=2, borderaxespad=0, title = 'Monetary Gauage',
        title_fontsize = 'xx-large',
        frameon = False)

    return fig, ax


index = data_budget_quantities.index.values
income = {'quantities': pd.Series(data_budget_quantities['Income']).tolist(),
          'proportions': pd.Series(data_budget_proportions['Income_Proportion']).tolist()}
reserve = {'quantities': pd.Series(data_budget_quantities['Reserve']).tolist(),
          'proportions': pd.Series(data_budget_proportions['Reserve_Proportion']).tolist()}
print('\n----')
print('index:')
print(index)
print('income:')
print(income)
print('reserve:')
print(reserve)

# fig, ax = reserve_chart(data_budget_quantities_proportions, sort = ['Needs', 'Discretionary', 'Savings'], invert = True)
fig, ax = reserve_chart(data_budget_quantities_proportions, sort = ['Needs', 'Discretionary', 'Savings'], invert = False)

# plt.show()

