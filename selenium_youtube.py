from time import sleep
from selenium import webdriver
import sys
from colorama import Fore
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
turn_on = input(max(["""
                  ┌──────────────────────────┐
                  │ Bấm enter để bật con bot │
                  └──────────────────────────┘
"""], default=True))
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
def start_on(on_youtube, on_bot = turn_on):
    print(on_bot)
    sleep(2)
    print(on_youtube)
input("")
start_on("""
                          ┌─────────────┐
                          │ Bật Youtube │
                          └─────────────┘""")
sleep(2)
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
tuong.get("https://www.youtube.com/watch?v=x_OwcYTNbHs")
sleep(5)
input("""\n 
           ┌───────────────────────────────────────┐
           │ông chủ bấm enter ra lệnh cho cháu đi ạ│
           └───────────────────────────────────────┘\n""")
tuong.get("https://www.youtube.com/watch?v=YDX9jlOUjNE")
input('''\n
           ┌───────────────────────────────────────┐
           │ông chủ bấm enter ra lệnh cho cháu đi ạ│
           └───────────────────────────────────────┘\n''')
start_on("""\n
                       ┌───────────────┐
                       │Bật google dịch│
                       └───────────────┘\n""")
sleep(3)
tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l3j0i512j0i131i433i512j69i60.824j0j7&sourceid=chrome&ie=UTF-8")
sleep(3)
input("""\n
           ┌───────────────────────────────────────┐
           │ông chủ bấm enter ra lệnh cho cháu đi ạ│
           └───────────────────────────────────────┘\n""")
start_git()
tuong.get("https://github.com/login")
login_git("""\n
                           ┌─────────┐
                           │Đăng nhập│
                           └─────────┘
\n""")
sleep(2)
tuong.find_element_by_id("login_field").send_keys("tuongclearlove7")
sleep(2)
login_git("""\n
                         ┌──────────────┐
                         │Nhập mật khẩu │
                         └──────────────┘\n""")
sleep(2)
tuong.find_element_by_id("password").send_keys("tuongyeuthao1")
sleep(2)
start_git("""\n
                          ┌─────────────┐
                          │Đặng nhập vào│
                          └─────────────┘\n""")
tuong.find_element_by_name("commit").click()
sleep(2)
tuong.execute_script("window.scroll(0,600)")
input("""\n 
            ┌───────────────────────────────────────┐
            │ông chủ bấm enter ra lệnh cho cháu đi ạ│
            └───────────────────────────────────────┘\n""")
end_bot()
bot_turn_off = '{:^55}'.format("""
            ┌───────────────────────────────────────┐
            │Vâng ạ, cháu tắt đây ạ tạm biệt ông chủ│
            └───────────────────────────────────────┘""")
for i in bot_turn_off:
    print(i,end="", flush=True)
    sleep(0.02)
sleep(2)
tuong.quit()
#tuong.get("https://www.youtube.com/watch?v=6KJrNWC0tfw")
#sleep(5)
#tuong.get("https://www.youtube.com/watch?v=wUAbxnkma24")
#sleep(5)
#tuong.get("https://www.youtube.com/watch?v=tooO2A-RNy0")
#sleep(10)
#tuong.quit()







