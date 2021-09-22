"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
from preprocess import load_model
from sklearn.svm import SVC


def app():
    """This funciton runs the prediction page"""

    # Set the title of the page
    st.title("Welcome to the prediction page")
    # Get model and score
    model, score = load_model(SVC)
    st.write(score)