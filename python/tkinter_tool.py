from array import array
from email import charset, message
from os import pipe
from re import T
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
import base64
import pygame

def passkey():
    while True:
        while True:
                password = input("nhap pass : ")
                my_password = "tuongyeuthao1"
                key_encode = my_password.encode('ascii')
                byte64 = base64.b64encode(key_encode)
                log_decode = byte64.decode('ascii')
                if password == log_decode:
                    print("log decode :  ",log_decode)
                    print("you were inputing correct password ")
                    Mytool()
                elif password != log_decode:
                    print("you were inputing wrong password")
                    print("please! re-enter ")
                    break
def Mytool():
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream # text color
    pygame.init()
    bot = pyttsx3.init()
    voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
    bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)
    tool = Tk()
    tool.geometry("560x220")# set screen (thiết lập khung tool)
    # this will create a label widget (tạo tiện ích label : nhãn)
    tool.iconbitmap('tuongclearlove7.ico') # set icon
    tool.title("My Software")# set title
    tool.configure(background="#099D9D") # set background

    # grid method to arrange labels in respective (phương pháp lưới để sắp xếp các nhãn)
    # rows and columns as specified  (tương ứng hàng và cột như đã chỉ định)
    class Class_multithreading: # class multithreading (lớp đa luồng)
        def __init__(self):
                super().__init__()
                print(self,super)
        def multithreading_youtube(self):
            self.multithreading1=Thread(target=on_youtube)
            self.multithreading1.start()
        def multithreading_facebook(self):
            self.multithreading2=Thread(target=on_tool)
            self.multithreading2.start()
        def multithreading_google_translate(self):
            self.multithreading3=Thread(target=on_google_translate)
            self.multithreading3.start()
        def multithreading_github(self):
            self.multithreading4=Thread(target=on_github)
            self.multithreading4.start()
        def multithreading_sound(self):
            self.multithreading_S=Thread(target=play_sound)
            self.multithreading_S.start()
        def multithreading_game(self):
            self.multithreading_game7=Thread(target=play_game)
            self.multithreading_game7.start()
    object = Class_multithreading()
    #setting sound and time in tool (thiết lập thời gian trong tool) 
    class myGame():
        def gamecl():
                import pygame
                pygame.init()

                text_color = (255,255,255)
                Width = 500
                Height = 500
                background_1 = 0
                background_2 = 0
                character_1 = 400
                character_2 = 200
                player_1 = 0 # vị trí character
                player_2 = 0
                size_character_1 = 100
                size_character_2 = 100
                FPS = 1000000


                screen = pygame.display.set_mode((Width, Height))
                fpsClock  = pygame.time.Clock()
                icon = pygame.image.load("tuongclearlove7.jpg")
                background = pygame.image.load("tuongclearlove7.png")
                font = pygame.font.SysFont('javanesetext', 30)
                font2 = pygame.font.SysFont('javanesetext',30)

                pygame.display.set_caption("game")
                character_image = pygame.image.load("dude.gif")
                character_image = pygame.transform.scale(character_image,(size_character_1, size_character_2))

                def character(x, y): # tạo hàm character để thêm nhân vật vào game 
                    screen.blit(character_image, (x, y)) # được truyền vào biến x, y

                tuong = True

                while tuong: # vòng lặp 
                    
                    screen.blit(background, (background_1,background_2))
                    text = font.render('Hello world',True , text_color)

                    pygame.display.set_icon(icon)
                    screen.blit(text,(180,-10))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            tuong = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player_1 = -1
                                print('left')
                                # tốc độ bắt đầu đi sang trái của nhân vật
                            if event.key == pygame.K_RIGHT:
                                player_1 = 1
                                print("right")
                                # tốc độ bắt đầu đi sang phải của nhân vật
                            if event.key == pygame.K_UP:
                                player_2 = -1
                                print("up")
                            # tốc độ bắt đầu đi lên của nhân vật
                            if event.key == pygame.K_DOWN:
                                player_2 = 1
                                print("down")
                            # tốc độ bắt đầu đi xuống của nhân vật
                            

                        if event.type == pygame.KEYUP: # xác định vị trí muốn dừng của tên lửa
                            if event.key == pygame.K_LEFT:
                                player_1 = 0
                            if event.key == pygame.K_RIGHT:
                                player_1 = 0
                            if event.key == pygame.K_DOWN:
                                player_2 = 0
                            if event.key == pygame.K_UP:
                                player_2 = 0
                            

                    character_1 += player_1
                    if character_1 <= -12:
                        character_1 = -12
                #vị trí lề trái game mà nhân vật đi tới và đứng lại
                    elif character_1 >= 840:
                        character_1 = 840
                #vị trí lề phải game mà nhân vật đi tới và đứng lại

                    character_2 += player_2
                    if character_2 <= -15:
                        character_2 = -15
                #vị trí lề trên game mà nhân vật đi tới và đứng lại
                    elif character_2 >= 415:
                        character_2 = 415
                #vị trí lề dưới game mà nhân vật đi tới và đứng lại

                    character(character_1, character_2)# cho nhân vật vô game
                    print(character_1,character_2)
                    fpsClock.tick(FPS)
                    pygame.display.update()
                    break
                    
    def play_game():    
        number = int(input("loop game : "))
        global a
        a = myGame.gamecl()    
        for a in range(number):
            myGame.gamecl()
            break
    def play_sound():
        pygame.mixer.music.load("vippro76.mp3") #Loading File Into Mixer
        pygame.mixer.music.play() #Playing It In The Whole Device
    def new_time():
        time_string = strftime("Time : %H:%M:%S %p") # time format (định dạng thời gian)
        label_time.config(text = time_string)
        label_time.after(1000, new_time) # time delay of 1000 milliseconds (thời gian dừng khoảng 1000 mili giây)
    def on_google_translate():
        tuong = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
        tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l2j0i433i512j0i131i433i512l2j69i60.2320j0j7&sourceid=chrome&ie=UTF-8")
        tuong.find_element_by_id("tw-source-text-ta").send_keys("hello world")
        tuong.execute_script("window.scroll(0,240)")

    class tool_face:
        def handle():
            global time
            global loop
            global tuong
            try:
                loop = int(input("input integer create account : "))
                time  = int(input("input integer time each time off : "))
                for tuong in range(loop):
                    val = int(loop)
                    print("number of loop : ")
                    print(val)
                    bot.say("create account")
                    bot.runAndWait()
                    tool_face.web1()
            except ValueError:
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
        while True:
            tool_face.handle()
            break
    #setting time and my name (thiết lập thời gian và tên của tôi)
    # I will become a Software Developer (tôi sẽ trở thành một nhà phát triển phần mềm trong tương lai)
    my_font=('fantasy',10,'bold')
    label_time=tk.Label(tool,font=my_font, bg="#099D9D",fg="black")
    label_time.grid(row=0,column=0,padx=5,pady=25)
    name_dev = "By Clearlove7 Developer"
    color_dev = ("black")
    font_dev = ("fantasy",10,"bold")
    l1 = Label(tool, text = name_dev, font = font_dev, fg = color_dev, bg="#099D9D")
    l1.grid(row = 1, column = 0, sticky = W, pady = 1)
    # grid method to arrange labels in respective ( phương pháp lưới để sắp xếp các nhãn tương ứng)
    # rows and columns as specified (hàng và cột như đã chỉ định)
    tick = Checkbutton(tool, text = "Accept", bg="#099D9D",width=5)# set tick (thiết lập ô tick)
    tick.grid(row = 2, column = 0, sticky = W, columnspan = 2)#position tick and pressed the tick (vị trí tick và bấm vào tick)
    # adding image (remember image should be PNG and not JPG) (thêm ảnh hãy nhớ hình ảnh phải là PNG chứ không phải JPG )
    img = PhotoImage(file = "tuongclearlove7.png")# set image (thiết lập ảnh)
    img1 = img.subsample(2, 3)
    # setting image with the help of label (thiết lập ảnh đc trợ giúp bởi label : nhãn)
    Label(tool, image = img1).grid(row = 0, column = 2, 
    columnspan = 2, rowspan = 2, padx = 5, pady = 5)
    # button widget (tiện ích nút)
    click_bg_button_Y = "#FF6666" # click button color
    click_bg_button_F = "#3399FF"
    click_bg_button_GG = "silver"
    click_bg_button_Git = "#CC3399"
    b1 = Button(tool, text= "Youtube", bg="red", activebackground=click_bg_button_Y, width = 7, command =object.multithreading_youtube)# set button (thiết lập nút
    b2 = Button(tool, text= "Facebook",bg="blue",activebackground=click_bg_button_F, width = 7, command=object.multithreading_facebook)
    b3 = Button(tool, text = "Google translate",bg="white",activebackground=click_bg_button_GG, width = 13, command=object.multithreading_google_translate)
    b4 = Button(tool, text = "Github", bg="#663399",activebackground=click_bg_button_Git ,width = 7, command=object.multithreading_github)
    button_sound = Button(tool,text="introduce",bg="#006699",activebackground="#99CCFF",command=object.multithreading_sound)
    button_game = Button(tool,text="play game",bg="#3366CC",activebackground="#99CCFF",width = 8 ,command=object.multithreading_game)
    b1.grid(row = 2, column = 1)#potision button(vị trí nút)
    b2.grid(row = 2, column = 2)
    b3.grid(row = 2, column = 3)
    b4.grid(row = 2, column = 4)
    button_sound.grid(row=1, column=1)
    button_game.grid(row=1,column=4)
    # infinite loop which can be terminated (mainloop) (vòng lặp vô hạn có thể được kết thúc bởi mainloop())
    # the tool will by keyboard or mouse interrupt(tool sẽ bị ngắt bằng bàn phím điều khiển hoặc chuột)
    new_time()
    tool.mainloop()
    sys.exit("end tool") 
passkey()





















