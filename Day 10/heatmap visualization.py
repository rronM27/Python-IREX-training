import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('../Day 9/avgIQpercountry.csv')

df["Population - 2023"]=df["Population - 2023"].str.replace(",","").astype(float)

numerical_iq_data=df.select_dtypes(include='number')

sns.heatmap(numerical_iq_data.corr(),annot=True,cmap="coolwarm",fmt=".2f")

plt.show()