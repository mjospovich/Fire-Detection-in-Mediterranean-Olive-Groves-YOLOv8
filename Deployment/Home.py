import os
import io
import cv2
import time
import requests
from PIL import Image
import streamlit as st
from io import BytesIO
from Setup import setup
from Style import style
from ultralytics import YOLO
from datetime import datetime

# if issue with duplicate libraries, uncomment the line below
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


# * Function to load the YOLO model
@st.cache_resource
def load_model(model_name="nano"):
    # Depends on where the app is launched from
    path = rf"Deployment\Models\{model_name}.pt"
    model = YOLO(path)
    return model


# * Function to predict objects in the image
def predict_image(model, image, conf_threshold, iou_threshold):
    # Predict objects using the model
    res = model.predict(
        image,
        conf=conf_threshold,
        iou=iou_threshold,
        device="cpu",
    )

    class_name = model.model.names
    classes = res[0].boxes.cls
    class_counts = {}

    # Count the number of occurrences for each class
    for c in classes:
        c = int(c)
        class_counts[class_name[c]] = class_counts.get(class_name[c], 0) + 1

    # Generate prediction text
    prediction_text = "Predicted "
    for k, v in sorted(class_counts.items(), key=lambda item: item[1], reverse=True):
        prediction_text += f"{v} {k}"

        if v > 1:
            prediction_text += "s"

        prediction_text += " and "

    prediction_text = prediction_text[:-2]
    if len(class_counts) == 0:
        prediction_text = "No objects detected"

    # Calculate inference latency
    latency = sum(res[0].speed.values())  # in ms, need to convert to seconds
    latency = round(latency / 1000, 2)
    prediction_text += f" in {latency} seconds."

    # Convert the result image to RGB
    res_image = res[0].plot()
    res_image = cv2.cvtColor(res_image, cv2.COLOR_BGR2RGB)

    return res_image, prediction_text


# * Render the app
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
        unsafe_allow_html=True,
    )

    # Testing the model
    st.markdown(
        """ 
            <div style='text-align: center;'>
                <h2>Test the model</h2>
                <p>
                    Select the model you want to use, play with the IOU and confidence thresholds,
                    and upload an image or use one of ours to test the model.
                </p>
                <hr>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # Select the model
    model_type = st.radio(
        "Select model:", ("model_nano", "model_large"), index=0)
    model = load_model(model_type[6:])

    # Explain the models
    with st.expander("What do different models do?"):
        st.caption("We have 2 models to choose from:")
        st.caption("- Nano model is faster but less accurate.")
        st.caption("- Large model is slower but more accurate.")

    col1, col2 = st.columns(2)
    # Change the IOU threshold
    with col1:
        io_threshold = st.slider("IOU threshold:", 0.0, 1.0, 0.5, 0.02)

    # Change the confidence threshold
    with col2:
        confidence_threshold = st.slider(
            "Confidence threshold:", 0.0, 1.0, 0.2, 0.02)

    # Explain the thresholds
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("What is the IOU Threshold?"):
            st.caption("The IOU Threshold (0-1):")
            st.caption(
                "- Sets the overlap needed for two detections to be considered the same object."
            )
            st.caption("- Default is 0.5.")
            st.caption(
                "- Higher values: more overlapping detections, as each box needs to closely match the ground truth."
            )
            st.caption(
                "- Lower values: fewer detections, as the model is more lenient with overlap."
            )

    with col2:
        with st.expander("What is the Confidence Threshold?"):
            st.caption("The Confidence Threshold (0-1):")
            st.caption(
                "- Sets the minimum confidence for an object to be detected.")
            st.caption("- Default is 0.2.")
            st.caption(
                "- Higher values: only high-confidence detections are shown.")
            st.caption(
                "- Lower values: more detections, including less certain ones.")

    st.divider()

    # Select image source
    image_source = st.radio(
        "Select image source:", ("Upload from Computer",
                                 "Enter URL", "Use one of ours")
    )

    # Set variables to None
    image_file = None
    image_url = None

    # Set the image source
    if image_source == "Enter URL":
        image_url = st.text_input("Enter image URL:")
    elif image_source == "Upload from Computer":
        image_file = st.file_uploader(
            "Upload image:", type=["jpg", "jpeg", "png"])
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
                prediction, prediction_text = predict_image(
                    model, image, confidence_threshold, io_threshold
                )

            # Display the prediction image
            st.image(
                prediction,
                caption="Fire and smoke detection results",
                use_column_width=True,
            )
            st.success(prediction_text)

            # Create a BytesIO object to temporarily store the image data
            prediction_image = Image.fromarray(prediction)
            image_buffer = io.BytesIO()
            prediction_image.save(image_buffer, format="PNG")

            # Create a download button for the image
            current_date = datetime.now().strftime("%Y_%m_%d")
            st.download_button(
                label="Download Prediction",
                data=image_buffer.getvalue(),
                file_name=f"prediction_{current_date}.png",
                mime="image/png",
            )


if __name__ == "__main__":
    setup()
    app()
    style()
