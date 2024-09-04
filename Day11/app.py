import streamlit as st

# button widget
if st.button("Click Me"):
    st.write("Button clicked successfully!!!!")

# checkbox widget
if st.checkbox("Check Me!"):
    st.write("You are seeing this message because you checked this checkbox")

# user_input widget
user_input = st.text_input("Enter Your Name !")
st.write("You entered:  ",user_input)

# number input
age = st.number_input("Enter Your Age !", min_value=0 , max_value=100 )
st.write(f"Your age is:  {age}")

#text area
message = st.text_area("Enter Your Message ")
st.write (f"Your message is:  {message}")

# Radio buttons
choice = st.radio("Pick one", ["Choice 1","Choice 2","Choice 3","Choice 4"])
st.write(f"You choose : {choice}")

#
if st.button("Success"):
    st.success("Operation was successful!")

# Exception message
try:
    1/0
except Exception as e:
    st.exception(e)