from tkinter import *
import tkinter as tk 
from threading import *
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import pygame
pygame.init()
pygame.init()
video_name = "vippro77.mp4" #This is your video file path
video = imageio.get_reader(video_name)
def game():
        import game7
        pass
def multithreading_game():
    multithreading_game7=threading.Thread(target=game)
    multithreading_game7.start()
def play_sound():
    pygame.mixer.music.load("vippro76.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def multithreading_sound():
    multithreading_sound1=threading.Thread(target=play_sound)
    multithreading_sound1.start()
def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":
    tool = tk.Tk()
    tool.geometry("400x300")
    my_label = tk.Label(tool)
    my_label.pack(side=BOTTOM)
    thread = threading.Thread(target=stream, args=(my_label))
    thread.daemon = 1
    thread.start()
    #tool.configure(background="#099D9D") # set background
    button_sound = Button(tool,text="play sound",bg="white",width = 8, command=multithreading_sound)
    button_game = Button(tool,text="play game",bg="white",width = 8 , command=multithreading_game)
    button_sound.pack(side=BOTTOM)
    button_game.pack(side=TOP)  
    tool.mainloop()