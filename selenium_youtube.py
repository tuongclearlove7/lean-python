from time import sleep
from selenium import webdriver
import sys
from colorama import Fore
from colorama import init, AnsiToWin32
import pyttsx3
init(wrap=False)
bot = pyttsx3.init()
stream = AnsiToWin32(sys.stderr).stream
turn_on = input(max(["""
                  ┌──────────────────────────┐
                  │ Bấm enter để bật con bot │
                  └──────────────────────────┘
"""], default=True))
bot.say("bot runing")
bot.runAndWait()
print(Fore.BLUE + '{:^65}'.format("hello Ông chủ !"), file=stream)
print(Fore.RED + "", file=stream)
bot_turn_on = '{:^60}'.format("""
    ┌───────────────────────────────────────────────────────────┐
    │Cháu bật lên rồi ạ, ông chủ bấm enter ra lệnh cho cháu đi ạ│
    └───────────────────────────────────────────────────────────┘
""")
for c in bot_turn_on:
    print(c ,end="", flush=True)
    sleep(0.01)
bot.say("press enter to control over me")
bot.runAndWait()
def start_on(on_youtube, on_bot = turn_on):
    print(on_bot)
    sleep(2)
    print(on_youtube)
input("")
bot.say("turn on youtube")
bot.runAndWait()
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
def start_git(on_github="""
                         ┌────────────┐
                         │ Bật Github │
                         └────────────┘"""):
    print(on_github)
def login_git(login):
    print(login)
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(750,700)
tuong.get("https://www.youtube.com/watch?v=oa7KbSfAajg")
sleep(3)
bot.say("press enter to control over me")
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
tuong.get("https://www.facebook.com/watch/?ref=search&v=1285016218598062&external_log_id=ea7139ba-20ec-49a5-af76-afc980e95a2a&q=bao%20l%C3%A2u%20ta%20l%E1%BA%A1i%20y%C3%AAu%20m%E1%BB%99t%20ng%C6%B0%E1%BB%9Di%20lofi")
tuong.execute_script("window.scroll(0,200)")
bot.say("press enter to control over me")
bot.runAndWait()
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
sleep(1)
bot.say("press enter to control over me")
bot.runAndWait()
input("""\n
           ┌───────────────────────────────────────┐
           │ông chủ bấm enter ra lệnh cho cháu đi ạ│
           └───────────────────────────────────────┘\n""")
bot.say("turn on github")
bot.runAndWait()
start_git()
tuong.get("https://github.com/login")
bot.say("login")
bot.runAndWait()
login_git("""\n
                           ┌─────────┐
                           │Đăng nhập│
                           └─────────┘\n""")
sleep(1)
tuong.find_element_by_id("login_field").send_keys("tuongclearlove7")
sleep(1)
login_git("""\n
                         ┌──────────────┐
                         │Nhập mật khẩu │
                         └──────────────┘\n""")
sleep(1)
bot.say("enter password")
bot.runAndWait()
tuong.find_element_by_id("password").send_keys("tuongyeuthao1")
sleep(1)
start_git("""\n
                          ┌─────────────┐
                          │Đặng nhập vào│
                          └─────────────┘\n""")
bot.say("click sign in")
bot.runAndWait()
tuong.find_element_by_name("commit").click()
sleep(2)
tuong.execute_script("window.scroll(0,600)")
bot.say("press enter to control over me")
bot.runAndWait()
input("""\n 
            ┌───────────────────────────────────────┐
            │ông chủ bấm enter ra lệnh cho cháu đi ạ│
            └───────────────────────────────────────┘\n""")
end_bot()
bot.say("exit bot")
bot.runAndWait()
bot_turn_off = '{:^55}'.format("""\n
            ┌───────────────────────────────────────┐
            │Vâng ạ, cháu tắt đây ạ tạm biệt ông chủ│
            └───────────────────────────────────────┘\n""")
for i in bot_turn_off:
    print(i,end="", flush=True)
    sleep(0.01)
bot.say("Yes, I will turn it off bye bye boss")
bot.runAndWait()
sleep(2)
tuong.quit()
#tuong.get("https://www.youtube.com/watch?v=6KJrNWC0tfw")
#sleep(5)
#tuong.get("https://www.youtube.com/watch?v=wUAbxnkma24")
#sleep(5)
#tuong.get("https://www.youtube.com/watch?v=tooO2A-RNy0")
#sleep(10)
#tuong.quit()







