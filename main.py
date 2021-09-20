import streamlit as st
import home, data, prediction, visualization, scope, model, about


pages = {
    "Home": home,
    "Data Info": data,
    "Prediction": prediction,
    "Visualization": visualization,
    "Scope": scope,
    "Model info": model,
    "About me": about
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(pages.keys()))

pages[page].app()