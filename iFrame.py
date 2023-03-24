import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.herokuapp.com/iframe-demo.html")
driver.switch_to.frame("email")
driver.find_element(By.ID, "email").send_keys("recepozturk@gmail.com")
time.sleep(2)
# default_content => anasayfaya döndürür
# parent_frame => bir üstteki frame e geçiş yapar
driver.switch_to.default_content()
driver.find_element(By.ID, "isim").send_keys("yesimozturk@gmail.com")
time.sleep(2)
driver.quit()
