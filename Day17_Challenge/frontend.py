import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# Categories Section
st.header("Categories")

with st.form(key='category_form'):
    category_name = st.text_input("Category Name")
    submit_button = st.form_submit_button("Add Category")

    if submit_button and category_name:
        response = requests.post(f"{API_URL}/categories/", json={"name": category_name})
        if response.status_code == 201:
            st.success("Category added!")
        else:
            st.error("Error adding category!")

# Display Categories
categories = requests.get(f"{API_URL}/categories/").json()
for category in categories:
    st.write(category['name'])

# Recipes Section
st.header("Recipes")

with st.form(key='recipe_form'):
    recipe_name = st.text_input("Recipe Name")
    description = st.text_input("Description (optional)")
    ingredients = st.text_area("Ingredients")
    instructions = st.text_area("Instructions")
    cuisine = st.text_input("Cuisine")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    category_id = st.number_input("Category ID (optional)", min_value=0)
    submit_button = st.form_submit_button("Add Recipe")

    if submit_button and recipe_name and ingredients and instructions:
        recipe_data = {
            "name": recipe_name,
            "description": description,
            "ingredients": ingredients,
            "instructions": instructions,
            "cuisine": cuisine,
            "difficulty": difficulty,
            "category_id": category_id or None
        }
        response = requests.post(f"{API_URL}/recipes/", json=recipe_data)
        if response.status_code == 201:
            st.success("Recipe added!")
        else:
            st.error("Error adding recipe!")

# Display Recipes
recipes = requests.get(f"{API_URL}/recipes/").json()
for recipe in recipes:
    st.write(recipe['name'])
