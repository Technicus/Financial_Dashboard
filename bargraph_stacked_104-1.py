#! /bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rc


print('---------------')
print('[ data_sandbox ]')
print('---------------')

categories_expenses = ['Wants', 'Needs', 'Savings', 'Salary']
data_sandbox = pd.read_csv('./data/cashflow.csv', sep=';')
print('data_sandbox:')
print(data_sandbox)
print('---------------')


data_sandbox = data_sandbox.loc[data_sandbox['Budget']\
    .isin(categories_expenses), ['Category', 'Budget', 'Monthly_Total']].copy()
data_sandbox.dropna(inplace=True)

data_sandbox_pivot = data_sandbox
data_sandbox_pivot.pivot(columns='Budget', values='Category')

categories_expenses = ['Needs', 'Wants', 'Savings']
data_sandbox_filtered_expenses = data_sandbox[data_sandbox['Budget']\
    .isin(categories_expenses)]

print('---------------')
print('data_sandbox.pivot_table:')
print(data_sandbox.pivot_table(index='Budget',
                               columns='Category',
                               values='Monthly_Total'))
print('---------------')
print('crosstab:')
print(pd.crosstab(index=data_sandbox['Budget'],
                  columns=data_sandbox['Category'],))

print('---------------')

print('\n---------------')
print('[ cashflow ]')
print('---------------')
data_sandbox = pd.read_csv('./data/cashflow.csv', sep=';')
print('data_sandbox:')
print(data_sandbox)
print('---------------')
budget = data_sandbox['Budget'].values.tolist()
print('budget:')
print(budget)
print('---------------')
data_sandbox = data_sandbox.loc[data_sandbox['Budget']\
    .isin(budget), ['Category', 'Budget', 'Monthly_Total']].copy()
data_sandbox.dropna(inplace=True)
print('---------------')
print('data_sandbox:')
print(data_sandbox)
print('---------------')


agg_functions = {'Category':'first', 'Monthly_Total': 'sum'}

data_sandbox_monthly = data_sandbox.groupby(data_sandbox['Budget']).aggregate(agg_functions)
data_sandbox_income = data_sandbox_monthly[data_sandbox_monthly['Category'] == 'Income']
data_sandbox_spending = data_sandbox_monthly[data_sandbox_monthly['Category'] == 'Spending']

print('---------------')
print('data_sandbox_income:')
print(data_sandbox_income)
total_income = data_sandbox_income.loc['Cash', 'Monthly_Total']
print('---------------')
print('total_income:')
print(total_income)
print('---------------')
print('data_sandbox_spending:')
print(data_sandbox_spending)
print('---------------')

budget_desired = {'Needs': 50, 'Savings': 20, 'Discretionary': 30}
budget_desired['Total'] = budget_desired['Needs'] + budget_desired['Savings'] + budget_desired['Discretionary']
print('budget_desired:')
print(budget_desired)
print('---------------')
total_row = pd.Series(index=['Total'], dtype='float64')

data_sandbox_budget = data_sandbox_spending.drop(['Category'], axis=1)
data_sandbox_budget.insert(loc = 0, column = 'Budget_Desired', value = '')
data_sandbox_budget.insert(loc = 1, column = 'Budget_Actual', value = '')
data_sandbox_budget.insert(loc = 2, column = 'Income', value = '')
data_sandbox_budget.insert(loc = 4, column = 'Reserve', value = '')
data_sandbox_budget.rename(index={'Wants': 'Discretionary'}, inplace=True)
data_sandbox_budget.rename(columns={'Monthly_Total': 'Spending'}, inplace=True)
data_sandbox_budget = pd.concat([data_sandbox_budget, total_row])
data_sandbox_budget.drop([0], axis=1, inplace=True)

def percentage(num_a, num_b):
    try:
        return round((num_b * num_a)/100, 2)
    except ZeroDivisionError:
        return float('inf')

print('---------------')
income = {}
income['Needs'] = percentage(total_income, budget_desired['Needs'])
income['Savings'] = percentage(total_income, budget_desired['Savings'])
income['Discretionary'] = percentage(total_income, budget_desired['Discretionary'])
income['Total'] = income['Needs'] + income['Savings'] + income['Discretionary']
print('income:')
print(income)
print('---------------')

def percentage_actual(num_a, num_b):
    try:
        return round((num_a / num_b)*100)
    except ZeroDivisionError:
        return float('inf')

print('Budget_Actual:'.format(data_sandbox_budget.loc['Needs']['Budget_Actual']))
print('---------------')
budget_actual = {}
budget_actual['Needs'] = percentage_actual(data_sandbox_budget.loc['Needs']['Spending'], total_income )
budget_actual['Savings'] = percentage_actual(data_sandbox_budget.loc['Savings']['Spending'], total_income)
budget_actual['Discretionary'] = percentage_actual(data_sandbox_budget.loc['Discretionary']['Spending'], total_income)
budget_actual['Total'] = budget_actual['Needs'] + budget_actual['Savings'] + budget_actual['Discretionary']
print('Budget_Actual:')
print(budget_actual)
print('---------------')
#IF((I5*G2)-J2<0,0,(I5*G2)-J2)
reserve = {}
if ((income['Needs']) - data_sandbox_budget.loc['Needs']['Spending']) <= 0:
    reserve['Needs'] = 0
