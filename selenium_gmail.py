from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1000,1000)
tuong.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
tuong.find_element_by_id("identifierId").send_keys("lol00sever@gmail.com")
sleep(2)
tuong.find_element_by_id("identifierNext").click()

sleep(2)
tuong.find_element_by_id("").send_keys("")
sleep(2)
tuong.find_element_by_name("").click()
input()