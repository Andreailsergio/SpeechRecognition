# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:24:13 2021

@author: andrea_sergiacomi

https://machinelearningknowledge.ai/create-ai-voice-assistant-with-speech-recognition-python-project-source-code/
"""

# pip install SpeechRecognition

# PROCEDURA NON FUNZIONANTE
# pip install PyAudio
''' PyAudio installation requires a build-in set-up for C++ binaries in your system 
and will throw an error if it is not installed already.
The C++ binaries can be installed from the following link 
https://visualstudio.microsoft.com/visual-cpp-build-tools/
'''

# PROCEDURA FUNZIONANTE
# pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
'''
file PyAudio wheel per python 3.8 e Windows 10 64 bit
PyAudio-0.2.11-cp38-cp38-win_amd64.whl
scaricato da https://www.lfd.uci.edu/~gohlke/pythonlibs/
e messo nella cartella C: Users andrea_sergiacomi
'''

# pip install pyttsx3
''' Requirement already satisfied '''
# A SEGUITO DI ERRORI IN ESECUZIONE
''' 
KeyError: None
AttributeError: module 'comtypes.gen.SpeechLib' has no attribute 'ISpeechVoice' '''
# pip uninstall pyttsx3
# pip install pyttsx3==2.7
# O MEGLIO
# pip install --upgrade comtypes

# pip install pywhatkit

# pip install wikipedia
''' Requirement already satisfied '''



# TEST INPUT DA MICROFONO E RICONOSCIMENTO SPEECH_TO_TEXT CON RECOGNIZE_GOOGLE
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as web
import requests

listener = sr.Recognizer()

# TEST TEXT_TO_SPEECH
'''
engine = pyttsx3.init()
engine.say('hey sir how are you')
engine.say('hey what you want')
engine.runAndWait()
'''
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as data_taker:
            print("Say Something")
            voice = listener.listen(data_taker)
            instruct = listener.recognize_google(voice)
            instruct = instruct.lower()
            print(instruct)
            if 'max' in instruct:
                # print(instruct)
                instruct = instruct.replace('max', '')
                return instruct
            return None
    except:
        pass
    
def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        # pywhatkit.playonyt(song)
        # finchè PyWhatKit PlayOnYT non funziona (restituisce URL: https://www.youtube.com%3E%3C/form%3E%3Ca%20href=)
        url = requests.get(f"https://mypywhatkit.herokuapp.com/playonyt?topic={song}").text
        # print(url)
        x = web.get('windows-default') # 'chrome'
        x.open(url)
        print(song)
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I: %M')
        print(time)
        talk('current time is' + time)
    elif 'tell me about' in instruct:
        thing = instruct.replace('tell me about', '')
        info = wikipedia.summary(thing, 2)
        print(info)
        talk(info)
    elif 'who are you' in instruct:
        talk('I am your personal Assistant Max')
    elif 'what can you do for me' in instruct:
        talk('I can play songs, tell time, and help you go with wikipedia')
    else:
        talk('I did not understand, can you repeat again')
'''
usando pywhatkit.playonyt
per risolvere SSLError: HTTPSConnectionPool(host='consent.youtube.com', port=443): Max retries exceeded with url: /m?continue=https%3A%2F%2Fwww.youtube.com%2Fresults%3Fq%3Dmax%2B%2Bdespacito&gl=IT&m=0&pc=yt&uxe=23983172&hl=it&src=1 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1108)')))
copiare libcrypto-1_1-x64.dll e libssl-1_1-x64.dll da Anaconda Library Bin a Anaconda DLLs

per risolvere SSL error per tutte le librerie usate
pip install pywhatkit --trusted-host youtube.com
pip install wikipedia --trusted-host en.wikipedia.org
pip install requests --trusted-host mypywhatkit.herokuapp.com
pip install requests --trusted-host google.com
'''

# loop for continuous usage
while True:
    print('CTRL C per uscire')
    run_Max()
# for example
# “MAX Play Despacito song”
# "Max what time is it?"
# "Max tell me about Churchill (something to find on wikipedia)"
# "Max who are you"
# "Max what you can do for me"

