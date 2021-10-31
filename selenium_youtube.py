from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1000,1000)
tuong.get("https://www.youtube.com/watch?v=sX1Y2JMK6g8")
sleep(5)
tuong.get("https://www.youtube.com/watch?v=6KJrNWC0tfw")
sleep(5)
tuong.get("https://www.youtube.com/watch?v=wUAbxnkma24")
sleep(5)
tuong.get("https://www.youtube.com/watch?v=tooO2A-RNy0")
sleep(10)
tuong.quit()
