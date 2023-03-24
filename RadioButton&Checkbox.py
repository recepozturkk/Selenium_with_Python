

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
ortaboy = driver.find_element(By.CSS_SELECTOR, "input[value=Orta]")
zeytin = driver.find_element(By.CSS_SELECTOR, "input[value=zeytin]")
mantar = driver.find_element(By.CSS_SELECTOR, "input[value=mantar]")
print(zeytin.is_selected())
print(mantar.is_selected())
print(ortaboy.is_selected())
ortaboy.click()
zeytin.click()
mantar.click()
print(zeytin.is_selected())
print(mantar.is_selected())
print(ortaboy.is_selected())

driver.quit()