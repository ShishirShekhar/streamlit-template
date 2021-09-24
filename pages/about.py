"""This is about page"""

# import necessary modules
import streamlit as st


def app():
    """This function runs the about page"""
    # Add balloons animation when page opens
    st.balloons()

    # Add title
    st.title("Welcome to the about me page")

    # Add an image
    st.image("./images/iris_classification_model.jpg")
    
    # Add Contact Details
    st.header('Contact Us')

    # Add email
    st.markdown('''### Name:
    Shishir Shekhar''')

    # Add name
    st.markdown('''### Email:
    sspdav02@gmail.com''')

    # Add github
    st.markdown('''### GitHub: [ShishirShekhar](https://github.com/ShishirShekhar/)''')

    # Add linkedin
    st.markdown('''### Linkedin: [ShishirShekhar](https://www.linkedin.com/in/shishir-shekhar/)''')