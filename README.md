# speech-to-text

In this project we are going to to build a deep learning model that is capable of transcribing a speech to text. 

# DATA 
 The package contains swahili speech corpus with audio data in the directory /data. The data directory contains 1 folder and a file :
a. wav - this contains subdirectories of audion files 
b. teext - contains transcription of the audio files and the tags to each file
formore information on swahili corpus and  information about the format, please refer to Kaldi website http://kaldi-asr.org/doc/data_prep.html

# Preprocessing 
all in the preprocessyting.py file and preprocessing.ipynb
●	Convert into stereo channels 
    ○	Some of the sound files are mono (ie. 1 audio channel) while most of them are stereo (ie. 2 audio channels). Since the Neural network model expects all items to have the same dimensions, we will convert the mono files to stereo, by duplicating the first channel to the second
●	Standardize sampling rate
      ○	We  standardize and convert all audio to the same sampling rate so that all arrays have the same dimensions.
●	Resize to the same length
      ○	Resize to get an equal-sized audio sample by extending duration by padding it with silence, or by truncating it.
●	Data argumentation 
      ○	Perform data augmentation on the raw audio signal by applying a Time Shift to shift the audio to the left or the right by a random amount. 
●	Feature extraction: Speech recognition methods derive features from the audio, such as Spectrogram or Mel Frequency Cepstrum (MFCC).
      ○	Convert the augmented audio to a Mel Spectrogram.

# Modeling 


# deployment 
