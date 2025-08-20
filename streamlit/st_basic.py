import streamlit as st
import pandas as pd
import time as ts
from datetime import time

st.title("Hi i'm web app, my passion is creating website!")
st.subheader("my name is subheader")
st.header("hai frnds, i'm also part of thizzz!")
st.text("Its easy to deploy the model...and development speed is high.")
st.markdown("**helllo** hai welcome!")
st.markdown("> helllo hai!")
st.markdown("#welcome!")
st.markdown("[Google](https://www.google.com)")
# st.markdown("![image](image.jpg)")  => img=img.open(link)
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.latex(r"\lparen\rparen") #o/p as ()
mab = {"x":"a,b,i","y":"v,u,l,e,m"}
st.json(mab)
ab="""
num=int(input("enter a year:"))
if num % 4 == 0:
    return "it's leap year";
else:
    return "its not a leap year";
"""
st.code(ab, language='python')

#swiss army knife
st.write("## mahabi") # like h2 tag
#matrix
st.metric(label="windspeed", value="1.28ms-1", delta="1.4ms-1")

#create a table using dataframe 
tab = ({"maha":['vul','2004.08.10'],"abi":['em','2003.16.09']})
st.table(tab)
st.dataframe(tab)

#create image and audio and video to web app
st.image(r"C:\Users\balam\OneDrive\Desktop\streamlit\python_framework\WIN_20250701_14_26_09_Pro.jpg")
st.video(r"C:\Users\balam\OneDrive\Desktop\streamlit\python_framework\WIN_20250701_14_25_58_Pro.mp4")

#interactive widgets using checkbox, radiobuttons

def hello():
    print(st.session_state.checker)
state = st.checkbox("check", value=True, on_change=hello, key="checker")
if state:
    st.write("Hi messi!")
else:
    pass

# using radio button
a = st.radio("which is your fav color?", options=("white","black","pink"))
print(a)
abi = st.radio("Abi will you marry me?", options=("1.yes","2.sure","3.1","4.2"))
print(abi)

#using button
def click():
    print("choose one")
a=st.button("choose me!", on_click=click)

#multiple selection
sel = st.selectbox("which is your fav food?", options=("biriyani","dosa","parota"))
print(sel)

ms = st.multiselect("what is fav subject?", options=("maths","english","hindi"))
print(ms)

abi = st.multiselect("Abi will you marry me?", options=("1.yes","2.sure","3.1","4.2"))
st.write(abi)

#file uploader
img = st.file_uploader("choose your file here!", type=["png","jpeg","jpg"])
if img is not None:
    st.image(img)

#slider 
b = st.slider("This is slider", min_value=30, max_value=160, value=50)
print(b)

#one line text
st.text_input("about moon!")
#this area space is bigger than text_input like type course description
st.text_area("About chatgpt")

#converter
def convert(value):
    h,m,s = value.split(":")
    t_s = int(m)*60 + int(s)+int(m)/1000
    return t_s

#set date and time_input
st.date_input("set the date for family trip")
val = st.time_input("set timer", value=time(0,0,0))

# print(type(val))
if str(val) == "00.00.00":
    st.write("set timer")
else:
    # print("perform other functions")
    sec = convert(str(val))
    print(sec)
    bar = st.progress(0)
    per =sec/100
    progress_status=st.empty()
    for i in range(10):
        bar.progress(i+1)
        # st.write(str(i) + "%")
        progress_status.write(str(i+1) + "%")
        ts.sleep(per)

#progress bar with time

bar = st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    ts.sleep(2)  #holding time




