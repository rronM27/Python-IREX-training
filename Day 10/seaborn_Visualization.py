import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('../Day 9/avgIQpercountry.csv')

plt.figure(figsize=(10,6))
sns.histplot(df["Average IQ"])
plt.title("Average IQ")
plt.xlabel("Average IQ")
plt.ylabel("Count")
plt.tight_layout()
plt.show()