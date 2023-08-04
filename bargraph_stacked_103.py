#! /bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rc

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

print('\n---------------')
print('data:\n')
print(data)
print('\n---------------')
print('cross_tab_prop:\n')
print(cross_tab_prop)
print('\n---------------')
print('cross_tab:')
print(cross_tab)
# print('---------------')
#
#
# data_cashflow = pd.read_csv('./data/cashflow.csv', sep=';')
#
# cross_tab_prop_cashflow = pd.crosstab(index=data_cashflow['Budget'],
#                              columns=data_cashflow['Category'],
#                              normalize='index')
# print('\n---------------')
# print('[ cashflow.csv ]\n')
# print(data_cashflow)
# print('\n---------------')
# print('cross_tab_prop_cashflow:\n')
# print(cross_tab_prop_cashflow)
#
#
#
# print('---------------')
# print('[ Sandbox Data ]')
# print('---------------')
#
# categories_expenses = ['Wants', 'Needs', 'Savings', 'Salary']
# data_sandbox = pd.read_csv('./data/cashflow.csv', sep=';')
# # data_sandbox = pd.read_csv('./data/Sandbox_data.csv', sep=';')
# print('data_sandbox:')
# print(data_sandbox)
#
# data_sandbox = data_sandbox.loc[data_sandbox['Category']\
#     .isin(categories_expenses), ['Budget', 'Category', 'Total']].copy()
# # data_sandbox = data_sandbox.loc[data_sandbox['Subcategory']\
# #     .isin(categories_expenses), ['Category', 'Subcategory', 'Total']].copy()
# data_sandbox.dropna(inplace=True)
#
# data_sandbox_pivot = data_sandbox
# # data_sandbox_pivot.pivot(columns='Subcategory', values='Category')
# data_sandbox_pivot.pivot(columns='Budget', values='Category')
#
# categories_expenses = ['Wants', 'Needs', 'Savings']
# data_sandbox_filtered_expenses = data_sandbox[data_sandbox['Category']\
#     .isin(categories_expenses)]
# # print('data_sandbox_filtered_expenses:')
# # print(data_sandbox_filtered_expenses)
#
# print('---------------')
# # pivoted = data_filtered_expenses.pivot(columns='Subcategory')
# # pivoted = data_filtered_expenses.pivot(index='Category'\
#     # ,columns='Subcategory', values='Total')
# # data_sandbox_filtered_pivoted = \
#     # data_sandbox_filtered_expenses.pivot(columns='Subcategory', values='Total')
# print('data_sandbox.pivot_table:')
# # print(data_sandbox_filtered_pivoted)
# # print(data_sandbox_filtered_pivoted.pivot(columns='Subcategory',
#                                           # values='Total'))
# print(data_sandbox.pivot_table(index='Budget',
#                                columns='Category',
#                                values='Total'))
# print('---------------')
# print('crosstab:')
# print(pd.crosstab(index=data_sandbox['Budget'],
#                   columns=data_sandbox['Category'],))



def create_plot(data):
    cross_tab_prop = pd.crosstab(index=data['release_year'],
                                 columns=data['type'],
                                 normalize='index')

    cross_tab_prop.index.name = None


    cross_tab = pd.crosstab(index=data['release_year'],
                            columns=data['type'])


    cross_tab_prop.plot(kind='bar',
                        stacked=True,
                        colormap='tab10',
                        figsize=(5, 5))

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
               ncol=2, borderaxespad=0, title = 'Cashflow Dashboard',
               title_fontsize = 'xx-large',
               frameon = False)

    for n, x in enumerate([*cross_tab.index.values]):
        for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
                                       cross_tab_prop.loc[x].cumsum()):
            plt.text(x=n - 0.17,
                     y=(y_loc - proportion) + (proportion / 2 ), # Position of percentag
                     # y=(y_loc- proportion) + (proportion - 30 ),
                     # ax.bar_label(p, label_type='center'),
                     s=f'{np.round(proportion * 100, 1)}%',
                     color='yellow',
                     fontsize=9,
                     fontweight='bold')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    # plt.set_title('Contour plot of Delaunay triangulation')
    # plt.title(label=None)
    # plt.title(label='Title')
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()

    return plt

plt = create_plot(data)
plt.show()
