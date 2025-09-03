import streamlit as st
from bs4 import BeautifulSoup
import requests
st.markdown("<h1 style='text-align:center;'>keyword extractor</h1>", unsafe_allow_html=True)
st.markdown("---")
url = st.text_input("youtube url here")
if url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"lxml")
    meta_tag = soup.select("meta[name='keywords']")
    # print(meta_tag[0]["content"]) #keyword disply on command prompt
    til = soup.find("title")
    keywords = meta_tag[0]["content"] #keyword display on streamlit web page
    st.title("Title")
    st.markdown(f"<h4 style:'color=#101820FF'>{til.text}</h4>", unsafe_allow_html=True)
    st.title("Tags")
    st.markdown(f"<h5 style: 'color=#101820FF'>{keywords}</h5>", unsafe_allow_html=True)
