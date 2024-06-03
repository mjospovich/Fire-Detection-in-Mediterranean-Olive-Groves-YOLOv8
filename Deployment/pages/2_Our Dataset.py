import os
import random
from PIL import Image
import streamlit as st
from Setup import setup
from Style import style
from zipfile import ZipFile


# Function to display the dataset images and provide a download link
def our_dataset():
    st.markdown(
        "<h1 class='small-margin-title'> Our Dataset </h1>", unsafe_allow_html=True
    )
    st.write("<hr class='small-margin-divider'>", unsafe_allow_html=True)

    # Description of the dataset
    st.write(
        """
    ### Description
    This dataset contains images of fire and smoke used for aditional training and testing of our fire detection model.
    The dataset includes images of smoky fires in olive groves captured in coastal Croatia. It offers 
    further training data for fire detection models that specialze in detecting small fires on mediterranean landscapes.
    """
    )
    st.write(
        "You can download at the bottom of this page and use it freely for your own projects.<br><br>",
        unsafe_allow_html=True,
    )

    st.write("### Dataset Preview")

    # Path to the dataset folder
    dataset_folder = "Deployment/assets/croatia_fire_dataset"
    zip_file_path = "Deployment/assets/croatia_fire_dataset.zip"

    # Get a list of all image files in the dataset folder
    image_files = [
        f
        for f in os.listdir(dataset_folder)
        if f.lower().endswith(("jpg", "jpeg", "png"))
    ]

    random.shuffle(image_files)
    selected_images = image_files[:16]

    # Display selected images in rows of two
    for i, image_file in enumerate(selected_images):
        if i % 2 == 0:
            # Create a new row for every second image
            cols = st.columns(2)
        image_path = os.path.join(dataset_folder, image_file)
        image = Image.open(image_path)
        cols[i % 2].image(image, caption=image_file, use_column_width=True)

    # Check if the zip file exists, create if not
    if not os.path.exists(zip_file_path):
        with ZipFile(zip_file_path, "w") as zipf:
            for image_file in image_files:
                zipf.write(os.path.join(dataset_folder, image_file), image_file)

    st.markdown("<br>", unsafe_allow_html=True)
    st.write("### Download the Dataset")
    st.write("Click the button below to download the dataset as a zip file.")

    # Provide a download button for the dataset zip file
    with open(zip_file_path, "rb") as zip_file:
        st.download_button(
            label="Download Dataset",
            data=zip_file,
            file_name="croatia_fire_dataset.zip",
            mime="application/zip",
        )


# Run the setup, page content, and style functions
setup(title="Our Dataset")
our_dataset()
style()