else:
    reserve['Needs'] = income['Needs'] - data_sandbox_budget.loc['Needs']['Spending']

if ((income['Savings']) - data_sandbox_budget.loc['Savings']['Spending']) <= 0:
    reserve['Savings'] = 0
else:
    reserve['Savings'] = income['Savings'] - data_sandbox_budget.loc['Savings']['Spending']

if ((income['Discretionary']) - data_sandbox_budget.loc['Discretionary']['Spending']) <= 0:
    reserve['Discretionary'] = 0
else:
    reserve['Discretionary'] = income['Discretionary'] - data_sandbox_budget.loc['Discretionary']['Spending']
reserve['Total'] = reserve['Needs'] + reserve['Savings'] + reserve['Discretionary']
print('reserve:')
print(reserve)
print('---------------')


index_of_data = data_sandbox_budget.index.values.tolist()
print('data_sandbox_budget.index.tolist():')
print(index_of_data)

for key, value in budget_desired.items():
    print('key = {}'.format(key))
    print('value = {}'.format(value))
    data_sandbox_budget.loc[key, 'Budget_Desired'] = value

for key, value in income.items():
    print('key = {}'.format(key))
    print('value = {}'.format(value))
    data_sandbox_budget.loc[key, 'Income'] = value

for key, value in budget_actual.items():
    print('key = {}'.format(key))
    print('value = {}'.format(value))
    data_sandbox_budget.loc[key, 'Budget_Actual'] = value

for key, value in reserve.items():
    print('key = {}'.format(key))
    print('value = {}'.format(value))
    data_sandbox_budget.loc[key, 'Reserve'] = value

print('---------------')
data_sandbox_budget.loc['Total', 'Income'] = total_income

print('total_spending:')
total_spending = data_sandbox_budget.loc['Needs']['Spending'] + data_sandbox_budget.loc['Savings']['Spending'] + data_sandbox_budget.loc['Discretionary']['Spending']
print(total_spending)
data_sandbox_budget.loc['Total', 'Spending'] = total_spending
print('---------------')
print('data_sandbox_budget:')
print(data_sandbox_budget)
print('---------------')

data_sandbox_proportions = data_sandbox_budget.drop(['Budget_Desired', 'Budget_Actual', 'Spending'], axis=1)
data_sandbox_proportions = data_sandbox_proportions.drop(['Total'], axis=0)
print('data_sandbox_proportions:')
print(data_sandbox_proportions)
print('---------------')



def create_plot(data):
    # cross_tab_prop = pd.crosstab(index=data['release_year'],
    # cross_tab_prop = pd.crosstab(index=data['Budget'],
    #                              columns=data[['Income', 'Reserve']],
    #                              normalize='index')
    cross_tab_prop = data
    cross_tab_prop.index.name = None
    cross_tab_prop.plot(kind='bar',
                        stacked=True,
                        colormap='tab10',
                        figsize=(5, 5))
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
               ncol=2, borderaxespad=0, title = 'Cashflow Dashboard',
               title_fontsize = 'xx-large',
               frameon = False)
    for n, x in enumerate([*cross_tab_prop.index.values]):
        for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
                                       cross_tab_prop.loc[x].cumsum()):
            # plt.text(x=n - 0.17,
            plt.text(x=n - 0.20,
                     # y=(y_loc - proportion) + (proportion / 2 ), # Position of percentag
                     # y=(proportion), # Position of percentag
                     y = y_loc - 150,
                     # s='${:,.2f}'.format(np.round(proportion, 12)),
                     s='${:,.2f}'.format(proportion),
                     color='yellow',
                     fontsize=9,
                     fontweight='bold')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    return plt
plt = create_plot(data_sandbox_proportions)
# data_sandbox_budget.rename('Budget', inplace=True)
# plt = create_plot(data_sandbox_budget)
plt.show()


# print(data_sandbox_filtered_expenses)
# print('data_sandbox_filtered_expenses:')
# pivoted = data_filtered_expenses.pivot(columns='Budget')
# pivoted = data_filtered_expenses.pivot(index='Category'\
    # ,columns='Budget', values='Monthly_Total')
# data_sandbox_filtered_pivoted = \
    # data_sandbox_filtered_expenses.pivot(columns='Budget', values='Monthly_Total')
# print(data_sandbox_filtered_pivoted)
# print(data_sandbox_filtered_pivoted.pivot(columns='Budget',
                                          # values='Monthly_Total'))
