from time import sleep
from selenium import webdriver
import sys
from colorama import Fore
from colorama import init, AnsiToWin32
import pyttsx3
bot = pyttsx3.init()  
voices = bot.getProperty('voices') #nhận thông tin về giọng
bot.setProperty('voice', voices[1].id)  # giọng nữ
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
turn_on = input(max(["""
                  ┌──────────────────────────┐
                  │ Bấm enter để bật con bot │
                  └──────────────────────────┘
"""], default=True))
bot.say("bot runing")
bot.runAndWait()
print(Fore.RED + '{:^65}'.format("hello Clearlove7 !"), file=stream)
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
bot.say("press enter to control over me")
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
tuong.get("https://www.facebook.com/watch?ref=search&v=792650660907793&external_log_id=b7e2e990-7dad-4077-838f-782ad81c1c58&q=skt%20vs%20edg%20lol%20esport")
tuong.execute_script("window.scroll(100,0)")
bot.say("press enter to control over me")
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
sleep(1)
bot.say("press enter to control over me")
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
                          │Đăng nhập vào│
                          └─────────────┘\n""")
bot.say("click sign in")
bot.runAndWait()
tuong.find_element_by_name("commit").click()
sleep(2)
tuong.execute_script("window.scroll(0,900)")
bot.say("press enter to control over me")
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
bot.say("Yes, I will turn it off bye bye boss")
bot.runAndWait()
sleep(1.5)
tuong.quit()








