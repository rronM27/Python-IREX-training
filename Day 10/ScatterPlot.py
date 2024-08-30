import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('../Day 9/avgIQpercountry.csv')

plt.figure(figsize=(10,6))

plt.scatter(df['Mean years of schooling - 2021'],df["Average IQ"])


plt.show()
