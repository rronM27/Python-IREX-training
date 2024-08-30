import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('../Day 9/avgIQpercountry.csv')

ave_iq_by_country=df.groupby('Continent')['Average IQ'].mean()

plt.figure(figsize=(10,6))

ave_iq_by_country.plot(kind="line")

plt.title("Average IQ by Country")
plt.xlabel("Country")
plt.ylabel("Average IQ")

plt.grid(axis="both",linestyle="--",alpha=0.5)


plt.show()