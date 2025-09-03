import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
st.markdown("<h1 style='text-align: center;'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("___")
image = st.file_uploader("upload your images", type=["jpg","png"])
info = st.markdown("<h2 style='text-align: center;'>Information</h2>",unsafe_allow_html=True)
size =st.empty()
format_=st.empty()
mode = st.empty()
if Image:
    img = Image.open(image)
    size.markdown(f"<h6>size of image: {img.size}",unsafe_allow_html=True)
    format_.markdown(f"<h6>format of image: {img.format}",unsafe_allow_html=True)
    mode.markdown(f"<h6>mode of image: {img.mode}",unsafe_allow_html=True)
    # print(img.mode)
    # print(img.size)
    # print(img.format)

    # resize= to see separate width and height
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>",unsafe_allow_html=True)
    Width = st.number_input("width",value=img.width)
    Height =st.number_input("height", value=img.height)

    # rotation
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>",unsafe_allow_html=True)
    degree = st.number_input("Degree")
    st.markdown("<h2 style='text-align: center;'>Filters</h2>",unsafe_allow_html=True)
    filter = st.selectbox("Filters", options=("None","Blur","Detail","Emboss","Smooth"))
    sb = st.button("Submit")
    if sb:
        edit = img.resize((Width, Height)).rotate(degree)
        fil = edit
        if filter!="None":
            if filter == "Blur":
                fil = edit.filter(BLUR)
            elif filter == "Detail":
                fil = edit.filter(DETAIL)
            elif filter == "Emboss":
                fil = edit.filter(EMBOSS)
            else:
                fil = edit.filter(SMOOTH)
        st.image(fil)




