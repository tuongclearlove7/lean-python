from ast import While
import json, requests, time, os, sys
from time import strftime
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
#import undetected_chromedriver.v2 as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
geckodriver_autoinstaller.install()

profile = webdriver.FirefoxProfile(
    '/Users/<user name>/Library/Application Support/Firefox/Profiles/xxxxx.default-release')

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)

if __name__ == "__main__":
    #driver = webdriver.Edge(executable_path=".\Driver\msedgedriver.exe")
    link = f'https://www.google.com'
    driver.get(link)
    driver.get('https://google.com')
    driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&followup=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dvi&hl=vi&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    sleep(1)

    link = driver.find_element_by_id('identifierId').send_keys('lahahalahao007@gmail.com')

    #driver.find_element_by_id("identifierNext").click()
    pyautogui.press('enter')
    sleep(4)
    link2 = driver.find_element_by_id("password").send_keys("nhao0071002003")

    sleep(5)
    driver.get('https://www.youtube.com/watch?v=78nhuJ9E1es&t=1s')
    sleep(10)



