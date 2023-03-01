from time import sleep
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color
with open('happy.txt',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
for line in R_data:
    print(line.strip())
    sleep(0.001)











