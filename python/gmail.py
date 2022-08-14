#open chrome driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(r'C:\Users\clearlove7\Documents\GitHub\clearlove7.github.io\python\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(r"https://www.google.com/search?q=gg+d%E1%BB%8Bch&rlz=1C1FKPE_viVN997VN997&oq=gg&aqs=chrome.0.69i59l3j0i131i433i512l4j69i60.826j0j7&sourceid=chrome&ie=UTF-8")
#find bằng id
element = driver.find_element(By.ID, "element_id")
#file bằng name
element = driver.find_element(By.NAME, "element_name")
#file bằng link_text
element = driver.find_element(By.LINK_TEXT, "element_link_text")
#find bằng partial_link_text
element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
#find bằng tag_name
element = driver.find_element(By.TAG_NAME, "element_tag_name")
#find bằng css_selector
element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
#find bằng xpath
element = driver.find_element(By.XPATH, "element_xpath")








