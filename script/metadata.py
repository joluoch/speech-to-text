import os
import shutil
import json
import logging

logging.basicConfig(filename='..\logs\model.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

directory=('../data/train/wav')
files=[]
target=('../data/alldata')



rootdir = 'path/to/dir'


def merge_files():
    #this function loops through all the folders and extracts all the wav files into one folder 
    for folders in os.listdir(directory):
        #try cacth erros
        try:
        
            print("========== Accessing root directory ============== \n ")
            logging.info("======= Accessing root directory ============= \n")
            
            print("================== Accessing Subfolders ============= \n")
            #accessing subfolders inside train/wav directory
            subfolder = os.path.join(directory,folders)
            
            #looping through all contents in the subfolder
            for wavz in os.listdir(subfolder):

                print("================ Accessing files ============= \n")
                files.append(wavz)
                finalpath = os.path.join(subfolder,wavz)
                #copying files to new audio_path
                print("================ copying files to new audio_path============= \n")
                shutil.copy(finalpath, target)
        except FileNotFoundError:
            print(" !!! Error File Not Found  !!!!! \n")
            print(" !!! Program Failed !!!!! \n")
            logging.error(" !!! Error Program Failed !!!!! \n")
        except Exception as e:
            print(" !!! Error !!!!! \n")
            print (" !!! An excetion occurred Error: {} ".format(e.__class__))


name_to_text={}

## creating metadatfile 
def meta_data():
    logging.info("===================== Initializing meat_data function ==================== \n")
    print ("===================== Creating metadata file ================= \n ")
    filename=('../data/train/text')
    with open (filename, encoding="utf-8")as f:
        try:
            #open the txt file containnig file and matching text file
            print(" ========= Opening files ========= \n")
            logging.info("===================== Opening text file ========= \n ")
            f.readline()
            for line in f:
                #split first half to be the value and second part is the key/text
                
                name=line.split("\t")[-1]
                name=name.rstrip()
                file=line.split("\t")[0]
                file=file+".wav"
                length=len(name)         
                name_to_text[file]=[name,length]
            print(" ========== Completed =========== \n ")
        except Exception as e:
            print (" !!!! Error !!!! ")
            print (" !!!! The system raised an exception {} !!!!!".format(e.__class__))

    with open("../data/meta_data.json", "w") as outfile: 
        json.dump(name_to_text, outfile)

if (__name__== '__main__'):
    merge_files()
    meta_data()