###################################### Imports##################################################################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocketsphinx.pocketsphinx import *
from commands import command,notify;
import pyaudio
import subprocess
import time

import spotipy


birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print((album['name']))

###################################### Variables ##################################################################################################################


kws_hmm = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/pocketsphinx/model/it/it'
kws_dict = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/pocketsphinx/model/it/voxforge_it_sphinx.dic'
reset_message = 'No commands heard. Back to Activation...'


###################################### Decode_function ##################################################################################################################

def decode_sphinx(kws, message, threshold, quitTimeS=-1):
    print(int(threshold))
    ###################################### (Configurations-set) ##################################################################################################################

    config = Decoder.default_config()

    config.set_string('-kws', kws)
    config.set_string('-hmm', kws_hmm )
    config.set_string('-dict', kws_dict)

    ## debug ##
    
    config.set_string("-logfn", "null")
    config.set_string("-verbose", "yes")

    ## tests ##
    threshold= 1*+(10**int(threshold))
    print(threshold)
    
    config.set_float('-kws_threshold',threshold)
    config.set_string("-doublebw", "yes")
    # config.set_int("-kws_delay", 1)
    # config.set_int("-vad_prespeech", 100)
    # config.set_int("-vad_startspeech", 1)
    # config.set_float("-vad_postspeech", 100)
    config.set_float("-vad_threshold", 0.1)

    decoder = Decoder(config)

    ###################################### (Microphon-set) ##################################################################################################################

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, output=True, frames_per_buffer=1024)
    stream.start_stream()

    ###################################### (Recognition-start) ##################################################################################################################

    decoder.start_utt()

    print(message)
    recognized=False
    audio=""

 
    if quitTimeS!=-1:
        startTime = time.time()


    while recognized==False:
        buf = stream.read(1024, exception_on_overflow=False)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        
        
        if quitTimeS!=-1:
            endTime = time.time()
            elapsedTime=endTime - startTime;
            # print(elapsedTime)
            if elapsedTime > quitTimeS and decoder.hyp() is None:
                print(reset_message)
                break 

        if decoder.hyp() is not None:
            for seg in decoder.seg():
                recognized=True
                print("word: "+ str(seg.word) + " activations: " + str(recognized))
                audio=seg.word


    decoder.end_utt()

    return audio

###################################### Main-loop ##################################################################################################################
