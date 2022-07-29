import pyttsx3
import datetime, os
import speech_recognition as sr
import webbrowser as wb
from random import choice
from time import sleep

def Turn_on_browser():
    url = ['https://www.facebook.com/','https://www.youtube.com/watch?v=JNdP_BpOAU8']
    for i in range(len(url)):
        print("get link "+ str(i+1)+" "+str(url[i]))
        pass
    tool = wb.open(url[0])
    tool = wb.open(url[1])


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('BOT: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def start():
    speak("Hi, I'm assistant") 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<24:
        speak("Good Evening")
    # mở nhạc
    list_music = [
        "https://www.youtube.com/watch?v=",
        "https://www.youtube.com/watch?v=",
        "https://www.youtube.com/watch?v=",
        "https://www.youtube.com/watch?v=",
        "https://www.youtube.com/watch?v="
    ]
    url = choice(list_music)
    wb.get().open(url)
    speak(f'Music start')
    speak(f'Good luck, fighting')
if __name__=="_main_":
    start()






