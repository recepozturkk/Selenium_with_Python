from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.duckduckgo.com")
driver.maximize_window()
aramakutusu = driver.find_element(By.ID, "search_form_input_homepage")
aramakutusu.send_keys("selenium")
driver.find_element(By.ID, "search_button_homepage").click()
driver.find_element(By.ID, "r1-3").click()
