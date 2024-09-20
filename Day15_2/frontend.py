import streamlit as st
import requests
import pandas as pd



st.title("Project Managment App")

st.header("Add a Developer")
dev_name=st.text_input("Developer Name")
dev_experience=st.text_input("Developer Experience")

if st.button("Add Developer"):
    dev_data={
        "name":dev_name,
        "experience":dev_experience
    }
    api_url="http://127.0.0.1:8000/developers/"
    response = requests.post(api_url,json=dev_data)
    st.json(response.json())