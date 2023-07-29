import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

print('---------------')
categories_expenses = ['Wants', 'Needs', 'Savings', 'Salary']
data_sandbox = pd.read_csv('./data/Sandbox_data.csv', sep=';')
print('data_sandbox:')
print(data_sandbox)
print('---------------')


data_sandbox = data_sandbox.loc[data_sandbox['Subcategory'].isin(categories_expenses),
                        ['Category', 'Subcategory', 'Total']].copy()
data_sandbox.dropna(inplace=True)

data_sandbox_pivot = data_sandbox
data_sandbox_pivot.pivot(columns='Subcategory', values='Category')

categories_expenses = ['Wants', 'Needs', 'Savings']
data_sandbox_filtered_expenses = data_sandbox[data_sandbox['Subcategory'].isin(categories_expenses)]
# print('data_sandbox_filtered_expenses:')
# print(data_sandbox_filtered_expenses)

print('---------------')
# pivoted = data_filtered_expenses.pivot(columns='Subcategory')
# pivoted = data_filtered_expenses.pivot(index='Category', columns='Subcategory', values='Total')
# data_sandbox_filtered_pivoted = data_sandbox_filtered_expenses.pivot(columns='Subcategory', values='Total')
print('data_sandbox.pivot_table:')
# print(data_sandbox_filtered_pivoted)
# print(data_sandbox_filtered_pivoted.pivot(columns='Subcategory',
                                          # values='Total'))
print(data_sandbox.pivot_table(index='Subcategory',
                               columns='Category',
                               values='Total'))
print('---------------')
print('crosstab:')

print(pd.crosstab(index=data_sandbox['Subcategory'],
                  columns=data_sandbox['Category'],))

print('---------------')
# print('data_sandbox:')
# print(data_sandbox.to_string(index=False))
# print('---------------')

# print('data_sandbox_pivot:')
# print(data_sandbox_pivot.to_string(index=False))

print('---------------')
data = pd.read_csv('./data/netflix_titles.csv')

data = data.loc[data['release_year'].isin([*range(2017, 2020)]), ['type', 'release_year']].copy()
data.dropna(inplace=True)
data['release_year'] = data['release_year'].astype('int')

cross_tab_prop = pd.crosstab(index=data['release_year'],
                             columns=data['type'],
                             normalize='index')

cross_tab = pd.crosstab(index=data['release_year'],
                        columns=data['type'])

print('cross_tab_prop:')
print(cross_tab_prop)

print('---------------')
print('cross_tab:')
print(cross_tab)

print('---------------')
