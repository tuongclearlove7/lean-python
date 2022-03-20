from tkinter import*
from tkinter import messagebox
import pyscreeze
from threading import *
import pyautogui, pyperclip, random
from time import sleep

win = Tk()
win.title('Đòi Nợ')
win.geometry('475x230')
#win.resizable(False,False)

text_content = IntVar()
de_time = StringVar()
input_content = StringVar()
box_1 = Text(win, width=50, height=4, font=('arial',13))
box_1.place(x=10, y=77)
def multi():
    multithreading1=Thread(target=handle)
    multithreading1.start()
    
def handle():
    global content,i
    content = input_content.get()
    Delay = de_time.get()
    num = text_content.get()
    send_spam = box_1.get(1.0, END)
    if int(num) == 0: 
        messagebox.askokcancel('Cảnh báo', 'Số tin không được phép bằng 0')
    elif float(Delay)<0.02: 
        messagebox.askokcancel('Cảnh báo', 'Delay không được nhỏ hơn 0.2')
    elif str(send_spam) == '':
        messagebox.askokcancel('Cảnh báo', 'Chưa nhập nội dung, nếu nhiều câu thì các câu cách nhau bằng |')
    else:
        shutdown_text = send_spam.split('\n')
        for i in range(num+1):
            pyperclip.copy(random.choice(shutdown_text))
            pyautogui.hotkey("ctrl","v")
            print(num)
            en = "enter"
            pyautogui.press(en)
            print(en)
            sleep(float(Delay))

Label(win, text = 'number spam',fg = 'blue', font=('arial',12)).place(x= 20, y= 20)
Entry(win, width=15, textvariable= text_content, font=('arial',10)).place(x=135, y= 21)
Label(win, text = 'content',fg = 'blue' ,font=('arial',12)).place(x= 20, y= 50)
Label(win, text = 'Delay',fg = 'blue' ,font=('arial',12)).place(x=280, y= 20)
Entry(win, width=10, textvariable= de_time).place(x=340, y= 20)
Button(win, text = 'Thực hiện', fg = 'blue',bg = 'yellow', font=('arial',10), command=multi).place(x= 220, y =195)

win.mainloop()











