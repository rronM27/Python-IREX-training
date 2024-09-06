import pandas as pd
import streamlit as st

st.header('Welcome to Displaying Dataframe 101')

df=pd.DataFrame({
    'Name':["Alice","Bob","Charlie","Dave"],
    'Age':[28,28,24,32],
    'City':["New York","San Francisco","San Francisco","Los Angeles"],
})


st.write(df)
