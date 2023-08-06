#! /bin/python


import pandas as pd
import numpy as np

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

# data_sandbox_values = data_sandbox_budget.drop(['Budget_Desired', 'Budget_Actual', 'Spending'], axis=1)
# data_sandbox_values = data_sandbox_values.drop(['Total'], axis=0)
data_sandbox_values = data_sandbox_budget
data_sandbox_values['Proportion'] = [0,0,0,0]
data_sandbox_values.at['Needs','Proportion'] = data_sandbox_values.loc['Needs']['Income']+data_sandbox_values.loc['Needs']['Reserve']
data_sandbox_values.at['Savings','Proportion'] = data_sandbox_values.loc['Savings']['Income']+data_sandbox_values.loc['Savings']['Reserve']
data_sandbox_values.at['Discretionary','Proportion'] = data_sandbox_values.loc['Discretionary']['Income']+data_sandbox_values.loc['Discretionary']['Reserve']
data_sandbox_values.at['Total','Proportion'] = data_sandbox_values.loc['Needs']['Proportion']+data_sandbox_values.loc['Savings']['Proportion']+data_sandbox_values.loc['Discretionary']['Proportion']

proportion_row = [0,0,0,0,0,0]
data_sandbox_values.loc['Proportion'] = proportion_row

data_sandbox_values.at['Proportion','Budget_Desired'] = data_sandbox_values.loc['Total']['Budget_Desired']/data_sandbox_values.loc['Total']['Proportion']
data_sandbox_values.at['Proportion','Budget_Actual'] = data_sandbox_values.loc['Total']['Budget_Actual']/data_sandbox_values.loc['Total']['Proportion']
data_sandbox_values.at['Proportion','Income'] = data_sandbox_values.loc['Total']['Income']/data_sandbox_values.loc['Total']['Proportion']
data_sandbox_values.at['Proportion','Spending'] = data_sandbox_values.loc['Total']['Spending']/data_sandbox_values.loc['Total']['Proportion']
data_sandbox_values.at['Proportion','Reserve'] = data_sandbox_values.loc['Total']['Reserve']/data_sandbox_values.loc['Total']['Proportion']
data_sandbox_values.at['Proportion','Proportion'] = data_sandbox_values.loc['Total']['Proportion']/data_sandbox_values.loc['Total']['Proportion']


print('data_sandbox_values:')
print(data_sandbox_values)
print('---------------')

data_sandbox_proportions_intermediate = data_sandbox_budget.drop(['Budget_Desired', 'Budget_Actual', 'Spending'], axis=1)
data_sandbox_proportions_intermediate = data_sandbox_proportions_intermediate.drop(['Total'], axis=0)

data_sandbox_proportions_intermediate.at['Needs','Income'] = data_sandbox_proportions_intermediate.loc['Needs']['Income']/data_sandbox_proportions_intermediate.loc['Needs']['Proportion']
data_sandbox_proportions_intermediate.at['Savings','Income'] = data_sandbox_proportions_intermediate.loc['Savings']['Income']/data_sandbox_proportions_intermediate.loc['Savings']['Proportion']
data_sandbox_proportions_intermediate.at['Discretionary','Income'] = data_sandbox_proportions_intermediate.loc['Discretionary']['Income']/data_sandbox_proportions_intermediate.loc['Discretionary']['Proportion']

data_sandbox_proportions_intermediate.at['Needs','Reserve'] = data_sandbox_proportions_intermediate.loc['Needs']['Reserve']/data_sandbox_proportions_intermediate.loc['Needs']['Proportion']
data_sandbox_proportions_intermediate.at['Savings','Reserve'] = data_sandbox_proportions_intermediate.loc['Savings']['Reserve']/data_sandbox_proportions_intermediate.loc['Savings']['Proportion']
data_sandbox_proportions_intermediate.at['Discretionary','Reserve'] = data_sandbox_proportions_intermediate.loc['Discretionary']['Reserve']/data_sandbox_proportions_intermediate.loc['Discretionary']['Proportion']

print('data_sandbox_proportions_intermediate:')
print(data_sandbox_proportions_intermediate)
print('---------------')

data_sandbox_proportions = data_sandbox_proportions_intermediate.drop(['Proportion'], axis=1)
data_sandbox_proportions = data_sandbox_proportions.drop(['Proportion'], axis=0)
data_sandbox_proportions.rename(columns={"Income": "Income_Proportion", "Reserve": "Reserve_Proportion"}, inplace = True)
print('data_sandbox_proportions:')
print(data_sandbox_proportions)
print('---------------')

data_sandbox_quantities = data_sandbox_budget.drop(['Budget_Desired', 'Budget_Actual', 'Spending', 'Proportion'], axis=1)
data_sandbox_quantities = data_sandbox_quantities.drop(['Total', 'Proportion'], axis=0)
print('data_sandbox_quantities:')
print(data_sandbox_quantities)
print(type(data_sandbox_quantities))
print('---------------')

frames = [data_sandbox_quantities, data_sandbox_proportions]
data_sandbox_quantities_proportions = pd.concat(frames, axis=1)
print('data_sandbox_quantities_proportions:')
print(data_sandbox_quantities_proportions)
print('---------------')
