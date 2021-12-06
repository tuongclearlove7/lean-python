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

x = 2


top = Tk()
top.geometry("200x100")
 
def clickRedButton():
    messagebox.showinfo("Hello", "Red Button clicked")
 
def clickBlueButton():
    messagebox.showinfo("Hello", "Blue Button clicked")
 
b1 = Button(top, text = "Red", command = clickRedButton, activeforeground = "red", activebackground = "pink", pady = 10)
b2 = Button(top, text = "Blue", command = clickBlueButton, activeforeground = "blue", activebackground = "pink", pady = 10)
b3 = Button(top, text = "Green", activeforeground = "green", activebackground = "pink", pady = 10)
b4 = Button(top, text = "Yellow", activeforeground = "yellow", activebackground = "pink", pady = 10)
b1.pack(side = LEFT)
b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)
top.mainloop()