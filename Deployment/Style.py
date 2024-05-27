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

    .small-margin-title {
        margin-bottom: 0.5rem;
    }

    .small-margin-divider {
        margin-top: -0.5rem;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    """,
        unsafe_allow_html=True,
    )