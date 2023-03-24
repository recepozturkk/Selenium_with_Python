import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://demoqa.com/droppable/")

source = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div#draggable")
target = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div#droppable")

action = ActionChains(driver)
action.drag_and_drop(source, target)
time.sleep(1)
action.perform()
time.sleep(2)
print(target.text)
driver.quit()