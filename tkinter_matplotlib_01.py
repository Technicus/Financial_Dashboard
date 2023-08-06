#! /bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mtick
import parse_data_income_expense
import itertools

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

index = parse_data_income_expense.data_sandbox_quantities.index.values
income = {'quantities': pd.Series(parse_data_income_expense.data_sandbox_quantities['Income']).tolist(),
          'proportions': pd.Series(parse_data_income_expense.data_sandbox_proportions['Income']).tolist()}
# reserve = pd.Series(parse_data_income_expense.data_sandbox_quantities['Reserve']).tolist()
reserve = {'quantities': pd.Series(parse_data_income_expense.data_sandbox_quantities['Reserve']).tolist(),
          'proportions': pd.Series(parse_data_income_expense.data_sandbox_proportions['Reserve']).tolist()}
print('\n----')
print(index)
print(income)
print(reserve)

width = 0.5
# x_income  = [x - width for x in range(len(index))]
x_income  = [x for x in range(len(index))]
x_reserve = [x for x in range(len(index))]

# ytickformat('$%,.0f')
fig, ax = plt.subplots()

# bar_income = ax.bar(x_income, income['proportions'], width, label = 'income', color = 'cyan')
# bar_reserve = ax.bar(x_reserve, reserve, width, label = 'reserve', color = 'green')
# bar_reserve = ax.bar(x_reserve, reserve['proportions'], width, label = 'reserve', color = 'green', bottom = income['proportions'])
bar_reserve = ax.bar(x_reserve, reserve['proportions'], width, label = 'reserve', bottom = income['proportions'], color = 'palegreen')
bar_income  = ax.bar(x_income,  income['proportions'],  width, label = 'income',  color = 'lightgrey')
# bar_reserve = ax.bar(x_reserve, reserve['proportions'], width, label = 'reserve', color = 'palegreen')
# bar_income  = ax.bar(x_income,  income['proportions'],  width, label = 'income',  color = 'lightgrey', bottom = reserve['proportions'],)

# ax.plot(index, [0, 0, 0])

ax.set_title('')
ax.set_ylabel('')
ax.set_xlabel('')
ax.legend()
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))
ax.set_axisbelow(True)

plt.xticks(range(0, 3))
ax.set_xticklabels(index)
# ax.set_xlabels(index)
# ax.bar_label('p', label_type='center')

# autolabel(bar_income, income['quantities'], income['proportions'],)
autolabel(bar_income, income['quantities'], [0,0,0])
autolabel(bar_reserve, reserve['quantities'], income['proportions'],)
# autolabel(bar_reserve, reserve['quantities'], [0,0,0],)
# autolabel(bar_income, income['quantities'], income['proportions'])

plt.yticks(range(0, 1))
plt.yticks([0, 0.25, 0.50, 0.75, 1.00])

# plt.grid(axis = 'y')
# plt.grid(True, color = "grey", linewidth = "1.4", linestyle = "-.")
plt.grid(axis = 'y', color = "grey", linewidth = "1")

plt.legend(
    bbox_to_anchor=(0., 1.02, 1., .102),
    loc='lower center',
    ncol=2, borderaxespad=0, title = 'Cashflow Dashboard',
    title_fontsize = 'xx-large',
    frameon = False)

plt.show()
