from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.google.com")
driver.maximize_window()
aramakutusu = driver.find_element(By.NAME, "q")
aramakutusu.send_keys("selenium")
aramakutusu.send_keys(Keys.ENTER)
