# All references, links and other stuff used to create the project are mentioned here.
import streamlit as st

def credits():
    st.markdown("""
    <style>
    .credits-title {
        margin-bottom: 0.5rem;
    }
    .divider {
        margin-top: -0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='credits-title'>Credits</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <hr class='divider'>
    
    ### Libraries
    - **Deep Learning Model Library:** [Ultralytics](https://github.com/ultralytics/ultralytics)
    
    ### Dataset
    - **Fire Detection Dataset:** [DFireDataset](https://github.com/gaiasd/DFireDataset?tab=readme-ov-file)
    - **Paper Citation for Dataset Users:**
      - Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa: 
        *An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices.* 
        In: Neural Computing and Applications, 2022.
    
    ### Tutorials and Guides
    - **Help for entire process of training a model and making the dataset:**
      - Video: [YouTube Video](https://youtu.be/m9fH9OWn8YM?list=PL-3_-KnXE6iNEoXA2Ji5zfHniMfLjjmll)
      - Channel: [Computer Vision Engineer](https://www.youtube.com/@ComputerVisionEngineer)
    
    
    """, unsafe_allow_html=True)

# To display the credits page, call the function:
credits()
