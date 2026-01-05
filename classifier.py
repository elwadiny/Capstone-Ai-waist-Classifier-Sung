import streamlit as st

def classify_waste(image):
    st.write("starting Classifying the waste Image ...")
    st.write("Please wait ...")
    # later this will do real AI — for now:
    st.success("This is organic")
