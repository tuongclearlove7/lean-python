from lib2to3.pgen2 import driver
from os import pipe
from tkinter import *
from tkinter import messagebox
from tkinter import font
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys
import tkinter as tk 
from time import strftime
from threading import *
import pygame
import undetected_chromedriver.v2 as uc 
import base64
import json,requests,time,os,sys
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys 
import undetected_chromedriver.v2 as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import filedialog,Tk
from PIL import ImageTk,Image
import pyautogui, pyperclip, random
from time import sleep
from threading import *
import pyautogui, pyperclip, random
from time import sleep

win = Tk()
win.title('Spam')
win.geometry('630x250')
win.configure(background="#099D9D") # set background
#img = PhotoImage(file = "swift rose.png")# set image (thiết lập ảnh)
#img1 = img.subsample(7,8)
win.iconbitmap('C:\\Users\\clearlove7\\Documents\\GitHub\\clearlove7.github.io\\python\\tuongclearlove7.ico')
text_content = IntVar()
de_time = IntVar()
input_content = StringVar()
box_1 = Text(win, width=50, height=5, font=('arial',13))
box_1.place(x=10, y=77) 

class Multithreading():
    def Multi(args):
        args.multithreading1=Thread(target=Handle)
        args.multithreading1.start()
Obj = Multithreading()

def Handle():
    global content
    content = input_content.get()
    Delay = de_time.get()
    num_text = text_content.get()
    send_spam = box_1.get(1.0,END)
    shutdown_text = send_spam.split("\n")
    for index in range(10,0,-1):# countdown 10s
        print(index, end=" countdown... ",flush=True)
        sleep(1
        )
    print("\nstart\n")
    for i in range(num_text+1):
        pyperclip.copy(random.choice(shutdown_text))
        pyautogui.hotkey("ctrl","v")
        print(i," Enter {0}".format(""))
        pyautogui.press("enter")
        sleep(float(Delay))


#Label(win, image = img1).place(x=538,y=5)
Label(win, text = 'number spam',fg = 'black', bg="#099D9D", font=('arial',12)).place(x= 7, y= 20)
Entry(win, width=15, textvariable= text_content, font=('arial',12)).place(x=135, y= 20)
Label(win, text = 'content',fg = 'black',bg="#099D9D" ,font=('arial',12)).place(x= 20, y= 45)
Label(win, text = 'Delay',fg = 'black', bg="#099D9D", font=('arial',12)).place(x=280, y= 20)
Entry(win, width=10, textvariable= de_time ,font=("arial",12)).place(x=350, y= 20)
Button(win, text = 'Thực hiện', fg = 'black',bg = 'silver', font=('arial',10), command=Obj.Multi).place(x= 260, y =210)

win.mainloop()












































