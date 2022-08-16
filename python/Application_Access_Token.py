from time import sleep
import facebook as fb
from PIL import ImageTk,Image
from threading import *
from tkinter import *
import os
import tkinter as tk

readMode = ['r+','a+','a','x','r','+','b','U','w','t']
class MyApp:
    def app1():
        class App_Post:
            def Application():
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
                    write_token = open("token.txt",readMode[2],encoding="utf-8")
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
                TOKEN = Entry(App,textvariable=token_var,width=70).place(x=100,y=10)
                Labelcontent = Label(App,text='nhập nội dung',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=40)
                CONTENT = Entry(App,textvariable=content_var,width=30).place(x=110,y=40)
                Button_started = Button(App,text="start",font=('calibre',10, 'bold'), command=multiple_threading)
                Button_started.place(x=280,y=80)

                App.mainloop()
        while True:
            Key = input("nhap key : ")
            try:
                file_key = open('Application.txt',mode=readMode[0],encoding="utf-8")
                data = file_key.read()
                App_API = {data:[App_Post.Application]}
                for i in App_API[Key]:
                    print("My Application "+str(i))
                    print(App_API)
                    print("key la "+data)
                    if __name__ == "__main__":
                        App_Post.Application()
                break
            except:
                print(False)
# MyApp.app1()

mydict = {'id':1,'porn':2003,'address':'DaNang city',
          'developer':'Clearlove7','app':[MyApp],
          'family':['father','mother','sister','me'],
          'num':4}
print(mydict['family'])
for key in mydict['family']:
    print('value : '+key)
print(mydict)







