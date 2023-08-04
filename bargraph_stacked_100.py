#! /bin/python

# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

data = pd.read_csv('./data/Sandbox_data.csv', sep=';')
print('---------------')
print('[ Sandbox_data.csv ]')
print(data)
print('---------------')
print('Income: ', end='')
sum_income = data[data['Category'] == 'Income']['Total'].sum()
print(sum_income)
# print(data[data['Category'] == 'Income']['Total'].sum())
print('---------------')
print('Wants: ', end='')
sum_wants = data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Wants')]['Total'].sum()
print(sum_wants)
# print(data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Wants')]['Total'].sum())
print('---------------')
print('Needs: ', end='')
sum_needs = data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Needs')]['Total'].sum()
print(sum_needs)
# print(data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Needs')]['Total'].sum())
print('---------------')
print('Savings: ', end='')
sum_savings = data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Savings')]['Total'].sum()
print(sum_savings)
# print(data[(data['Category'] == 'Expense') & (data['Subcategory'] == 'Savings')]['Total'].sum())
print('---------------')
categories_expenses = ['Wants', 'Needs', 'Savings']
data_filtered_expenses = data[data['Subcategory'].isin(categories_expenses)]
print('data_filtered_expenses:')
print(data_filtered_expenses)
# pivoted = data_filtered_expenses.pivot(index='Category', columns='Subcategory', values='Total')
pivoted = data_filtered_expenses.pivot(columns='Subcategory', values='Total')
# pivoted = data_filtered_expenses.pivot(columns='Subcategory')
print('pivoted:')
print(pivoted)
# data_crosstab = data.pivot(filtered['Category'], data['Subcategory'])
# data_crosstab_piviot = data_crosstab.pivot(index="date", columns="variable", values="value")
# data_crosstab_piviot = data_crosstab.pivot(columns='Needs')
# print(data_crosstab_piviot)
print('---------------')



categories = data.groupby('Category')['Subcategory'].unique().apply(list).to_dict()
for key, value in categories.items():
    print(key)
    print(value)
    # print(data[data['Category'] == value]['Total'].sum())
    # print(data[(data['Category'] == key) & (data['Subcategory'] == value)]['Total'].sum())
print('---------------')
# print(categories['Expense'])

#				Budget		Income		Expenses	Cashflow
#	Needs		50%			$4,000		$2,941		$1,059
#	Wants		30%			$2,400		$716		$1,684
#	Savings		20%			$1,600		$700		$900
#				100%		$8000		$4357		$3643

budget_percentage = {'needs': 50,
                     'wants': 30,
                     'savings':20}
budget_income = {'needs': sum_income * budget_percentage['needs'] / 100,
                 'wants': sum_income * budget_percentage['wants'] / 100,
                 'savings': sum_income * budget_percentage['savings'] / 100}
budget_expenses = {'needs': sum_needs,
                   'wants': sum_wants,
                   'savings':sum_savings}
budget_cashflow = {'needs': budget_income['needs'] - sum_needs,
                   'wants': budget_income['wants'] - sum_wants,
                   'savings': budget_income['savings'] - sum_savings}
budget_totals = {'budget_percentage': sum(budget_percentage.values()),
                 'budget_income': sum_income,
                 'budget_expenses': sum(budget_expenses.values()),
                 'budget_cashflow': sum(budget_cashflow.values())}

print('---------------')
print('budget_percentage: ', end='')
print(budget_percentage)
print('---------------')
print('budget_income: ', end='')
print(budget_income)
print('---------------')
print('budget_expenses: ', end='')
print(budget_expenses)
print('---------------')
print('budget_cashflow: ', end='')
print(budget_cashflow)
print('---------------')
print('budget_totals: ', end='')
print(budget_totals)
print('---------------')
# Convert Values into proportions
# Using sum() + loop
# temp = sum(test_dict.values())
# for key, val in test_dict.items():
#     test_dict[key] = val / temp
#
# # printing result
# print('The proportions divided values : ' + str(test_dict))



# Graph 1
# Data
r = [0,1,2]
# raw_data = {'greenBars': [20, 1.5, 7], 'orangeBars': [5, 15, 5],'blueBars': [2, 15, 18]}
# raw_data = {'greenBars': [50, 1.5, 7], 'blueBars': [2, 15, 18]}
raw_data = {'greenBars': list(budget_expenses.values()),
            'blueBars': list(budget_cashflow.values())}

df = pd.DataFrame(raw_data)

# From raw value to percentage
# totals = [i+j+k for i,j,k in zip(df['greenBars'], df['orangeBars'], df['blueBars'])]
totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
print('---------------')
print('totals')
print(totals)
print('---------------')
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20 }
print('The original dictionary is : ' + str(test_dict))
temp = sum(test_dict.values())
for key, val in test_dict.items():
    test_dict[key] = val / temp

# printing result
print('The proportions divided values : ' + str(test_dict))
print('---------------')


greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
print('---------------')
print('greenBars')
print(greenBars)
print('---------------')# orangeBars = [i / j * 100 for i,j in zip(df['orangeBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]
print('---------------')
print('blueBars')
print(blueBars)
print('---------------')
# plot
barWidth = 0.85
names = categories['Expense'] #('A','B','C','D','E')

