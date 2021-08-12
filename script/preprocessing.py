import os
import wave,array
import librosa
import numpy as np
import logging
import sklearn
from pydub import AudioSegment
import IPython.display as ipd
import soundfile as sf

logging.basicConfig(filename='..\script\preprocessing.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)




def make_stereo(audio_path):
        #this function converts mono audio channels into stereo channels 
    #     logging.info(" ============ Conerting audio sample from mono to stereo ================= ")
        print("======= Mono to stereo audio conversion")
        ifile = wave.open(audio_path)
        #log the info on adio files
    #     logging.info(ifile.getparams())
        print (ifile.getparams())
        # (1, 2, 44100, 2013900, 'NONE', 'not compressed')
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = ifile.getparams()
        assert (comptype == 'NONE')  # Compressed not supported yet
        array_type = {1:'B', 2: 'h', 4: 'l'}[sampwidth]
        print(" ======= Calculting left channel type =====")
        left_channel = array.array(array_type, ifile.readframes(nframes))[::nchannels]
        ifile.close()

        #convert the number of channels to 2
        print("====== converting channels ======= ")
        stereo = 2 * left_channel
        stereo[0::2] = stereo[1::2] = left_channel
        #overwrite the wav file making it a stereo file
        print("====== overwriting wav file ======= ")
        ofile = wave.open(audio_path, 'w')
        ofile.setparams((2, sampwidth, framerate, nframes, comptype, compname))
        ofile.writeframes(stereo.tostring())#stereo.tobytes()
        ofile.close()




def caclulate_duration(audio_file):
        print(" ============ Calculating duration of audio file =================")


        logging.info(" ============ Calculating duration of audio file ================= ")
        #pick audio file and let librosa calculate the sample_rate and samples which we shall use to calculate the duration
        
        samples, sample_rate = librosa.load(audio_file)
        duration=float(len(samples)/sample_rate)




def resample (file_path):
        samples,sample_rate=librosa.load(file_path,8000)
        samples=librosa.resample(samples,sample_rate,8000)
        sf.write(file_path,samples,sample_rate)




def pad(audio_file):
        print(" ============ checking duration of audio file to add padding  =================")


        logging.info(" ============ if duration is below 6 we add silence  ================= ")
        #pick audio file and let librosa calculate the sample_rate and samples which we shall use to calculate the duration
        
        samples, sample_rate = librosa.load(audio_file)
        duration=float(len(samples)/sample_rate)

        print('the duration is ', duration)
        if duration < 6 :
            print(" ============  duration is below 6  =================")
            pad_ms = 4000
            audio = AudioSegment.from_wav(audio_file)
            silence = AudioSegment.silent(duration=pad_ms)
            padded = audio + silence
            samples, sample_rate = librosa.load(padded)
            newduration=float(len(samples)/sample_rate)
            sf.write(audio_file, samples, sample_rate)
            

        else :
            print(" ============  duration is above 6  =================")
        pass



def shift (file_path):
        logging.info(" ============ Augmenting audio by shifting ================= ")
        samples, sample_rate = librosa.load(file_path)
        wav_roll = np.roll(samples,int(sample_rate/10))
        #plot_spec(data=wav_roll,sr=sample_rate,title=f'Shfiting the wave by Times {sample_rate/10}',fpath=wav)
        ipd.Audio(wav_roll,rate=sample_rate)
        sf.write(file_path, wav_roll, sample_rate)



def mfcc(wav):
    logging.info(" ============ feature extraction mfcc  ================= ")
    samples, sample_rate = librosa.load(wav)
    mfcc = librosa.feature.mfcc(samples, sr=sample_rate)
    # Center MFCC coefficient dimensions to the mean and unit variance
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    librosa.display.specshow(mfcc, sr=sample_rate, x_axis='time')
        #print (f'MFCC is of type {type(mfcc)} with shape {mfcc.shape}')
        # MFCC is of type <class 'numpy.ndarray'> with shape (, )
    sf.write(wav, samples, sample_rate)
    return mfcc
