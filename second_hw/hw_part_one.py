import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C"

#population_data = pd.read_html(url)[13]
population_data = pd.read_html(url, match='Коефіцієнт народжуваності в регіонах України')[0]
print(population_data.head())
print(population_data.shape)
population_data = population_data.replace("—", np.nan)
print(population_data.head())
print(population_data.dtypes)
population_data[['2014', '2019']] = population_data[['2014', '2019']].apply(pd.to_numeric)
print(population_data.isnull().sum())
#population_data = population_data.drop(27, axis=0, inplace=True)

population_data = population_data[:-1]
population_data = population_data.fillna(
    {
        "1950": population_data["1950"].mean(), 
        "1960": population_data["1960"].mean(),
        "1970": population_data["1970"].mean(),
        "2014": population_data["2014"].mean(),
        "2019": population_data["2019"].mean()
        })
print(population_data)
#print(population_data[population_data['2019'] > population_data['2019'].mean()])
print(population_data[population_data['2019'] > population_data['2019'].mean()]['Регіон'])
print(population_data[population_data['2014'] == population_data['2014'].max()])

# Задання індексу потрібно для відображення регіонів на графіку замість цифр
population_data.set_index('Регіон', inplace=True)

# За допомогою функції subplots можливо створити 3 графіки в одному вікні(figure), але через назви Регіонів це виглядає не дуже.
# 1 Графік. Лінійний
plt.figure(figsize=(10, 6))
plt.plot(population_data["2019"], 'bo-', color='blue')
plt.xlabel("Регіон", fontsize=15, fontstyle='italic', fontweight="black")
plt.xticks(rotation=90)
plt.ylabel("Коефіцієнт", fontsize=15, fontstyle='italic', fontweight="black")
plt.title("Коефіцієнт народжуваності в Україні 2019 року", fontsize=18, fontweight="black")

# 2 Графік. Вертикальна стовпчаста діаграма
plt.figure(figsize=(10, 6))
plt.bar(population_data.index, population_data["2019"], color='green', edgecolor='black')
plt.xlabel("Регіон", fontsize=15, fontstyle='italic', fontweight="black")
plt.xticks(rotation=90)
plt.ylabel("Коефіцієнт", fontsize=15, fontstyle='italic', fontweight="black")
plt.title("Коефіцієнт народжуваності в Україні 2019 року", fontsize=18, fontweight="black")

# 3 Графік. Горизонтальна стовпчаста діаграма. Для горизонтального стовпчикового графіка треба змінювати назви осей
plt.figure(figsize=(10, 6))
plt.barh(population_data.index, population_data["2019"], color='red', edgecolor='green')
plt.xlabel("Коефіцієнт", fontsize=15, fontstyle='italic', fontweight="black")
plt.xticks(rotation=90)
plt.ylabel("Регіон", fontsize=15, fontstyle='italic', fontweight="black")
plt.title("Коефіцієнт народжуваності в Україні 2019 року", fontsize=18, fontweight="black")
plt.show()