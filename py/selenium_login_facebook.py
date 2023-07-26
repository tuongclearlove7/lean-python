from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1000,1000)
tuong.get("https://www.facebook.com/login")
tuong.find_element_by_id("email").send_keys("")
sleep(2)
tuong.find_element_by_id("pass").send_keys("")
sleep(2)
tuong.find_element_by_name("login").click()

#tuong.get("https://www.facebook.com/profile.php?id=100016786003167")
#tuong.find_elements_by_class_name("").click()
#tuong.execute_script("window.scroll(0,1000)")

