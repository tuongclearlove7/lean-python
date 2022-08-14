import pyttsx3
import datetime, os
import speech_recognition as sr
import webbrowser as wb
from random import choice
from time import sleep
from threading import *

chat = pyttsx3.init()
voices = chat.getProperty('voices')
chat.setProperty('voice', voices[1].id) 

def Speak(audio):
    print('BOT: ' + audio)
    chat.say(audio)
    chat.runAndWait()

def Time_count():
    cowndown = range(1,101, +1)
    for i in range(len(cowndown)):
        print("""|loading... """,cowndown[i], end = "")
        print("%|")
        sleep(0.020)

def BOT():
    Speak("Hi, I'm Clearlove7")
    os.system("cls")
    sleep(1)

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:Speak("good morning")
    elif hour>=12 and hour<18:Speak("good afternoon")
    elif hour>=18 and hour<24:Speak("good everning")
    
    turn_on = ["turn on facebook",
               "turn on youtube",
               "start music",
               "turn on Visual Studio Code",
               "turn on Dev Cpp",
               "turn on unikey"]
    url = [r"https://www.facebook.com/",
           r"https://www.youtube.com/",
           r"https://zingmp3.vn/album/Ngay-Anh-Xa-Miu-Le/ZWZ9EWAB.html",
           r'"D:\Microsoft VS Code\Code.exe"',
           
          ]
    if(turn_on[0]):
        Speak(turn_on[0])
        Time_count()
        wb.open(url[0])
        os.system("cls")
    if(turn_on[1]):
        Speak(turn_on[1])
        Time_count()
        wb.open(url[1])
        os.system("cls")
    if(turn_on[2]):
        Speak(turn_on[2])
        Time_count()
        wb.open(url[2])
        os.system("cls")
    if(turn_on[3]):
        Speak(turn_on[3])
        Time_count()
        os.system(url[3])
        sleep(1)
   
            
BOT()
Speak('Good luck')







