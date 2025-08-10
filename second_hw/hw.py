import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C"

#population_data = pd.read_html(url)[13]
population_data = pd.read_html(url, match='Коефіцієнт народжуваності в регіонах України')[0]
#print(population_data.head())
#print(population_data.shape)
population_data = population_data.replace("—", np.nan)
#print(population_data.dtypes)
population_data[['2014', '2019']] = population_data[['2014', '2019']].apply(pd.to_numeric)
#print(population_data.isnull().sum())
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
#print(population_data[population_data['2019'] > population_data['2019'].mean()])
print(population_data[population_data['2014'] == population_data['2014'].max()])
#print(population_data)
population_data["2019"].plot(kind='bar', title='Коефіцієнт народжуваності в Україні 2019 року')
plt.show()