import pandas as pd

products=["Apple","Banana","Orange","Pear"]
sales=[150,30,40,55]
sales_series=pd.Series(sales,index=products)
print(sales_series)
    