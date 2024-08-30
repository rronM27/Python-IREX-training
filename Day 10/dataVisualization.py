import matplotlib.pyplot as plt
import pandas as pd

tedhenat=pd.read_csv('../Day 9/avgIQpercountry.csv')

tedhenatMeKusht=tedhenat[tedhenat['Average IQ']>=100].sort_values(by='Average IQ', ascending=False)
print(tedhenatMeKusht)

plt.figure(figsize=(14,8))

bars=plt.bar(tedhenatMeKusht["Country"],tedhenatMeKusht["Average IQ"],color='skyblue')

plt.xlabel("Country")
plt.xticks(rotation=90, fontsize=14)

plt.ylabel("Average IQ")
plt.yticks(fontsize=14)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.bar_label(bars,color="black")

plt.tight_layout()

plt.show()