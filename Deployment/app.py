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
        <div style='text-align: center;'>
        Our fire and smoke detection model was built using the {yolo_link} model, 
        trained on the {dfire_link} dataset and some our own data as well. <br>
        This app enables you to choose an image and use it to test our model and detect
        fire or smoke if present in the image.
    	<br><br><br><br>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    # Testing the model
    st.markdown(
        """ 
            <div style='text-align: center;'>
                <h2>Test the model</h2>
            </div>
        """,
        unsafe_allow_html=True,
        )
    
    image_source = st.radio("Select image source:", ("Enter URL", "Upload from Computer"))
    
    if image_source == "Enter URL":
        image_url = st.text_input("Enter image URL:")
    else:
        image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png"])
    



if __name__ == "__main__":
    app()