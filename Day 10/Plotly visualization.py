import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df=pd.read_csv('../Day 9/avgIQpercountry.csv')
df["Population - 2023"]=df["Population - 2023"].str.replace(",","").astype(float)

fig=px.scatter_geo(df,locations="Country",locationmode="country names",
                   hover_name="Country",size="Average IQ",color="Continent"
                   projection="natural earth".title=("Average IQ per country",
                   size_max=20,template="plotly_dark")

plt.show()