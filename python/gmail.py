import json,requests,time,os,sys
from time import strftime
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys 
import undetected_chromedriver.v2 as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":
        driver = uc.Chrome()
        link = f'https://www.google.com'
        driver.get(link)
        driver.get('https://google.com')
        driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&followup=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&hl=vi&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('lol00sever@gmail.com')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() 
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('12343211234321')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
        sleep(2)
        driver.get('https://www.youtube.com/watch?v=78nhuJ9E1es&t=1s')
        sleep(10)

