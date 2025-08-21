import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Момент спостереження": [1, 2, 3, 4, 5, 6],
    "Прибутковість A, %": [25, -10, 10, 5, 35, 13],
    "Прибутковість B, %": [0, 15, -5, 5, 20, 25],
    "Прибутковість C, %": [10, 25, -15, -5, -5, 15],
}

df = pd.DataFrame(data)
#df.set_index("Момент спостереження", inplace=True)

plt.figure(figsize=(10, 6))
sns.regplot(x='Прибутковість A, %', y='Прибутковість B, %', data=df)
plt.figure(figsize=(10, 6))
sns.regplot(x='Прибутковість A, %', y='Прибутковість C, %', data=df)
plt.figure(figsize=(10, 6))
sns.regplot(x='Прибутковість B, %', y='Прибутковість C, %', data=df)

plt.show()

# Відповідь: Акції A та B