# budget = ['Wants', 'Needs', 'Savings', 'Cash']
# budget = np.unique(budget)
# budget.drop_duplicates(subset=['brand'])
# budget_desired = [{'Needs': 50}, {'Savings': 20}, {'Discretionary': 30}]
# budget_actual = []
# income = []
        # return round((num_a / num_b) * 100, 2)
        # return (num_a % num_b)
# print('Income:'.format(data_sandbox_budget.loc['Needs']['Budget_Actual']))
        # return round((num_a / num_b) * 100, 2)
        # return round((num_b * num_a)/100, 2)
        # return (num_a % num_b)
# data_sandbox_budget.loc['Total']['Spending'] = data_sandbox_budget.loc[['Needs','Savings', 'Discretionary']].sum()
# data_sandbox_budget.loc['Total']['Spending'] = data_sandbox_budget.loc['Needs']['Spending'] + data_sandbox_budget.loc['Savings']['Spending'] + data_sandbox_budget.loc['Discretionary']['Spending']
# data_sandbox_budget.insert('Budget_Desired', budget_desired)
# data_sandbox_budget.loc[len(data_sandbox_budget.index)] = ['Total', '', '', '', '', '', '']
# data_sandbox_budget = pd.concat([data_sandbox_budget, total_row])
# data_sandbox_budget = data_sandbox_budget.concat(pd.Series('', index = data_sandbox_budget.columns, name = 'Total'))
# total_spending = data_sandbox_budget.loc[':2'].eval('Sum = Spending')
# total_spending = data_sandbox_budget.eval('Sum = Spending')
# print('---------------')
# print('data_sandbox_budget.loc[\'Total\'][\'Spending\']:')
# print(total_spending)
# print('---------------')
# data_sandbox_budget.style.format({'Budget_Desired': ':2%', 'Budget_Actual': ':2%'})
# data_sandbox_budget.style.format({'Income':'${0:,.0f}'})
                                 # {'Income': '${0:,.0f}'}, {'Income': '${0:,.0f}'},
                                 # {'Spending': '${0:,.0f}'}, {'Reserve': '${0:,.0f}'})
# data_sandbox_budget.style.format({'Budget_Actual', ':2%'})
# data_sandbox_budget.style.format({'Income', '${0:,.0f}'})
# data_sandbox_budget.style.format({'Spending', '${0:,.0f}'})
# data_sandbox_budget.style.format({'Reserve', '${0:,.0f}'})
# print(data_sandbox_budget.style.format({'Income':'${0:,.0f}'}))
# data_sandbox_new = data_sandbox.groupby(data_sandbox['Budget']).aggregate(agg_functions)
# data_sandbox_new = data_sandbox_new.assign(cash_flow = (data_sandbox_new.loc['Cash', 'Monthly_Total'] / data_sandbox_new.Monthly_Total) * 100)
# data_sandbox_budget = data_sandbox.groupby(data_sandbox_spending['Category']).aggregate(agg_functions)
# data_sandbox_new = data_sandbox_new.assign(desired_budget = budget_desired)
#
# data_sandbox.dropna(inplace=True)
#
# data_sandbox_filtered_expenses = data_sandbox[data_sandbox['Category']\
#     .isin(budget)]
#
# print('data_sandbox_filtered_expenses:')
# print(data_sandbox_filtered_expenses)
#
# print('---------------')
# # pivoted = data_filtered_expenses.pivot(columns='Budget')
# # pivoted = data_filtered_expenses.pivot(index='Category'\
#     # ,columns='Budget', values='Monthly_Total')
# # data_sandbox_filtered_pivoted = \
#     # data_sandbox_filtered_expenses.pivot(columns='Budget', values='Monthly_Total')
# print('---------------')
# print('data_sandbox.pivot_table 1:')
# print(data_sandbox_filtered_pivoted)
# print(data_sandbox_filtered_pivoted.pivot(columns='Budget',
                                          # values='Monthly_Total'))
# print(data_sandbox.pivot_table(index='Budget',
#                                columns='Category',
#                                values='Monthly_Total'))
# data_piv = data_sandbox.pivot_table(index='Budget',
#                                     columns='Category',
#                                     values='Monthly_Total').fillna(0)
# print(data_piv)
# print('---------------')
# print('Processing:')
# for index, row in data_piv.iterrows():
#     print(index, row['Income'], row['Spending'])
#     if index == 'Cash':
#         print('index is cash')
#         total_cash = row['Income']
#     else:
#         data_piv.loc[index,'Income'] = total_cash - row['Spending']
# print(data_piv)
# print('---------------')
# print('data_sandbox.pivot_table 2:')
# data_sandbox_pivot = data_sandbox
# data_sandbox_pivot.pivot(columns='Budget', values='Category')
# print(data_sandbox_pivot)
# print('---------------')
# print('crosstab:')
# print(pd.crosstab(index=data_sandbox['Budget'],
#                   columns=data_sandbox['Category'],))
# print('---------------')
#
