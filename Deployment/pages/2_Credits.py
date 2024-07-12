# All references, links and other stuff used to create the project are mentioned here.
import streamlit as st
from Setup import setup
from Style import style


def credits():
    
    st.markdown("<h1 class='small-margin-title'>Credits</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <hr class='small-margin-divider'>
    
    <h3>Libraries</h3>
    <ul>
        <li><b>Deep Learning Model Library:</b> <a href='https://github.com/ultralytics/ultralytics' target='_blank'>Ultralytics</a></li>
    </ul>
    
    <h3>Dataset</h3>
    <ul>
        <li><b>Fire Detection Dataset:</b> <a href='https://github.com/gaiasd/DFireDataset?tab=readme-ov-file' target='_blank'>DFireDataset</a></li>
        <li><b>Paper Citation for Dataset Users:</b>
            <ul>
                <li>Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa: 
                <i>An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices.</i> 
                In: Neural Computing and Applications, 2022.</li>
            </ul>
        </li>
    </ul>
    
    <h3>Tutorials and Guides</h3>
    <ul>
        <li><b>Help for entire process of training a model and making the dataset:</b>
            <ul>
                <li>Video: <a href='https://youtu.be/m9fH9OWn8YM?list=PL-3_-KnXE6iNEoXA2Ji5zfHniMfLjjmll' target='_blank'>YouTube Video</a></li>
                <li>Channel: <a href='https://www.youtube.com/@ComputerVisionEngineer' target='_blank'>Computer Vision Engineer</a></li>
            </ul>
        </li>
    </ul>
    
    """, unsafe_allow_html=True)

# To display the credits page, call the function:
setup(title="Credits")
credits()
style()
