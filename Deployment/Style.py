import streamlit as st

# * Defines global style
def style():
    st.markdown(
        """
    <style>
    a {
        text-decoration: none !important;
        color: #ABC !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )