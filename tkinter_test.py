from os import pipe
import tkinter
from time import sleep
from tkinter import *
from tkinter import messagebox
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys
import pyttsx3
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color
bot = pyttsx3.init() 
voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)

tool = Tk()
tool.geometry("520x220")# set screen
# this will create a label widget
tool.iconbitmap('clearlove7.ico') # set icon
tool.title("My Software")# set title
tool.configure(background='grey') # set background
# grid method to arrange labels in respective
# rows and columns as specified
def on_youtube():
    bot.say("turn on youtube")# bot said 
    if bot.runAndWait() == print(Fore.RED + "", file=stream):# print text color
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        tuong.set_window_size(750,700)
    tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")
def on_facebook():
    bot.say("turn on facebook")# bot said 
    if bot.runAndWait() == print(Fore.BLUE + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        tuong.get("https://www.facebook.com/watch?ref=search&v=792650660907793&external_log_id=b7e2e990-7dad-4077-838f-782ad81c1c58&q=skt%20vs%20edg%20lol%20esport")
def on_google_translate():
    bot.say("turn on google translate")# bot said 
    if bot.runAndWait() == print(Fore.WHITE + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l2j0i433i512j0i131i433i512l2j69i60.2320j0j7&sourceid=chrome&ie=UTF-8")
def on_github():
    bot.say("turn on github")# bot said 
    if bot.runAndWait() == print(Fore.MAGENTA + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    if tuong.get("https://github.com/") == sleep(3):
        tuong.get("https://github.com/login")
    elif sleep(1):
        print("đăng nhập")
    if tuong.find_element_by_id("login_field").send_keys("tuongclearlove7"
    ) == tuong.find_element_by_id("password").send_keys("tuongyeuthao1"):
        tuong.find_element_by_name("commit").click()
    tuong.execute_script("window.scroll(0,900)")
    sleep(3)
    tuong.get("https://github.com/tuongclearlove7")


l1 = Label(tool, text = "Name", bg="gray")
l2 = Label(tool, text = "send", bg="gray")
  
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
# entry widgets, used to take entry from user
e1 = Entry(tool)
e2 = Entry(tool)
# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
# checkbutton widget
c1 = Checkbutton(tool, text = "Preserve", bg="gray",width=5)
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)
# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = "clearlove7.png")
img1 = img.subsample(2, 3)
# setting image with the help of label
Label(tool, image = img1).grid(row = 0, column = 2,
columnspan = 2, rowspan = 2, padx = 5, pady = 5)
# button widget
b1 = Button(tool, text= "youtube", bg="red", width = 7, command =on_youtube)
b2 = Button(tool, text= "facebook",bg="blue", width = 10, command=on_facebook)
b3 = Button(tool, text = "google translate", bg="white", width = 13, command=on_google_translate )
b4 = Button(tool, text = "github", bg="#663399", width = 10, command=on_github)
# arranging button widgets
b1.grid(row = 2, column = 1)
b2.grid(row = 2, column = 2)
b3.grid(row = 2, column = 3)
b4.grid(row = 2, column = 4)
# infinite loop which can be terminated 
# by keyboard or mouse interrupt
tool.mainloop()



