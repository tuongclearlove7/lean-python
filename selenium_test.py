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
bot = pyttsx3.init() 
voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)

tool = Tk()
tool.geometry("350x300")# set screen
tool.title("My Software")# set title
tool.iconbitmap('application.ico') # set icon
#tool.configure(background="pink")
img = PhotoImage(file = "tool3.png")

def on_youtube():
    bot.say("turn on youtube")# bot said 
    bot.runAndWait()
    print(Fore.RED + "", file=stream)# print text color
    tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    tuong.set_window_size(750,700)
    tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")
def on_facebook():
    bot.say("turn on facebook")# bot said 
    bot.runAndWait()
    print(Fore.BLUE + "", file=stream)
    tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    tuong.get("https://www.facebook.com/watch?ref=search&v=792650660907793&external_log_id=b7e2e990-7dad-4077-838f-782ad81c1c58&q=skt%20vs%20edg%20lol%20esport")
def on_google_translate():
    bot.say("turn on google translate")# bot said 
    bot.runAndWait()
    print(Fore.WHITE + "", file=stream)
    tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l2j0i433i512j0i131i433i512l2j69i60.2320j0j7&sourceid=chrome&ie=UTF-8")
def on_github():
    bot.say("turn on github")# bot said 
    bot.runAndWait()
    print(Fore.MAGENTA + "", file=stream)
    tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    tuong.get("https://github.com/")
    sleep(3)
    tuong.get("https://github.com/login")
    sleep(1)
    if tuong.find_element_by_id("login_field").send_keys("tuongclearlove7"
    ) == tuong.find_element_by_id("password").send_keys("tuongyeuthao1"):
        print("đã nhập mật khẩu")
    tuong.find_element_by_name("commit").click()
    tuong.execute_script("window.scroll(0,900)")
    sleep(3)
    tuong.get("https://github.com/tuongclearlove7")

b1 = Button(tool, text = "Bật youtube", command = on_youtube,background="red"
, activeforeground = "black", activebackground = "firebrick1",font=("consolas",10,"bold"), width = 10)
b2 = Button(tool, text = "Bật facebook", command = on_facebook,background="blue"
, activeforeground = "black", activebackground = "dodgerblue3",font=("consolas",10,"bold"), width = 10)
b3 = Button(tool, text = "bật google dịch", command = on_google_translate, background="white"
, activeforeground = "black", activebackground = "whitesmoke", font=("consolas",10,"bold"),width = 15)
b4 = Button(tool, text = "bật github",command = on_github,background = "blueviolet"
, activeforeground = "black", activebackground = "mediumpurple1",font=("consolas",10,"bold"), width = 10)
label = Label(tool, text="Welcome to my Software", font=("Helvetica", 15), bg="silver", width=200)
label.pack(side = TOP)
b1.pack(side = RIGHT)
b2.pack(side = RIGHT)
b3.pack(side = RIGHT)
b4.pack(side = RIGHT)
tool.update()
tool.mainloop()
sys.exit()











