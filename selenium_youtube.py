from time import sleep
from selenium import webdriver
import sys
from colorama import Fore
from colorama import init, AnsiToWin32
import pyttsx3
bot = pyttsx3.init()  
voices = bot.getProperty('voices') #nhận thông tin về giọng
bot.setProperty('voice', voices[1].id)  # giọng nữ id là 1
bot_said = "press enter to control over me"
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
turn_on = input(max(["""
                  ┌──────────────────────────┐
                  │ Bấm enter để bật con bot │
                  └──────────────────────────┘
"""], default=True))
bot.say("bot runing")
bot.runAndWait()
print(Fore.RED + '{:^65}'.format("Hello Clearlove7 !"), file=stream)
print(Fore.GREEN + "", file=stream)
bot.say(" hello Clearlove7")
bot.runAndWait()
bot_turn_on = '{:^60}'.format("""
    ┌───────────────────────────────────────────────────────────┐
    │Cháu bật lên rồi ạ, ông chủ bấm enter ra lệnh cho cháu đi ạ│
    └───────────────────────────────────────────────────────────┘
""")
for c in bot_turn_on:
    print(c ,end="", flush=True)
    sleep(0.01)
print(Fore.GREEN + "", file=stream)
bot.say(bot_said)
bot.runAndWait()
def start_on(on_youtube, on_bot = turn_on):
    print(on_bot)
    sleep(2)
    print(on_youtube)
input("")
bot.say("turn on youtube")
bot.runAndWait()
print(Fore.RED + "", file=stream)
start_on("""
                          ┌─────────────┐
                          │ Bật Youtube │
                          └─────────────┘""")
sleep(1)
def end_bot(exit="""          
                                   ┌─────┐
                                   │ Tắt │
                                   └─────┘"""):
    print(exit)
print(Fore.BLUE + "", file=stream)
def start_git(on_github="""
                              ┌────────────┐
                              │ Bật Github │
                              └────────────┘"""):
    print(on_github)
def login_git(login):
    print(login)
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(750,700)
tuong.get("https://www.youtube.com/watch?v=BPUPMJ0nYO0")
sleep(3)
bot.say(bot_said)
bot.runAndWait()
input("""\n 
               ┌───────────────────────────────────────┐
               │ông chủ bấm enter ra lệnh cho cháu đi ạ│
               └───────────────────────────────────────┘\n""")
bot.say("turn on Facebook")
bot.runAndWait()
print("""\n
                           ┌────────────┐
                           │bật facebook│
                           └────────────┘\n""")
tuong.get("https://www.facebook.com/watch?ref=search&v=792650660907793&external_log_id=b7e2e990-7dad-4077-838f-782ad81c1c58&q=skt%20vs%20edg%20lol%20esport")
tuong.execute_script("window.scroll(100,0)")
bot.say(bot_said)
bot.runAndWait()
print(Fore.WHITE + "", file=stream)
input('''\n
                 ┌───────────────────────────────────────┐
                 │ông chủ bấm enter ra lệnh cho cháu đi ạ│
                 └───────────────────────────────────────┘\n''')
start_on("""\n
                           ┌───────────────┐
                           │Bật google dịch│
                           └───────────────┘\n""")
bot.say("turn on google translate")
bot.runAndWait()
tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l2j0i433i512j0i131i433i512l2j69i60.2320j0j7&sourceid=chrome&ie=UTF-8")
tuong.find_element_by_id("tw-source-text-ta").send_keys("""Machines, robots, and androids, 
are not a recent invention: artificial life forms have kindled the imagination of mankind for centuries. 
We already know concepts of robots from earlier times like Greek mythology and literature of past centuries.
Pandora was formed out of clay by Hephaestus; Olimpia is the robot woman whom the protagonist in ETA Hoffmann's "Sandman" falls in love with, and Hadaly was the first fictional artificial life form which was called "Android". 
Meanwhile, several decades (and in some cases even centuries) ago, robots made the leap from fantasy to reality.
In our analysis of the naming of robots though, we do not distinguish between real and fictional machines, 
automata and artificial intelligences. 
We deal with all kinds of names for artificial life forms: robots, machines, and automata, whether they exist, have existed, or whether they are sprung from the realm of legend or the imagination of science fiction writers.
""")
tuong.execute_script("window.scroll(0,180)")
sleep(1)
bot.say(bot_said)
bot.runAndWait()
print(Fore.MAGENTA + "", file=stream)
input("""\n
               ┌───────────────────────────────────────┐
               │ông chủ bấm enter ra lệnh cho cháu đi ạ│
               └───────────────────────────────────────┘\n""")
bot.say("turn on github")
bot.runAndWait()
start_git()
tuong.get("https://github.com/")
tuong.execute_script("window.scroll(0,400)")
sleep(3)
tuong.get("https://github.com/login")
bot.say("login")
bot.runAndWait()
login_git("""\n
                                ┌─────────┐
                                │Đăng nhập│
                                └─────────┘\n""")
sleep(1)
tuong.find_element_by_id("login_field").send_keys("")
sleep(1)
login_git("""\n
                              ┌──────────────┐
                              │Nhập mật khẩu │
                              └──────────────┘\n""")
sleep(1)
bot.say("enter password")
bot.runAndWait()
tuong.find_element_by_id("password").send_keys("")
sleep(1)
start_git("""\n
                               ┌─────────────┐
                               │Đăng nhập vào│
                               └─────────────┘\n""")
bot.say("click sign in")
bot.runAndWait()
tuong.find_element_by_name("commit").click()
sleep(2)
tuong.execute_script("window.scroll(0,900)")
sleep(2)
tuong.get("https://github.com/tuongclearlove7")
bot.say(bot_said)
bot.runAndWait()
print(Fore.GREEN + "", file=stream)
input("""\n 
                   ┌───────────────────────────────────────┐
                   │ông chủ bấm enter ra lệnh cho cháu đi ạ│
                   └───────────────────────────────────────┘\n""")
end_bot()
print(Fore.RED + "", file=stream)
bot.say("exit bot")
bot.runAndWait()
bot_turn_off = '{:^55}'.format("""\n
                   ┌───────────────────────────────────────┐
                   │Vâng ạ, cháu tắt đây ạ tạm biệt ông chủ│
                   └───────────────────────────────────────┘\n""")
for i in bot_turn_off:
    print(i,end="", flush=True)
    sleep(0.01)
bot.say("Yes, I will turn off , good bye boss")
bot.runAndWait()
sleep(1.5)
tuong.quit()








