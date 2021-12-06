#import os
#os.system("run2.bat")
#a = 1 
#while True:
 #   a+=1
  #  print(a)
#key = 'tuong'
#print({
#'tuong': lambda: 'Clearlove7'} [key]())
#key = "youtube"
#print({'facebook': lambda: 'Intagram',
#'youtube': lambda: 'zalo'}[key]())
from tkinter import *
import tkinter as tk 
from threading import *
import tkinter as tk, threading
from colorama.ansi import BEL
import imageio
from PIL import Image, ImageTk
import pygame
pygame.init()


tool = Tk()
tool.geometry("560x220")# set screen (thiết lập khung tool)
# this will create a label widget (tạo tiện ích label : nhãn)
tool.iconbitmap('clearlove7.ico') # set icon
tool.title("My Software")# set title
tool.configure(background="#099D9D") # set background
def game():
    import game7
    pass
def multithreading_game():
    multithreading_game7=Thread(target=game)
    multithreading_game7.start()
def play_sound():
    pygame.mixer.music.load("vippro76.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def multithreading_sound():
    multithreading_sound1=Thread(target=play_sound)
    multithreading_sound1.start()

button_sound = Button(tool,text="play sound",bg="white",width = 8, command=multithreading_sound)
button_game = Button(tool,text="play game",bg="white",width = 8 , command=multithreading_game)
button_sound.pack(side=BOTTOM)
button_game.pack(side=TOP)
tool.mainloop()





