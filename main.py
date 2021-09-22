""""This is main file to run the web app"""

# import necessary modules
import streamlit as st

# import pages
from pages import home, data, prediction, visualization, scope, model, about

# Dictionary for pages
pages = {
    "Home": home,
    "Data Info": data,
    "Prediction": prediction,
    "Visualization": visualization,
    "Scope": scope,
    "Model info": model,
    "About me": about
}

# Creating sidebar navigation
st.sidebar.title("Navigation")
# get value of selected page using radio
page = st.sidebar.radio("Pages", list(pages.keys()))

# Call app funciton for the selected page
pages[page].app()