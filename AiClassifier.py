import streamlit as st
from PIL import Image
from classifier import classify_waste

st.title("Hello to AI Waste Classifier")

st.write("Choose a photo of waste:")

uploaded_image = st.file_uploader("Upload photo", type=["jpg", "jpeg", "png"])
camera_image = st.camera_input("Or take a photo")

image_to_use = None

if uploaded_image:
    image_to_use = uploaded_image
elif camera_image:
    image_to_use = camera_image

if image_to_use:
    st.image(image_to_use, caption="Selected Image", width=300)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cancel"):
            st.rerun()


    with col2:
        if st.button("Classify Waste"):
            classify_waste(image_to_use)
