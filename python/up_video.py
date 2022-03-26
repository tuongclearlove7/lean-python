from time import sleep
from selenium import webdriver
class Login_Gmail():
    def On_Gmail():
        Gmail = webdriver.Chrome(executable_path=r"C:\Users\clearlove7\Documents\GitHub\clearlove7.github.io\python\chromedriver.exe")
        Gmail.set_window_size(1000,1000)
        Gmail.get("https://www.youtube.com/")
        sleep(2)
        Gmail.find_element_by_name("button").click()
        sleep(2)
        Gmail.find_element_by_name("").click()

Login_Gmail.On_Gmail()













