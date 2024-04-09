import streamlit as st

def app():
    st.title("Fire and Smoke Detection")
    st.write("Welcome to the Fire and Smoke Detection App!")
    st.write("Here you can test our DL model for detecting fire and smoke in images.Please upload an image and click on the 'Predict' button to see the results.")


if __name__ == "__main__":
    app()