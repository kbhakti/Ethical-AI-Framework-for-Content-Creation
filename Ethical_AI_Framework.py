import streamlit as st

# Set the title of the page
st.title("Simple Streamlit UI")

# Add a heading
st.header("Enter your text below")

# Create a text input widget
user_input = st.text_input("Your Text:")

# Create a submit button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")
