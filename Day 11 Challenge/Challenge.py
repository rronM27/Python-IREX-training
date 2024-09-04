import pandas as pd
import matplotlib.pyplot as plt

tedhenat=pd.read_csv('../Day 11 Challenge/weather_tokyo_data.csv')
average_temp_per_dataset=df.groupby('Month')['Average Temperature'].mean()

print(average_temp_per_dataset)

average_temp_per_dataset_sorted=average_temp_per_dataset.sort_values(ascending=True)
print(average_temp_per_dataset_sorted)

total_temp_per_month=df.groupby('Month')['Average Temperature'].sum()
print(total_temp_per_month)

plt.figure(figsize=(14,8))
bars=plt.bar(["Month"],["Average IQ"],color='skyblue')

