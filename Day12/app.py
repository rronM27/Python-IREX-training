import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('../../Module15/weather_tokyo_data.csv')

# Print information about the dataframe
print(df.info())

# Combine year and day columns into a new column full_date
df["full_date"] = pd.to_datetime(df["year"].astype(str) + '/' + df["day"], format='%Y/%m/%d')

# Clean the temperature column
df["temperature"] = df["temperature"].str.replace(r'\([^)]*\)', '', regex=True)  # Remove anything within parentheses
df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')  # Convert to numeric, coerce errors to NaN

# Drop rows with NaN values in temperature
df = df.dropna()

# Sort dataframe by full_date
df = df.sort_values(by="full_date")

# Print updated information about the dataframe
print(df.info())

# 1. Temperature Overview
mean_temperature = df['temperature'].mean()
print(f"The average temperature for the entire dataset is {mean_temperature:.2f} °C")

# 2. Monthly Temperature:

mean_temp_by_month = df.groupby(df["full_date"].dt.month)["temperature"].mean()
print("\nThe mean temperature for each month is:\n", mean_temp_by_month)

# Visualize the mean temperature by month
plt.figure(figsize=(10, 6))
plt.bar(mean_temp_by_month.index, mean_temp_by_month.values)
plt.title('Mean Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Mean Temperature (°C)')
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Highs and Lows
hottest_day = df[df["temperature"] == df["temperature"].max()]
print(f"\nThe hottest day recorded:\n{hottest_day}")

coldest_day = df[df["temperature"] == df["temperature"].min()]
print(f"The coldest day recorded:\n{coldest_day}")

# 4. Temperature Trends: Line graph showing temperature changes over time
plt.figure(figsize=(12, 6))
plt.plot(df["full_date"], df["temperature"])
plt.title('Temperature Trends')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()


# 5. Seasonal Average Temperature

# Define seasons based on months
def get_season(month):
    if month in [12, 1, 2]:  # Winter: December, January, February
        return 'Winter'
    elif month in [3, 4, 5]:  # Spring: March, April, May
        return 'Spring'
    elif month in [6, 7, 8]:  # Summer: June, July, August
        return 'Summer'
    else:  # Fall: September, October, November
        return 'Fall'


df['season'] = df['full_date'].dt.month.apply(get_season)

# Group by season and calculate average temperature
seasonal_temperature = df.groupby('season')['temperature'].mean()

# Visualize seasonal average temperature using a line plot
plt.figure(figsize=(10, 6))
plt.plot(seasonal_temperature.index, seasonal_temperature.values, marker='o', linestyle='-', color='skyblue',
         linewidth=2)
plt.title('Seasonal Average Temperature')
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
