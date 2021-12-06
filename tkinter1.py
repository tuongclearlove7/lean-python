
from os import pipe
from time import sleep
from tkinter import *
from tkinter import messagebox
from colorama.ansi import BEL
from selenium import webdriver

tool = Tk()
tool.geometry("350x300")
tool.title("My Software")
tool.iconbitmap('application.ico')
#tool.configure(background="pink")
background = PhotoImage( file = "tool3.png")
# Show image using label
label_1 = Label( tool, image = background)
label_1.place(x = 0,y = 0)
def on_youtube():
    tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
    tuong.set_window_size(750,700)
    tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")


b1 = Button(tool, text = "Bật youtube", command = on_youtube,background="red"
, activeforeground = "black", activebackground = "firebrick1", width = 10)
label = Label(tool, text="Welcome to my Software", font=("Helvetica", 20))
label.pack(side = TOP)
b1.pack(side = TOP)
tool.update()
tool.mainloop()












