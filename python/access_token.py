from time import sleep
import facebook as fb
from PIL import ImageTk,Image
from threading import *
from tkinter import *
import tkinter as tk

App = Tk()
App.geometry("550x150")
App.title("Tool API Post Stt Facebook")
App.iconbitmap("tuongclearlove7.ico")
App.configure(background="#099D9D")
token_var=tk.StringVar()
content_var=tk.StringVar()

def F_Token(token):
    file_token = open('token.txt')
    data = file_token.read()
    print(token+data)
F_Token("token : ")

def Post_status(My_access_token,My_msg):
    try:
        api = fb.GraphAPI(My_access_token)
        api.put_object('me','feed',message = My_msg)
        succes = [Label(App,text="Successfully✅",bg="green",font=('calibre',10, 'bold')).place(x=250,y=115),"successfully"]
        print(succes[1])
    except:
        err = [Label(App,text="Error ❌",bg="red",font=('calibre',10, 'bold')).place(x=270,y=115),"error"]
        print(err[1])

def Run_API():
    """token : EAASCDwYEjcUBAD4mQNo2lMdUvBq4Q66PmVZAgahrD4LEv3xZCYTF46qbAMc6WkefCSagXyBPZBbXZBmyoJNspQGSlyEUEdw3uA
    c3IWNMx1fTmXbvAg5gPPuOa4TTT15OqUUA0pQkBZALSqWvsZBAY2d4fh7BEomck2NXe8HgcQXo3F6jZBZC1ZBUzmrrNZCSxPzBIrygX5HnsANgZDZD"""
    get_token=token_var.get()
    get_content=content_var.get()
    Post_status(get_token,get_content)
    # token_var.set('')
    # content_var.set('')
 
def multiple_threading():
    multithreading2=Thread(target=Run_API)
    multithreading2.start()

inputtoken = Label(App,text='nhập token',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=10)
token = Entry(App,textvariable=token_var,width=70).place(x=100,y=10)
imputcontent = Label(App,text='nhập nội dung',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=40)
content = Entry(App,textvariable=content_var,width=30).place(x=110,y=40)
Button_started = Button(App,text="start",font=('calibre',10, 'bold'), command=multiple_threading)
Button_started.place(x=280,y=80)

App.mainloop()















