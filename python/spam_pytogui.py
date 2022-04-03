from tkinter import*
from tkinter import messagebox
from threading import *
import pyautogui, pyperclip, random
from time import sleep

win = Tk()
win.title('Spam')
win.geometry('630x250')
win.configure(background="#099D9D") # set background
win.iconbitmap("tuongclearlove7.ico")
img = PhotoImage(file = "tuongclearlove7.png")# set image (thiết lập ảnh)
img1 = img.subsample(7,8)

text_content = IntVar()
de_time = IntVar()
input_content = StringVar()
box_1 = Text(win, width=50, height=5, font=('arial',13))
box_1.place(x=10, y=77) 

class Multithreading():
    def Multi(args):
        args.multithreading1=Thread(target=Handle)
        args.multithreading1.start()
Obj = Multithreading()

def Handle():
    global content
    content = input_content.get()
    Delay = de_time.get()
    num = text_content.get()
    send_spam = box_1.get(1.0,END)
    shutdown_text = send_spam.split('\n')
    for index in range(10,0,-1):# countdown 10s
        print(index, end=" countdown... ",flush=True)
        sleep(1)
    print("start")
    for i in range(num+1):
            pyperclip.copy(random.choice(shutdown_text))
            pyautogui.hotkey("ctrl","v")
            print(i)
            en = "enter"
            pyautogui.press(en)
            print(en)
            sleep(float(Delay))

Label(win, image = img1).place(x=538,y=5)
Label(win, text = 'number spam',fg = 'black', bg="#099D9D", font=('arial',12)).place(x= 7, y= 20)
Entry(win, width=15, textvariable= text_content, font=('arial',12)).place(x=135, y= 20)
Label(win, text = 'content',fg = 'black',bg="#099D9D" ,font=('arial',12)).place(x= 20, y= 45)
Label(win, text = 'Delay',fg = 'black', bg="#099D9D", font=('arial',12)).place(x=280, y= 20)
Entry(win, width=10, textvariable= de_time ,font=("arial",12)).place(x=350, y= 20)
Button(win, text = 'Thực hiện', fg = 'black',bg = 'silver', font=('arial',10), command=Obj.Multi).place(x= 260, y =210)

win.mainloop()