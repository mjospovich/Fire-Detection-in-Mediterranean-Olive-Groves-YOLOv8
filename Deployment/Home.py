# Imports
import streamlit as st
import time

def setup():
    #* Set the page config
    st.set_page_config(
        page_title="Fire and Smoke Detection",
        page_icon="🔥",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    
    #* Set the sidebar
    st.sidebar.title("Links:")
    st.sidebar.markdown("LinkedIn: [Profile](https://www.linkedin.com/in/mjospovich)")
    st.sidebar.markdown("GitHub: [Profile](https://github.com/mjospovich)")
    st.sidebar.markdown("GitHub: [Repository](https://github.com/mjospovich/Fire-Smoke-Detection)")
    st.sidebar.markdown("Email: [mjosip01@fesb.hr](mailto:mjosip01@fesb.hr)")
    st.sidebar.caption("Developed by Martin Josipović, 2024.")
    st.sidebar.image(
        "Deployment/assets/wildfire2.png",
        caption="Ai generated image of a wildfire",
        use_column_width="always"
        )


#* Render the app
def app():

    #* Title, intro and image
    st.title("Fire and Smoke Detection")
    st.write("by Martin Josipović")
    st.divider()
    st.image(
        "Deployment/assets/wildfire.png", # Images at Deployment/assets
        caption="AI generated image of a wildfire",
        use_column_width="always",
        )
    
    #* Description
    yolo_link = '<a hrf="https://github.com/ultralytics/ultralytics">YOLOv8</a>'
    dfire_link = '<a hrf="https://github.com/gaiasd/DFireDataset">D-Fire</a>'

    st.write(
        f"""<br>
        <div style='text-align: center;'>
        Our fire and smoke detection model was built using the {yolo_link} model, 
        trained on the {dfire_link} dataset and some our own data as well.
        This app enables you to provide an image and use it to test our model and detect
        fire or smoke if present in the image.
    	<br><br><br><br>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    #* Testing the model
    st.markdown(
        """ 
            <div style='text-align: center;'>
                <h2>Test the model</h2>
                <p>Select the way you wish to provide the image and test out our model on it!</p>
                <hr>
            </div>
        """,
        unsafe_allow_html=True,
        )
    
    #* Select the model info
    col1, col2 = st.columns(2)
    with col1:
        model_type = st.radio(
            "Select model:",
            ("model_nano", "model_large"),
            index=0
            )
    #* Change the confidence threshold
    with col2:
        confidence_threshold = st.slider(
            "Confidence threshold:",
            0.0, 1.0, 0.2, 0.01
            )


    col1, col2 = st.columns(2)
    with col1:
        with st.expander("What do different models do?"):
            st.caption("We have 2 models to choose from:")
            st.caption("Nano model is faster but less accurate.")
            st.caption("Large model is slower but more accurate.")
    with col2:
        with st.expander("What is the Confidence Threshold?"):
                st.caption("The Confidence Treshold is the minimum confidence level required for a detection to be displayed.")
                st.caption("The value is between 0 and 1, while the current default value is 0.2.")
                st.caption("Lower values will result in fewer detections, while higher values will result in more detections.")

    st.divider()

    #* Select image source
    image_source = st.radio(
        "Select image source:",
        ("Upload from Computer", "Enter URL", "Use one of ours")
        )
    
    # Set variables to None
    image_file = None
    image_url = None

    #* Set the image source
    if image_source == "Enter URL":
        image_url = st.text_input("Enter image URL:")
    elif image_source == "Upload from Computer":
        image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png"])
    else:
        image_file = "Deployment/assets/test_image.jpg"

    #* Display the image
    if image_file or image_url:
        with st.spinner("Loading image..."):
            time.sleep(0.8)
            if image_source == "Enter URL":
                st.image(image_url, use_column_width="always")
            elif image_source == "Upload from Computer":
                st.image(image_file, use_column_width="always")
            else:
                st.image(image_file, use_column_width="always")


#! Run the app
if __name__ == "__main__":
    setup()
    app()