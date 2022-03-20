from lib2to3.pgen2.driver import Driver
from multiprocessing.connection import wait
from this import d
from time import sleep
from selenium import webdriver
import undetected_chromedriver.v2 as uc 
# class Login_Gmail():
#     def On_Gmail():
#         Gmail = uc.Chrome(executable_path=r"D:\python\chromedriver.exe")
#         Gmail.set_window_size(1000,1000)
#         Gmail.get("https://accounts.google.com/AddSession/identifier?hl=vi&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3D%25C4%2591%25C4%2583ng%2Bnh%25E1%25BA%25ADp%2Bgmail%26oq%3D%25C4%2591%25C4%2583ng%26aqs%3Dchrome.1.69i57j0i433i512l2j0i131i433i512j0i433i512j69i60j69i61j69i60.3520j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAlAAQ&flowName=GlifWebSignIn&flowEntry=AddSession")
#         Gmail.find_element_by_id("identifierId").send_keys("lol00sever@gmail.com")
#         sleep(2)    
#         Gmail.find_element_by_xpath("//*[@id='identifierNext']").click()
#         sleep(2)
#         Gmail.find_element_by_id("next").click()
#         sleep(2)
#         Gmail.find_element_by_id("password").send_keys("")
#         sleep(2)
#         Gmail.find_element_by_name("passwordNext").click()
# Looptions = webdriver.ChromeOptions()
class tool():
        def on_web():
            while True:
                global driver
                driver =  uc.Chrome()
                driver.get("https://accounts.google.com/AddSession/identifier?hl=vi&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3D%25C4%2591%25C4%2583ng%2Bnh%25E1%25BA%25ADp%2Bgmail%26oq%3D%25C4%2591%25C4%2583ng%26aqs%3Dchrome.1.69i57j0i433i512l2j0i131i433i512j0i433i512j69i60j69i61j69i60.3520j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAlAAQ&flowName=GlifWebSignIn&flowEntry=AddSession")
            
                if driver.find_element_by_id("identifierId").send_keys("lol00sever@gmail.com")==driver.find_element_by_xpath("//*[@id='identifierNext']").click():
                    driver.find_element_by_id("password").send_keys("12343211234321")
                    driver.find_element_by_name("passwordNext").click() 
                break;      
tool.on_web()
# ok nhá bạn có thể để độ trễ cao hơn cho nó load  #
# đợi e test cho nó đc luôn đk bác )):đc



