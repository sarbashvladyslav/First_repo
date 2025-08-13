import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

"""file = os.path.abspath("2017_jun_final.csv")
print(file)"""

os.chdir("d:/Studies/repos/First_repo/second_hw")
tables = pd.read_csv("csv/2017_jun_final.csv")

'''print(tables.head())
print(tables.shape)
print(tables.dtypes)
print(tables.isnull().sum())'''

tables.drop(labels=['Специализация', 'Университет', 'Предметная.область', 'Валюта', 'cls'], axis=1, inplace=True)
print(tables.isnull().sum())
tables.dropna(inplace=True)
print(tables.shape)

python_data = tables[tables['Язык.программирования'] == 'Python']
print(python_data.shape)
python_data = python_data.groupby("Должность")
print(python_data.head())

min_max_salary = python_data['Зарплата.в.месяц'].agg(['min', 'max'])
print(min_max_salary)

"""# Функція з прикладу
def fill_avg_salary(row):
    return (row["min"] + row["max"])/2"""

# Фукція повертає середню зарплату, але рахує середнюю по всій колонці, а не рядку.
# При цьому при роботі з методом apply() функція застосовуєтся к каждому рядку. Можливо через створеня нового стовпця.
def fill_avg_salary(salary_mean):
    return salary_mean.agg(['mean'])

min_max_salary['avg'] = min_max_salary.apply(fill_avg_salary, axis=1)
print(min_max_salary['avg'].describe())

min_max_salary.to_csv('it_salary.csv')