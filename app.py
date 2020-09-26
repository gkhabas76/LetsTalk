
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import playsound


def Daisy(text):
    print(text)
    tts = gTTS(text=text, lang='en-uk')
    soundSource = 'audio.mp3'
    tts.save(soundSource)
    playsound.playsound(soundSource)
    os.remove(soundSource)


def myWords():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        myInputAudio = ''

        try:
            myInputAudio = r.recognize_google(audio)
            print(myInputAudio)
        except Exception as e:
            Daisy('Could you please repeat once again?' + str(e))
    return myInputAudio


Daisy('Welcome to- Digital Assistant as Integrated Speech Yonder. By the way, you can call me Daisy.')

# Todo --> Login verification function
#Daisy('Please say the password')


def commands(command):
    if 'hello' in command:
        Daisy('Hi, Govinda. How are you?')
    elif 'stop the program' in command:
        Daisy('Shutting down the program')
        quit()

# Todo Extra functions and commands for automation


while True:
    commands(myWords())
