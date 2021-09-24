"""This page is for future scopes of our model"""

# Import necessary modules
import streamlit as st


def app():
    """This function runs the model info page"""
    # Add title to page
    st.title("Welcome to the project scope page")

    # Add image
    st.image("./images/iris_classification_model.jpg")

    # Add model description
    st.write("project scope")