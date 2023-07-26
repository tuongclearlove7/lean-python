from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1000,1000)
tuong.get("https://www.text-image.com/convert/ascii.html?fbclid=IwAR1_WTPvKgfmaHNIDPNUiox9onNhpMRDO-3hGiQFvKw43zFNPqDAhuX_b3s")
