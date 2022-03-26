from os import pipe
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tracemalloc import start
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from numpy import tile
from selenium import webdriver
import os , sys
import pyttsx3
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
from time import sleep


init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color
pygame.init()
bot = pyttsx3.init()
voices = bot.getProperty("voices") 
bot.setProperty("voice", voices[1].id) 
tool = Tk()
tool.geometry("603x413")
tool.iconbitmap("tuongclearlove7.ico")
tool.title("My Software")# set title
tool.configure(background="#099D9D")


class Class_multithreading(): 
    def Multiple(args):
        args.multithreading2=Thread(target=Multi_tool)
        args.multithreading2.start()
Object = Class_multithreading()

def new_time():
    time_string = strftime("Time : %H:%M:%S %p") 
    label_time.config(text = time_string)
    label_time.after(1000, new_time) 
def openfile():
    Filepath = filedialog.askopenfilename(
    initialdir="C:\\Users\\clearlove7\Documents\\GitHub\\clearlove7.github.io\\python",
    title="you are open file",
    filetypes=[
        ("MKV file",".mkv"),
        ("PNG file",".png")
    ])
    file = open(Filepath,"r")
    print(file.read())
    file.close()

class Software():
    def handle():
        global Delay
        global loop
        global tuong
        try:
            loop = int(input("input number integer login google : "))
            Delay  = int(input("input integer time each time off : "))
            for tuong in range(loop):
                val = int(loop)
                print("number of loop : ")
                print(val)
                bot.say("login google")
                bot.runAndWait()
                Software.Login()
        except ValueError:
            bot_said = "you were inputing wrong format "
            print(bot_said)
            bot.say(bot_said)
            bot.runAndWait()

    def Login():
    #num = int(input("input integer create account : "))
    #time  = int(input("input integer time each time off : "))
        while True:
            if __name__ == "__main__":
                driver = uc.Chrome()
                link = f'https://www.google.com'
                driver.get(link)
                driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&followup=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&hl=vi&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
                WebDriverWait(driver, 10)
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('lol00sever@gmail.com')
                sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() 
                sleep(1)
                base64_message = 'MTIzNDMyMTEyMzQzMjE='
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                data = message_bytes.decode('ascii')
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(data)
                sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
                sleep(2)
            if __name__ == "__main__":
                driver.get(f'https://www.youtube.com/watch?v=78nhuJ9E1es&t=1s')
                sleep(2)
                driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon').click()
                sleep(2)
                driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]').click()
                sleep(2)
                driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div').click()
                sleep(Delay)
                print("Exit browser")
            break
def Multi_tool():
    try:
        Software.handle()
    except ValueError:
        print("error!, Your browser has been turned off ")

my_font=("fantasy",10,"bold")
label_time=tk.Label(tool,font=my_font, bg="#099D9D",fg="black")
label_time.grid(row=0,column=0,padx=5,pady=25)
name_dev = "By Clearlove7 Developer"
color_dev = ("black")
font_dev = ("fantasy",10,"bold")
l1 = Label(tool, text = name_dev, font = font_dev, fg = color_dev, bg="#099D9D")
l1.grid(row = 1, column = 0, sticky = W, pady = 1)
tick = Checkbutton(tool, text = "Accept", bg="#099D9D",width=5) 
tick.grid(row = 2, column = 0, sticky = W, columnspan = 2) 

    
img = PhotoImage(file = "anhyeuthao.png") 
my_image = Label(tool, image=img)
my_image.place(x=200, y=5,width=400 ,height=400)
b2 = Button(tool, text= "Login Google",bg="white",activebackground="#3399FF", width = 15, command=Object.Multiple)
b2.place(x=70,y=200)
Button_file = Button(text="open", command=openfile)
Button_file.place(x=10,y=200)

new_time()
tool.mainloop()
sys.exit("end tool") 















