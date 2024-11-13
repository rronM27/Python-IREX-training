import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app title and description
st.title("Personal Finance Tracker")
st.write(
    """
    This app helps you track your income, expenses, and savings.
    Visualize your spending habits, and get a sense of where your money is going.
    """
)
# Input for adding a new expense or income
expense_type = st.selectbox("What are you adding?", ["Expense", "Income"])
category = st.text_input("Category (e.g., Rent, Groceries, Salary):")
amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
date = st.date_input("Date", pd.to_datetime("today"))

# Button to add the entry
if st.button("Add Entry"):
    # Create a new DataFrame to store data (in practice, you would save this to a CSV or database)
    try:
        if "finance_data" not in st.session_state:
            st.session_state["finance_data"] = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])

        new_data = pd.DataFrame([[date, category, amount, expense_type]],
                                columns=["Date", "Category", "Amount", "Type"])

        # Append new data to the existing DataFrame
        st.session_state["finance_data"] = pd.concat([st.session_state["finance_data"], new_data], ignore_index=True)

        st.success(f"{expense_type} added successfully!")
    except Exception as e:
        st.error(f"Error adding entry: {e}")
# Display the data table
st.subheader("Your Finance Data")
if "finance_data" in st.session_state and not st.session_state["finance_data"].empty:
    st.dataframe(st.session_state["finance_data"])

    # Pie chart of expenses vs income
    st.subheader("Expense vs Income Distribution")
    expense_data = st.session_state["finance_data"].groupby("Type")["Amount"].sum()
    fig, ax = plt.subplots()
    expense_data.plot(kind="pie", autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel("")  # Remove the ylabel for aesthetics
    st.pyplot(fig)

    # Bar chart for expenses by category
    st.subheader("Expenses by Category")
    category_data = st.session_state["finance_data"][st.session_state["finance_data"]["Type"] == "Expense"].groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    category_data.plot(kind="bar", ax=ax)
    ax.set_ylabel("Amount ($)")
    ax.set_title("Expenses by Category")
    st.pyplot(fig)
else:
    st.write("No data to display yet.")
