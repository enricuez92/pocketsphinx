#!/usr/bin/env python

import os
from os import environ, path, listdir

import json
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *


cwd = os.getcwd()


###################################### Function-recognition ##################################################################################################################

def recognition(namefile, parameter, value):
    #import numpy
    #return numpy.random.randint(0,3)
    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string(
        '-hmm', os.path.join(cwd, "pocketsphinx/model/it/it"))
    config.set_string(
        '-dict', os.path.join(cwd, "pocketsphinx/model/it/voxforge_custom_it_sphinx.dic"))
    config.set_string(
        '-kws', os.path.join(cwd, "keyphrases.txt"))
    
    # # config.set_string("-logfn", "null")
    # config.set_string('-agc', "noise")
    # # config.set_string('-agcthresh', "4.0")
    # config.set_string('-allphone_ci', "yes")
    # config.set_float('-alpha', 13.7)
    # # config.set_int('-ceplen', 7)
    # config.set_string('-cmn', "none")

    # config.set_string('-compallsen', "yes")
    # config.set_string('-dither', "yes")
    # config.set_string('-doublebw', "yes")

    # # config.set_string('-fsgusealtpron', "yes")
    # # config.set_string('-fsgusefiller', "yes")
    # # config.set_string('-fwdflat', "yes")
    # config.set_float('-kws_delay', 1)
    # config.set_float('-kws_plp', 0.01)
    # config.set_float('-kws_threshold', 10)
    # config.set_int('-ncep', 13)

    # config.set_int('-nfft', 1024)
    # config.set_int('-nfilt', 80)
    # config.set_float('-nwpen', 2.0)

    # config.set_string('-remove_dc', 'yes')
    # # config.set_string('-remove_noise', 'no')
    # # config.set_string('-remove_silence', 'no')
    # # config.set_string('-round_filters', 'no')

    # config.set_float('-silprob', 0.25)
    # # config.set_string('-smoothspec', 'yes')
    # config.set_string('-time', "yes")

    # config.set_int('-topn', 16)
    # config.set_string('-transform', "dct")
    # # config.set_string('-unit_area', "no")

    # config.set_float('-uw', 0.25)
    # config.set_int('-vad_postpeech', 250)
    # config.set_int('-vad_prespeech', 50)
    # config.set_int('-vad_startspeech', 50)
    # config.set_float('-vad_threshold', 8.0)

    # config.set_string('-varnorm', "yes")
    # config.set_string('-verbose', "yes")


    namefile = os.path.join(cwd, INPUT_FILES_PATH+ namefile)

    ############### PARAMETRI PER IL TEST SPECIFICO
    config.set_string(parameter,value);

    decoder = Decoder(config)

    # Decode streaming data.
    decoder.start_utt()
    stream = open(namefile, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()

    results = [seg.word for seg in decoder.seg()]
    print('Best hypothesis segments: ', results)
    print('activation found: ', len(results))
    print(namefile)
    nActivations=len(results);
    return nActivations


# def getListFileToAnalyze():
#     #questa funzione deve ritornare la lista di file da analizzare.
#     from os import listdir
#     from os.path import isfile, join
#     mypath= os.path.join(cwd, INPUT_FILES_PATH)
#     onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-4:]==".wav"]
#     #print(onlyfiles)
#     onlyfiles.sort()
#     return onlyfiles
#     # return ["File001.wav","File002.wav","File003.wav"]

# def writeResultsToFile(dictResults):
#     json.dump(dictResults, open(NAME_FILE_RESULTS,'w'), sort_keys=True,indent=-4, separators=(',', ': ') )

# def readResultsFromFile():
#     dictSTring=json.load(open(NAME_FILE_RESULTS))
#     dictNew={}
#     for key in dictSTring:
#         integerKey=int(key)
#         dictNew[integerKey]=dictSTring[key]
#     return dictNew
#     #questo file deve contenere una riga per ogni test cosi' formattata:
#     # 0 ; (parametri cambiati rispetto al default ) ; [ lista contenente tutte le attivazioni individuate]
# '''
# questo dizionario, dato l'indice del test da fare, ritorna una dizionario contente 
# -il parametro da cambiare
# -il relativo valore da impostare
# -i risultati (inizialmente vuoti)
# '''
# # dictResults={
# #     0   : {'parameter' : '-agc' , 'value' : '-max' , 'result':[]},
# #     1   : {'parameter' : '-agc' , 'value' : '-emax' , 'result':[]},
# #     2   : {'parameter' : '-agc' , 'value' : '-noise' , 'result':[]}
# #     #3  : da completare con nome parametro,valore parametro,risultato)
# # }

# #scorro tutti i possibili test
# for indiceTest in range(0,len(dictResults)):
#     parameter=dictResults[indiceTest]['parameter']
#     value=dictResults[indiceTest]['value']

#     print("In questo test verrano settato il parametro {}  al valore di {} ".format(parameter,value) )
    
#     print("Ottengo la lista dei file di cui fare il riconoscimento....")
#     fileList = getListFileToAnalyze()
#     print("Fatto.")
    
#     ######### tolgo DS_STORE ########
#     #def cancella(lista):
#     #    del lista[0]
#     #cancella(fileList)
#     recognitionResults=[];
#     for filename in fileList:
#         activationFound=recognition(filename,parameter,value)
#         recognitionResults.append(activationFound)
#     print (recognitionResults)

#     dictResults[indiceTest]['result']=recognitionResults
#     print("Test is over \n\n")

#     break

# print (dictResults)
# print("\n\n")
# writeResultsToFile(dictResults)

# #dictResults=[]
# #dictResults=readResultsFromFile()
