import streamlit as st


def app():
    st.title("Welcome to the Iris Specie prediction app")
    st.image("./images/iris_classification_model.jpg", width=500)
    st.text("This web app helps in the prediction of iris specie using svm model.")