# Create green Bars
plt.bar(r,
        greenBars,
        color='#b5ffb9',
        edgecolor='white',
        width=barWidth,
        label='Expenses')
# Create orange Bars
# plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label='group B')
# plt.bar(r, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label='group B')
# Create blue Bars
# plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white', width=barWidth, label='group C')
# plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, greenBars)], color='#a3acff', edgecolor='white', width=barWidth, label='Cashflow')
plt.bar(r,
        blueBars,
        bottom=[i+j for i,
                j in zip(greenBars, greenBars)],
        color='#a3acff',
        edgecolor='white',
        width=barWidth,
        label='Cashflow')

# Custom x axis
plt.xticks(r, names)
# plt.xlabel('group')

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# Show graphic
plt.tight_layout()

# Graph 2
# data = pd.read_csv('./data/netflix_titles.csv')

# data = data.loc[data['release_year'].isin([*range(2016, 2020)]), ['type', 'release_year']].copy()
# data.dropna(inplace=True)
# data['release_year'] = data['release_year'].astype('int')
#
# cross_tab_prop = pd.crosstab(index=data['release_year'],
#                              columns=data['type'],
#                              normalize='index')
#
# cross_tab_prop = categories['Expense']
# cross_tab = pd.crosstab(index=data['release_year'],
#                         columns=data['type'])
#
# cross_tab_prop.plot(kind='bar',
#                         stacked=True,
#                         colormap='tab10',
#                         figsize=(5, 5))
#
# plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
#
# for n, x in enumerate([*cross_tab.index.values]):
#     for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
#                                    cross_tab_prop.loc[x].cumsum()):
#         plt.text(x=n - 0.17,
#                  y=(y_loc - proportion) + (proportion / 2),
#                  s=f'{np.round(proportion * 100, 1)}%',
#                  color='yellow',
#                  fontsize=9,
#                  fontweight='bold')
#
# plt.tight_layout()
# plt.show()
#


#
#
# Graph 2 saved

categories_expenses = ['Wants', 'Needs', 'Savings', 'Salary']
data_sandbox = pd.read_csv('./data/Sandbox_data.csv', sep=';')
data_sandbox = data.loc[data['Subcategory'].isin(categories_expenses),
                        ['Category', 'Subcategory', 'Total']].copy()
# data_sandbox.dropna(inplace=True)

data_sandbox_pivot = data_sandbox
data_sandbox_pivot.pivot(columns='Subcategory', values='Category')

print('---------------')
categories_expenses = ['Wants', 'Needs', 'Savings']
data_sandbox_filtered_expenses = data_sandbox[data_sandbox['Subcategory'].isin(categories_expenses)]
print('data_sandbox_filtered_expenses:')
print(data_sandbox_filtered_expenses)

print('---------------')
# pivoted = data_filtered_expenses.pivot(columns='Subcategory')
# pivoted = data_filtered_expenses.pivot(index='Category', columns='Subcategory', values='Total')
data_sandbox_filtered_pivoted = data_sandbox_filtered_expenses.pivot(columns='Subcategory', values='Total')
print('data_sandbox_filtered_pivoted:')
print(data_sandbox_filtered_pivoted)

print('---------------')
# print('data_sandbox:')
# print(data_sandbox.to_string(index=False))
print('---------------')
print('data_sandbox_pivot:')
print(data_sandbox_pivot.to_string(index=False))
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
plt.show()



# ax.set_title('Cashflow Dashboard')
# ax.legend(loc='upper right')
# plt.legend(loc='lower left', ncol=2)
# plt.legend(loc='upper right', ncol=2)
# ax.set_title('Cashflow Dashboard')
# plt.legend(loc='upper right', bbox_to_anchor=(1,1), ncol=1)

# Custom x axis
# plt.xticks(r, names)
# plt.xlabel('Expenses')
# plt.xlabel('Release Year')
# plt.ylabel('Proportion')
# plt.xlabel('group')
# ax.set_title('Cashflow Dashboard')
# ax.legend(loc='upper right')

# # Data
# r = [0,1,2,3,4]
# raw_data = {'greenBars': [20, 1.5, 7, 10, 5], 'orangeBars': [5, 15, 5, 10, 15],'blueBars': [2, 15, 18, 5, 10]}
# df = pd.DataFrame(raw_data)
#
# # From raw value to percentage
# totals = [i+j+k for i,j,k in zip(df['greenBars'], df['orangeBars'], df['blueBars'])]
# greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
# orangeBars = [i / j * 100 for i,j in zip(df['orangeBars'], totals)]
# blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]
#
# # plot
# barWidth = 0.85
# names = ('A','B','C','D','E')
#
# # Create green Bars
# plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth, label='group A')
# # Create orange Bars
# plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label='group B')
# # Create blue Bars
# plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white', width=barWidth, label='group C')
#
# # Custom x axis
# plt.xticks(r, names)
# plt.xlabel('group')
#
# # Add a legend
# plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
#
# # Show graphic
# plt.tight_layout()
#
# # Show graphic
# plt.show()
