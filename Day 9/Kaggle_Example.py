import pandas as pd

df=pd.read_csv('avgIQpercountry.csv')
# print(df.info())
# print (df.head())

# select only the two columns that are needed
subset=df[['Country','Average IQ']]
#print(subset)


# see countries and info for those whos IQ is above 100
filtered_df=subset[subset['Average IQ']>100]
print(filtered_df)

# handle example where data is missing or has duplicates
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)

# removing the unwanted data
df.dropna(inplace=True)
print(df.info())

#find duplicates
duplicate_count=df.duplicated().sum(0)
print(duplicate_count)

df.drop_duplicates(keep='first', inplace=True)