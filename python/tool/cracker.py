import random
from time import sleep
from os import pipe
from time import sleep
from tkinter import *
from tkinter import messagebox
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys
import pyttsx3
#call module
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color

def crack():
    char = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    arr = list(char)
    key = input("input password : ")
    guess_pass = ""
    
    while (guess_pass!=key):
        guess_pass = random.choices(arr,k=len(key))
        print(Fore.CYAN + "", file=stream)
        print(Fore.RED + "", file=stream)
        print(Fore.GREEN + "", file=stream)
        print(guess_pass)
        if guess_pass==list(key):
            print("password is "+"".join(guess_pass))
            break

crack()





