from time import sleep
from selenium import webdriver
turn_on =input(max(["bấm enter để bật con bot"], default=True))
bot_turn_on = '{:^70}'.format('cháu bật lên rồi ạ, ông chủ ra lệnh cho cháu đi ạ')
for i in bot_turn_on:
    print(i,end="", flush=True)
    sleep(0.02)
def start_on(on_youtube, on_bot = turn_on):
    print(on_bot)
    sleep(2)
    print(on_youtube)
input("") 
start_on("bật youtube")
sleep(2)
def end_bot(exit="tắt"):
    print(exit)
def start_git(on_github="bật github"):
    print(on_github)
def login_git(login):
    print(login)
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(750,700)
tuong.get("https://www.youtube.com/watch?v=x_OwcYTNbHs")
sleep(5)
input("\nra lệnh tiếp cho cháu đi ạ\n")
tuong.get("https://www.youtube.com/watch?v=YDX9jlOUjNE")
input('\nra lệnh tiếp cho cháu đi ạ\n')
start_on("\nbật google dịch\n")
sleep(3)
tuong.get("https://www.google.com/search?q=gg+d%E1%BB%8Bch&oq=gg&aqs=chrome.0.69i59j69i57j0i131i433i512l3j0i512j0i131i433i512j69i60.824j0j7&sourceid=chrome&ie=UTF-8")
sleep(3)
input("\nra lệnh tiếp cho cháu đi ạ\n")
start_git()
tuong.get("https://github.com/login")
login_git("\nđăng nhập\n")
sleep(2)
tuong.find_element_by_id("login_field").send_keys("tuongclearlove7")
sleep(2)
login_git("\nnhập mật khẩu\n")
sleep(2)
tuong.find_element_by_id("password").send_keys("tuongyeuthao1")
sleep(2)
start_git("\nđăng nhập vào\n")
tuong.find_element_by_name("commit").click()
input("\nra lệnh tiếp cho cháu đi ạ\n")
end_bot()
bot_turn_off = '{:^70}'.format('vâng ạ, cháu tắt đây ạ tạm biệt ông chủ.')
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







