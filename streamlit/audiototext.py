import streamlit as st
from pydub import AudioSegment
st.markdown("<h1 style='text-align:center;'>Audio to Text</h1>", unsafe_allow_html=True)
st.markdown("---")
audio = st.file_uploader("Upload your Audio file", type=["mp3", "wav"])
if audio:
    aud_seg = AudioSegment.from_file(audio)
    print(aud_seg)