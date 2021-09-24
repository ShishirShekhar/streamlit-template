""""This is main file to run the web app"""

# import necessary modules
import streamlit as st
from sklearn.svm import SVC

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
if page == "Prediction":
    prediction.app(SVC)
else:
    pages[page].app()