import streamlit as st
import numpy as np
import soundfile as sf
import os
import librosa
import glob
from helper import  create_spectrogram, read_audio, record, save_record

"# Speech to text demo"

st.header("1. Record your own voice")

filename = st.text_input("Choose a filename: ")

if st.button(f"Click to Record"):
    if filename == "":
        st.warning("Choose a filename.")
    else:
        record_state = st.text("Recording...")
        duration = 5  # seconds
        fs = 48000
        myrecording = record(duration, fs)
        record_state.text(f"Saving sample as {filename}.wav")

        path_myrecording = f"./samples/{filename}.wav"

        save_record(path_myrecording, myrecording, fs)
        record_state.text(f"Done! Saved sample as {filename}.wav")

        st.audio(read_audio(path_myrecording))

        fig = create_spectrogram(path_myrecording)
        st.pyplot(fig)
"## 2. Choose an audio record"

audio_folder = "samples"
filenames = glob.glob(os.path.join(audio_folder, "*.wav"))
selected_filename = st.selectbox("Select a file", filenames)

