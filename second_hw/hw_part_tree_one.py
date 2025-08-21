import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("d:/Studies/repos/First_repo/second_hw")
tables = pd.read_csv("csv/bestsellers_with_categories.csv")
print(tables.head())
print(tables.shape)
'''
Про скільки книг зберігає дані датасет?
Відповідь: Датасет містить дані про 550 книг.
'''

tables.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']
print(tables.isna().sum())
"""
Чи є в якихось змінних пропуски?
Відповідь: Пропусків немає, всі змінні заповнені.
"""

print(tables['genre'].unique())
"""
Які є унікальні жанри?
Відповідь: Унікальні жанри: 'Fiction' та 'Non Fiction'
"""

#tables['price'].plot(kind='hist', bins=20, title='Розподіл цін на книги')
#plt.show()

print(tables['price'].min())
# Мінімальна ціна? Відповідь: 0
print(tables['price'].max())
# Максимальна ціна? Відповідь: 105
print(tables['price'].mean())
# Середня ціна? Відповідь: 13.1
print(tables['price'].median())
# Медіанна ціна? Відповідь: 11.0

print(tables['user_rating'].max())
# Який рейтинг у датасеті найвищий? Відповідь: 4.9

print(tables[tables['user_rating'] == tables['user_rating'].max()])
# Скільки книг мають такий рейтинг? Відповідь: 52

print(tables[tables['reviews'] == tables['reviews'].max()]['name'])
# Яка книга має найбільше відгуків? Відповідь: "Where the Crawdads Sing"

top_books = tables[tables['year'] == 2015]
top_books = top_books[top_books['price'] == top_books['price'].max()]
print(top_books['name'])
# З тих книг, що потрапили до Топ-50 у 2015 році, яка книга найдорожча (можна використати проміжний датафрейм)?
# Відповідь: Publication Manual of the American Psychologic...

print(tables[(tables.year == 2010) & (tables.genre == 'Fiction')].shape)
# Скільки книжок жанру Fiction потрапили до Топ-50 у 2010 році? Відповідь: 20

print(tables[(tables.year == 2010) | (tables.year == 2011)][tables.user_rating >= 4.9])
# Приклад з ДЗ: df[(df.user_rating == 4.9) & (df.year.isin([2010, 2011]))].shape

# Скільки книг з рейтингом 4.9 потрапили до рейтингу у 2010 та 2011 роках? Відповідь: 1

print(tables[(tables['year'] == 2015) & (tables.price < 8)].sort_values('price'))

# Яка книга остання у відсортованому списку? Відповідь: 253 Old School (Diary of a Wimpy Kid #10)

print(tables[['genre', 'price']].groupby('genre').agg(['min', 'max']))

"""Максимальна ціна для жанру Fiction: Відповідь: 82
Мінімальна ціна для жанру Fiction: Відповідь: 0
Максимальна ціна для жанру Non Fiction: Відповідь: 105
Мінімальна ціна для жанру Non Fiction: Відповідь: 0"""

authors_books = tables[['name', 'author']].groupby('author').agg('count')
print(authors_books.shape)
print(authors_books[authors_books.name == authors_books.name.max()])

"""
Якої розмірності вийшла таблиця? Відповідь: (248, 1)
У якого автора найбільше книжок? Відповідь: Jeff Kinney
Скільки книг у цього автора? Відповідь: 12
"""

authors_user_rating = tables[['user_rating', 'author']].groupby('author').agg('mean')
print(authors_user_rating)
print(authors_user_rating[authors_user_rating.user_rating == authors_user_rating.user_rating.min()])

"""
У якого автора середній рейтинг мінімальний? Відповідь: Donna Tartt
Який у цього автора середній рейтинг? Відповідь: 3.9
"""

authors_data = pd.concat([authors_books, authors_user_rating], axis=1)
print(authors_data.sort_values(['name', 'user_rating']))

# Який автор перший у списку? Відповідь: Muriel Barbery

""" Треба доробити. Лінійна діаграмма відходить дуже погано
top5_authors_by_number_of_books = authors_data.sort_values(['name'], ascending=False).head(5)

fig, axs = plt.subplots(2, 1, figsize=(16, 8))
plt.tight_layout()
axs[0].plot(top5_authors_by_number_of_books.index, top5_authors_by_number_of_books['user_rating'], 'x:' , markerfacecolor='black', markersize=12, color='red')
axs[0].set_title('Топ-5 авторів за рейтингом', fontsize=16)
axs[1].plot(top5_authors_by_number_of_books.index, top5_authors_by_number_of_books['name'], 'x-.' , markerfacecolor='red', markersize=12, color='green')
axs[1].set_title('Топ-5 авторів за кількістю книг', fontsize=16)


plt.show()"""
