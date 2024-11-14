import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Custom CSS to style the app
st.markdown(
    """
    <style>
    /* Body background and font settings */
    body {
        background-color: #121212; /* Dark background */
        color: #ffffff; /* White text */
        font-family: 'Arial', sans-serif;
    }
    /* Button styling */
    .stButton>button {
        background-color: #FF8C00; /* Button color */
        color: white;
        font-weight: bold;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton>button:hover {
        background-color: #FF5722; /* Hover color */
    }
    .stButton>button i {
        margin-right: 8px;
    }
    /* Input field styling */
    .stTextInput>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>input {
        background-color: #333333;
        color: white;
        border-radius: 5px;
        font-size: 16px;
    }
    .stTextArea>div>textarea {
        height: 80px; /* Increase height for better UX */
    }
    .stDataFrame {
        background-color: #1a1a1a;
        color: white;
    }
    h1, h2 {
        color: #FF8C00;
        font-size: 2rem;
        font-weight: bold;
    }
    /* Success, Error, Info, and Warning messages */
    .stWarning, .stError, .stSuccess, .stInfo {
        font-weight: bold;
    }
    .stSuccess {
        color: #4CAF50;
    }
    .stError {
        color: #F44336;
    }
    .stWarning {
        color: #FF9800;
    }
    .stInfo {
        color: #2196F3;
    }
    /* Hover effect for the finance entries table */
    .stDataFrame:hover {
        background-color: #333333;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title and description
st.title("Personal Finance Tracker")
st.write("""
    This app helps you track your income, expenses, and savings.
    Visualize your spending habits, and get a sense of where your money is going.
    """)

# Initialize finance data if not present
if "finance_data" not in st.session_state:
    st.session_state["finance_data"] = pd.DataFrame(columns=["Date", "Category", "Amount", "Type", "Note"])

# Sidebar layout
st.sidebar.header("Add Your Finance Entry")
expense_type = st.sidebar.selectbox("What are you adding?", ["Expense", "Income"])
category = st.sidebar.text_input("Category (e.g., Rent, Groceries, Salary):")
amount = st.sidebar.number_input("Amount ($)", min_value=0.0, step=0.01)
date = st.sidebar.date_input("Date", pd.to_datetime("today"))
note = st.sidebar.text_area("Note (optional)", "")

# Button to add the entry with an icon
add_entry_button = st.sidebar.button("Add Entry", key="add_entry", help="Click to add your entry")
if add_entry_button:
    try:
        # Create a new DataFrame to store data
        new_data = pd.DataFrame([[date, category, amount, expense_type, note]],
                                columns=["Date", "Category", "Amount", "Type", "Note"])

        # Append new data to the existing DataFrame
        st.session_state["finance_data"] = pd.concat([st.session_state["finance_data"], new_data], ignore_index=True)

        st.success(f"{expense_type} added successfully!")
    except Exception as e:
        st.error(f"Error adding entry: {e}")

# Display the data table
st.subheader("Your Finance Data")
if not st.session_state["finance_data"].empty:
    st.dataframe(st.session_state["finance_data"])
else:
    st.write("No data to display yet.")

# Expense vs Income Pie Chart
if not st.session_state["finance_data"].empty:
    # Group the data by 'Type' (Income or Expense)
    expense_data = st.session_state["finance_data"].groupby("Type")["Amount"].sum()

    # Ensure the data has valid values before plotting
    if expense_data.empty:
        st.warning("No expense or income data available to plot.")
    else:
        fig, ax = plt.subplots(figsize=(8, 8))  # Set the figure size to avoid a minimized chart
        expense_data.plot(kind="pie", autopct='%1.1f%%', startangle=90, ax=ax, colors=['#FF8C00', '#2196F3'])
        ax.set_ylabel("")  # Remove the ylabel for aesthetics
        st.pyplot(fig)
else:
    st.warning("Please add some data first to see the pie chart.")

# Bar chart for Expenses by Category
if not st.session_state["finance_data"].empty:
    category_data = st.session_state["finance_data"][st.session_state["finance_data"]["Type"] == "Expense"].groupby("Category")["Amount"].sum()

    # Ensure the category data is numeric before plotting
    if not category_data.empty:
        fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size for better layout
        category_data.plot(kind="bar", ax=ax, color='#FF8C00')
        ax.set_ylabel("Amount ($)")
        ax.set_title("Expenses by Category")
        st.pyplot(fig)
    else:
        st.warning("No expense data available to plot by category.")
else:
    st.warning("Please add some data first to see the bar chart.")

# Real-time Budget Feedback (Feature 6)
st.subheader("Budget Feedback")

# Calculate total income and total expenses
total_income = st.session_state["finance_data"][st.session_state["finance_data"]["Type"] == "Income"]["Amount"].sum()
total_expenses = st.session_state["finance_data"][st.session_state["finance_data"]["Type"] == "Expense"]["Amount"].sum()

# Provide feedback based on the comparison of total income and expenses
if total_income == 0:
    st.warning("You haven't added any income data yet. Consider adding income first.")

if total_expenses > total_income:
    st.error("You are spending more than you earn! Try cutting back on unnecessary expenses.")
elif total_expenses < 0.5 * total_income:
    st.success("Great job! You're spending less than half of your income. Keep it up!")
else:
    st.info("You're spending a healthy portion of your income. Consider setting goals to save more.")


