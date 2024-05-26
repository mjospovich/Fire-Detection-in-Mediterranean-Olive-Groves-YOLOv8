import streamlit as st


# * Function to setup the page
def setup(
    icon="Deployment/assets/icons/icons8-fire-48.png",
    title="Fire and Smoke Detection",
    sidebar="collapsed",
):
    # Set the page config
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="centered",
        initial_sidebar_state=sidebar,
    )
    # Set the sidebar
    st.sidebar.title("Links:")
    st.sidebar.markdown("LinkedIn [Profile](https://github.com/mjospovich)")
    st.sidebar.markdown("GitHub [Profile](https://github.com/mjospovich)")
    st.sidebar.markdown(
        "GitHub [Repository](https://github.com/mjospovich/Fire-Smoke-Detection)"
    )
    st.sidebar.markdown("Email: [mjosip01@fesb.hr](mailto:mjosip01@fesb.hr)")
    st.sidebar.caption("Developed by Martin Josipović, 2024.")
    st.sidebar.image(
        "Deployment/assets/wildfire2.png",
        caption="AI generated image of a wildfire",
        use_column_width="always",
    )
