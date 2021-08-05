import os
import wave,array






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
    ofile.writeframes(stereo.tostring())
    ofile.close()