import streamlit as st
import cv2
from ultralytics import YOLO
import requests
from PIL import Image
import os
from glob import glob
from numpy import random
import io
from io import BytesIO
import time
from datetime import datetime

#os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

#* Function to load the YOLO model
@st.cache_resource
def load_model(model_name="nano"):
    model = YOLO(rf"\Github\Fire-Smoke-Detection\Deployment\Models\{model_name}.pt")
    return model

#* Function to predict objects in the image
def predict_image(model, image, conf_threshold, iou_threshold):
    # Predict objects using the model
    res = model.predict(
        image,
        conf=conf_threshold,
        iou=iou_threshold,
        device='gpu',
    )

    class_name = model.model.names
    classes = res[0].boxes.cls
    class_counts = {}

    # Count the number of occurrences for each class
    for c in classes:
        c = int(c)
        class_counts[class_name[c]] = class_counts.get(class_name[c], 0) + 1

    # Generate prediction text
    prediction_text = 'Predicted '
    for k, v in sorted(class_counts.items(), key=lambda item: item[1], reverse=True):
        prediction_text += f'{v} {k}'

        if v > 1:
            prediction_text += 's'

        prediction_text += ' and '

    prediction_text = prediction_text[:-2]
    if len(class_counts) == 0:
        prediction_text = "No objects detected"

    # Calculate inference latency
    latency = sum(res[0].speed.values())  # in ms, need to convert to seconds
    latency = round(latency / 1000, 2)
    prediction_text += f' in {latency} seconds.'

    # Convert the result image to RGB
    res_image = res[0].plot()
    res_image = cv2.cvtColor(res_image, cv2.COLOR_BGR2RGB)

    return res_image, prediction_text

def style():
    st.markdown("""
    <style>
    a {
        text-decoration: none !important;
        color: #ABC !important;
    }
    </style>
    """, unsafe_allow_html=True)

#* Function to setup the app
def setup():
    # Set the page config
    st.set_page_config(
        page_title="Fire and Smoke Detection",
        page_icon="🔥",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    # Set the sidebar
    st.sidebar.title("Links:")
    st.sidebar.markdown("LinkedIn [Profile](https://github.com/mjospovich)")
    st.sidebar.markdown("GitHub [Profile](https://github.com/mjospovich)")
    st.sidebar.markdown("GitHub [Repository](https://github.com/mjospovich/Fire-Smoke-Detection)")
    st.sidebar.markdown("Email: [mjosip01@fesb.hr](mailto:mjosip01@fesb.hr)")
    st.sidebar.caption("Developed by Martin Josipović, 2024.")
    st.sidebar.image(
        "Deployment/assets/wildfire2.png",
        caption="AI generated image of a wildfire",
        use_column_width="always"
    )

#* Render the app
def app():
    # Title, intro and image
    st.title("Fire and Smoke Detection")
    st.write("by Martin Josipović")
    st.divider()
    st.image(
        "Deployment/assets/wildfire.png",  # Images at Deployment/assets
        caption="AI generated image of a wildfire",
        use_column_width="always",
    )

    # Description
    yolo_link = '<a href="https://github.com/ultralytics/ultralytics">YOLOv8</a>'
    dfire_link = '<a href="https://github.com/gaiasd/DFireDataset">D-Fire</a>'

    st.write(
        f"""<br>
        <div style='text-align: center;'>
        Our fire and smoke detection model was built using the {yolo_link} model, 
        trained on the {dfire_link} dataset and some of our own data as well.
        This app enables you to provide an image and use it to test our model and detect
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
                <p>Select the way you wish to provide the image and test out our model on it!</p>
                <hr>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # Select the model info
    col1, col2 = st.columns(2)
    with col1:
        model_type = st.radio(
            "Select model:",
            ("model_nano", "model_large"),
            index=0
        )
        model = load_model(model_type[6:])
    # Change the confidence threshold
    with col2:
        confidence_threshold = st.slider(
            "Confidence threshold:",
            0.0, 1.0, 0.2, 0.02
        )

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("What do different models do?"):
            st.caption("We have 2 models to choose from:")
            st.caption("Nano model is faster but less accurate.")
            st.caption("Large model is slower but more accurate.")
    with col2:
        with st.expander("What is the Confidence Threshold?"):
            st.caption("The Confidence Threshold is the minimum confidence level required for a detection to be displayed.")
            st.caption("The value is between 0 and 1, while the current default value is 0.2.")
            st.caption("Lower values will result in fewer detections, while higher values will result in more detections.")

    st.divider()

    # Select image source
    image_source = st.radio(
        "Select image source:",
        ("Upload from Computer", "Enter URL", "Use one of ours")
    )

    # Set variables to None
    image_file = None
    image_url = None

    # Set the image source
    if image_source == "Enter URL":
        image_url = st.text_input("Enter image URL:")
    elif image_source == "Upload from Computer":
        image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png"])
    else:
        image_file = "Deployment/assets/test_image.jpg"

    # Display the image and run model
    if image_file or image_url:
        with st.spinner("Loading image..."):
            time.sleep(0.8)
            if image_source == "Enter URL":
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))
            elif image_source == "Upload from Computer":
                image = Image.open(image_file)
            else:
                image = Image.open(image_file)

            with st.spinner("Predicting..."):
                time.sleep(0.8)
                # Run the model
                prediction, prediction_text = predict_image(model, image, confidence_threshold, 0.5)
                
            # Display the prediction image
            st.image(prediction, caption="Fire and smoke detection results", use_column_width=True)
            st.success(prediction_text)

            # Create a BytesIO object to temporarily store the image data
            prediction_image = Image.fromarray(prediction)
            image_buffer = io.BytesIO()
            prediction_image.save(image_buffer, format='PNG')

            # Create a download button for the image
            current_date = datetime.now().strftime("%Y_%m_%d")
            st.download_button(
                label='Download Prediction',
                data=image_buffer.getvalue(),
                file_name=f'prediction_{current_date}.png',
                mime='image/png'
            )

if __name__ == "__main__":
    setup()
    app()
    style()
