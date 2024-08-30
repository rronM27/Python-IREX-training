import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('../Day 9/avgIQpercountry.csv')

nobel_prizes_by_continent=df.groupby("Continent")["Nobel Prices"].sum()

no_of_continents=nobel_prices_by_continent.count()

print(no_of_continents)

colors=["gold","lightcoral","yellow","green","orange"]\

plt.figure(figsize=(10,10))

nobel_prices_by_continent.plot(kind='pie',autopct='%1.1%%',color=colors)

plt.show()
