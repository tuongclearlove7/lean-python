from os import pipe
import threading
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
import pygame

#class main():
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color
pygame.init()
bot = pyttsx3.init()
voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)

tool = Tk()
tool.geometry("560x220")# set screen (thiết lập khung tool)
# this will create a label widget (tạo tiện ích label : nhãn)
tool.iconbitmap('clearlove7.ico') # set icon
tool.title("My Software")# set title
tool.configure(background="#099D9D") # set background
# grid method to arrange labels in respective (phương pháp lưới để sắp xếp các nhãn)
# rows and columns as specified  (tương ứng hàng và cột như đã chỉ định)

class Class_multithreading: # class multithreading (lớp đa luồng)
    def __init__(self):
            super().__init__()
            print(self,super)
    def multithreading_youtube(self):
        self.multithreading1=Thread(target=on_youtube)
        self.multithreading1.start()
    def multithreading_facebook(self):
        self.multithreading2=Thread(target=on_facebook)
        self.multithreading2.start()
    def multithreading_google_translate(self):
        self.multithreading3=Thread(target=on_google_translate)
        self.multithreading3.start()
    def multithreading_github(self):
        self.multithreading4=Thread(target=on_github)
        self.multithreading4.start()
    def multithreading_sound(self):
        self.multithreading_S=Thread(target=play_sound)
        self.multithreading_S.start() #multi()
object = Class_multithreading()
print(type(object))

#setting sound and time in tool (thiết lập thời gian trong tool) 
def multithreading_game():
    multithreading_game7=Thread(target=play_game)
    multithreading_game7.start()
def play_game():
    import game7
    pass
def play_sound():
    pygame.mixer.music.load("tuong.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def new_time():
    time_string = strftime("Time : %H:%M:%S %p") # time format (định dạng thời gian)
    #print(time_string)
    label_time.config(text = time_string)
    label_time.after(1000, new_time) # time delay of 1000 milliseconds (thời gian dừng khoảng 1000 mili giây)
def on_youtube():
    bot.say("turn on youtube")# bot said 
    if bot.runAndWait() == print(Fore.RED + "", file=stream):# print text color (in chữ màu)
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        #print("tool running please wait !\n"*1000)
        tuong.set_window_size(750,700) == tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")
def on_facebook():
    bot.say("turn on facebook")
    if bot.runAndWait() == print(Fore.BLUE + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        tuong.get("https://www.facebook.com/watch?ref=search&v=792650660907793&external_log_id=b7e2e990-7dad-4077-838f-782ad81tickc58&q=skt%20vs%20edg%20lol%20esport")
def on_google_translate():
    bot.say("turn on google translate")
    if bot.runAndWait() == print(Fore.WHITE + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
        tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l2j0i433i512j0i131i433i512l2j69i60.2320j0j7&sourceid=chrome&ie=UTF-8")
    if sleep(2) == print("text translate"):
        file_object = open('clearlove7_developer_tool.txt')
        data_text = file_object.read()
        tuong.find_element_by_id("tw-source-text-ta").send_keys(data_text)
        tuong.execute_script("window.scroll(0,240)")
def on_github():
    bot.say("turn on github")
    if bot.runAndWait() == print(Fore.MAGENTA + "", file=stream):
        tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    if tuong.get("https://github.com/") == sleep(3) == print("go to github"):
        tuong.get("https://github.com/login")
    if tuong.find_element_by_id("login_field").send_keys("tuongclearlove7"
    ) == tuong.find_element_by_id("password").send_keys("tuongyeuthao1"):
        tuong.find_element_by_name("commit").click()
        tuong.execute_script("window.scroll(0,900)")
    if sleep(3)== print("coming profile"):
        tuong.get("https://github.com/tuongclearlove7")

    #setting time and my name (thiết lập thời gian và tên của tôi)
    # I will become a Software Developer (tôi sẽ trở thành một nhà phát triển phần mềm trong tương lai)
my_font=('fantasy',10,'bold')
label_time=tk.Label(tool,font=my_font, bg="#099D9D",fg="black")
label_time.grid(row=0,column=0,padx=5,pady=25)
name_dev = "By Clearlove7 Developer"
color_dev = ("black")
font_dev = ("fantasy",10,"bold")
l1 = Label(tool, text = name_dev, font = font_dev, fg = color_dev, bg="#099D9D")
l1.grid(row = 1, column = 0, sticky = W, pady = 1)
# grid method to arrange labels in respective ( phương pháp lưới để sắp xếp các nhãn tương ứng)
# rows and columns as specified (hàng và cột như đã chỉ định)

tick = Checkbutton(tool, text = "Accept", bg="#099D9D",width=5)# set tick (thiết lập ô tick)
tick.grid(row = 2, column = 0, sticky = W, columnspan = 2)#position tick and pressed the tick (vị trí tick và bấm vào tick)

# adding image (remember image should be PNG and not JPG) (thêm ảnh hãy nhớ hình ảnh phải là PNG chứ không phải JPG )
img = PhotoImage(file = "clearlove7.png")# set image (thiết lập ảnh)
img1 = img.subsample(2, 3)
# setting image with the help of label (thiết lập ảnh đc trợ giúp bởi label : nhãn)
Label(tool, image = img1).grid(row = 0, column = 2, 
columnspan = 2, rowspan = 2, padx = 5, pady = 5)
# button widget (tiện ích nút)
click_bg_button_Y = "#FF6666" # click button color
click_bg_button_F = "#3399FF"
click_bg_button_GG = "silver"
click_bg_button_Git = "#CC3399"
b1 = Button(tool, text= "Youtube", bg="red", activebackground=click_bg_button_Y, width = 7, command =object.multithreading_youtube)# set button (thiết lập nút
b2 = Button(tool, text= "Facebook",bg="blue",activebackground=click_bg_button_F, width = 7, command=object.multithreading_facebook)
b3 = Button(tool, text = "Google translate",bg="white",activebackground=click_bg_button_GG, width = 13, command=object.multithreading_google_translate)
b4 = Button(tool, text = "Github", bg="#663399",activebackground=click_bg_button_Git ,width = 7, command=object.multithreading_github)
button_sound = Button(tool,text="introduce",bg="#006699",activebackground="#99CCFF",command=object.multithreading_sound)
button_game = Button(tool,text="play game",bg="#FF6600",activebackground="#99CCFF",width = 8 ,command=multithreading_game)

b1.grid(row = 2, column = 1)#potision button(vị trí nút)
b2.grid(row = 2, column = 2)
b3.grid(row = 2, column = 3)
b4.grid(row = 2, column = 4)
button_sound.grid(row=1, column=1)
button_game.grid(row=1,column=1, sticky=S)
 # infinite loop which can be terminated (mainloop) (vòng lặp vô hạn có thể được kết thúc bởi mainloop())
 # the tool will by keyboard or mouse interrupt(tool sẽ bị ngắt bằng bàn phím điều khiển hoặc chuột)
new_time()
tool.mainloop()
#import hack_log
sys.exit("end tool")


