from time import sleep
import facebook as fb
from PIL import ImageTk,Image
from threading import *
from tkinter import *
import os
import tkinter as tk
#                                                  App_Me[0]
readMode = ['r+','a+','a','x','r','+','b','U','w','t']
file_key_global = open('Application.txt',mode=readMode[0],encoding="utf-8")
myset = {'set'}
data = file_key_global.read()
mydict = {'id':1604011220022001,'porn':2003,'address':'DaNang city',
          'developer':'© By Clearlove7','app':['. Access Token Application'],
          'num':5,'key':lambda:data,'mode':readMode}
print(mydict)
for lbl in mydict['app']:
    pass
App_Me = [False,True,None,0,1,readMode,myset,mydict]# start app 

class MyApp:
    def Api_Acess_Token():
        App = Tk()
        App.geometry("550x150")
        App.title("Tool API Post Status Facebook")
        App.iconbitmap("tuongclearlove7.ico")
        App.configure(background="#099D9D")
        token_var=tk.StringVar()
        content_var=tk.StringVar()

        def Run_API(My_access_token,My_msg):
            try:
                api = fb.GraphAPI(My_access_token)
                api.put_object('me','feed',message = My_msg)
                succes = [Label(App,text="Successfully✅",bg="green",font=('calibre',10, 'bold'),width=15).place(x=240,y=115),"Successfully"]
                print(succes[1])
            except:
                err = [Label(App,text="Error ❌",bg="red",font=('calibre',10, 'bold'),width=15).place(x=240,y=115),"Error"]
                print(err[1])

        def Handle_token():
            """token : """
            global get_token,get_content
            get_token=token_var.get()
            get_content=content_var.get()
            Run_API(get_token,get_content)
            str_token_content = str("token : "+get_token+"\n"+"content : "+get_content+"\n")
            print(str_token_content)
            write_token = open("token.txt",readMode[1],encoding="utf-8")
            H_data = write_token.write(str_token_content)
            write_token.close() 
            token_var.set('')
            content_var.set('')

        def multiple_threading():
            multi=Thread(target=Handle_token)
            multi.start()
                
        def F_Token(msg_token):
            file_token = open('token.txt',mode=readMode[0],encoding="utf-8")
            F_data = file_token.read()
            print(msg_token+F_data)
        F_Token("")

        Labeltoken = Label(App,text='nhập token',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=10)
        Labelcontent = Label(App,text='nhập nội dung',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=40)
        Label_dev= Label(App,text=mydict['developer'],fg='white',bg="#099D9D").place(x=0,y=130)
        Label_dev= Label(App,text=lbl,bg="#099D9D",fg='white').place(x=87,y=130)
        token = Entry(App,textvariable=token_var,width=70).place(x=100,y=10)
        content = Entry(App,textvariable=content_var,width=30).place(x=110,y=40)
        Button_started = Button(App,text="start",font=('calibre',10, 'bold'), command=multiple_threading)
        Button_started.place(x=280,y=80)

        App.mainloop()

def die():
    while App_Me[2]:
        Key = input("nhap pass : ")
        try:
            App_API = {data:[MyApp.Application]}
            for i in App_API[Key]:
                print("My Application "+str(i))
                print(App_API)
                print("key la "+data)
            MyApp.Api_Acess_Token()
            break
        except:
            print(False)
def pass_life():
    while App_Me[2]:
        try:
            Key = input("nhap pass : ")
            handle_key = {data: lambda:MyApp.Api_Acess_Token()}[Key]()
            break;
        except:
            print(False)
pass_life()







