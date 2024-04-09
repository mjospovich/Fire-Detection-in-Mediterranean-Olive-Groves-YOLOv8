# Imports
import streamlit as st

#* Set the page config
st.set_page_config(
    page_title="Fire and Smoke Detection",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded"
    )

#* Render the app
def app():

    # Title, intro and image
    st.title("Fire and Smoke Detection")
    st.write("by Martin Josipović")
    st.divider()
    st.image(
        "Deployment/assets/wildfire.png", # Images at Deployment/assets
        caption="AI generated image of a wildfire",
        use_column_width="always",
        )
    
    # Description
    yolo_link = '<a hrf="https://github.com/ultralytics/ultralytics">YOLOv8</a>'
    dfire_link = '<a hrf="https://github.com/gaiasd/DFireDataset">D-Fire</a>'

    st.write(
        f"""<br>
        Our fire and smoke detection model was built using the {yolo_link} model, 
        trained on the {dfire_link} dataset and some our own data as well. <br>
        This app enables you to upload an image of your choice and use our model to detect
        fire and smoke if present in the image.
    	<br><br><br>
        """,
        unsafe_allow_html=True
        )
    
    # Testing the model
    st.write("## Test the model")

    



if __name__ == "__main__":
    app()