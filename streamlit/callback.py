import streamlit as st
# call  back
# def printer(name,age,city):
#     print(name,age,city)
# input = st.text_input("Enter your Name")
# c1,c2 = st.columns(2)
# a=c1.text_input("Enter your age")
# b=c2.text_input("Enter your city")
# but = st.button("SUBMIT")
# if but:
#     st.checkbox("want to display name?", on_change=printer, args=(input,a,b,))


# session states
# text = "Mahabi"
# if "click" not in st.session_state:
#     st.session_state.click = False
# else:
#     if st.session_state.click == False:
#         text = "amoremio"
#         st.session_state.click = True
#     else:
#         text = "mahabi"
#         st.session_state.click = False
# btn = st.button(text)

# cache in
import time
@st.cache(suppress_st_warning=True)
def printer():
    st.write("Running")
    time.sleep(3)
    return "Message"
st.write(printer())
