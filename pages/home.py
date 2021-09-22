"""This is the home page of the web app"""

import streamlit as st

def app():
    """This function runs the home page"""
    # Add title to the home page
    st.title("Welcome to the Iris Specie prediction app")
    # Add image to the home page
    st.image("./images/iris_classification_model.jpg", width=500)
    # Add brief describtion of your web app
    st.text("This web app helps in the prediction of iris specie using svm model.")