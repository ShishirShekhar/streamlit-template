"""This page is for Visualization of data."""

# Import necessary moduels
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import functions
from preprocess import load_data

def app():
    """This function will run this whole page"""
    st.title("Welcome to the visualization page")

    # Load feature and target data
    X, y = load_data()
    df = pd.concat([X, y], axis=1)

    # Create scatterplot for all the features\
    st.header("Scatter Plots")

    # Take input from user of the feature on x axis
    feat = st.multiselect("Select X axis feature", list(X.columns))

    # Creating scatter plot for all select features from user
    for i in feat:
        fig = plt.figure(figsize=(12, 5))
        plt.title(f"Scatter plot between target and {i}", fontsize=18)
        plt.scatter(X[i], y, c=y)
        plt.xlabel(i, fontsize=14)
        plt.ylabel(y.name, fontsize=14)
        st.pyplot(fig)

    # Ploting data using different plots
    st.header("Visulisation Selector")

    # Get input about type of plot from the user
    plots = st.multiselect("Select the type of plot", ["Heatmap", "Histogram", "Boxplot", "Pie Chart",  "Count Plot"])

    # Plot the plots selected by the user.
    # Plot the Heatmap
    if ("Heatmap" in plots):
        st.subheader("Heatmap")
        fig = plt.figure(figsize=(12, 5))
        sns.heatmap(df.corr(), annot=True)
        st.pyplot(fig)
    
    # Plot the Histogram
    if ("Histogram" in plots):
        st.subheader("Histogram")
        col = st.selectbox("Select the column for histogram", list(df.columns))
        fig = plt.figure(figsize=(12, 5))
        sns.histplot(df[col])
        st.pyplot(fig)

    # Plot the boxplot
    if ("Boxplot" in plots):
        st.subheader("Boxplot")
        col = st.selectbox("Select the column for boxplot", list(df.columns))
        fig = plt.figure(figsize=(12, 5))
        sns.boxplot(df[col])
        st.pyplot(fig)

    # Plot the Pie Chart
    if ("Pie Chart" in plots):
        st.subheader("Pie Chart")
        col = st.selectbox("Select the column for pie chart", list(df.columns))
        fig = plt.figure(figsize=(12, 5))
        plt.pie(df[col].value_counts(), labels=df[col].unique())
        st.pyplot(fig)

    # Plot the Count Plot
    if ("Count Plot" in plots):
        st.subheader("Count plot")
        col = st.selectbox("Select the column for Count plot", list(df.columns))
        fig = plt.figure(figsize=(12, 5))
        sns.countplot(df[col])
        st.pyplot(fig)
