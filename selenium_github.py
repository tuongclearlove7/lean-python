from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1100,700)
tuong.get("https://github.com/login")
tuong.find_element_by_id("login_field").send_keys("tuongclearlove7")
sleep(2)
tuong.find_element_by_id("password").send_keys("tuongyeuthao1")
sleep(2)
tuong.find_element_by_name("commit").click()
input()

