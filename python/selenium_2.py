from time import sleep
from selenium import webdriver
from threading import *
import pyttsx3
from tkinter import *

tool = Tk()
tool.geometry("560x220")# set screen (thiết lập khung tool)

bot = pyttsx3.init()
voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)\


class tool_face:
    def handle():
        global tuong
        global time
        #loop = int(input("input integer create account : "))
        try:
            loop = int(input("input integer create account : "))
            time  = int(input("input integer time each time off : "))   
            for tuong in range(loop):
                bot.say("create account")
                bot.say(tuong)
                bot.runAndWait()
                print(tuong)
                tool_face.web1()
        except:
            bot_said = "you were inputing wrong format "
            print(bot_said)
            bot.say(bot_said)
            bot.runAndWait()  
        
    def web1():
        #num = int(input("input integer create account : "))
        #time  = int(input("input integer time each time off : "))
        while True:
            tuong = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
            tuong.set_window_size(1000,1000)
            tuong.get("https://www.facebook.com/campaign/landing.php?campaign_id=1661697991&extra_1=s%7Cc%7C432702091386%7Cb%7C%C4%91%C4%83ng%20ky%CC%81%20facebook%7C&placement=&creative=432702091386&keyword=%C4%91%C4%83ng%20ky%CC%81%20facebook&partner_id=googlesem&extra_2=campaignid%3D1661697991%26adgroupid%3D65157403438%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-369935470948%26loc_physical_ms%3D9047170%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMInK-f1ouz9gIV0m4qCh3s3Q27EAAYASAAEgLRovD_BwE") 
            tuong.find_element_by_name("lastname").send_keys(" trần")
            tuong.find_element_by_name("firstname").send_keys("tường")
            tuong.find_element_by_name("reg_email__").send_keys("thetuongyt@gmail.com")
            sleep(2)
            tuong.find_element_by_name("reg_email_confirmation__").send_keys("thetuongyt@gmail.com")
            tuong.find_element_by_id("password_step_input").send_keys("tuongyeuthao")
            tuong.find_element_by_name("birthday_day").click()
            tuong.find_element_by_name("birthday_month").click()
            tuong.find_element_by_name("birthday_year").click()
            tuong.find_element_by_name("sex").click()
            sleep(2)
            tuong.find_element_by_name("websubmit").click()
            tuong.find_element_by_name("websubmit").click()
            tuong.find_element_by_name("birthday_age").send_keys("22")
            tuong.find_element_by_name("websubmit").click()
            if sleep(time) == bot.say("exit"):
                bot.runAndWait()
            break

def on_tool():
    global b
    while True:
        print("loop")
        tool_face.handle()
        break

class class_multithreading: # class multithreading (lớp đa luồng)
    def __init__(self):
            super().__init__()
            print(self,super)
    def multithreading_tool(self):
        self.multi1=Thread(target=on_tool)
        self.multi1.start()
obj = class_multithreading()

b = Button(tool, text = 'Click me !', bd = '5',command =obj.multithreading_tool)
 
# Set the position of button on the top of window.  
b.pack(side = 'top')
tool.mainloop()






















