
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import playsound


def Daisy(text):
    # print(text)
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


def playSong():
    url = 'https://www.youtube.com/watch?v=2Vv-BfVoq4g'
    browserPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(browserPath))
    webbrowser.get('chrome').open_new_tab(url)


Daisy('Welcome to- Digital Assistant as Integrated Speech Yonder. By the way, you can call me Daisy.')

# Todo --> Login verification function
# Todo from file. Store some text as password for Daisy to read.
#Daisy('Please say the password')


def commands(command):
    if 'hello' in command:
        Daisy('Hi, Govinda. How are you?')

    elif 'could you please play any songs of your choice' in command:
        Daisy('Cool. I will play the song, titled, Perfect by Ed Sheeran')
        return playSong()

    elif 'open pycharm' in command:
        Daisy('Opening PyCharm. Please wait.')
        os.startfile(
            r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\bin\pycharm64.exe")

    elif 'stop the program please' in command:
        Daisy('Shutting down the program')
        quit()

# Todo Extra functions and commands for automation


while True:
    commands(myWords())
