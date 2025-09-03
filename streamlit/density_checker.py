import streamlit as st
import re
st.markdown("<h1 style='text-align:center;'>Keyword Density Checker</h1>", unsafe_allow_html=True)
st.markdown("---")
text = st.text_area("paragraph")
c1,c2,c3 = st.columns(3)
words_dict=dict()
if text:
    c1.markdown("<h3 style='text-align:center;'>Keyword</h3>", unsafe_allow_html=True)
    c2.markdown("<h3 style='text-align:center;'>Occurances</h3>", unsafe_allow_html=True)
    c3.markdown("<h3 style='text-align:center;'>Percentage</h3>", unsafe_allow_html=True)
    words =sim_text = re.sub("[.,?!:;*]"," ", text)
    print(sim_text.lower().split())
    t_len = len(words)
    for word in words:
        if word in words_dict:
            words_dict[word]=words_dict[word]+1
        else:
            words_dict[word]=1
            # print(words_dict) #counting words in a paragraph or line
    keys = list(words_dict.keys())
    values = list(words_dict.values())
    for i in range(len(keys)):
        c1.markdown(f"<h5 style='text-align:center;'>{keys[i]}</h5>", unsafe_allow_html=True)
        c2.markdown(f"<h5 style='text-align:center;'>{values[i]}</h5>", unsafe_allow_html=True)
        c3.markdown(f"<h5 style='text-align:center;'>{round((values[i]/t_len)*100)}%</h5>", unsafe_allow_html=True)