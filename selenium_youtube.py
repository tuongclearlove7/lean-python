from time import sleep
from selenium import webdriver
import sys
from colorama import Fore
from colorama import init, AnsiToWin32
import pyttsx3
init(wrap=False)

bot = pyttsx3.init() 
voices = bot.getProperty('voices') # information about voices (thông tin về giọng nói)
bot.setProperty('voice', voices[1].id) #female voice id 1 (giọng nữ id là 1)
bot_said = "press enter to control over me"
file_object = open('text.txt')
data_text = file_object.read() # reading file text.txt
stream = AnsiToWin32(sys.stderr).stream
turn_on = input(max(["""
                     ┌──────────────────────────┐
                     │ Bấm enter để bật con bot │
                     └──────────────────────────┘
"""], default=True)
                        )
print(Fore.CYAN + "", file=stream
                            )
with open("bot.txt", "r") as file: #"bot.txt" is file (là file chứa text-image đã tạo.)
    for line in file:
        print(line.strip(
                            )
                                 )
        sleep(0.05                   )
bot.say("bot runing")# bot said 
bot.runAndWait()

print(Fore.RED + '{:^75}'.format("Hello Clearlove7 !"), file=stream) # distance ^75 (khoảng cách căn lề giữa ^75)
print(Fore.GREEN + "", file=stream)# text color 
bot.say(" hello Clearlove7")
bot.runAndWait()
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(750,700)
tuong.get("https://i.pinimg.com/originals/7d/9b/1d/7d9b1d662b28cd365b33a01a3d0288e1.gif")
sleep(2)

bot_turn_on = '{:^60}'.format("""\n
        ┌───────────────────────────────────────────────────────────┐
        │Cháu bật lên rồi ạ, ông chủ bấm enter ra lệnh cho cháu đi ạ│
        └───────────────────────────────────────────────────────────┘\n""") 
for c in bot_turn_on:
    print(c ,end="", flush=True)
    sleep(0.005)
print(Fore.GREEN + "", file=stream)
bot.say(bot_said)
bot.runAndWait()

def start_on(on_youtube, on_bot = turn_on): # define (tạo hàm để bật bot và bật youtube...)
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

print(Fore.BLUE + "", file=stream)
def facebook_on(fb):
  return """\n
                           ┌────────────┐
                           │bật facebook│
                           └────────────┘\n""" * fb
def start_git(on_github="""
                              ┌────────────┐
                              │ Bật Github │
                              └────────────┘"""):
    print(on_github)

def login_git(login):
    print(login)


def end_bot(exit="""          
                                   ┌─────┐
                                   │ Tắt │
                                   └─────┘"""):
    print(exit)

tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")
sleep(3)
bot.say(bot_said)
bot.runAndWait()
input("""\n 
               ┌───────────────────────────────────────┐
               │ông chủ bấm enter ra lệnh cho cháu đi ạ│
               └───────────────────────────────────────┘\n""")
bot.say("turn on Facebook")
bot.runAndWait()
print(facebook_on(1))
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
send_text = tuong.find_element_by_id("tw-source-text-ta").send_keys(data_text)
if send_text == tuong.find_element_by_id("tw-spkr-button").click():
    print(send_text ,"""
                                ┌────┐
                                │dịch│
                                └────┘

    """)
    send_text == tuong.execute_script("window.scroll(0,180)")
sleep(2)
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
tuong.get("https://www.stoneshot.com/stoneshotblog/wp-content/uploads/2021/02/No-Robots_V4.gif")
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







