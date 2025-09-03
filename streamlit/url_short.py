import streamlit as st
import pyshorteners as pyst
import pyperclip 
shortner = pyst.Shortener()
def copi():
    pyperclip.copy(shorted_url)
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>URL Shortener</h1>", unsafe_allow_html=True)
form = st.form("Name")
url = form.text_input("URL HERE")
sb = form.form_submit_button("Short")
if sb:
    shorted_url = shortner.tinyurl.short(url)
    # print(shorted_url)
    st.markdown("<h6 style='text-align: center;'> Shorted url</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> {Shorted url}</h6>", unsafe_allow_html=True)
    st.button("copy", on_click=copi)
