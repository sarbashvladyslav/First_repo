import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

"""# Абсолютний шлях до файлу
file = os.path.abspath("2017_jun_final.csv")
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

# 1 Графік. Лінійний
fig1, axs1 = plt.subplots(3, 1, figsize=(16, 8))
plt.tight_layout()
axs1[0].plot(min_max_salary['min'], 'rv--', color='red')
axs1[0].set_title('Мінімальна зарплата', fontsize=16)
axs1[1].plot(min_max_salary['max'], 'g^:', color='green')
axs1[1].set_title('Максимальна зарплата', fontsize=16)
axs1[2].plot(min_max_salary['avg'], 'bD-', color='blue')
axs1[2].set_title('Середня зарплата', fontsize=16)

# 2 Графік. Вертикальна стовпчаста діаграма.
fig2, axs2 = plt.subplots(3, 1, figsize=(16, 8))
plt.tight_layout()
axs2[0].bar(min_max_salary.index, min_max_salary['min'], color='red')
axs2[0].set_title('Мінімальна зарплата', fontsize=16)
axs2[1].bar(min_max_salary.index, min_max_salary['max'], color='green')
axs2[1].set_title('Максимальна зарплата', fontsize=16)
axs2[2].bar(min_max_salary.index, min_max_salary['avg'], color='blue')
axs2[2].set_title('Середня зарплата', fontsize=16)

# 3 Графік. Горизонтальна стовпчаста діаграма.
fig3, axs3 = plt.subplots(3, 1, figsize=(16, 8))
axs3[0].barh(min_max_salary.index, min_max_salary['min'], color='red')
axs3[0].set_title('Мінімальна зарплата', fontsize=16)
axs3[1].barh(min_max_salary.index, min_max_salary['max'], color='green')
axs3[1].set_title('Максимальна зарплата', fontsize=16)
axs3[2].barh(min_max_salary.index, min_max_salary['avg'], color='blue')
axs3[2].set_title('Середня зарплата', fontsize=16)

plt.show()