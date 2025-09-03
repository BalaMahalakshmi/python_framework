import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# model 1
st.markdown("<h1> User Registration </h1>", unsafe_allow_html=True)
form = st.form("form 1")
form.text_input("First Name")
form.text_input("Last Name")
form.text_input("Mail id")
form.form_submit_button("Submit")

# model 2
st.markdown("<h1> User Registration </h1>", unsafe_allow_html=True)
with st.form("Form 2"):
    st.text_input("Email id")
    st.form_submit_button("submit")

#add columns 
st.markdown("<h1 style='text_align: center;'> User Registration </h1>", unsafe_allow_html=True)
with st.form("Form 3"):
    col1, col2 = st.columns(2)
    fname = col1.text_input("First Name")
    lname = col2.text_input("Last Name")
    st.text_input("Email id")
    st.text_input("password")
    s_state = st.form_submit_button("submit")
    if s_state:
        if fname == "" and lname == "":
            st.warning("please fill the fields")
        else:
            st.success("submitted succesfully")

#sidebars and graphs
table = pd.DataFrame({"col1":[1,2,3,4,5], "col2":[11,12,13,14,15]})
x = np.linspace(0,10,100)
bx = np.array([1,2,3,4,5])
opt = st.sidebar.radio("select any graph", options=("line", "bar", "hbar"))
if opt == "line":
    st.markdown("<h2 style='text_align:center'> line chart </h2>",unsafe_allow_html=True)
    fig = plt.figure()
    # plt.style.use("link")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x),'--')
    st.write(fig)
elif opt == "bar":
    st.markdown("<h2 style='text_align:center'>bar chart</h2>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.bar(bx, bx*10)
    st.write(fig)
else:
    st.markdown("<h2 style='text_align:center'>h-barchart </h2>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.barh(bx*10,bx)
    st.write(fig)






