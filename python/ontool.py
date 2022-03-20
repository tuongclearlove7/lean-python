from os import pipe
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import font
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys
import pyttsx3
import tkinter as tk 
from time import strftime
from threading import *
import base64
import pygame

tool = Tk()
tool.geometry("350x300")
tool.title("My Software")
tool.iconbitmap('tuongclearlove7.ico')
#tool.configure(background="pink")
background = PhotoImage( file = "tuongclearlove7.png")
# Show image using label
label_1 = Label( tool, image = background)
label_1.place(x = 0,y = 0)

class Class_multithreading: # class multithreading (lớp đa luồng)
        def __init__(self):
                super().__init__()
                print(self,super)
        def multithreading_youtube(self):
            self.multithreading1=Thread(target=on_youtube)
            self.multithreading1.start()
object = Class_multithreading()

class login():
    def login_gmail():
        while True:
            Gmail = webdriver.Chrome(executable_path=r"C:\Users\clearlove7\Documents\GitHub\clearlove7.github.io\python\chromedriver.exe")
            Gmail.set_window_size(1000,1000)
            Gmail.get("http://gmail.com")
            Gmail.find_element_by_id("identifierId").send_keys("lol00sever@gmail.com")
            sleep(2)    
            Gmail.find_element_by_xpath("//*[@id='identifierNext']").click()
            sleep(2)
            Gmail.find_element_by_id("next").click()
            sleep(2)
            Gmail.find_element_by_id("password").send_keys("")
            sleep(2)
            Gmail.find_element_by_name("passwordNext").click()
            break
        

def on_youtube():
    login.login_gmail()
    pass

b1 = Button(tool, text = "Bật youtube", command = object.multithreading_youtube,background="red"
, activeforeground = "black", activebackground = "firebrick1", width = 10)
label = Label(tool, text="Welcome to my Software", font=("Helvetica", 20))
label.pack(side = TOP)
b1.pack(side = TOP)
tool.update()
tool.mainloop()















