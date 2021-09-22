"""
This page preprocess the data and train the model, 
and return the trained model and score
"""

# Import necesssary modelues
import numpy as np
import pandas as pd
import streamlit as st

@st.cache()
def load_data():
    """
    This function preprocess the data and return feature(X) and target(y)
    """
    # load the dataset
    df = pd.read_csv("./Database/iris_species.csv")
    
    # preprocessing

    # Drop the Id column from the dataset
    df.drop(['Id'], axis=1, inplace=True)

    # Perform label encoding on target column
    df.iloc[:, -1].replace({
        "Iris-virginica": 0,
        "Iris-versicolor": 1,
        "Iris-setosa": 2
    }, inplace=True)

    # feature and target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    return X, y


@st.cache()
def load_model(algo):
    """
    This function train the model and return trained model and model score
    """
    # Load the data
    X, y = load_data()

    # create the model and fit the data
    model = algo()
    model.fit(X, y)

    # get the score
    score = model.score(X, y)
    return model, score
