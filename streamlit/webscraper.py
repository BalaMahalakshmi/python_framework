import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
st.set_page_config(page_title="web scraper", page_icon=":globe_with_meridians:", layout="wide")
# st.image("https://images.unsplash.com/photo-1741557571786-e922da981949?")

st.markdown("<h1 style='text-align: center;'>Web scraper</h1>",unsafe_allow_html=True)
with st.form("search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()   
if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    print(page.status_code) 
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="I7e4t")
    c1,c2 = placeholder.columns(2)
    print(len(rows))
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img",class_="YVj9w")
            # print(img["srcset"])
            # print("\n\n")
            list =img["srcset"].split("?")
            if i == 0:
                c1.image(list[0])
                btn = c1.button("Download", key=str(index)+str(i))
                if btn:
                    print("Button pressed")
            else:
                c2.image(list[0])
                btn = c2.button("Download", key=str(index)+str(i))
                if btn:
                    print("Button pressed")
                    

