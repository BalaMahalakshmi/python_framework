import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
figure = plt.figure()
def date_convert(date_col):
    result=list()
    values = date_col.values
    for value in values:
        result.append(str(value).split("T")[0])
    return result
st.markdown("<h1 style='text-align: center;'>Data Visualizer</h1>",unsafe_allow_html=True)
st.markdown("___")
fn = list()
files = st.file_uploader("upload your files", type=["xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        fn.append(file.name)
    select_files = st.multiselect("select files", options=fn)
    if select_files:
        option = st.radio("select entity date", options=["None","GPU","CPU","MOUSE","KEYBOARD","CASTING"])
        if option!="None":
            # print(option)
            for file in files:
                if file.name in select_files:
                    data = pd.read_excel(file, index_col=0)
                    item = list(data)
                    dates = date_convert(data["DATE"])
                    index = np.arrange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.plot(index,item,label = file.name, marker = 'o')
                    plt.xlabel("Date")
                    plt.ylabel(option)
                    plt.title(option+"chart")
                    plt.grid(True)
                    plt.legend()
                    print(dates)
            st.write(figure)

    
