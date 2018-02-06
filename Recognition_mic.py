###################################### Imports ##################################################################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocketsphinx import *
from ctypes import *
#from commands import command, notify
import pyaudio
import subprocess
import time
import struct
import math


###################################### Variables ##################################################################################################################


kws_hmm = 'pocketsphinx/model/it/it'
kws_dict = 'pocketsphinx/model/it/custom/voxforge_it_sphinx_custom04.dic'
kws_activation = 'custom_keyphrases/keyphrases01.txt'
kws_commands = 'commands.txt'

activation_message = 'Started listening for activation...'
commands_message = 'Started listening for commands...'
reset_message = 'No commands heard. Back to Activation...'

SHORT_NORMALIZE = (1.0 / 32768.0)
RATE = 16000
INPUT_BLOCK_TIME = 1
INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)
SUPPRESS_ALSA_ERROR = True

###################################### ALSA error handler ###############################################################################################################

# From alsa-lib Git 3fd4ab9be0db7c7430ebd258f2717a976381715d
# $ grep -rn snd_lib_error_handler_t
# include/error.h:59:typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...) /* __attribute__ ((format (printf, 5, 6))) */;
# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
      #print 'messages are yummy'
      return
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
# Set error handler
if SUPPRESS_ALSA_ERROR:
    asound.snd_lib_error_set_handler(c_error_handler)
else:
    asound.snd_lib_error_set_handler(NULL)

###################################### Decode_function ##################################################################################################################


def get_rms(block):
    count = len(block) / 2
    format = "%dh" % (count)
    shorts = struct.unpack(format, block)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n
    return math.sqrt(sum_squares / count)


def decode_sphinx(kws, message, quitTimeS=-1):

    ###################################### (Configurations-set) ##################################################################################################################
    # print(kws)
    config = Decoder.default_config()

    config.set_string('-kws', kws)
    config.set_string('-hmm', kws_hmm)
    config.set_string('-dict', kws_dict)

    ## debug ##

    config.set_string("-logfn", "null")
    config.set_string("-verbose", "yes")

    ## tests ##

    config.set_string("-doublebw", "yes")
    config.set_float("-vad_threshold", 0.1)
    # + precision - recall
    # config.set_float("-alpha", 1.0)
    # config.set_float("-vad_postspeech", 0.01)
    config.set_float("-kws_plp", 0.3)
    config.set_float("-vad_startspeech", 1)
    # config.set_string("-dither", 'yes')

    decoder = Decoder(config)

    ###################################### (Microphon-set) ##################################################################################################################

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, output=True, frames_per_buffer=1024)
    stream.start_stream()

    ###################################### noiselevel-detection ##################################################################################################################

    am = []
    block = stream.read(INPUT_FRAMES_PER_BLOCK)
    # print(block)
    amplitude = get_rms(block)
    # print(amplitude)
    am.append(round(amplitude, 3))
    # print(am)
    print ("amplitude",round(amplitude*100, 2))
    somma = 0
    media = 0
    for i in am:
        somma += i
    media = somma / len(am)
    # print("somma: ",somma)
    # print("media: ",media)

    ###################################### (Recognition-start) ##################################################################################################################

    decoder.start_utt()

    print(message)
    recognized = False
    audio = ""

    if quitTimeS != -1:
        startTime = time.time()

    while recognized == False:

        buf = stream.read(1024, exception_on_overflow=False)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break

        if quitTimeS != -1:
            endTime = time.time()
            elapsedTime = endTime - startTime

            # print(elapsedTime)
            if elapsedTime > quitTimeS and decoder.hyp() is None:
                print(reset_message)
                break

        if decoder.hyp() is not None:
            for seg in decoder.seg():
                recognized = True
                print("word: " + str(seg.word) +
                      " activations: " + str(recognized))
                audio = seg.word

    decoder.end_utt()
    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    # p.terminate()

    return audio, media

###################################### Main-loop ##################################################################################################################

noiseLevel = 0

while True:
    print("-----------------------------------------")


    # subprocess.call(["/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/Parallel.py"])

    audio_a, noiseLevel = decode_sphinx(
        kws_activation, activation_message, quitTimeS=15)

    


    if audio_a == "okscala" or audio_a == "eiscala":
        
        print('attivazione avvenuta con successo');

        audio_file = "suoni-attivazione/Ding.wav"
        #notify('Chat-bot', 'Hey!')
        #return_code = subprocess.call(["afplay", audio_file])

        # audio_c = decode_sphinx(kws_commands, commands_message, quitTimeS=10)

        # command(audio_c)

        # audio_file = "/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/suoni-attivazione/Ding2.wav"
        # return_code = subprocess.call(["afplay", audio_file])



    if noiseLevel > 0.007:
        print("prossima 01: ", noiseLevel)
        kws_activation = 'custom_keyphrases/keyphrases00.txt'
    else:
        print("prossima 00: ", noiseLevel)
        kws_activation = 'custom_keyphrases/keyphrases01.txt'

